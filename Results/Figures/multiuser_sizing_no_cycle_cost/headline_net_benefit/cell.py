### The headline comparison: net annual benefit at each household's optimal size
# Horizontal bars, one row per household, so the household name is a full-length
# label whatever the count and the figure grows downwards.
#
# Two figures rather than two panels: EUR/a and % are different scales, and a
# 16-row grouped bar chart does not read at half of \textwidth.
n = len(LABEL_ORDER)
y = np.arange(n)
height = 0.84 / len(CONTRACT_ORDER)
# Height scales with the number of bars, not of households: nine contracts in a
# 0.44 in row would give each bar less space than the line around it.
BAR_IN = 0.115
RATIO = (BAR_IN * len(CONTRACT_ORDER) * n + 2.6) / pf.PRESETS[pf.PRESET]
SUBTITLE = (f"Vsako gospodinjstvo pri svoji najboljši velikosti na vsaki pogodbi. Stolpci levo "
            f"od ničle pri {CAPEX_EUR_PER_KWH:,.0f} EUR/kWh + {CAPEX_FIXED_EUR:,.0f} EUR "
            f"pomenijo izgubo. Vsak produkt nastopa dvakrat, enkrat v obliki samooskrba in "
            f"enkrat brez odkupa; par si deli barvo. Sivi stolpec je zaprta pogodba NET "
            f"meritve, za gospodinjstva, ki jo že imajo — ni med paketi v ponudbi, "
            f"gospodinjstva brez proizvodnje pa zanjo nimajo stolpca. Vrednosti so v tabeli 8.2.")

for value, xlabel, fmt, title, export in [
    ("Net_Annual_EUR", "Neto korist [EUR/a]", EUR,
     "Neto letna korist pri optimalni velikosti", "headline_net_benefit"),
    ("ROI_pct", "Diskontirani ROI [%]", PLAIN,
     "Donos na vloženi kapital čez življenjsko dobo", "headline_roi"),
]:
    fig, ax = plt.subplots(figsize=pf.figsize(ratio=RATIO))
    for i, contract in enumerate(CONTRACT_ORDER):
        # NaN where the household was never quoted the list — matplotlib draws
        # no bar for it, which is the honest mark: not a zero benefit, no offer.
        cells = [
            best_table.loc[(best_table["Label"] == lab)
                           & (best_table["Contract"] == contract), value]
            for lab in LABEL_ORDER
        ]
        vals = [float(c.iloc[0]) if len(c) else np.nan for c in cells]
        # Offsets run downwards so the bar order inside a group matches the
        # legend order top to bottom (the y axis is inverted below).
        ax.barh(y + (i - (len(CONTRACT_ORDER) - 1) / 2) * height, vals, height * 0.9,
                color=CONTRACT_COLOR[contract], zorder=2)
    ax.axvline(0, color=BASELINE, lw=1.0, zorder=3)
    ax.margins(x=0.08)
    ax.grid(axis="y", visible=False)
    ax.set_yticks(y, LABEL_ORDER, fontsize=8.5)
    ax.set_ylim(n - 0.5, -0.5)          # first household at the top
    finish(ax, xlabel=xlabel, xfmt=fmt)
    pf.chart_frame(fig, f"Pri kateri pogodbi se nakup baterije izplača — {title.lower()}",
                   SUBTITLE, handles=contract_handles("bar"))
    pf.show(fig, export, layout="frame")