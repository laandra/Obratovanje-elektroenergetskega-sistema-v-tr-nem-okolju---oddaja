### How the bill splits, and what the battery moves inside each part
# Two questions, two figures. First: the shape of the bill -- what share of the
# gross each item takes, which is what a household actually chooses between.
# Second: how many euros the battery takes off (or adds to) that same item.
# Colour means the same item in both and in the chart above. They are two
# figures rather than two panels because half of \textwidth is \columnwidth,
# where a five-series grouped bar chart is unreadable.
PARTS = COST_PARTS + [CREDIT_PART]

# Shares are taken of the gross, so the four items add to 100 % and the credit
# hangs below as the fraction of the gross it cancels.
gross = TOTALS["Gross_EUR"].to_numpy(dtype=float)
share = {col: 100 * TOTALS[col].fillna(0.0).to_numpy(dtype=float) / gross
         for col, *_ in COST_PARTS}
credit_share = -100 * TOTALS["Credit_EUR"].fillna(0.0).to_numpy(dtype=float) / gross
net_share = 100 * TOTALS["Total_EUR"].to_numpy(dtype=float) / gross

# The battery's effect, item by item, signed so that positive always means
# "the annual bill is lower with the batteries in". A cost item helps by
# shrinking, the credit by growing; the five add up to the net saving.
effect = {col: BASE[col].fillna(0.0).to_numpy(dtype=float)
               - TOTALS[col].fillna(0.0).to_numpy(dtype=float)
          for col, *_ in COST_PARTS}
effect["Credit_EUR"] = (TOTALS["Credit_EUR"].fillna(0.0).to_numpy(dtype=float)
                        - BASE["Credit_EUR"].fillna(0.0).to_numpy(dtype=float))
net_effect = BASE["Total_EUR"].to_numpy(dtype=float) - TOTALS["Total_EUR"].to_numpy(dtype=float)

# The five parts are summed over 50 households x a year of quarter-hours before
# they are compared with the net saving, so ~1e-6 EUR of float accumulation is
# expected on a ~1e4 EUR quantity -- a relative error of 1e-10. A bit-exact test
# here only measures summation order. The tolerance is three orders under the
# cent these bills are quoted in: it swallows the noise and still trips on any
# real mis-split. Same reasoning as the reconciliation in the cell above, which
# already checks its residual at 1e-3.
_DECOMP_TOL_EUR = 1e-4
resid = np.abs(sum(effect.values()) - net_effect).max()
print(f"The five item effects reproduce the net saving to {resid:.2e} EUR")
assert resid < _DECOMP_TOL_EUR, (
    f"the battery effect does not decompose into the billed items: {resid:.3g} EUR"
)

x = np.arange(len(TOTALS))

# --- the shape of the bill --------------------------------------------------
fig, axL = plt.subplots(figsize=pf.figsize(ratio=0.55))
bottom = np.zeros(len(TOTALS))
for col, label, color in COST_PARTS:
    vals = share[col]
    axL.bar(x, vals, bottom=bottom, width=0.56, label=label,
            color=color, edgecolor=SURFACE, linewidth=2)
    for xi, val, base in zip(x, vals, bottom):
        if val > 6:
            axL.annotate(f"{val:.0f} %", (xi, base + val / 2), ha="center",
                         va="center", fontsize=8.5,
                         color=SURFACE if color in BLUES[4:] else INK)
    bottom += vals
axL.bar(x, credit_share, width=0.56, color=CREDIT_PART[2], edgecolor=SURFACE,
        linewidth=2, label=CREDIT_PART[1])
for xi, val, net in zip(x, credit_share, net_share):
    axL.annotate(f"{val:.0f} %", (xi, val), xytext=(0, -12),
                 textcoords="offset points", ha="center", fontsize=8.5, color=INK_2)
    axL.annotate(f"neto {net:.0f} %", (xi, 0.99), xycoords=axL.get_xaxis_transform(),
                 ha="center", va="top", fontsize=9.5, fontweight="semibold", color=INK)

axL.axhline(0, color=MUTED, linewidth=0.8)
axL.set_xticks(x)
axL.set_xticklabels(TOTALS["Scenario"], fontsize=10.5, fontweight="semibold")
axL.tick_params(axis="x", length=0)
axL.margins(y=0.12)
finish(axL, title="Iz česa je račun sestavljen",
       subtitle="delež bruto računa, z baterijami",
       ylabel="delež bruto računa", yfmt=PCT)
pf.key_legend(axL, [Patch(facecolor=c, label=l) for _, l, c in PARTS], ncol=3)
pf.show(fig, "bill_composition")

# --- what the battery moves -------------------------------------------------
fig, axR = plt.subplots(figsize=pf.figsize(ratio=0.55))
width = 0.15
span = max(abs(v).max() for v in effect.values())
for i, (col, label, color) in enumerate(PARTS):
    vals = effect[col]
    pos = x + (i - (len(PARTS) - 1) / 2) * (width + 0.02)
    axR.bar(pos, vals, width=width, color=color, edgecolor=SURFACE, linewidth=1.2)
    for xi, val in zip(pos, vals):
        if abs(val) > 0.05 * span:
            axR.annotate(f"{val:+,.0f}", (xi, val),
                         xytext=(0, 4 if val >= 0 else -12),
                         textcoords="offset points", ha="center", fontsize=8,
                         rotation=90, va="bottom" if val >= 0 else "top",
                         color=INK_2)

# Headroom is set by hand so the net figures sit in a clean row above the bars.
lo = min(0.0, min(v.min() for v in effect.values()))
hi = max(0.0, max(v.max() for v in effect.values()))
axR.set_ylim(lo - 0.16 * (hi - lo), hi + 0.24 * (hi - lo))
for xi, net in zip(x, net_effect):
    axR.annotate(f"neto {net:+,.0f}", (xi, 0.99), xycoords=axR.get_xaxis_transform(),
                 ha="center", va="top", fontsize=10, fontweight="semibold",
                 color=INK if net >= 0 else SERIES[1])

axR.axhline(0, color=MUTED, linewidth=0.8)
axR.set_xticks(x)
axR.set_xticklabels(TOTALS["Scenario"], fontsize=10.5, fontweight="semibold")
axR.tick_params(axis="x", length=0)
finish(axR, title="Kaj baterija premakne po postavkah",
       subtitle="razlika proti istemu letu brez baterij; nad črto postavka račun zniža",
       ylabel="učinek na letni račun [EUR]", yfmt=EUR)
pf.key_legend(axR, [Patch(facecolor=c, label=l) for _, l, c in PARTS], ncol=3)
pf.show(fig, "battery_effect_by_item")

BATTERY_EFFECT = pd.DataFrame({
    "Scenario": TOTALS["Scenario"],
    **{label: effect[col].round(1) for col, label, _ in PARTS},
    "Neto [EUR]": net_effect.round(1),
    "Neto [%]": (100 * net_effect / BASE["Total_EUR"].to_numpy(dtype=float)).round(2),
})
BATTERY_EFFECT