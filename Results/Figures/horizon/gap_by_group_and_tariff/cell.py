### Does the household type change the answer? One panel per price list, one hue per panel
plot_cols = [s for s in STRAT_ORDER if s != "full_period_carry"]
vmax = float(np.nanmax(by_group[[(t, s) for t in TARIFFS_READY for s in plot_cols]].to_numpy()))

# Stacked rather than side by side: the panels share the strategy axis, and one
# heatmap per row is still readable at \\textwidth.
fig, axes = plt.subplots(len(TARIFFS_READY), 1, squeeze=False,
                         figsize=pf.figsize(ratio=0.36 * len(TARIFFS_READY)))

for ax, tariff in zip(axes[:, 0], TARIFFS_READY):
    values = by_group[[(tariff, s) for s in plot_cols]].to_numpy()
    im = ax.imshow(values, cmap=TARIFF_RAMP[tariff], aspect="auto", vmin=0, vmax=vmax)

    ax.set_xticks(range(len(plot_cols)),
                  [f"{LABEL[s]}\n{hc.STRATEGIES[s][2]}" for s in plot_cols], fontsize=8.5)
    ax.set_yticks(range(by_group.shape[0]), by_group.index, fontsize=9)
    ax.grid(visible=False)
    for r in range(values.shape[0]):
        for c in range(values.shape[1]):
            v = values[r, c]
            ax.annotate(fmt_pct(v), xy=(c, r), ha="center", va="center", fontsize=8.5,
                        color=SURFACE if v > 0.55 * vmax else INK, fontweight="semibold")
    panel_title(ax, tariff)
    cbar = fig.colorbar(im, ax=ax, pad=0.015)
    cbar.set_label("Vrzel [%]", color=INK_2)
    cbar.outline.set_visible(False)

pf.chart_frame(fig, f"Vrzel po tipu gospodinjstva in ceniku, enaka skala 0-{vmax:.0f} % "
                    "na vseh grafih")
pf.show(fig, "gap_by_group_and_tariff", layout="frame")