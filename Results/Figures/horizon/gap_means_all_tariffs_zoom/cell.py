### Vsi ceniki na eni osi: povprečje po strategijah, ena pika na cenik
# The same averages on one shared axis, one dot per (cenik, strategija), so the
# ranking between lists reads directly. The thin bar behind each dot is
# best..worst household on that list.
row_off = np.linspace(0.26, -0.26, len(TARIFFS_READY))   # one lane per list inside a strategy band
base = np.arange(len(STRAT_ORDER))[::-1]


def draw_means(ax, xmax, labels=True):
    for i, tariff in enumerate(TARIFFS_READY):
        ypos = base + row_off[i]
        for y, strat in zip(ypos, STRAT_ORDER):
            row = summary.loc[(tariff, strat)]
            mean, lo, hi = (float(row["Gap_pct"]), float(row["Best_Gap_pct"]),
                            float(row["Worst_Gap_pct"]))
            ax.plot([lo, hi], [y, y], color=TARIFF_COLOR[tariff], lw=1.4, alpha=0.35,
                    solid_capstyle="round", zorder=2)
            ax.scatter([mean], [y], s=95, marker=MODE_MARKER[hc.STRATEGIES[strat][2]],
                       color=strat_color(tariff, strat), edgecolor=TARIFF_COLOR[tariff],
                       lw=1.0, zorder=4)
            # Direct value labels, so no dot is read by colour alone.
            if labels and mean < xmax * 0.93:
                ax.annotate(fmt_pct(mean), xy=(mean, y), xytext=(7, 0),
                            textcoords="offset points", va="center",
                            color=INK_2, fontsize=7.5)
    for y in base[:-1] - 0.5:           # one separator between strategy bands
        ax.axhline(y, color=pf.GRID, lw=0.8, zorder=1)
    ax.axvline(0, color=MUTED, lw=1.1, ls="--", zorder=1)
    ax.set_xlim(-xmax * 0.02, xmax)
    ax.set_ylim(-0.7, len(STRAT_ORDER) - 0.3)
    ax.set_yticks(base, [LABEL[s] for s in STRAT_ORDER])
    ax.grid(axis="y", visible=False)


# Same full-scale / zoom split as the bar chart, and for the same reason it is
# two figures rather than two panels. The zoom is scaled on the averages, so the
# wider lists' spread bars run off its right edge.
widest = max(TARIFFS_READY,
             key=lambda t: max(float(summary.loc[(t, s), "Gap_pct"]) for s in STRAT_ORDER))
rest = [t for t in TARIFFS_READY if t != widest]
zoom_max = max((float(summary.loc[(t, s), "Gap_pct"]) for t in rest for s in STRAT_ORDER),
               default=0.0) * 1.45

fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.62))
draw_means(ax, max(float(summary["Worst_Gap_pct"].max()) * 1.06, 1.0))
finish(ax, title="Povprečje vseh cenikov na eni osi",
       xlabel="Povprečna vrzel [%]")
leg = tariff_legend(ax, where="lower right", title="Cenik")
if soc_mode_legend(ax, kind="marker", where="center right", title="Način SOC"):
    ax.add_artist(leg)
pf.show(fig, "gap_means_all_tariffs")

if rest and zoom_max > 0:
    fig, ax_zoom = plt.subplots(figsize=pf.figsize(ratio=0.62))
    draw_means(ax_zoom, max(zoom_max, 0.5))
    finish(ax_zoom,
           title=f"Povečava na {', '.join(rest)} "
                 f"({widest} in daljši razponi segajo čez desni rob)",
           xlabel="Povprečna vrzel [%]")
    pf.show(fig, "gap_means_all_tariffs_zoom")