### The ranking, and where each list's bill comes from
by_group_pv = df_pv.pivot_table(index="Option", columns="Dataset",
                                values="Cost_EUR").reindex(pv_summary.index)
by_group_pv_rel = 100.0 * (by_group_pv / by_group_pv.min() - 1.0)

fig, ax = plt.subplots(figsize=pf.figsize(ratio=rows_ratio(len(pv_summary))))
ranked_bill_panel(ax, pv_summary, REGIME_COLOR["credited"],
                  "S PV, brez baterije: cenik odloča o prevzemni ceni in o odkupu presežkov",
                  "Povprečni letni račun [EUR/a]")
pf.show(fig, "pv_bill_ranking")

# The composition, on the same row order: import against what the buyback gives
# back, as two stacked parts of one bar with a 2 px surface gap.
fig, ax = plt.subplots(figsize=pf.figsize(ratio=rows_ratio(len(pv_summary))))
ypos = np.arange(len(pv_summary))[::-1]
imp = pv_summary["Import_EUR"].to_numpy()
cred = pv_summary["Export_Credit_EUR"].to_numpy()
ax.barh(ypos, imp, height=0.68, color=pf.mix(REGIME_COLOR["credited"], "#ffffff", 0.55),
        label="prevzem (z omrežnino in dajatvami)")
ax.barh(ypos, -cred, height=0.68, color=REGIME_COLOR["credited"],
        label="dobropis za oddane presežke")
ax.axvline(0, color=INK_2, lw=1.0, zorder=4)
ax.set_yticks(ypos, [short_list_name(p) for p in pv_summary.index], fontsize=8.5)
for y, i, c in zip(ypos, imp, cred):
    ax.text(i + imp.max() * 0.015, y, f"{i:.0f}", va="center", ha="left",
            fontsize=8, color=INK_2)
    ax.text(-c - imp.max() * 0.015, y, "0" if c < 0.5 else f"−{c:.0f}",
            va="center", ha="right", fontsize=8, color=INK_2)
ax.set_xlim(-imp.max() * 0.42, imp.max() * 1.16)
finish(ax, title="S PV: iz česa je sestavljen energijski del računa",
       xlabel="Energijski del letnega računa [EUR/a]")
key_below(ax, [Patch(facecolor=pf.mix(REGIME_COLOR["credited"], "#ffffff", 0.55)),
               Patch(facecolor=REGIME_COLOR["credited"])],
          ["prevzem (z omrežnino in dajatvami)",
           "dobropis za presežke"], ncol=2)
ax.grid(axis="x")
ax.spines["left"].set_visible(False)
pf.show(fig, "pv_bill_composition")

fig, ax = plt.subplots(figsize=pf.figsize(ratio=rows_ratio(len(by_group_pv_rel),
                                                           per_row=0.30)))
overpay_heatmap(ax, by_group_pv_rel, REGIME_COLOR["credited"],
                "S PV, presežke odkupi dobavitelj: preplačilo po tipu gospodinjstva [%]",
                fig=fig)
pf.show(fig, "pv_overpay_by_group", preset="column")

anonymise(by_group_pv_rel).round(2)