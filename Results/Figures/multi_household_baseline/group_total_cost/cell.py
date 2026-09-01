# Quick visual for group total comparison.
group_plot_df = group_only[["scenario", "total_cost_eur"]].copy()
ax = group_plot_df.plot(kind="bar", x="scenario", y="total_cost_eur",
                        legend=False, color=SERIES[0])
finish(ax, title="Primerjava skupnega stroška skupine",
       xlabel="Scenarij", ylabel="Skupni strošek [EUR]", yfmt=EUR)
pf.show(ax, "group_total_cost")