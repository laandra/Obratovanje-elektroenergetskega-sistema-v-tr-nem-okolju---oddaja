### Equivalent full cycles vs battery size
fig, ax = plt.subplots()

ax.plot(cap, df_sizing["Equivalent_Full_Cycles"], color=SERIES[2], lw=2,
        marker="o", ms=4, mfc=SURFACE, mew=1.4)
ax.set_ylim(bottom=0)
finish(ax, title="Ekvivalentni polni cikli na leto", xlabel="Kapaciteta baterije [kWh]",
       ylabel="EFC/leto", yfmt=PLAIN)
pf.show(fig, "equivalent_full_cycles")

df_sizing[["Capacity_kWh", "Equivalent_Full_Cycles"]].round(1)