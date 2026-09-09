peak = (
    scored.groupby("Controller")
    .agg(Peak_kW=("Peak_Import_kW", "mean"),
         Power_EUR=("Power_EUR", "mean"),
         Energy_EUR=("Energy_EUR", "mean"),
         Cycles=("Equivalent_Full_Cycles", "mean"))
    .reindex(CONTROLLERS)
)
floor_kw = peak.loc["no_battery", "Peak_kW"]
floor_eur = peak.loc["no_battery", "Power_EUR"]

order = [c for c in CONTROLLERS if c != "no_battery"]
y = np.arange(len(order))

fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.52))
bars = ax.barh(y, peak.loc[order, "Peak_kW"], height=0.62,
               color=[controller_color(c) for c in order])
ax.axvline(floor_kw, color=INK, lw=1.6, ls="--")
# Anchored on the reference line itself, not on the axes edge -- the label is
# naming that line.
ax.text(floor_kw, len(order) - 0.3, "  no battery", color=INK, fontsize=9, va="center")
ax.set_yticks(y, [CONTROLLER_LABEL[c] for c in order])
bar_labels(ax, bars, list(peak.loc[order, "Peak_kW"]), fmt="{:.2f}")
finish(ax, title="Peak grid import — what the ratchet is measured on",
       xlabel="Peak grid import [kW]")
pf.show(fig, "peak_grid_import")

fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.52))
bars = ax.barh(y, peak.loc[order, "Power_EUR"], height=0.62,
               color=[controller_color(c) for c in order])
ax.axvline(floor_eur, color=INK, lw=1.6, ls="--")
ax.text(floor_eur, len(order) - 0.3, "  no battery", color=INK, fontsize=9, va="center")
ax.set_yticks(y, [CONTROLLER_LABEL[c] for c in order])
bar_labels(ax, bars, list(peak.loc[order, "Power_EUR"]), fmt="{:.2f}")
finish(ax, title="Excess-power charge — the part a kW meter alone can attack",
       xlabel="Excess-power charge [EUR/a]", xfmt=EUR)
pf.show(fig, "excess_power_charge")

display(peak.round(2))

# Stated as a computed fact rather than as prose: which controller actually pays
# the least excess-power charge, and what it gave up elsewhere to get there.
best_rule_on_power = peak.loc[POLICIES, "Power_EUR"].idxmin()
milp_power = peak.loc["milp_full_period", "Power_EUR"]
rule_power = peak.loc[best_rule_on_power, "Power_EUR"]
print(f"Excess-power charge: {peak.loc['no_battery', 'Power_EUR']:.2f} EUR/a with no battery, "
      f"{milp_power:.2f} for the MILP, {rule_power:.2f} for the best rule "
      f"({CONTROLLER_LABEL[best_rule_on_power]}).")
print(f"The rule lands within {abs(rule_power - milp_power) / max(milp_power, 1e-9):.0%} of "
      f"perfect foresight on this line, while giving up "
      f"{ranking.loc[best_rule_on_power, 'Gap_pct']:.0f}% of the saving overall — "
      f"the ratchet is the one part of the bill a kW meter is nearly enough for.")
print(f"It pays {peak.loc[best_rule_on_power, 'Energy_EUR'] - peak.loc['milp_full_period', 'Energy_EUR']:+,.0f} "
      f"EUR/a more than the MILP on energy to get there.")
print(f"Meanwhile the MILP runs the {'HIGHEST' if peak.loc['milp_full_period', 'Peak_kW'] == peak['Peak_kW'].max() else 'a lower'} "
      f"metered peak of any controller ({peak.loc['milp_full_period', 'Peak_kW']:.2f} kW against "
      f"{peak.loc['no_battery', 'Peak_kW']:.2f} kW with no battery) and still pays the least for "
      f"it — it moves its imports into the cheap network blocks. Minimising one bill line is "
      f"not minimising the bill.")