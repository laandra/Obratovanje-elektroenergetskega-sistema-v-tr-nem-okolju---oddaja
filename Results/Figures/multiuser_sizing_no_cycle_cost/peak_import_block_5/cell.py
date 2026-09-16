### The same peak inside each network-tariff block — five figures, one per block
# The network tariff prices power per time block, so a battery that moves a 10 kW
# draw out of block 1 and into block 5 leaves the annual peak untouched and still
# changes the bill.
#
# All five share one kW scale: here the comparison is between the blocks -- where
# the peak sits is the point -- and a per-figure scale would draw the cheapest
# block exactly like the dearest.
if not BLOCK_PEAKS_READY:
    print("No per-block peaks in this cache — nothing to draw. Set REQUIRE_BLOCK_PEAKS = True "
          "in section 1 and re-run section 6: the block peaks of a solved run cannot be "
          "recovered from its cached summary, so those runs have to be solved again.")
else:
    # Agreed power per block, median household: a property of the profile, so
    # one pass over the five columns rather than one groupby per figure.
    agreed_median = df.groupby("Label")[BLOCK_AGREED_COLS].first().median()
    by_cap_block = (
        peak_runs.groupby(["Contract", "Capacity_kWh"], observed=True)[BLOCK_PEAK_COLS].median()
    )
    # One scale for all five, with room for the reference labels at the top.
    block_ymax = 1.12 * float(by_cap_block.to_numpy().max())

    for b in TARIFF_BLOCKS:
        col = f"Peak_Import_B{b}_kW"
        fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.61))
        for contract in CONTRACT_ORDER:
            series = by_cap_block[col].loc[contract]
            ax.plot(series.index, series.values, color=CONTRACT_COLOR[contract],
                    ls=CONTRACT_DASH[contract], lw=CONTRACT_LW[contract], zorder=3)

        base_b = float(block_base[col].groupby(level="Label").median().median())
        # The agreed power of this block, which its excess charge is measured
        # against. The schedule is non-decreasing across blocks, so the cheap
        # night blocks are agreed higher than the expensive daytime one.
        agreed_b = float(agreed_median[f"Agreed_Power_B{b}_kW"])
        ax.axhline(base_b, color=BASELINE, lw=1.2, zorder=2)
        pf.edge_label(ax, base_b, f"brez baterije: {base_b:,.1f} kW", side="left")
        #ax.axhline(agreed_b, color=MUTED, lw=1.1, ls=(0, (5, 4)), zorder=2)
        #pf.edge_label(ax, agreed_b, f"mediana dogovorjene moči v bloku {b}: {agreed_b:,.1f} kW")
        ax.set_ylim(0, block_ymax)
        ax.margins(x=0.02)
        finish(ax, xlabel="Kapaciteta baterije [kWh]",
               ylabel="Konica odjema [kW]", yfmt=KW)

        season = ""
        if b == 1:
            season = " Nastopi samo nov.–feb., po najvišji tarifi za moč."
        elif b == 5:
            season = " Nastopi samo mar.–okt., po najnižji tarifi za moč."
        pf.chart_frame(fig, f"Blok {b}: konica odjema iz omrežja ({BLOCK_ROLE_SI[b]})",
              f"Samo intervali v bloku {b} — {BLOCK_WHEN_SI[b]} — mediana "
              f"{len(LABEL_ORDER)} gospodinjstev. Črti sta konica tega bloka brez baterije "
              f"({base_b:,.1f} kW) in mediana dogovorjene moči za ta blok ({agreed_b:,.1f} kW), "
              f"nad katero se plača presežna moč. Vseh pet grafov ima isto skalo, zato jih "
              f"berite drug ob drugem.{season}",
               ncol=3) #handles=contract_handles(),
        pf.show(fig, f"peak_import_block_{b}", layout="frame",preset="column")