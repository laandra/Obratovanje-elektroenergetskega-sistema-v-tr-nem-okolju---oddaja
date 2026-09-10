### The share of shared energy -- the figure the study is for
# One figure per battery scenario, not two panels: half of \textwidth is
# \columnwidth, and a curve with its optimum labelled does not read there.
SUBTITLE = (f"Cenik {MAIN_CONFIG}, {len(HOUSEHOLD_KEYS)} gospodinjstev, celo leto 2024, "
            f"interna cena {INTERNAL_PRICE:.3f} EUR/kWh, značilni primer {ZNACILNI_PRIMER}. "
            f"Polna črta = pogodbeni (statični) delež, črtkano = prosta razdelitev po "
            f"intervalih. Oznaka = delež z najnižjim računom skupnosti. Razmik med polno in "
            f"črtkano črto je cena tega, da je delež v pogodbi fiksen.")

for battery in SWEEP_BATTERIES:
    fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.55))
    baseline = float(ind[ind["battery"] == battery]["Community_cost_EUR"].iloc[0])
    ax.axhline(baseline, color=MUTED, linewidth=1.0, linestyle=":", zorder=1)
    ax.annotate("brez delitve", (0.02, baseline), xytext=(0, 4), textcoords="offset points",
                color=MUTED, fontsize=8, va="bottom")
    for scheme in (ccm.SCHEME_SOUPORABA, ccm.SCHEME_SKUPNOST):
        sub = sweep[(sweep["battery"] == battery) & (sweep["scheme"] == scheme)
                    ].sort_values("share")
        color = SCHEME_COLOR[scheme]
        ax.plot(sub["share"], sub["Community_cost_EUR"], color=color, linewidth=2.0,
                marker="o", markersize=4.5, markerfacecolor=SURFACE, markeredgewidth=1.6,
                label=SCHEME_LABEL[scheme], zorder=3)
        free = dyn[(dyn["battery"] == battery) & (dyn["scheme"] == scheme)]
        if len(free):
            level = float(free["Community_cost_EUR"].iloc[0])
            ax.axhline(level, color=color, linewidth=1.0, linestyle="--", alpha=0.65, zorder=2)
        best = sub.loc[sub["Community_cost_EUR"].idxmin()]
        ax.plot([best["share"]], [best["Community_cost_EUR"]], marker="o", markersize=8,
                color=color, zorder=4)
        # The x axis already says [%]; the callout is the value, not the unit.
        ax.annotate(f"{best['share'] * 100:.0f}", (best["share"], best["Community_cost_EUR"]),
                    xytext=(0, -13), textcoords="offset points", ha="center",
                    color=color, fontsize=8.5, fontweight="bold")
    ax.grid(axis="y", linewidth=0.6)
    ax.set_axisbelow(True)
    finish(ax, xlabel="Pogodbeni delež deljene energije [%]",
           ylabel="Letni račun skupnosti [EUR/a]", yfmt=EUR, xfmt=SHARE)
    pf.chart_frame(fig, f"Optimalni delež deljene energije — {battery}", SUBTITLE,
                   handles=scheme_keys((ccm.SCHEME_SOUPORABA, ccm.SCHEME_SKUPNOST)), ncol=2)
    pf.show(fig, f"share_sweep_bill_{pf.slug(battery)}", layout="frame")