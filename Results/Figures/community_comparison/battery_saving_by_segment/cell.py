### What the 30 kWh battery is worth
fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.52))

saving = COUNTERFACTUAL.groupby(["Scenario", "segment"])["Saving_EUR"].mean().unstack()
saving = saving.reindex([cs.SCENARIOS[s]["label"] for s in SCEN_ORDER if s != "souporaba"])
x = np.arange(len(saving))
width = 0.36

for i, seg in enumerate(saving.columns):
    ax.bar(x + (i - 0.5) * width, saving[seg], width=width * 0.92,
           color=SEG_COLOR[seg], edgecolor=SURFACE, linewidth=2, label=seg)
    for xi, val in zip(x + (i - 0.5) * width, saving[seg]):
        ax.annotate(f"{val:,.0f}", (xi, val), xytext=(0, 4),
                    textcoords="offset points", ha="center", fontsize=9, color=INK_2)

ax.set_xticks(x)
ax.set_xticklabels(saving.index)
ax.legend(ncol=2, loc="upper left")
finish(ax, title="Letni prihranek s 30 kWh baterijo",
       subtitle="isto gospodinjstvo, obračunano brez baterije, vse drugo nespremenjeno",
       ylabel="prihranek [EUR / leto]", yfmt=EUR)
pf.show(fig, "battery_saving_by_segment")