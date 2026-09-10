### Marginal value of capacity vs what capacity costs
fig, ax = plt.subplots()
mid = (df_sizing["Capacity_kWh"] + df_sizing["Capacity_kWh"].shift()) / 2

ax.plot(mid, df_sizing["Marginal_EUR_per_kWh"], color=SERIES[0], lw=2,
        marker="o", ms=4, mfc=SURFACE, mew=1.4)

for capex in CAPEX_SCENARIOS_EUR_PER_KWH:
    # Capital recovery plus O&M: what owning that kWh costs for a year.
    level = capex * yearly_cost_factor
    ax.axhline(level, color=MUTED, lw=1.1, ls="--")
    ax.annotate(f"{capex:,.0f} EUR/kWh vgrajene kapacitete  ({level:,.1f} EUR/kWh/a)",
                xy=(mid.max(), level), xytext=(-4, 4), textcoords="offset points",
                ha="right", color=INK_2, fontsize=9)

ax.set_ylim(bottom=0)
finish(ax, title="Kje se naslednja kWh hrambe ne izplača več",
       xlabel="Kapaciteta baterije [kWh]", ylabel="Mejna vrednost kapacitete [EUR/kWh/a]", yfmt=EUR)
pf.show(fig, "marginal_value")