### Total return on the investment over the service life, by size and price
# What the battery earns over its whole life against what it costs to own, and
# the difference -- the net return -- for every price scenario of section 1.
# Every figure is a present value at DISCOUNT_RATE over BATTERY_LIFETIME_YEARS,
# taken from Battery_Economics.battery_economics with this study's simpler model
# (no install fee, flat calendar life), so the net line IS section 5b's NPV_EUR.
#
#   earnings         savings(C) * PVF                    one curve: price-free
#   battery price    C * capex * (1 + o * PVF)           purchase + O&M over life
#   net return       earnings - battery price = NPV
#
# The price line is read back as earnings - NPV rather than re-derived, so it
# cannot disagree with the NPV the tables report.
from matplotlib.lines import Line2D

# The scenarios are an ordered price, not categories: one hue, darker = dearer,
# run from a tint to a shade of it so five steps stay apart on paper.
CAPEX_SHADE = {
    capex: pf.mix(pf.mix(SERIES[0], SURFACE, 0.55), pf.mix(SERIES[0], INK, 0.55), t)
    for capex, t in zip(CAPEX_SCENARIOS_EUR_PER_KWH,
                        np.linspace(0.0, 1.0, len(CAPEX_SCENARIOS_EUR_PER_KWH)))
}

lifetime_econ = {
    capex: be.battery_economics(
        df_sizing["Savings_EUR"].to_numpy(),
        df_sizing["Capacity_kWh"].to_numpy(),
        df_sizing["Equivalent_Full_Cycles"].to_numpy(),
        capex_eur_per_kwh=capex,
        capex_fixed_eur=0.0,
        opex_frac=OPEX_FRAC_OF_CAPEX_PER_YEAR,
        calendar_life_y=BATTERY_LIFETIME_YEARS,
        cycle_limit_efc=None,
        discount_rate=DISCOUNT_RATE,
    )
    for capex in CAPEX_SCENARIOS_EUR_PER_KWH
}
lifetime_pvf = be.present_value_factor(DISCOUNT_RATE, BATTERY_LIFETIME_YEARS)
earnings_total = df_sizing["Savings_EUR"].to_numpy() * lifetime_pvf

fig, ax = plt.subplots()
ax.plot(cap, earnings_total, color=INK, lw=2.2, zorder=4)
for capex, econ in lifetime_econ.items():
    colour = CAPEX_SHADE[capex]
    ax.plot(cap, earnings_total - econ["NPV_EUR"], color=colour, lw=1.1, ls="--")
    ax.plot(cap, econ["NPV_EUR"], color=colour, lw=1.9)
    best = int(np.argmax(econ["NPV_EUR"]))
    ax.plot([cap.iloc[best]], [econ["NPV_EUR"][best]], marker="o", ms=6, color=colour,
            mec=SURFACE, mew=1.4, zorder=5)
ax.axhline(0, color=MUTED, lw=1.0)

# The dearest price lines leave the chart within a few kWh; the window is set
# by what the battery can earn, which is the scale the decision is made on.
top = float(np.nanmax(earnings_total))
ax.set_ylim(-0.9 * top, 1.25 * top)
finish(ax, title=f"Skupni donos naložbe v {BATTERY_LIFETIME_YEARS:.0f} letih: "
                 "prihranek − cena baterije",
       xlabel="Kapaciteta baterije [kWh]", ylabel="Sedanja vrednost [EUR]", yfmt=EUR)
pf.key_legend(ax, [
    Line2D([], [], color=INK, lw=2.2, label="prihranek"),
    Line2D([], [], color=MUTED, lw=1.1, ls="--", label="cena baterije z vzdrževanjem"),
    Line2D([], [], color=MUTED, lw=1.9, label="neto donos"),
] + [
    Line2D([], [], color=CAPEX_SHADE[c], lw=4, label=f"{c:,.0f} EUR/kWh")
    for c in CAPEX_SCENARIOS_EUR_PER_KWH
], ncol=4)
pf.show(fig, "total_return_vs_capacity")

for capex, econ in lifetime_econ.items():
    best = int(np.argmax(econ["NPV_EUR"]))
    if cap.iloc[best] == 0:
        print(f"{capex:6,.0f} EUR/kWh -> no size returns its price; the best battery is none")
        continue
    print(f"{capex:6,.0f} EUR/kWh -> best {cap.iloc[best]:5.1f} kWh: "
          f"earns {earnings_total[best]:9,.0f}, costs {earnings_total[best] - econ['NPV_EUR'][best]:9,.0f}, "
          f"net {econ['NPV_EUR'][best]:+9,.0f} EUR  (ROI {econ['ROI_pct'][best]:+6.1f} %, "
          f"IRR {econ['IRR_pct'][best]:5.1f} %)")