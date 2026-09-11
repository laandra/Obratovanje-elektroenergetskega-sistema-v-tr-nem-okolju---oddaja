### Where the next kWh of storage stops paying for itself
fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.44))
marginal = (
    df.dropna(subset=["Marginal_Value_EUR_per_kWh"])
    .groupby(["Contract", "Capacity_kWh"], observed=True)["Marginal_Value_EUR_per_kWh"]
    .median()
)
# Plotted at the midpoint of the interval the difference was taken over.
caps = np.sort(df["Capacity_kWh"].unique())
midpoints = dict(zip(caps[1:], (caps[1:] + caps[:-1]) / 2))

# Recovery plus O&M: what a euro of storage costs to own for a year. The O&M
# share is charged on the storage price alone here, matching the line's own
# question -- these levels deliberately exclude the fixed install.
crf_ref = annualized_cost_factor(DISCOUNT_RATE, BATTERY_CALENDAR_LIFE_Y,
                                 OPEX_FRAC_OF_CAPEX_PER_YEAR)
# Cost lines first, so the curves and their markers sit on top of them. The
# assumed price gets a solid line; the rest of the scenarios are dashed.
for capex_per_kwh in sorted(set(CAPEX_SCENARIOS_EUR_PER_KWH) | {CAPEX_EUR_PER_KWH}):
    assumed = capex_per_kwh == CAPEX_EUR_PER_KWH
    level = capex_per_kwh * crf_ref
    ax.axhline(level, color=INK_2 if assumed else MUTED, lw=1.2 if assumed else 1.1,
               ls="-" if assumed else (0, (5, 4)), zorder=1)
    pf.edge_label(ax, level, f"{capex_per_kwh:,.0f} EUR/kWh vgrajene kapacitete  ({level:,.1f} EUR/kWh/a)"
                          + ("  <- predpostavljeno" if assumed else ""))

for contract in CONTRACT_ORDER:
    series = marginal.loc[contract]
    ax.plot([midpoints[c] for c in series.index], series.values,
            color=CONTRACT_COLOR[contract], ls=CONTRACT_DASH[contract], lw=CONTRACT_LW[contract],
            marker="o", ms=5, mfc=SURFACE, mew=1.4, zorder=3)

ax.set_ylim(bottom=0)
ax.margins(x=0.02)
finish(ax, xlabel="Kapaciteta baterije [kWh]",
       ylabel="Mejna vrednost kapacitete [EUR/kWh/a]", yfmt=PLAIN)
pf.chart_frame(fig, "Kje se naslednja kWh hrambe ne izplača več",
      f"Mediana po {len(LABEL_ORDER)} gospodinjstvih. Kapaciteto se splača dodajati, dokler je "
      f"njena krivulja nad črto stroška. Te črte so strošek hrambe na kWh, porazdeljen na leto "
      f"čez celotno {BATTERY_CALENDAR_LIFE_Y}-letno koledarsko dobo, z "
      f"{OPEX_FRAC_OF_CAPEX_PER_YEAR:.1%} letnega vzdrževanja; ne vključujejo "
      f"{CAPEX_FIXED_EUR:,.0f} EUR vgradnje, ki se zaračuna enkrat ne glede na velikost. Kjer "
      f"krivulja seka črto {CAPEX_EUR_PER_KWH:,.0f} EUR/kWh, je velikost iz tabele 8.4.",
      handles=contract_handles())
pf.show(fig, "marginal_value", layout="frame")