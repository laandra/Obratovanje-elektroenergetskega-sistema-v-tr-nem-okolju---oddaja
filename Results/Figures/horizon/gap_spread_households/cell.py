### Spread across households: one dot per household-unit, one panel per price list
# pf.panel_grid scales the panel text to the FINAL panel width, which is what
# keeps a row of four panels legible once it is squeezed to \textwidth.
fig, axes = pf.panel_grid(len(TARIFFS_READY), ncols=len(TARIFFS_READY),
                          panel=(4.0, 5.2), sharex=True, sharey=True)
rng = np.random.default_rng(0)
xmax = float(df_scored["Gap_pct"].max())

for ax, tariff in zip(axes, TARIFFS_READY):
    sub = df_scored[df_scored["Tariff"] == tariff]
    for i, strat in enumerate(STRAT_ORDER):
        y = len(STRAT_ORDER) - 1 - i
        vals = sub.loc[sub["Strategy"] == strat, "Gap_pct"]
        soc_mode = hc.STRATEGIES[strat][2]
        ax.scatter(vals, y + rng.uniform(-0.17, 0.17, len(vals)), s=30,
                   marker=MODE_MARKER[soc_mode], color=strat_color(tariff, strat),
                   alpha=0.6, lw=0.7, edgecolor=SURFACE, zorder=3)
        ax.scatter([vals.mean()], [y], s=140, marker="|", color=INK, lw=2.0, zorder=4)
    ax.axvline(0, color=MUTED, lw=1.1, ls="--")
    panel_title(ax, tariff)
    ax.set_xlabel("Vrzel [%]")
    ax.grid(axis="y", visible=False)

axes[0].set_yticks(np.arange(len(STRAT_ORDER))[::-1], [LABEL[s] for s in STRAT_ORDER])
axes[0].set_xlim(-0.6, xmax * 1.06)

# One figure-level header and one shared key, measured in inches, in place of
# suptitle + legend + tight_layout.
pf.chart_frame(fig, "Vsako gospodinjstvo, vsaka strategija, vsak cenik",
               # chart_frame draws fig.legend, which reads each handle's own
               # label -- there is no labels= to pass alongside.
               handles=[plt.Line2D([], [], marker=MODE_MARKER[m], ls="", ms=8,
                                   color=MUTED, label=MODE_LABEL[m])
                        for m in SOC_MODES] if len(SOC_MODES) > 1 else None,
               ncol=2)
pf.show(fig, "gap_spread_households", layout="frame")