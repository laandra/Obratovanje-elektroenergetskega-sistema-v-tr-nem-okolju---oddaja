### What the battery actually does: throughput and curtailment
# Peak import used to be the third panel here; it is the whole of the next
# figure now, where there is room for the no-battery and contracted-power
# references that make a kW number mean anything.
#
# Including 0 kWh: grid charging is zero there by definition, but curtailment is
# not — a household with no store already spills PV it cannot export at a profit,
# and that level is what the curve should be read against.
grouped = df.groupby(["Contract", "Capacity_kWh"], observed=True)

# Two figures, not two panels: these are different quantities, and neither reads
# at half of \textwidth.
SUBTITLE = (f"Mediana po {len(LABEL_ORDER)} gospodinjstvih, z začetkom pri izračunu brez "
            f"baterije pri 0 kWh. Polnjenje iz omrežja je prihodek iz trgovanja, ne lastna "
            f"raba; zavrnjena proizvodnja je model, ki noče oddajati z izgubo. Krivulje, ki "
            f"ležijo na ničli, se prekrivajo — ločite jih po vzorcu črtkanja.")
for value, title, ylabel, export in [
    ("Grid_Charged_kWh", "Napolnjeno iz omrežja", "Energija [kWh/a]", "grid_charged"),
    ("Curtailed_kWh", "Zavrnjena proizvodnja PV", "Energija [kWh/a]", "curtailed"),
]:
    fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.52))
    for contract in CONTRACT_ORDER:
        series = grouped[value].median().loc[contract]
        ax.plot(series.index, series.values, color=CONTRACT_COLOR[contract],
                ls=CONTRACT_DASH[contract], lw=CONTRACT_LW[contract])
    ax.set_ylim(bottom=0)
    finish(ax, xlabel="Kapaciteta baterije [kWh]", ylabel=ylabel, yfmt=PLAIN)
    pf.chart_frame(fig, f"Od kod prihajajo prihranki: {title.lower()}", SUBTITLE,
                   handles=contract_handles())
    pf.show(fig, export, layout="frame")