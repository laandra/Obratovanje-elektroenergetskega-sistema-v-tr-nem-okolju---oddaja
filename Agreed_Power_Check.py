"""Validation for the agreed billing power (dogovorjena obracunska moc) rule.

In the style of `Rule_Based_Control_Check.py` -- a print-driven script with
assertions, run directly rather than through a test runner:

    .venv/bin/python Agreed_Power_Check.py            # 4 months, every window
    .venv/bin/python Agreed_Power_Check.py --quick    # 3 months, window 1 only
    .venv/bin/python Agreed_Power_Check.py --year     # the whole calendar year

The rule under test: month M's agreed power is the MEAN of the `n_peaks` highest
15-minute peaks per block, pooled over `n_months_window` months ending at
M - `lag`. It lives in `si_moc.mesecni_razpored` and EVERY algorithm reads it
from there -- the MILP through `add_endogenous_agreed_power`, the rule-based
controllers and the community model through `Environment.converge_agreed_power`.
The point of check 2 is that those two encodings really are the same rule.

What each check is for:

  1  the statistic is right           top-1 reduces to the old max; top-5 is the
                                      mean of five; a window pools RAW peaks
  2  the LP encodes the same rule     the contract the MILP solves for equals the
                                      one si_moc derives from the draw it achieved
  3  only billed blocks are contracted a month carries no agreed power in a block
                                      it is not billed for, so a winter block-1
                                      peak cannot inflate a summer block-2 bill
  4  the statute dominates the proxy  sqrt(sum d^2) >= max d, always
  5  the MILP is a lower bound        no rule may beat it on the objective it
                                      actually minimized
  6  the causal roll IS a fixed point  rolling the contract forward one month
                                      at a time lands on the contract its own
                                      peaks derive, in one pass instead of one
                                      per month -- and where the whole-roll
                                      iteration converges at all, it converges
                                      to exactly that
  7  the surrogate prices the tariff  the shadow price a short horizon shaves
                                      against is the operator's own EUR/kW, it
                                      lowers the contract, and it still cannot
                                      beat perfect foresight
"""

from __future__ import annotations

import sys

import numpy as np

import Horizon_Comparison as hc
import MILP_Household as mh
import Rule_Based_Control as rbc
from Environment import monthly_top_peaks_by_block
from Pricing_Functions import mesecni_razpored_moci

sys.path.append(str(hc.Path(__file__).resolve().parent / "New pricing functions"))
from si_cas import bloki_v_mesecu                              # noqa: E402
from si_obracun import Pravila                                 # noqa: E402
from si_tarife import DDV                                      # noqa: E402
import si_moc as M                                             # noqa: E402

DATASET, HOUSEHOLD = "Fluvius_HP", 1
STEPS_PER_DAY = 96

QUICK = "--quick" in sys.argv
YEAR = "--year" in sys.argv
N_MONTHS = 3 if QUICK else (12 if YEAR else 4)
WINDOWS = (1,) if QUICK else (1, 2, 12)

# Real month ids, so `bloki_v_mesecu` is meaningful: 2026-01 and 2026-02 are
# billed for blocks 1-4 (higher season), 2026-03 for blocks 2-5.
JAN, FEB, MAR = 24312, 24313, 24314


# ---------------------------------------------------------------------------
def check_the_statistic():
    """1. top-1 is the old maximum, top-5 is the operator's mean, a window pools
    the RAW peaks rather than averaging monthly averages."""
    print("\n1. the statistic")
    peaks = {
        JAN: {1: [1.0, .9, .8, .7, .6], 2: [5., 4., 3., 2., 1.], 3: [6.] * 5, 4: [6.] * 5},
        FEB: {1: [1.] * 5, 2: [9., 1., 1., 1., 1.], 3: [7.] * 5, 4: [7.] * 5},
        MAR: {2: [2.] * 5, 3: [8.] * 5, 4: [8.] * 5, 5: [8.] * 5},
    }
    boot = {1: [.5] * 5, 2: [8.] * 5, 3: [9.] * 5, 4: [9.] * 5}
    kw = dict(zamik_mesecev=1, zacetne_konice=boot)

    top1 = M.mesecni_razpored(peaks, st_konic=1, n_months_window=1, **kw)
    assert top1[FEB][2] == 5.0 and top1[MAR][2] == 9.0, top1
    print(f"   top-1, window 1 == the previous month's max      FEB b2 = {top1[FEB][2]:.3f}")

    top5 = M.mesecni_razpored(peaks, st_konic=5, n_months_window=1, **kw)
    assert abs(top5[FEB][2] - 3.0) < 1e-12, top5          # mean(5,4,3,2,1)
    assert abs(top5[MAR][2] - 2.6) < 1e-12, top5          # mean(9,1,1,1,1)
    print(f"   top-5, window 1 == the mean of the five highest  FEB b2 = {top5[FEB][2]:.3f}")

    # MAR <- JAN+FEB pooled: [5,4,3,2,1]+[9,1,1,1,1]; top5 = 9,5,4,3,2 -> 4.6.
    # Averaging the two monthly means would give (3.0+2.6)/2 = 2.8.
    win2 = M.mesecni_razpored(peaks, st_konic=5, n_months_window=2, **kw)
    assert abs(win2[MAR][2] - 4.6) < 1e-12, win2
    print(f"   window 2 pools raw peaks, not monthly means      MAR b2 = "
          f"{win2[MAR][2]:.3f} (mean-of-means would be 2.800)")

    # A window reaching past the start of the data pools the walked-in history.
    win12 = M.mesecni_razpored(peaks, st_konic=5, n_months_window=12, **kw)
    assert abs(win12[FEB][2] - 8.0) < 1e-12, win12
    print(f"   a window past the data start pools the bootstrap FEB b2 = {win12[FEB][2]:.3f}")

    # Block 5 is never read from its own peaks; it comes out of monotonicity.
    big5 = {JAN: {2: [1.], 3: [1.], 4: [1.]}, FEB: {2: [1.], 3: [1.], 4: [1.]},
            MAR: {2: [1.], 3: [1.], 4: [1.], 5: [99.]}}
    rb = M.mesecni_razpored(big5, st_konic=1, n_months_window=1, zamik_mesecev=1,
                            zacetne_konice={2: [1.], 3: [1.], 4: [1.]})
    assert rb[MAR][5] == 1.0 and rb[MAR][5] == rb[MAR][4], rb[MAR]
    print(f"   block 5 == block 4, its own 99 kW peaks ignored  MAR b5 = {rb[MAR][5]:.3f}")


def check_only_billed_blocks_are_contracted():
    """3. A month carries agreed power only in the blocks it is billed for."""
    print("\n3. only billed blocks are contracted")
    hot = {JAN: {1: [50.] * 5, 2: [1.] * 5, 3: [1.] * 5, 4: [1.] * 5},
           FEB: {1: [50.] * 5, 2: [1.] * 5, 3: [1.] * 5, 4: [1.] * 5},
           MAR: {2: [1.] * 5, 3: [1.] * 5, 4: [1.] * 5, 5: [1.] * 5}}
    r = M.mesecni_razpored(hot, st_konic=5, n_months_window=1, zamik_mesecev=1,
                           zacetne_konice={1: [1.], 2: [1.], 3: [1.], 4: [1.]})
    for m, v in r.items():
        y, mo = m // 12, m % 12 + 1
        assert set(v) == set(bloki_v_mesecu(y, mo, "2024")), (m, sorted(v))
    print(f"   contracted blocks == billed blocks               "
          f"MAR = {sorted(r[MAR])}, JAN = {sorted(r[JAN])}")
    # In season the 50 kW block-1 peak does raise block 2 through monotonicity;
    # out of season block 1 is not contracted at all, so it cannot.
    assert r[FEB][1] == 50.0 and r[FEB][2] == 50.0, r[FEB]
    assert r[MAR][2] == 1.0, r[MAR]
    print(f"   a winter block-1 peak does not reach the summer  "
          f"FEB b2 = {r[FEB][2]:.1f}, MAR b2 = {r[MAR][2]:.1f}")


# ---------------------------------------------------------------------------
def _env(n_peaks, window):
    env = hc.build_env(hc.load_user(HOUSEHOLD, DATASET))
    env.agreed_power_n_peaks = n_peaks
    env.agreed_power_n_months_window = window
    # `clear_achieved_power` early-returns on a fresh env, so force the rebuild
    # that actually re-reads the two knobs above.
    env._install_agreed_power_schedule(env._build_agreed_power_schedule(None))
    return env


def check_lp_encodes_the_rule(n_peaks=5, window=1):
    """2. The contract the MILP solves for is the one si_moc derives from the
    draw that solve achieved -- so the LP and the rule-based path really are
    running the same rule, not two that happen to agree on easy months."""
    env = _env(n_peaks, window)
    n_steps = min(N_MONTHS * 31 * STEPS_PER_DAY, int(env.episode_length))
    df = mh.solve_household(env, n_steps=n_steps, verbose=False,
                            endogenous_agreed_power=True,
                            solver=mh.full_period_solver())
    solved = env.agreed_power_schedule

    hours = env.interval_minutes / 60.0
    import_kw = np.maximum(mh.net_grid_kwh(df), 0.0) / hours
    derived = mesecni_razpored_moci(
        monthly_top_peaks_by_block(
            import_kw, np.asarray(env.tariff_blocks[:n_steps]),
            np.asarray(env.month_ids[:n_steps]), n_peaks=n_peaks),
        minimalna_moc_kw=env.min_agreed_power_kw,
        prikljucna_moc_kw=env.connection_power_kw,
        zamik_mesecev=env.agreed_power_lag_months,
        prenesi_manjkajoce_bloke=env.agreed_power_carry_missing_blocks,
        zacetne_konice=env.agreed_power_bootstrap_kw,
        st_konic=n_peaks, n_months_window=window,
    )

    # The leading `lag` months are a constant the LP was handed, not a decision.
    lag = int(env.agreed_power_lag_months)
    months = sorted(set(solved) & set(derived))
    worst, above, below = 0.0, [], []
    for i, m in enumerate(months):
        if i < lag:
            continue
        for b in sorted(derived[m]):
            a, d = solved[m].get(b, 0.0), derived[m][b]
            worst = max(worst, abs(a - d))
            if a - d > 1e-6:
                above.append((m, b, a, d))
            elif d - a > 1e-6:
                below.append((m, b, a, d))

    print(f"   n_peaks={n_peaks} window={window:2d}: {len(months) - lag} months, "
          f"worst |solved-derived| = {worst:.2e} kW", end="")
    if below:
        print("\n   CONTRACTED BELOW THE RULE -- the LP encoding is wrong:")
        for m, b, a, d in below[:10]:
            print(f"      {m//12:04d}-{m%12+1:02d} b{b}: solved={a:.4f} rule={d:.4f}")
    assert not below, "the LP contracted below the rule; the encoding is wrong"
    if above:
        # Not an encoding error: with faktor_presezne_moci > 1 exceeding costs
        # more per kW than contracting, so a cost-minimizing household buys the
        # cover instead. The LP may do that; the rule-based path may not.
        print(f"   -- {len(above)} block-month(s) contracted ABOVE the rule "
              f"(excess cover, faktor > 1):")
        peak = monthly_top_peaks_by_block(
            import_kw, np.asarray(env.tariff_blocks[:n_steps]),
            np.asarray(env.month_ids[:n_steps]), n_peaks=1)
        for m, b, a, d in above[:6]:
            pk = (peak.get(m, {}).get(b) or [float("nan")])[0]
            print(f"      {m//12:04d}-{m%12+1:02d} b{b}: solved={a:.4f} rule={d:.4f} "
                  f"realized peak={pk:.4f}{'  == peak' if abs(pk - a) < 1e-4 else ''}")
    else:
        print("   (nothing contracted above the rule either)")
    return env, df


def check_statute_dominates_the_proxy():
    """4. The bill's sqrt(sum of squared exceedances) is never below the linear
    max(0, peak - agreed) the MILP minimizes."""
    print("\n4. the statute dominates the linear proxy")
    n_steps = min(N_MONTHS * 31 * STEPS_PER_DAY,
                  int(hc.build_env(hc.load_user(HOUSEHOLD, DATASET)).episode_length))
    df = hc.run_user(HOUSEHOLD, DATASET, n_steps=n_steps,
                     strategies=["day_block"], verbose=False)
    row = df.iloc[0]
    assert row["Excess_Statutory_EUR"] >= row["Excess_Linear_EUR"] - 1e-9, row
    print(f"   linear (MILP objective)  {row['Excess_Linear_EUR']:8.3f} EUR")
    print(f"   statutory (the invoice)  {row['Excess_Statutory_EUR']:8.3f} EUR")
    print(f"   gap                      {row['Excess_Gap_EUR']:8.3f} EUR "
          f"({100 * row['Excess_Gap_EUR'] / row['Invoice_EUR']:.2f} % of the bill)")


def check_milp_is_a_lower_bound():
    """5. No rule may beat the MILP on the objective the MILP minimized."""
    print("\n5. the MILP is a lower bound")
    env = _env(hc.AGREED_POWER_N_PEAKS, hc.AGREED_POWER_N_MONTHS_WINDOW)
    n_steps = min(N_MONTHS * 31 * STEPS_PER_DAY, int(env.episode_length))
    env.clear_achieved_power()
    milp = hc.run_strategy(env, "period", "block", soc_mode="fixed50", n_steps=n_steps)
    print(f"   {'MILP full_period':32s} {milp['Cost_EUR']:9.2f} EUR")

    sig = rbc.build_signals(env, n_steps)
    worst = None
    for name in rbc.POLICY_ORDER:
        env.clear_achieved_power()
        out = rbc.run_policy(env, rbc.make_policy(name), n_steps=n_steps, signals=sig)
        gap = out["Cost_EUR"] - milp["Cost_EUR"]
        print(f"   {name:32s} {out['Cost_EUR']:9.2f} EUR   gap {gap:+8.2f}"
              f"{'  <-- BEATS THE OPTIMUM' if gap < -1e-6 else ''}")
        worst = gap if worst is None else min(worst, gap)
    assert worst >= -1e-6, "a rule beat the MILP: that is a pricing bug, not a better policy"


def _contracted_kw(schedule, months):
    """Total agreed kW over the months a roll actually contracted."""
    return sum(sum(schedule[m].values()) for m in months if m in schedule)


def check_the_causal_roll_is_the_fixed_point():
    """6. The contract of month M depends only on the months before it, so the
    map is lower-triangular and forward substitution solves it exactly: rolling
    it forward one month at a time lands ON a fixed point of the rule, in one
    dispatch instead of one per month.

    Two things are asserted, and the second is the substantive one:

      * the causal roll's own output is a fixed point -- re-deriving the
        schedule from the peaks the executed trajectory actually metered
        reproduces the contract it was billed under, month for month;
      * where the whole-roll iteration converges too, it converges to exactly
        that, at several times the cost.

    Where it does NOT converge the two are compared but not asserted equal, and
    that is the other half of the point: the iteration is Jacobi on a triangular
    system, it needs about as many passes as there are months, and
    `AGREED_POWER_MAX_ITER` cuts it off long before a year is up.
    """
    from Environment import AGREED_POWER_MAX_ITER, AGREED_POWER_TOL_KW

    print(f"\n6. the causal roll is a fixed point ({N_MONTHS} months, the "
          f"iteration gets {AGREED_POWER_MAX_ITER} passes)")
    k_peaks, window = hc.AGREED_POWER_N_PEAKS, hc.AGREED_POWER_N_MONTHS_WINDOW
    env = _env(k_peaks, window)
    n_steps = min(N_MONTHS * 31 * STEPS_PER_DAY, int(env.episode_length))
    months = sorted(set(int(m) for m in env.month_ids[:n_steps]))
    lag = int(env.agreed_power_lag_months)

    was_roll, was_sur = hc.AGREED_POWER_ROLL, hc.AGREED_POWER_SURROGATE
    out = {}
    try:
        hc.AGREED_POWER_SURROGATE = False       # one thing at a time
        for roll in ("fixed_point", "causal"):
            hc.AGREED_POWER_ROLL = roll
            env.clear_achieved_power()
            r = hc.run_strategy(env, "day", "block", soc_mode="fixed50", n_steps=n_steps)
            out[roll] = (r, env.agreed_power_schedule)
            print(f"   {roll:12s} {r['Cost_EUR']:9.2f} EUR   {r['N_Solves']:5d} solves   "
                  f"{r['Agreed_Power_Iters']} pass(es)"
                  f"{'' if r['Agreed_Power_Converged'] else '  (no fixed point found)'}")
    finally:
        hc.AGREED_POWER_ROLL, hc.AGREED_POWER_SURROGATE = was_roll, was_sur

    (fp, fp_sched), (ca, ca_sched) = out["fixed_point"], out["causal"]

    # The causal roll's contract, re-derived from the draw it actually metered.
    hours = env.interval_minutes / 60.0
    import_kw = np.maximum(ca["_net_trace"], 0.0) / hours
    derived = mesecni_razpored_moci(
        monthly_top_peaks_by_block(
            import_kw, np.asarray(env.tariff_blocks[:n_steps]),
            np.asarray(env.month_ids[:n_steps]), n_peaks=k_peaks),
        minimalna_moc_kw=env.min_agreed_power_kw,
        prikljucna_moc_kw=env.connection_power_kw,
        zamik_mesecev=lag,
        prenesi_manjkajoce_bloke=env.agreed_power_carry_missing_blocks,
        zacetne_konice=env.agreed_power_bootstrap_kw,
        st_konic=k_peaks, n_months_window=window,
    )
    # Only the months whose whole lookback window lies inside the run: earlier
    # ones read the bootstrap, which the roll deliberately freezes at the
    # no-battery reading so a December registered late cannot move January.
    settled = [m for i, m in enumerate(months) if i >= lag + window - 1]
    worst_self = max((abs(ca_sched[m].get(b, 0.0) - derived[m].get(b, 0.0))
                      for m in settled for b in set(ca_sched[m]) | set(derived[m])),
                     default=0.0)
    print(f"   the causal contract is the one its own peaks derive: worst "
          f"|billed-derived| = {worst_self:.2e} kW over {len(settled)} month(s)")
    assert worst_self < AGREED_POWER_TOL_KW * 10, worst_self

    worst = max((abs(fp_sched[m].get(b, 0.0) - ca_sched[m].get(b, 0.0))
                 for m in months for b in set(fp_sched[m]) | set(ca_sched[m])),
                default=0.0)
    assert ca["N_Solves"] < fp["N_Solves"], (ca["N_Solves"], fp["N_Solves"])
    d_eur = ca["Cost_EUR"] - fp["Cost_EUR"]
    if not fp["Agreed_Power_Converged"]:
        print(f"   the iteration ran out of passes after {fp['N_Solves']} solves: "
              f"{d_eur:+.4f} EUR and {worst:.2e} kW off the causal contract, which is "
              f"what a triangular map costs to iterate  OK")
        return

    # Same contract -- that is what the roll determines, and it is exact.
    assert worst < AGREED_POWER_TOL_KW * 10, worst

    # The TRAJECTORIES are not bit-identical, and should not be. A window that
    # spans a month boundary is planned before the outgoing month is complete,
    # so the causal roll plans its tail under the contract still in force, while
    # the iteration's final pass had the settled one in place from the start:
    # it lets a boundary window peek at a contract the causal controller cannot
    # know yet. So the causal run is the DEARER of the two, by intervals sitting
    # at the boundaries, and it may never be the cheaper -- a controller with
    # less information does not get a lower bill out of having it.
    assert d_eur > -1e-6, (
        f"the causal roll came out {-d_eur:.4f} EUR BELOW the iteration it has "
        f"strictly less information than; that is a pricing bug, not a better roll")
    assert abs(d_eur) < 1e-4 * fp["Cost_EUR"], (
        f"the two rolls reached the same contract but bills {d_eur:+.4f} EUR apart, "
        f"which is too far to be the boundary windows alone")
    print(f"   the iteration converged to the same contract ({worst:.2e} kW) at "
          f"{fp['N_Solves'] / ca['N_Solves']:.0f}x the solves; the causal roll pays "
          f"{d_eur:+.6f} EUR for not seeing over the month boundary  OK")


def check_the_surrogate_prices_the_tariff():
    """7. The shadow price a rolling solve shaves against is the operator's own
    EUR/kW; shaving against it lowers the contract; and it still cannot buy the
    controller more than perfect foresight already has."""
    print("\n7. the surrogate prices the tariff")
    env = _env(hc.AGREED_POWER_N_PEAKS, hc.AGREED_POWER_N_MONTHS_WINDOW)
    pravila = Pravila.za_leto(hc.PRICING_REFERENCE_YEAR)
    options = dict(env.pricing_options, pricing_reference_year=hc.PRICING_REFERENCE_YEAR)

    # January is billed for blocks 1-4, so block 1 is the reference block the
    # OVE/SPTE levy rides on and blocks 2-4 carry the network rate alone.
    for b in (2, 3):
        got = mh.agreed_power_value_eur_per_kw(
            2026, 1, b, lag=1, window=1, interval_minutes=env.interval_minutes,
            scheme=env.pricing_scheme, pricing_options=options, pravila=pravila)
        want = pravila.omreznina.postavka_moc(b, True) * (1.0 + DDV)
        assert abs(got - want) < 1e-9, (b, got, want)
        print(f"   block {b}: surrogate {got:.4f} == postavka_moc x (1+DDV) {want:.4f} EUR/kW")
    # A block the following months never bill carries no signal at all.
    assert mh.agreed_power_value_eur_per_kw(
        2026, 1, 5, lag=1, window=1, interval_minutes=env.interval_minutes,
        scheme=env.pricing_scheme, pricing_options=options, pravila=pravila) == 0.0

    n_steps = min(N_MONTHS * 31 * STEPS_PER_DAY, int(env.episode_length))
    months = sorted(set(int(m) for m in env.month_ids[:n_steps]))
    env.clear_achieved_power()
    opt = hc.run_strategy(env, "period", "block", soc_mode="fixed50", n_steps=n_steps,
                          solver=hc.full_period_solver())

    was = hc.AGREED_POWER_SURROGATE
    runs = {}
    try:
        for sur in (False, True):
            hc.AGREED_POWER_SURROGATE = sur
            env.clear_achieved_power()
            r = hc.run_strategy(env, "day", "block", soc_mode="fixed50", n_steps=n_steps)
            runs[sur] = (r, _contracted_kw(env.agreed_power_schedule, months))
    finally:
        hc.AGREED_POWER_SURROGATE = was

    print(f"   {'full_period (foresight)':28s} {opt['Cost_EUR']:9.2f} EUR")
    for sur in (False, True):
        r, kw = runs[sur]
        print(f"   {'day_block, surrogate ' + ('on' if sur else 'off'):28s} "
              f"{r['Cost_EUR']:9.2f} EUR   gap {r['Cost_EUR'] - opt['Cost_EUR']:+8.2f}   "
              f"contracted {kw:7.2f} kW")
        assert r["Cost_EUR"] - opt["Cost_EUR"] > -1e-6, (
            "a rolling horizon beat perfect foresight: that is a pricing bug")
    assert runs[True][1] < runs[False][1], (
        "the surrogate did not lower the contract; it exists to shave it")
    print("   the surrogate shaves the contract and stays above the optimum  OK")


def main():
    print(f"agreed-power rule under test: {hc.AGREED_POWER_TAG}")
    print(f"contract roll under test:     {hc.CONTRACT_ROLL_TAG}")
    print(f"{DATASET}/{HOUSEHOLD}, {N_MONTHS} months, windows {WINDOWS}")

    check_the_statistic()

    print("\n2. the LP encodes the same rule si_moc does")
    for window in WINDOWS:
        check_lp_encodes_the_rule(n_peaks=5, window=window)
    check_lp_encodes_the_rule(n_peaks=1, window=1)

    check_only_billed_blocks_are_contracted()
    check_statute_dominates_the_proxy()
    check_milp_is_a_lower_bound()
    check_the_causal_roll_is_the_fixed_point()
    check_the_surrogate_prices_the_tariff()

    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
