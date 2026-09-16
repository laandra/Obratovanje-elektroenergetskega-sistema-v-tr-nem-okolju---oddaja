### The whole community on the year's price extremes
# Read off the community profile's own index so the slicing stays positional:
# the Fluvius files repeat the DST fall-back hour, so labels are duplicated.
ref_index = RESULTS[SCEN_ORDER[0]]["community_profile"].index
smp = pd.Series(
    next(iter(DATA.values()))[cs.PRICE_COLUMN].to_numpy(dtype=float)[: len(ref_index)] * 1000.0,
    index=ref_index,
)
day_of = ref_index.normalize()
daily = smp.groupby(day_of).agg(["mean", "min", "max"])
daily["range"] = daily["max"] - daily["min"]

# Dearest and cheapest by daily mean; the swing is the intra-day range, which is
# what a battery earns on. Ties take the runner-up, so the days always differ.
picks = []
for label, column, ascending in [("najdražji dan", "mean", False),
                                 ("najcenejši dan", "mean", True),
                                 ("največji razpon", "range", False)]:
    order = daily[column].sort_values(ascending=ascending).index
    picks.append((label, next(d for d in order if d not in [p[1] for p in picks])))

# Souporaba is dispatched by the Dinamicni solve (cs.DISPATCH_ALIAS) and
# settlement leaves no mark on a power chart, so the curve is drawn once.
FLOW_SCEN = [s for s in SCEN_ORDER if s not in cs.DISPATCH_ALIAS]
SHARES_DISPATCH = {}
for alias, target in cs.DISPATCH_ALIAS.items():
    SHARES_DISPATCH.setdefault(target, []).append(LABEL[alias])
FLOW_LABEL = {s: " = ".join([LABEL[s]] + SHARES_DISPATCH.get(s, [])) for s in FLOW_SCEN}

interval_hours = 24.0 / cs.STEPS_PER_DAY
MARK_EVERY = cs.STEPS_PER_DAY // 12      # an open circle every two hours
# A genuine small multiple: three days side by side, each a power panel over a
# price panel. It stays one figure because the comparison IS between the columns.
fig, axes = plt.subplots(2, 3, figsize=pf.figsize(ratio=0.48), sharex="col",
                         sharey="row", gridspec_kw={"height_ratios": [2, 1]})

def net_kw(profile, mask):
    """Net position of the community as a whole: everyone's import minus
    everyone's export, so PV feeding a neighbour nets out instead of counting
    twice."""
    window = profile.loc[mask]
    return (window["community_import_kwh"].to_numpy(dtype=float)
            - window["community_export_kwh"].to_numpy(dtype=float)) / interval_hours

for col, (label, day) in enumerate(picks):
    ax, axp = axes[0, col], axes[1, col]
    mask = (ref_index >= day) & (ref_index < day + pd.Timedelta(days=1))
    hours = (ref_index[mask] - day).total_seconds() / 3600.0

    # The unbatteried day underneath, in ink rather than a fourth hue, with open
    # circles every two hours so it stays followable under the crossing lines.
    ax.plot(hours, net_kw(BASE_PROFILE, mask), color=MUTED, linewidth=3, zorder=1,
            marker="o", markevery=MARK_EVERY, markersize=6,
            markerfacecolor=SURFACE, markeredgewidth=1.6,
            label="brez baterij" if col == 0 else None)
    for scenario in FLOW_SCEN:
        ax.plot(hours, net_kw(RESULTS[scenario]["community_profile"], mask),
                color=SCEN_COLOR[scenario], linewidth=1.8, zorder=2,
                label=FLOW_LABEL[scenario] if col == 0 else None)

    ax.axhline(0, color=MUTED, linewidth=0.8)
    row = daily.loc[day]
    # A panel heading, not the figure's caption -- set directly so it survives
    # titles=False, the way every panel label in a grid does.
    # ax.set_title(f"{label} — {day:%d.%m.%Y}\n"
    #              f"povprečje {row['mean']:.0f}, od {row['min']:.0f} do "
    #              f"{row['max']:.0f} EUR/MWh", fontsize=10)
    if col == 0:
        ax.set_ylabel("Moč [kW]")

    axp.plot(hours, smp.loc[mask].to_numpy(dtype=float), color=INK_2, linewidth=1.6)
    axp.axhline(0, color=MUTED, linewidth=0.8)
    axp.set_xlim(0, 24)
    axp.set_xticks([0, 6, 12, 18, 24])
    axp.set_xlabel("Ura dneva [h]")
    if col == 0:
        axp.set_ylabel("Cena [EUR/MWh]")

# Figure-level header and keys: these panels are full from top to bottom, and
# chart_frame measures both bands before it lays the axes out.
pf.chart_frame(fig, "Celotna skupnost ob cenovnih skrajnostih leta",
               handles=axes[0, 0].get_legend_handles_labels()[0],
               ncol=len(FLOW_SCEN) + 1)
pf.show(fig, "price_extreme_days", layout="frame", preset="column", ratio=0.6)

daily.loc[[d for _, d in picks]].assign(day=[l for l, _ in picks]).round(1)