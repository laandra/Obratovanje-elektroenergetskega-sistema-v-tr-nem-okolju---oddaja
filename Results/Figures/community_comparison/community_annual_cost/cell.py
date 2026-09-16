### Community annual cost by scenario, with the batteries and without them
resid = max(TOTALS["Category_Residual_EUR"].abs().max(),
            TOTALS_BASE["Category_Residual_EUR"].abs().max())
print(f"Supply + network + levies + fees - credit reproduces the billed total to {resid:.2e} EUR")
# A tenth of a cent: eight items per interval across 50 households and a year.
assert resid < 1e-3, "the cost split does not reconcile with the billed total"

# The bars are drawn by position, so the baseline is reordered explicitly.
BASE = TOTALS_BASE.set_index("scenario").loc[TOTALS["scenario"]].reset_index()

# Each scenario is drawn twice, with and without batteries. Colour means "which
# item is being paid" in both stacks; the pair is told apart by position.
#
# Built for \columnwidth, where eight bars share 2.8 in: a bar is 0.23 in wide
# and the centres of a pair are 0.29 in apart. So every figure is quoted in
# thousands -- "18,980" is wider than its own bar and two neighbouring totals in
# full euros overlap, where "19.0" and "26.5" clear with room to spare.
K = 1e3
fig, ax = plt.subplots()
x = np.arange(len(TOTALS))
width, off = 0.33, 0.21

def stacked(frame, offset, in_slice):
    """One stack per scenario at `offset`; returns the top of each gross stack."""
    bottom = np.zeros(len(frame))
    gross = frame["Gross_EUR"].to_numpy(dtype=float) / K
    for col, label, color in COST_PARTS:
        vals = frame[col].fillna(0.0).to_numpy(dtype=float) / K
        ax.bar(x + offset, vals, bottom=bottom, width=width,
               color=color, edgecolor=SURFACE, linewidth=2)
        if in_slice:
            # In-slice figure only where the slice is tall enough to hold it.
            for xi, val, base, tot in zip(x + offset, vals, bottom, gross):
                if val > 0.09 * tot:
                    ax.annotate(f"{val:.1f}", (xi, base + val / 2), ha="center",
                                va="center", fontsize=8.5,
                                color=SURFACE if color in BLUES[4:] else INK)
        bottom += vals
    credit = -frame["Credit_EUR"].fillna(0.0).to_numpy(dtype=float) / K
    ax.bar(x + offset, credit, width=width, color=CREDIT_PART[2], edgecolor=SURFACE,
           linewidth=2)
    for xi, val in zip(x + offset, credit):
        # Hung from its top edge, so the gap to the bar stays 3 pt whatever size
        # the text is restyled to.
        ax.annotate(f"{val:.1f}", (xi, val), xytext=(0, -3), textcoords="offset points",
                    ha="center", va="top", fontsize=8.5, color=INK_2)
    return bottom

top_batt = stacked(TOTALS, -off, in_slice=True)
top_base = stacked(BASE, +off, in_slice=False)

delta = BASE["Total_EUR"].to_numpy(dtype=float) - TOTALS["Total_EUR"].to_numpy(dtype=float)
for xi, y, total in zip(x - off, top_batt, TOTALS["Total_EUR"] / K):
    ax.annotate(f"{total:.1f}", (xi, y), xytext=(0, 3), textcoords="offset points",
                ha="center", va="bottom", fontsize=9.5, fontweight="semibold", color=INK)
for xi, y, total, d in zip(x + off, top_base, BASE["Total_EUR"] / K, delta / K):
    ax.annotate(f"{d:+.1f}\n{total:.1f}", (xi, y), xytext=(0, 3),
                textcoords="offset points", ha="center", va="bottom", fontsize=9.5,
                color=INK_2, linespacing=1.1)

# Headroom set by hand rather than by margins(): the two-line figure over the
# tallest stack and the credit figure under the deepest one need different
# amounts, and a symmetric margin gives each the other's.
lo = min(0.0, -TOTALS["Credit_EUR"].fillna(0.0).max() / K,
         -BASE["Credit_EUR"].fillna(0.0).max() / K)
hi = max(top_batt.max(), top_base.max())
ax.set_ylim(lo - 0.13 * (hi - lo), hi + 0.22 * (hi - lo))

ax.axhline(0, color=MUTED, linewidth=0.8)
ax.grid(axis="x", visible=False)
# Two levels on the x axis: which bill under each bar (minor ticks), which
# scenario under the pair (major). Both are tick labels rather than free text,
# so the layout and the legend below measure them. The bill labels stand upright
# because 0.43 in of "z baterijami" does not fit between centres 0.29 in apart.
# The major pad of 40 pt is those labels' length plus a gap -- retune it if they
# are ever reworded or translated, or the scenario row will run into them.
ax.set_xticks(np.concatenate([x - off, x + off]),
              ["z baterijami"] * len(x) + ["brez baterij"] * len(x), minor=True)
ax.set_xticks(x, TOTALS["Scenario"])
ax.tick_params(axis="x", which="both", length=0)
ax.tick_params(axis="x", which="minor", labelsize=8, labelcolor=INK_2,
               labelrotation=90, pad=3)
ax.tick_params(axis="x", which="major", labelsize=11, labelcolor=INK, pad=40)
for label in ax.get_xticklabels():
    label.set_fontweight("semibold")

finish(ax, title="Kolikšen je letni strošek skupnosti",
       subtitle=f"{len(MEMBERS)} gospodinjstev, z DDV; postavke nad črto, dobropis pod njo",
       ylabel="Letni strošek skupnosti [10³ EUR/a]", yfmt=EUR)
# key_legend rather than ax.legend: its ncol is re-fitted to the exported width.
# A plain ax.legend(ncol=3) is 7 in of keys on this 3.5 in canvas.
pf.key_legend(ax, [Patch(facecolor=c, label=l)
                   for _, l, c in COST_PARTS + [CREDIT_PART]], ncol=3)
# Its own ratio, for the reason bill_composition has one: the upright bill labels
# and the five keys -- one to a row at this width -- take half the canvas.
pf.show(fig, "community_annual_cost", preset="column", ratio=1.0)

pd.DataFrame({
    "Scenario": TOTALS["Scenario"],
    "Z baterijami [EUR]": TOTALS["Total_EUR"],
    "Brez baterij [EUR]": BASE["Total_EUR"],
    "Razlika [EUR]": delta,
    "Razlika [%]": 100 * delta / BASE["Total_EUR"],
    "Omrežnina z baterijami [EUR]": TOTALS["Network_EUR"],
    "Omrežnina brez [EUR]": BASE["Network_EUR"],
    "Dobropis z baterijami [EUR]": TOTALS["Credit_EUR"],
    "Dobropis brez [EUR]": BASE["Credit_EUR"],
}).round(1)