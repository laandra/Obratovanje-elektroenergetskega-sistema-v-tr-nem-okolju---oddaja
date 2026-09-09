by_tariff, _ = rbc.summarize(scored, by=["Tariff", "Controller"])
table = (by_tariff["Gap_pct"].unstack("Tariff")
         .reindex(index=POLICIES, columns=TARIFF_ORDER))

fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.50))
width = 0.8 / len(TARIFF_ORDER)
x = np.arange(len(POLICIES))
for k, tariff in enumerate(TARIFF_ORDER):
    values = table[tariff].to_numpy(dtype=float)
    offset = (k - (len(TARIFF_ORDER) - 1) / 2) * width
    ax.bar(x + offset, values, width=width * 0.92,
           color=pf.mix(INK_2, "#ffffff", 0.72 - 0.22 * k), label=tariff)
ax.set_xticks(x, [CONTROLLER_LABEL[c] for c in POLICIES], rotation=30, ha="right")
ax.legend(loc="upper left", ncols=len(TARIFF_ORDER), title="price list")
finish(ax, title="The gap depends on what the price signal offers",
       ylabel="Gap to the MILP [%]", yfmt=PCT)
pf.show(fig, "gap_by_price_list")
display(table.round(1))