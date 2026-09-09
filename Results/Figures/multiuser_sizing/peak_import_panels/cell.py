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
    baseline_col="Peak_Import_kW",    export="peak_import_panels",
)

### Aggregate and extremes, since a median peak is not what gets billed
# On sized runs only: every 0 kWh row is a 0.0 % change that would sit in the
# middle of the ranking and drag the medians towards zero.
sized_peaks = peak_runs[peak_runs["Capacity_kWh"] > 0]
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