# What each group had to gain in the first place, so a large gap can be read
# against the size of the prize rather than in isolation.
prize = (cross[cross["Controller"] == "milp_full_period"]
         .groupby("Dataset")
         .agg(Achievable_EUR=("Achievable_EUR", "mean"),
              No_Battery_EUR=("No_Battery_EUR", "mean"))
         .reindex(DATASET_GROUPS))

fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.42))
x = np.arange(len(prize))
bars = ax.bar(x, prize["Achievable_EUR"], width=0.6,
              color=pf.mix(FAMILY_COLOR["reference"], "#ffffff", 0.45))
ax.set_xticks(x, [group_label(g) for g in prize.index], rotation=20, ha="right")
bar_labels(ax, bars, list(prize["Achievable_EUR"]), fmt="{:,.0f}", horizontal=False)
finish(ax, title="What perfect foresight is worth to each household type",
       ylabel="Achievable saving [EUR/a]", yfmt=EUR)
pf.show(fig, "achievable_by_household_type")
display(prize.round(0))