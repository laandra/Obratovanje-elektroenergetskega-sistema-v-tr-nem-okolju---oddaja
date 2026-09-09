### The same ranking per household type, absolute and relative to that group's best
# Two figures, not two panels: half of \textwidth is \columnwidth, and a 25-row
# bar chart squeezed into it is unreadable. Same cell, one pf.show each.
by_group_cost = df_no_pv.pivot_table(index="Option", columns="Dataset",
                                     values="Cost_EUR").reindex(no_pv_summary.index)
by_group_rel = 100.0 * (by_group_cost / by_group_cost.min() - 1.0)

groups = list(by_group_cost.columns)
GROUP_SHADE = group_shades(groups)

fig, ax = plt.subplots(figsize=pf.figsize(ratio=rows_ratio(len(by_group_cost))))
ypos = np.arange(len(by_group_cost))[::-1]
bar_h = 0.80 / len(groups)
for i, g in enumerate(groups):
    ax.barh(ypos + 0.40 - bar_h * (i + 0.5), by_group_cost[g],
            height=bar_h * 0.86, color=GROUP_SHADE[i], label=group_label(g))
ax.set_yticks(ypos, [short_list_name(p) for p in by_group_cost.index], fontsize=8)
finish(ax, title="Brez PV, brez baterije: edini vzvod je pogodba",
       xlabel="Letni račun, brez PV in baterije [EUR/a]")
key_below(ax, [Patch(facecolor=c) for c in GROUP_SHADE],
          [group_label(g) for g in groups], ncol=4,
          title="tip gospodinjstva", title_fontsize=8)
ax.grid(axis="x")
ax.spines["left"].set_visible(False)
pf.show(fig, "no_pv_bill_by_group")

# Relative penalty against the cheapest list for that same household type: a
# magnitude with a floor at 0 %, so one hue ramped light -> dark. No PV means no
# export, so this chapter takes the neutral slot rather than a regime hue.
fig, ax = plt.subplots(figsize=pf.figsize(ratio=rows_ratio(len(by_group_rel),
                                                           per_row=0.30)))
overpay_heatmap(ax, by_group_rel, INK_2,
                "Brez PV: preplačilo glede na najcenejši cenik te skupine [%]",
                fig=fig, cell_fontsize=7.0)
pf.show(fig, "no_pv_overpay_by_group")

anonymise(by_group_rel).round(2)