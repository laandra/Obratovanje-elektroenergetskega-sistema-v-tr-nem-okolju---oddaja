### The share of shared energy -- the figure the study is for
# One figure with four lines: one for each battery/scheme combination.
SUBTITLE = (f"Cenik {MAIN_CONFIG}, {len(HOUSEHOLD_KEYS)} gospodinjstev, celo leto 2024, "
            f"interna cena {INTERNAL_PRICE:.3f} EUR/kWh, značilni primer {ZNACILNI_PRIMER}. "
            f"Polna črta = pogodbeni (statični) delež. Oznaka = delež z najnižjim "
            f"računom skupnosti. Barva = shema, slog črte = baterijski scenarij.")

fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.62))
for battery in SWEEP_BATTERIES:
    for scheme in (ccm.SCHEME_SOUPORABA, ccm.SCHEME_SKUPNOST):
        sub = sweep[(sweep["battery"] == battery) & (sweep["scheme"] == scheme)]\
            .sort_values("share")
        color = SCHEME_COLOR[scheme]
        linestyle = "--" if battery == "brez baterije" else "-"
        ax.plot(sub["share"], sub["Community_cost_EUR"], color=color, linewidth=2.0,
                linestyle=linestyle, marker="o", markersize=4.5, markerfacecolor=SURFACE,
                markeredgewidth=1.6,
                label=f"{SCHEME_LABEL[scheme]} — {battery}", zorder=3)
        best = sub.loc[sub["Community_cost_EUR"].idxmin()]
        ax.plot([best["share"]], [best["Community_cost_EUR"]], marker="o", markersize=8,
                color=color, zorder=4)
        ax.annotate(f"{best['share'] * 100:.0f}%", (best["share"], best["Community_cost_EUR"]),
                    xytext=(0, -13), textcoords="offset points", ha="center",
                    color=color, fontsize=8.5, fontweight="bold")
ax.grid(axis="y", linewidth=0.6)
ax.set_axisbelow(True)
finish(ax, xlabel="Pogodbeni delež deljene energije [%]",
       ylabel="Letni račun skupnosti [EUR/a]", yfmt=EUR, xfmt=SHARE)
line_keys = [
    plt.Line2D([], [], color=SCHEME_COLOR[scheme], linestyle=("--" if battery == "brez baterije" else "-"),
               linewidth=2.0, label=f"{SCHEME_LABEL[scheme]} — {battery}")
    for battery in SWEEP_BATTERIES
    for scheme in (ccm.SCHEME_SOUPORABA, ccm.SCHEME_SKUPNOST)
]
pf.chart_frame(fig, "Optimalni delež deljene energije", SUBTITLE,
               handles=line_keys, ncol=2)
pf.show(fig, "share_sweep_bill", layout="frame")