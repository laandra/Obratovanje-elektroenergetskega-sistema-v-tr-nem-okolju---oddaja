### What a shorter planning horizon costs, in % of the achievable saving
n_t = len(TARIFFS_READY)
group_h = 0.78
bar_h = group_h / n_t
base = np.arange(len(STRAT_ORDER))[::-1]


def gap_of(tariff, strat):
    return float(summary.loc[(tariff, strat), "Gap_pct"])


def draw_groups(ax, xmax):
    """One group of bars per strategy, one bar per price list, first list on top."""
    for i, tariff in enumerate(TARIFFS_READY):
        ypos = base + group_h / 2 - bar_h * (i + 0.5)
        gaps = [gap_of(tariff, s) for s in STRAT_ORDER]
        bars = ax.barh(ypos, gaps, height=bar_h * 0.86,   # surface gap between adjacent bars
                       color=[strat_color(tariff, s) for s in STRAT_ORDER],
                       edgecolor=SURFACE, linewidth=0.8)
        for patch, s in zip(bars, STRAT_ORDER):
            hatch = MODE_HATCH[hc.STRATEGIES[s][2]]
            if hatch:                   # carry, so the SOC mode is never colour-only
                patch.set_hatch(hatch)
                patch.set_edgecolor(pf.mix(TARIFF_COLOR[tariff], "#0b0b0b", 0.3))
        for y, v in zip(ypos, gaps):
            # Label only bars that round to something and fit on this axis.
            if v > 0.05 and v < xmax * 0.97:
                ax.annotate(fmt_pct(v), xy=(v, y), xytext=(5, 0), textcoords="offset points",
                            va="center", color=INK_2, fontsize=8)
    ax.axvline(0, color=MUTED, lw=1.1, ls="--")
    ax.set_xlim(0, xmax)
    ax.set_ylim(-0.7, len(STRAT_ORDER) - 0.3)
    ax.set_yticks(base, [LABEL[s] for s in STRAT_ORDER])
    ax.grid(axis="y", visible=False)


# One list usually dwarfs the rest, so the full scale is one figure and the
# others get a zoom in a SECOND figure rather than a panel beside it: half of
# \textwidth is \columnwidth, and neither of these reads at that width.
widest = max(TARIFFS_READY, key=lambda t: max(gap_of(t, s) for s in STRAT_ORDER))
rest = [t for t in TARIFFS_READY if t != widest]
zoom_max = max((gap_of(t, s) for t in rest for s in STRAT_ORDER), default=0.0) * 1.35

fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.62))
draw_groups(ax, max(float(summary["Gap_pct"].max()) * 1.16, 1.0))
finish(ax, title="Koliko stane krajši horizont načrtovanja, po cenikih",
       xlabel="Opuščeni delež prihranka [%]   (0 = celoletni optimum)")
leg = tariff_legend(ax, where="lower right", title="Cenik")
if soc_mode_legend(ax, kind="patch", where="center right", title="Način SOC"):
    ax.add_artist(leg)
pf.show(fig, "horizon_gap_by_tariff")

if rest and zoom_max > 0:
    fig, ax_zoom = plt.subplots(figsize=pf.figsize(ratio=0.62))
    draw_groups(ax_zoom, max(zoom_max, 0.5))
    finish(ax_zoom,
           title=f"Povečava na {', '.join(rest)} ({widest} sega čez desni rob)",
           xlabel="Isti stolpci [%]")
    pf.show(fig, "horizon_gap_by_tariff_zoom")