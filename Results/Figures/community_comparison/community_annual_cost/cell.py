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
fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.51))
x = np.arange(len(TOTALS))
width, off = 0.33, 0.21

def stacked(frame, offset, in_slice, legend):
    """One stack per scenario at `offset`; returns the top of each gross stack."""
    bottom = np.zeros(len(frame))
    gross = frame["Gross_EUR"].to_numpy(dtype=float)
    for col, label, color in COST_PARTS:
        vals = frame[col].fillna(0.0).to_numpy(dtype=float)
        ax.bar(x + offset, vals, bottom=bottom, width=width,
               label=label if legend else None,
               color=color, edgecolor=SURFACE, linewidth=2)
        if in_slice:
            # In-slice figure only where the slice is tall enough to hold it.
            for xi, val, base, tot in zip(x + offset, vals, bottom, gross):
                if val > 0.09 * tot:
                    ax.annotate(f"{val:,.0f}", (xi, base + val / 2), ha="center",
                                va="center", fontsize=8.5,
                                color=SURFACE if color in BLUES[4:] else INK)
        bottom += vals
    credit = -frame["Credit_EUR"].fillna(0.0).to_numpy(dtype=float)
    ax.bar(x + offset, credit, width=width, color=CREDIT_PART[2], edgecolor=SURFACE,
           linewidth=2, label=CREDIT_PART[1] if legend else None)
    for xi, val in zip(x + offset, credit):
        ax.annotate(f"{val:,.0f}", (xi, val), xytext=(0, -12), textcoords="offset points",
                    ha="center", fontsize=8.5, color=INK_2)
    return bottom

top_batt = stacked(TOTALS, -off, in_slice=True, legend=True)
top_base = stacked(BASE, +off, in_slice=False, legend=False)

delta = BASE["Total_EUR"].to_numpy(dtype=float) - TOTALS["Total_EUR"].to_numpy(dtype=float)
for xi, y, total in zip(x - off, top_batt, TOTALS["Total_EUR"]):
    ax.annotate(f"{total:,.0f}", (xi, y), xytext=(0, 6), textcoords="offset points",
                ha="center", va="bottom", fontsize=9.5, fontweight="semibold", color=INK)
for xi, y, total, d in zip(x + off, top_base, BASE["Total_EUR"], delta):
    ax.annotate(f"{d:+,.0f}\n{total:,.0f}", (xi, y), xytext=(0, 6),
                textcoords="offset points", ha="center", va="bottom", fontsize=9.5,
                color=INK_2)

ax.axhline(0, color=MUTED, linewidth=0.8)
# Two levels on the x axis: which bill under the bar, which scenario under the pair.
ax.set_xticks(np.concatenate([x - off, x + off]))
ax.set_xticklabels(["z baterijami"] * len(x) + ["brez baterij"] * len(x),
                   fontsize=8, color=INK_2)
ax.tick_params(axis="x", length=0)
for xi, name in zip(x, TOTALS["Scenario"]):
    ax.text(xi, -0.105, name, transform=ax.get_xaxis_transform(), ha="center",
            va="top", fontsize=11, fontweight="semibold", color=INK)
ax.margins(y=0.14)
ax.legend(ncol=3, loc="upper left", bbox_to_anchor=(0, -0.20))
finish(ax, title="Kolikšen je letni strošek skupnosti",
       subtitle=f"{len(MEMBERS)} gospodinjstev, z DDV; postavke nad črto, dobropis pod njo",
       ylabel="Letni strošek skupnosti [EUR/a]", yfmt=EUR)
pf.show(fig, "community_annual_cost", preset="column")

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