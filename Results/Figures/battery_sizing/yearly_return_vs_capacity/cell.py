### The same return, paid yearly: annual saving against the annual battery payment
# The capital spread over the service life as a level annuity -- what a loan at
# DISCOUNT_RATE over BATTERY_LIFETIME_YEARS would charge each year -- plus the
# yearly O&M. Same three quantities as the lifetime chart above, per year:
#
#   earnings         savings(C)
#   yearly payment   C * capex * (a + o)
#   net return       savings - payment = Net_Annual_EUR (section 6's Net_<capex>)
#
# Every curve here is the one above divided by the annuity factor PVF, so the two
# charts agree on the optimal size; this one is in the units of a monthly bill.
earnings_yearly = df_sizing["Savings_EUR"].to_numpy()

fig, ax = plt.subplots()
ax.plot(cap, earnings_yearly, color=INK, lw=2.2, zorder=4)
for capex, econ in lifetime_econ.items():
    colour = CAPEX_SHADE[capex]
    ax.plot(cap, earnings_yearly - econ["Net_Annual_EUR"], color=colour, lw=1.1, ls="--")
    ax.plot(cap, econ["Net_Annual_EUR"], color=colour, lw=1.9)
    best = int(np.argmax(econ["Net_Annual_EUR"]))
    ax.plot([cap.iloc[best]], [econ["Net_Annual_EUR"][best]], marker="o", ms=6, color=colour,
            mec=SURFACE, mew=1.4, zorder=5)
ax.axhline(0, color=MUTED, lw=1.0)

top = float(np.nanmax(earnings_yearly))
ax.set_ylim(-0.9 * top, 1.25 * top)
finish(ax, title="Letni donos: letni prihranek − letno odplačilo baterije",
       xlabel="Kapaciteta baterije [kWh]", ylabel="Letni znesek [EUR/a]", yfmt=EUR)
pf.key_legend(ax, [
    Line2D([], [], color=INK, lw=2.2, label="letni prihranek"),
    Line2D([], [], color=MUTED, lw=1.1, ls="--", label="letno odplačilo z vzdrževanjem"),
    Line2D([], [], color=MUTED, lw=1.9, label="neto letni donos"),
] + [
    Line2D([], [], color=CAPEX_SHADE[c], lw=4, label=f"{c:,.0f} EUR/kWh")
    for c in CAPEX_SCENARIOS_EUR_PER_KWH
], ncol=4)
pf.show(fig, "yearly_return_vs_capacity")

for capex, econ in lifetime_econ.items():
    best = int(np.argmax(econ["Net_Annual_EUR"]))
    if cap.iloc[best] == 0:
        print(f"{capex:6,.0f} EUR/kWh -> no size covers its yearly payment; the best battery is none")
        continue
    print(f"{capex:6,.0f} EUR/kWh -> best {cap.iloc[best]:5.1f} kWh: "
          f"saves {earnings_yearly[best]:7,.0f}, pays {earnings_yearly[best] - econ['Net_Annual_EUR'][best]:7,.0f}, "
          f"net {econ['Net_Annual_EUR'][best]:+7,.0f} EUR/a")