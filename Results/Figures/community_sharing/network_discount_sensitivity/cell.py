### How much of the community-self-supply advantage is the network discount
fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.47))
zp_runs = runs[(runs["scheme"] == ccm.SCHEME_SKUPNOST) & (runs["config"] == MAIN_CONFIG)
               & (runs["sharing"] == ccm.SHARING_DYNAMIC)
               & (runs["internal_price"] == INTERNAL_PRICE)]
for battery in [SENSITIVITY_BATTERY]:
    sub = zp_runs[zp_runs["battery"] == battery].sort_values("znacilni_primer")
    baseline = float(ind[ind["battery"] == battery]["Community_cost_EUR"].iloc[0])
    ax.plot(sub["znacilni_primer"], baseline - sub["Community_cost_EUR"],
            color=SCHEME_COLOR[ccm.SCHEME_SKUPNOST], linewidth=2.0,
            linestyle=BATTERY_STYLE[battery], marker="o", markersize=5,
            markerfacecolor=SURFACE, markeredgewidth=1.6, label=battery, zorder=3)
souporaba_level = {
    battery: float(ind[ind["battery"] == battery]["Community_cost_EUR"].iloc[0])
    - float(dyn[(dyn["battery"] == battery) & (dyn["scheme"] == ccm.SCHEME_SOUPORABA)
                ]["Community_cost_EUR"].iloc[0])
    for battery in [SENSITIVITY_BATTERY]}
for battery, level in souporaba_level.items():
    ax.axhline(level, color=SCHEME_COLOR[ccm.SCHEME_SOUPORABA], linewidth=1.4,
               linestyle=BATTERY_STYLE[battery], alpha=0.8)
    pf.edge_label(ax, level, f"souporaba, {battery}")
ax.set_xticks(ZNACILNI_PRIMER_GRID)
ax.grid(axis="y", linewidth=0.6)
ax.set_axisbelow(True)
ax.legend(loc="upper right", fontsize=8.5, title="skupnostna samooskrba", title_fontsize=8.5)
finish(ax, xlabel="Značilni primer priključitve (1 = ista TP, 4 = brez znižanja)",
       ylabel="Prihranek proti stanju brez delitve [EUR/a]", yfmt=EUR)
pf.chart_frame(fig, "Prednost skupnostne samooskrbe je znižana distribucijska postavka",
      "Pri značilnem primeru 4 je skupnostna distribucijska postavka praktično enaka polni "
      "(razlika je pod 0,0001 EUR/kWh), zato se prihranek skupnostne samooskrbe zoži na "
      "tisto, kar prihrani tudi souporaba — le da souporaba ob tem plača še nadomestilo "
      "organizatorju. Vsaka stopnja levo od 4 je omrežnina, ki je souporaba ne zniža.")
pf.show(fig, "network_discount_sensitivity", layout="frame")