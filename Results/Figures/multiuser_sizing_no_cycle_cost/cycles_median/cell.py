### The same usage question asked of the whole sample at once
# Same metric as the panels above, one pair of axes, medians -- the picture
# behind table 8.6.
#
# Cycles rather than kWh through the store, because cycles divide the throughput
# by the capacity it moved through and so compare across capacities and against
# the pack's own cycle budget. Median rather than mean, because these households
# differ several-fold in annual consumption.
fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.44))
usage = df.groupby(["Contract", "Capacity_kWh"], observed=True)

# The cycle budget first, so the curves sit on top of it: a curve above the line
# wears the pack out before its calendar warranty runs out.
efc_budget = BATTERY_CYCLE_LIMIT_EFC / BATTERY_CALENDAR_LIFE_Y
ax.axhline(efc_budget, color=MUTED, lw=1.1, ls=(0, (5, 4)), zorder=1)
pf.edge_label(ax, efc_budget,
           f"{efc_budget:,.0f} ciklov/leto — {BATTERY_CYCLE_LIMIT_EFC:,} EFC v "
           f"{BATTERY_CALENDAR_LIFE_Y} letih")

drawn = []
for contract in CONTRACT_ORDER:
    series = usage["Equivalent_Full_Cycles"].median().loc[contract]
    ls = CONTRACT_DASH[contract]
    # A curve that coincides with one already drawn is painted over entirely.
    # Shifting the dash phase by half a period puts the two colours in alternate
    # dashes along the same line, moving no data and no line style.
    if isinstance(ls, tuple) and any(np.allclose(series.values, prev, rtol=1e-3, atol=1e-6)
                                     for prev in drawn):
        ls = (ls[0] + sum(ls[1]) / 2.0, ls[1])
    drawn.append(series.values)
    ax.plot(series.index, series.values, color=CONTRACT_COLOR[contract],
            ls=ls, lw=CONTRACT_LW[contract], solid_capstyle="round", zorder=3)

ax.set_ylim(bottom=0)
ax.margins(x=0.02)
finish(ax, xlabel="Kapaciteta baterije [kWh]",
       ylabel="Ekvivalentni polni cikli [1/a]", yfmt=PLAIN)

# Two results stated in the subtitle, both of which otherwise read as a bug:
#
# 1. Redni 1T lies on the floor. A single ET rate leaves only the network energy
#    charge to arbitrage, ~0.011 EUR/kWh between blocks, against a round trip
#    costing ~0.016. What remains is self-consumption and the odd peak shave.
# 2. Curves overlap in pairs. Dispatch follows price differences across the day,
#    not the level: GENI_REDNI and GENI_FIKSNI carry the same 0.0220 VT-MT
#    spread, GENI_SAMO_AKTIVNI and GENI_SAMO_FIKSNI the same four-block spread.
#    Same spread, same trajectory, different bill.
roundtrip_loss_pct = 100.0 * (1.0 / (CHARGE_EFFICIENCY * DISCHARGE_EFFICIENCY) - 1.0)
n_pv = int(sum(HAS_PV.values()))
pf.chart_frame(fig, "Koliko je baterija sploh v uporabi",
      f"Mediana po {len(LABEL_ORDER)} gospodinjstvih, z začetkom pri izračunu brez baterije pri "
      f"0 kWh, kjer je ciklov po definiciji nič. Redni 1T leži tik nad ničlo: enotna tarifa nima "
      f"cenovnega razpona čez dan, ki bi pokril {roundtrip_loss_pct:.1f} % izgube krožnega cikla, "
      f"zato baterijo poganja le lastna raba PV — {len(LABEL_ORDER) - n_pv} gospodinjstev brez "
      f"PV je na tej pogodbi tako rekoč ne uporabi. Pari krivulj se prekrivajo (Aktivni s "
      f"Fiksni, Redni 2T s Fiksni BO): dispečiranje določa razpon cen čez dan in ne njihova "
      f"raven, razpon pa je pri teh cenikih isti — kjer sta krivulji povsem enaki, je črtkanje "
      f"zamaknjeno, da se vidita obe barvi. Redni + NM je sklenljiv le s PV, zato je "
      f"njegova mediana po {n_pv} gospodinjstvih in ne po vseh.",
      handles=contract_handles())
pf.show(fig, "cycles_median", layout="frame")

# The claim in the subtitle, as numbers. The threshold is about the pack rather
# than the money: under a cycle a month the store spends the year standing
# still.
IDLE_EFC_PER_YEAR = 12.0
peak_efc = usage["Equivalent_Full_Cycles"].median().groupby("Contract", observed=True).max()
best_efc = (df[df["Capacity_kWh"] > 0]
            .groupby(["Contract", "Label"], observed=True)["Equivalent_Full_Cycles"].max())
print(f"Peak median equivalent full cycles per year, over {len(LABEL_ORDER)} households, "
      f"and how many of them never reach {IDLE_EFC_PER_YEAR:.0f} EFC/a at ANY capacity:")
for contract, efc in peak_efc.sort_values(ascending=False).items():
    idle = best_efc.loc[contract]
    idle = idle[idle < IDLE_EFC_PER_YEAR]
    note = ("" if idle.empty else
            f"   <- idle for {len(idle)} of {len(LABEL_ORDER)}: "
            + ", ".join(sorted(idle.index)))
    print(f"  {contract:<13}{efc:7.1f}{note}")