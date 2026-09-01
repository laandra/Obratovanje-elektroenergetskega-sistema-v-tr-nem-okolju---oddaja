### Annual electricity cost vs battery size
fig, ax = plt.subplots()
cap = df_sizing["Capacity_kWh"]

ax.axhline(cost_no_battery, color=MUTED, lw=1.2, ls="--")
ax.annotate(f"brez baterije: {cost_no_battery:,.0f} EUR/a",
            xy=(cap.max(), cost_no_battery), xytext=(-4, 6),
            textcoords="offset points", ha="right", color=INK_2, fontsize=9)
ax.fill_between(cap, df_sizing["Cost_EUR"], cost_no_battery,
                color=SERIES[0], alpha=0.10, lw=0)
ax.plot(cap, df_sizing["Cost_EUR"], color=SERIES[0], lw=2,
        marker="o", ms=4, mfc=SURFACE, mew=1.4)
ax.axhline(0, color=MUTED, lw=0.8)

ax.annotate(f"{df_sizing['Cost_EUR'].iloc[-1]:,.0f} EUR/a",
            xy=(cap.iloc[-1], df_sizing["Cost_EUR"].iloc[-1]), xytext=(-6, -14),
            textcoords="offset points", ha="right", color=INK, fontsize=9,
            fontweight="semibold")

finish(ax, title="Letni strošek elektrike ob popolnem predvidevanju pada z velikostjo baterije",
       xlabel="Kapaciteta baterije [kWh]", ylabel="Letni strošek [EUR/a]", yfmt=EUR)
pf.show(fig, "cost_vs_capacity")