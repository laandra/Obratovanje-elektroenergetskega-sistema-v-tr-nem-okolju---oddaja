### Net annual benefit
fig, ax = plt.subplots()

optima = {}
label_offsets = [(12, 6), (14, -6), (14, -24)]
for capex, colour, offset in zip(CAPEX_SCENARIOS_EUR_PER_KWH, SERIES, label_offsets):
    net = df_sizing[f"Net_{int(capex)}"]
    ax.plot(cap, net, color=colour, lw=2, label=f"{capex:,.0f} EUR/kWh vgrajene kapacitete")
    best = int(net.idxmax())
    optima[capex] = (float(df_sizing["Capacity_kWh"][best]), float(net[best]))
    ax.plot([optima[capex][0]], [optima[capex][1]], marker="o", ms=9,
            color=colour, mfc=colour, mec=SURFACE, mew=2, zorder=3)
    ax.annotate(f"{optima[capex][0]:g} kWh  ({optima[capex][1]:,.0f} EUR/a)",
                xy=optima[capex], xytext=offset, textcoords="offset points",
                color=INK, fontsize=9, fontweight="semibold")

ax.axhline(0, color=MUTED, lw=1.0)
best_net = max(v for _, v in optima.values())
ax.set_ylim(-max(300.0, 3.5 * best_net), max(60.0, 1.6 * best_net))
finish(ax, title="Neto letna korist = prihranek MILP − letni strošek baterije",
       xlabel="Kapaciteta baterije [kWh]", ylabel="Neto korist [EUR/a]", yfmt=EUR)
ax.legend(loc="lower left")
pf.show(fig, "net_annual_benefit", save_pdf=True)

for capex, (size, net) in optima.items():
    print(f"{capex:6.0f} EUR/kWh installed -> optimal {size:5.1f} kWh, "
          f"net {net:8.2f} EUR/a")