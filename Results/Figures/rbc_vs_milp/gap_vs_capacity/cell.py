by_capacity, _ = rbc.summarize(cross, by=["Capacity_kWh", "Controller"])
gap_by_cap = by_capacity["Gap_pct"].unstack("Controller").reindex(columns=POLICIES)
save_by_cap = (rbc.summarize(cross, by=["Capacity_kWh", "Controller"])[0]["Savings_EUR"]
               .unstack("Controller").reindex(columns=POLICIES))
milp_saving = (cross[cross["Controller"] == "milp_full_period"]
               .groupby("Capacity_kWh")["Savings_EUR"].mean())

# Two figures rather than two panels: half of \textwidth is \columnwidth, and
# eight labelled lines do not read at that width. Same cell, one pf.show each.
# Four of the eight lines are blue, so the family legend alone cannot identify a
# line -- each figure carries the full controller key underneath.
CONTROLLER_KEYS = [Line2D([], [], color=controller_color(c), lw=2,
                          label=CONTROLLER_LABEL[c]) for c in POLICIES]

fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.52))
for name in POLICIES:
    ax.plot(gap_by_cap.index, gap_by_cap[name], marker="o", ms=5, lw=2,
            color=controller_color(name), label=CONTROLLER_LABEL[name])
ax.set_xticks(CAPACITIES_KWH)
finish(ax, title="The gap widens with the pack", xlabel="Nameplate capacity [kWh]",
       ylabel="Gap to the MILP [%]", yfmt=PCT)
pf.key_legend(ax, CONTROLLER_KEYS, ncol=3, fontsize=9)
pf.show(fig, "gap_vs_capacity")

fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.52))
for name in POLICIES:
    ax.plot(save_by_cap.index, save_by_cap[name], marker="o", ms=5, lw=2,
            color=controller_color(name))
ax.plot(milp_saving.index, milp_saving, lw=2.2, ls="--", color=INK, marker="D", ms=5,
        label=CONTROLLER_LABEL["milp_full_period"])
ax.axhline(0, color=MUTED, lw=1)
ax.set_xticks(CAPACITIES_KWH)
finish(ax, title="What each rule actually earns", xlabel="Nameplate capacity [kWh]",
       ylabel="Saving vs no battery [EUR/a]", yfmt=EUR)
pf.key_legend(ax, CONTROLLER_KEYS
              + [Line2D([], [], color=INK, lw=2.2, ls="--", marker="D", ms=5,
                        label=CONTROLLER_LABEL["milp_full_period"])],
              ncol=3, fontsize=9)
pf.show(fig, "saving_vs_capacity")
display(gap_by_cap.round(1))