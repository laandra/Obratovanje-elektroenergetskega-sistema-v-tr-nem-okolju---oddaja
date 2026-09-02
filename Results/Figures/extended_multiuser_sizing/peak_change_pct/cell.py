### What the battery does to the peak grid import
# The cost curves say what the battery is worth; this says what it does to the
# connection. Peak import is billed against contracted power under the SI network
# tariff, and the block-arbitrage lists charge from the grid at the cheapest hour
# of the day — a load the house never had — so their peak climbs with the
# inverter rating instead of falling with self-consumption.
peak_base = (
    df.loc[df["Capacity_kWh"] == 0.0]
    .set_index(["Label", "Contract"])["Peak_Import_kW"]
)
# 0 kWh included, so both curves start at the no-battery peak: on the left that
# is the kW the connection already sees, on the right it is 0 % by construction.
peaks = df.copy()
peaks["Peak_No_Battery_kW"] = [
    peak_base.loc[(lab, t)] for lab, t in zip(peaks["Label"], peaks["Contract"])
]
peaks["Peak_Change_pct"] = 100.0 * (
    peaks["Peak_Import_kW"] / peaks["Peak_No_Battery_kW"] - 1.0
)

by_cap = peaks.groupby(["Contract", "Capacity_kWh"], observed=True)
base_kw = float(peak_base.groupby(level="Label").median().median())
contracted_kw = float(df.groupby("Label")["Contracted_Power_kW"].first().median())

# Two figures rather than two panels: kW and % are different scales, and neither
# reads at half of \textwidth.
fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.55))
for contract in CONTRACT_ORDER:
    abs_kw = by_cap["Peak_Import_kW"].median().loc[contract]
    ax.plot(abs_kw.index, abs_kw.values, color=CONTRACT_COLOR[contract],
            ls=CONTRACT_DASH[contract], lw=CONTRACT_LW[contract], zorder=3)
ax.axhline(base_kw, color=BASELINE, lw=1.2, zorder=2)
pf.edge_label(ax, base_kw, f"brez baterije: {base_kw:,.1f} kW", side="left")
ax.axhline(contracted_kw, color=MUTED, lw=1.1, ls=(0, (5, 4)), zorder=2)
pf.edge_label(ax, contracted_kw,
              f"mediana dogovorjene obračunske moči: {contracted_kw:,.1f} kW")
ax.set_ylim(bottom=0)
ax.margins(x=0.02)
finish(ax, xlabel="Kapaciteta baterije [kWh]", ylabel="Konica odjema [kW]", yfmt=KW)
pf.chart_frame(fig, f"Konica odjema iz omrežja, mediana {len(LABEL_ORDER)} gospodinjstev",
      f"Mediana konice, ob konici brez baterije ({base_kw:,.1f} kW) in mediani dogovorjene "
      f"obračunske moči ({contracted_kw:,.1f} kW), po kateri se obračunava omrežnina za moč.",
      handles=contract_handles(), ncol=3)
pf.show(fig, "peak_import_median", layout="frame")

fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.55))
for contract in CONTRACT_ORDER:
    rel = by_cap["Peak_Change_pct"].median().loc[contract]
    lo = by_cap["Peak_Change_pct"].min().loc[contract]
    hi = by_cap["Peak_Change_pct"].max().loc[contract]
    # Band = the households' spread, so a median cannot hide one runaway.
    ax.fill_between(rel.index, lo.values, hi.values, color=CONTRACT_COLOR[contract],
                    alpha=0.10, lw=0, zorder=1)
    ax.plot(rel.index, rel.values, color=CONTRACT_COLOR[contract],
            ls=CONTRACT_DASH[contract], lw=CONTRACT_LW[contract], zorder=3)
ax.axhline(0, color=BASELINE, lw=1.2, zorder=2)
ax.margins(x=0.02)
finish(ax, xlabel="Kapaciteta baterije [kWh]",
       ylabel="Sprememba konice odjema [%]", yfmt=PCT_SIGNED)
pf.chart_frame(fig, "Sprememba glede na isto gospodinjstvo brez baterije",
      f"Vsako gospodinjstvo je primerjano samo s seboj brez baterije in na isti pogodbi: črta "
      f"je mediana, pas je celoten razpon vseh {len(LABEL_ORDER)}. Nad ničlo je baterija "
      f"konico priključka poslabšala, ne izboljšala.",
      handles=contract_handles(), ncol=3)
pf.show(fig, "peak_change_pct", layout="frame")

### The same thing household by household, each on its own scale
small_multiples(
    "Peak_Import_kW",
    "Konica odjema iz omrežja, po gospodinjstvih",
    f"Črtkana črta je konica tega gospodinjstva brez baterije; vsak graf ima svojo skalo v kW, "
    f"zato berite krivuljo glede na črtkano črto v ISTEM grafu, ne med grafi. Moč je omejena na "
    f"min({C_RATE:g} x kapaciteta, {INVERTER_MAX_KW:g} kW), kar je strop, v katerega pogodbe s "
    f"polnjenjem iz omrežja zadenejo od približno {INVERTER_MAX_KW / C_RATE:g} kWh naprej.",
    "Konica odjema [kW]",
    fmt=KW,
    baseline_col="Peak_Import_kW",
    export="peak_import_panels",
)

### Aggregate and extremes, since a median peak is not what gets billed
# On sized runs only: "the worst run" means the worst battery, and every 0 kWh
# row is a 0.0 % change that would sit in the middle of the ranking and drag the
# medians towards zero.
sized_peaks = peaks[peaks["Capacity_kWh"] > 0]
worst_row = sized_peaks.loc[sized_peaks["Peak_Change_pct"].idxmax()]
best_row = sized_peaks.loc[sized_peaks["Peak_Change_pct"].idxmin()]
print(f"Peak grid import across {len(LABEL_ORDER)} households x {len(CONTRACT_ORDER)} contracts "
      f"x {len(BATTERY_SIZES_KWH) - 1} sized runs")
print(f"  no battery, summed over the {len(LABEL_ORDER)} households: "
      f"{peak_base.groupby(level='Label').median().sum():,.1f} kW")
for contract in CONTRACT_ORDER:
    sub = sized_peaks[sized_peaks["Contract"] == contract]
    at_opt = best_table[best_table["Contract"] == contract]
    tag = "  (legacy)" if contract in LEGACY_CONTRACTS else ""
    print(f"  {contract:>12}: median {sub['Peak_Change_pct'].median():+6.1f} % over all sizes, "
          f"{at_opt['Peak_Import_kW'].sum():6.1f} kW summed at the optimal sizes, "
          f"worst single run {sub['Peak_Change_pct'].max():+6.1f} %{tag}")
print(f"  worst: {worst_row['Label']} on {worst_row['Contract']} at {worst_row['Capacity_kWh']:g} kWh — "
      f"{worst_row['Peak_No_Battery_kW']:.1f} -> {worst_row['Peak_Import_kW']:.1f} kW "
      f"({worst_row['Peak_Change_pct']:+.1f} %), {worst_row['Grid_Charged_kWh']:,.0f} kWh/a of it "
      f"charged from the grid")
print(f"  best:  {best_row['Label']} on {best_row['Contract']} at {best_row['Capacity_kWh']:g} kWh — "
      f"{best_row['Peak_No_Battery_kW']:.1f} -> {best_row['Peak_Import_kW']:.1f} kW "
      f"({best_row['Peak_Change_pct']:+.1f} %)")