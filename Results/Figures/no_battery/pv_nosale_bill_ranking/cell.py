### The ranking with no buyback, and how much of the bill is now beyond reach
by_group_pv0 = df_pv0.pivot_table(index="Option", columns="Dataset",
                                  values="Cost_EUR").reindex(pv0_summary.index)
by_group_pv0_rel = 100.0 * (by_group_pv0 / by_group_pv0.min() - 1.0)

fig, ax = plt.subplots(figsize=pf.figsize(ratio=rows_ratio(len(pv0_summary))))
ranked_bill_panel(ax, pv0_summary, REGIME_COLOR["nosale"],
                  "Brez odkupa presežkov: odloča samo še prevzemna cena",
                  "Povprečni letni račun [EUR/a]")
pf.show(fig, "pv_nosale_bill_ranking")

# With the credit gone the bill is import + fixed + excess, and only the first
# two differ between lists, so the bar splits at what a contract can move.
fig, ax = plt.subplots(figsize=pf.figsize(ratio=rows_ratio(len(pv0_summary))))
ypos = np.arange(len(pv0_summary))[::-1]
imp0 = pv0_summary["Import_EUR"].to_numpy()
fix0 = pv0_summary["Fixed_EUR"].to_numpy()
exc0 = pv0_summary["Excess_Power_EUR"].to_numpy()
# edgecolor=SURFACE gives the 2 px gap between stacked fills.
seg = dict(height=0.68, edgecolor=SURFACE, linewidth=1.6)
ax.barh(ypos, imp0, color=REGIME_COLOR["nosale"], **seg)
ax.barh(ypos, fix0, left=imp0,
        color=pf.mix(REGIME_COLOR["nosale"], "#ffffff", 0.58), **seg)
ax.barh(ypos, exc0, left=imp0 + fix0, color=MUTED, **seg)
ax.set_yticks(ypos, [short_list_name(p) for p in pv0_summary.index], fontsize=8.5)
bar_labels(ax, ypos, (imp0 + fix0 + exc0))
ax.set_xlim(0, (imp0 + fix0 + exc0).max() * 1.14)
finish(ax, title="Kaj cenik še lahko premakne in kaj ne", xlabel="Letni račun [EUR/a]")
# Explicit handles: the bars' SURFACE edge would read as a hollow swatch at
# legend size.
key_below(
    ax,
    [Patch(facecolor=REGIME_COLOR["nosale"], edgecolor="none"),
     Patch(facecolor=pf.mix(REGIME_COLOR["nosale"], "#ffffff", 0.58), edgecolor="none"),
     Patch(facecolor=MUTED, edgecolor="none")],
    ["prevzem -- konkurenčni del",
     "fiksni del (moč, prispevki, nadomestilo)",
     f"presežna moč -- {exc0.mean():.0f} EUR/a, povsod enaka"],
    ncol=1)
ax.grid(axis="x")
ax.spines["left"].set_visible(False)
pf.show(fig, "pv_nosale_bill_composition")

overpay_table(by_group_pv0_rel, REGIME_COLOR["nosale"],
              "Brez odkupa presežkov: preplačilo po tipu gospodinjstva [%]",
              "pv_nosale_overpay_by_group")

anonymise(by_group_pv0_rel).round(2)