### What the battery does to the peak grid import
# Peak import is billed against contracted power, and the block-arbitrage lists
# charge from the grid at the cheapest hour of the day -- a load the house never
# had -- so their peak climbs with the inverter rating rather than falling with
# self-consumption.
#
# Three questions, three sets of axes, one frame prepared here: the kW the
# connection sees, the change each household's own peak went through, and that
# same kW inside each network-tariff block, which is what gets billed.
peak_runs = df.copy()
peak_base = (
    df.loc[df["Capacity_kWh"] == 0.0]
    .set_index(["Label", "Contract"])["Peak_Import_kW"]
)
# 0 kWh included, so every curve starts at the no-battery peak: here that is the
# kW the connection already sees, in the next figure it is 0 % by construction.
peak_runs["Peak_No_Battery_kW"] = [
    peak_base.loc[(lab, t)] for lab, t in zip(peak_runs["Label"], peak_runs["Contract"])
]
peak_runs["Peak_Change_pct"] = 100.0 * (
    peak_runs["Peak_Import_kW"] / peak_runs["Peak_No_Battery_kW"] - 1.0
)
by_cap = peak_runs.groupby(["Contract", "Capacity_kWh"], observed=True)

# The same two columns per block, prepared here so the five figures and their
# read-out cannot read different baselines. Skipped, with a flag the cells below
# honour, when the cache predates the block columns.
BLOCK_PEAKS_READY = (set(BLOCK_PEAK_COLS + BLOCK_AGREED_COLS) <= set(peak_runs.columns)
                     and bool(peak_runs[BLOCK_PEAK_COLS].notna().all().all()))
if BLOCK_PEAKS_READY:
    block_base = (
        peak_runs.loc[peak_runs["Capacity_kWh"] == 0.0]
        .set_index(["Label", "Contract"])[BLOCK_PEAK_COLS]
    )
    for b in TARIFF_BLOCKS:
        base_map = block_base[f"Peak_Import_B{b}_kW"]
        peak_runs[f"Peak_No_Battery_B{b}_kW"] = [
            base_map.loc[(lab, t)]
            for lab, t in zip(peak_runs["Label"], peak_runs["Contract"])
        ]
        # A household that never draws from the grid in a block has no baseline
        # to be a percentage of — NaN, not an infinite improvement.
        peak_runs[f"Peak_Change_B{b}_pct"] = 100.0 * (
            peak_runs[f"Peak_Import_B{b}_kW"]
            / peak_runs[f"Peak_No_Battery_B{b}_kW"].replace(0.0, np.nan) - 1.0
        )

fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.61))
for contract in CONTRACT_ORDER:
    abs_kw = by_cap["Peak_Import_kW"].median().loc[contract]
    ax.plot(abs_kw.index, abs_kw.values, color=CONTRACT_COLOR[contract],
            ls=CONTRACT_DASH[contract], lw=CONTRACT_LW[contract], zorder=3)

base_kw = float(peak_base.groupby(level="Label").median().median())
# Block 1's agreed power, averaged over the months and taken to the median
# household. It is the lowest of the five, hence the one drawn here.
contracted_kw = float(df.groupby("Label")["Contracted_Power_kW"].first().median())
ax.axhline(base_kw, color=BASELINE, lw=1.2, zorder=2)
pf.edge_label(ax, base_kw, f"brez baterije: {base_kw:,.1f} kW", side="left")
ax.axhline(contracted_kw, color=MUTED, lw=1.1, ls=(0, (5, 4)), zorder=2)
pf.edge_label(ax, contracted_kw - 0.8, f"mediana dogovorjene moči v bloku 1: {contracted_kw:,.1f} kW")
ax.set_ylim(bottom=0)
ax.margins(x=0.02)
finish(ax, xlabel="Kapaciteta baterije [kWh]", ylabel="Konica odjema [kW]", yfmt=KW)

pf.chart_frame(fig, f"Konica odjema iz omrežja, mediana {len(LABEL_ORDER)} gospodinjstev",
      f"Najvišji četrturni odjem v letu, mediana po gospodinjstvih. Vodoravni črti sta konica "
      f"brez baterije ({base_kw:,.1f} kW) in mediana dogovorjene obračunske moči v bloku 1 "
      f"({contracted_kw:,.1f} kW), po kateri se obračunava omrežnina za moč. To je celoletna "
      f"vrednost; po časovnih blokih, kot se dejansko obračunava, je razdelana nižje.",
      ncol=3) #handles=contract_handles(),
pf.show(fig, "peak_import_median", layout="frame", preset="column")