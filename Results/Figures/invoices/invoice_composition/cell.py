PART_COLORS = {
    "Energija": SERIES[0],
    "Omrežnina": SERIES[1],
    "Prispevki in trošarina": SERIES[2],
    "Poslovanje": SERIES[3],
    "DDV": "#e87ba4",          # a fifth part; SERIES holds four categorical slots
}

labels = list(composition.index)
x = range(len(labels))
fig, (ax_bill, ax_price) = plt.subplots(
    2, 1, figsize=plots.figsize(ratio=0.78),
    sharex=True, height_ratios=[3, 2], constrained_layout=True,
)

bottom = [0.0] * len(labels)
for part, color in PART_COLORS.items():
    values = composition[part].tolist()
    # A surface-colored edge is the 2px gap between stacked segments.
    ax_bill.bar(x, values, bottom=bottom, color=color, label=part,
                edgecolor=SURFACE, linewidth=1.5, width=0.72)
    bottom = [b + v for b, v in zip(bottom, values)]

# One direct label per bar -- the total -- rather than a number on every segment.
for xi, total in zip(x, composition["Za plačilo"]):
    ax_bill.text(xi, total + max(bottom) * 0.02, f"{total:,.1f}", ha="center",
                 va="bottom", fontsize=8.5, color=INK)

ax_bill.grid(axis="y")
finish(ax_bill,
       title=f"{household.name} — sestava mesečnega računa ({household.paket_id})",
       ylabel="Za plačilo [EUR]", yfmt=EUR)
ax_bill.legend(loc="lower left", bbox_to_anchor=(0, 1.005), ncol=5, frameon=False,
               fontsize=8.5, labelcolor=INK_2, handlelength=1.1, columnspacing=1.3)
ax_bill.set_ylim(0, max(bottom) * 1.16)

prices = composition["Povprečna cena [EUR/kWh]"].tolist()
ax_price.plot(x, prices, color=PART_COLORS["Energija"], linewidth=2,
              marker="o", markersize=6, markeredgecolor=SURFACE, markeredgewidth=1.5)
ax_price.annotate(f"{prices[-1]:.3f}", (len(labels) - 1, prices[-1]),
                  textcoords="offset points", xytext=(6, 0), va="center",
                  fontsize=8.5, color=INK)
ax_price.grid(axis="y")
finish(ax_price, ylabel="Povprečna cena [EUR/kWh]")
ax_price.set_xticks(list(x))
ax_price.set_xticklabels(labels, rotation=45, ha="right")
ax_price.margins(x=0.04)

# constrained_layout already laid this out; a tight_layout pass would undo it.
plots.show(fig, "invoice_composition", layout="auto")