rules = [c for c in POLICIES]
gap = ranking.loc[rules, "Gap_pct"]
pooled = ranking.loc[rules, "Gap_pct_pooled"]
order = gap.sort_values(ascending=False).index

fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.46))
y = np.arange(len(order))
bars = ax.barh(y, gap[order], height=0.62,
               color=[controller_color(c) for c in order])
# The pooled figure as a tick, so the euro-weighted answer sits beside the
# per-household one instead of in a second chart with a second scale.
ax.scatter(pooled[order], y, s=42, color=INK, zorder=3, label="pooled by euros at stake")
ax.set_yticks(y, [CONTROLLER_LABEL[c] for c in order])
# A label COLUMN rather than a label on each data end: the pooled dots sit close
# to the bar ends and the two would collide on the rules that rank best.
label_x = float(gap.max()) * 1.04
ax.set_xlim(0, label_x * 1.10)
for row, value in zip(y, gap[order]):
    ax.text(label_x, row, f"{value:.0f}%", va="center", ha="left",
            fontsize=9, color=INK_2)
# Outside the axes: inside, the legend's sample dot reads as a data point.
ax.legend(loc="lower right", bbox_to_anchor=(1.0, 1.0))
finish(ax, title="How much of the achievable saving each rule gives up",
       xlabel="gap to the whole-year MILP  [% of achievable saving]", xfmt=PCT)
pf.show(fig, "gap_by_rule")