### The share of shared energy -- the figure the study is for
# One figure per battery scenario: bill and energy on aligned axes, because the
# question is both what the contract costs and how much of the allocation lands.

SUBTITLE = (f"Cenik {MAIN_CONFIG}, {len(HOUSEHOLD_KEYS)} gospodinjstev, celo leto 2024, "
            f"interna cena {INTERNAL_PRICE:.3f} EUR/kWh, značilni primer {ZNACILNI_PRIMER}. "
            f"Leva os = letni račun; desna os = deljena energija. Polna črta = "
            f"pogodbeni delež, črtkano = prosta razdelitev po intervalih. Oznaka = "
            f"delež z najnižjim računom skupnosti.")

for battery in SWEEP_BATTERIES:
    fig, ax_bill = plt.subplots(figsize=pf.figsize(ratio=0.62))
    ax_energy = ax_bill.twinx()
    bill_handles = []
    energy_handles = []
    baseline = float(ind[ind["battery"] == battery]["Community_cost_EUR"].iloc[0])
    ax_bill.axhline(baseline, color=MUTED, linewidth=1.0, linestyle=":", zorder=1)
    ax_bill.annotate("brez delitve", (0.02, baseline), xytext=(0, 4), textcoords="offset points",
                     color=MUTED, fontsize=8, va="bottom")

    for scheme in (ccm.SCHEME_SOUPORABA, ccm.SCHEME_SKUPNOST):
        sub = sweep[(sweep["battery"] == battery) & (sweep["scheme"] == scheme)].sort_values("share")
        color = SCHEME_COLOR[scheme]
        bill_line, = ax_bill.plot(
            sub["share"], sub["Community_cost_EUR"], color=color, linewidth=2.0,
            marker="o", markersize=4.5, markerfacecolor=SURFACE, markeredgewidth=1.6,
            label=SCHEME_LABEL[scheme], zorder=3)
        bill_handles.append(bill_line)
        free = dyn[(dyn["battery"] == battery) & (dyn["scheme"] == scheme)]
        if len(free):
            level = float(free["Community_cost_EUR"].iloc[0])
            ax_bill.axhline(level, color=color, linewidth=1.0, linestyle="--", alpha=0.65, zorder=2)
        best = sub.loc[sub["Community_cost_EUR"].idxmin()]
        ax_bill.plot([best["share"]], [best["Community_cost_EUR"]], marker="o", markersize=8,
                     color=color, zorder=4)
        ax_bill.annotate(f"{best['share'] * 100:.0f}",
                         (best["share"], best["Community_cost_EUR"]),
                         xytext=(0, -13), textcoords="offset points", ha="center",
                         color=color, fontsize=8.5, fontweight="bold")

        energy_line, = ax_energy.plot(sub["share"], sub["Shared_kWh"], color=color,
                                      linewidth=1.5, linestyle="-", alpha=0.75, zorder=3)
        energy_handles.append(plt.Line2D([], [], color=color, lw=1.5,
                                          label=f"{SCHEME_LABEL[scheme]} — porabljeno"))
        if sub["Wasted_kWh"].abs().max() > 1.0:
            ax_energy.fill_between(sub["share"], sub["Shared_kWh"],
                                   sub["Shared_kWh"] + sub["Wasted_kWh"], color=color,
                                   alpha=0.16, linewidth=0, zorder=2)
            energy_handles.append(Patch(facecolor=color, alpha=0.16,
                                        label=f"{SCHEME_LABEL[scheme]} — propade"))

    ax_energy.axhline(SHARING_CEILING_KWH, color=MUTED, linestyle=":", linewidth=1.0)
    ax_energy.annotate("sočasna zgornja meja", (0.02, SHARING_CEILING_KWH),
                       xytext=(0, 4), textcoords="offset points", color=MUTED, fontsize=8)
    ax_bill.grid(axis="y", linewidth=0.6)
    ax_bill.set_axisbelow(True)
    finish(ax_bill, xlabel="Pogodbeni delež deljene energije [%]",
           ylabel="Letni račun skupnosti [EUR/a]", yfmt=EUR, xfmt=SHARE)
    ax_energy.set_ylabel("Deljena energija [kWh/a]")
    ax_energy.yaxis.set_major_formatter(PLAIN)
    ax_energy.tick_params(axis="y", colors=MUTED)
    ax_energy.spines["right"].set_color(MUTED)
    pf.chart_frame(
        fig, f"Delež, račun in deljena energija — {battery}", SUBTITLE,
        handles=bill_handles + energy_handles, ncol=2)
    pf.show(fig, f"share_sweep_{pf.slug(battery)}", layout="frame")