### Diagnostics
fig, ax = plt.subplots()
ax.plot(cap, df_sizing["Discharged_kWh"], color=SERIES[0], lw=2, label="Izpraznjeno iz baterije")
ax.plot(cap, df_sizing["Grid_Charged_kWh"], color=SERIES[1], lw=2, label="Napolnjeno iz omrežja")
ax.axhline(annual_consumption_kwh, color=MUTED, lw=1.1, ls="--")
ax.annotate(f"poraba gospodinjstva {annual_consumption_kwh:,.0f} kWh/a",
            xy=(cap.max(), annual_consumption_kwh), xytext=(-4, 5),
            textcoords="offset points", ha="right", color=INK_2, fontsize=9)
finish(ax, title="Pretok energije skozi baterijo", xlabel="Kapaciteta baterije [kWh]",
       ylabel="Energija [kWh/a]", yfmt=PLAIN)
ax.legend(loc="upper left")
pf.show(fig, "energy_through_battery")

fig, ax = plt.subplots()
ax.plot(cap, df_sizing["Peak_Import_kW"], color=SERIES[0], lw=2)
contracted = float(list(build_env(0.0).contracted_power_kw.values())[0])
ax.axhline(contracted, color=MUTED, lw=1.1, ls="--")
ax.annotate(f"dogovorjena obračunska moč {contracted:,.1f} kW",
            xy=(cap.max(), contracted), xytext=(-4, 5), textcoords="offset points",
            ha="right", color=INK_2, fontsize=9)
finish(ax, title="Konica odjema iz omrežja", xlabel="Kapaciteta baterije [kWh]",
       ylabel="Konica odjema [kW]", yfmt=KW)
pf.show(fig, "peak_grid_import")