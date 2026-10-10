### The whole community on one pair of axes
# The per-household panels below answer "what should THIS household do", each on
# its own scale. This figure answers the other question — what the sixteen do
# together — and it is the only one where the levels are comparable, because a
# sum is the one aggregate that does not care that the households are different
# sizes. A median of sixteen absolute bills would be a statement about how big
# the middle household is, not about the contracts.
#
# Two FIGURES rather than two panels: EUR/a of bill and EUR/a of net benefit are
# different measures, putting them on one axis with two scales would invent a
# relationship between them, and half of \textwidth is \columnwidth, where
# neither would read.
peaks = {}
totals = (
    df.groupby(["Contract", "Capacity_kWh"], observed=True)[["Cost_EUR", "Net_Annual_EUR"]]
    .sum()
)

axes = {}
for value, title, ylabel, export in [
    ("Cost_EUR", f"Skupni letni račun za elektriko, vseh {len(LABEL_ORDER)} gospodinjstev",
     "Letni račun skupnosti [EUR/a]", "community_total_bill"),
    ("Net_Annual_EUR", "Skupna neto letna korist baterij",
     "Neto letna korist skupnosti [EUR/a]", "community_net_benefit"),
]:
    fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.52))
    axes[value] = (fig, ax, title, ylabel, export)
    for contract in CONTRACT_ORDER:
        # Both curves start at the 0 kWh solve. On the right that point is zero
        # by construction — no battery, no saving, no capex — and it is exactly
        # the baseline the rest of the curve is measured against, so it belongs
        # on the axis rather than being trimmed off it.
        series = totals[value].loc[contract].sort_index()
        ax.plot(series.index, series.values, color=CONTRACT_COLOR[contract],
                ls=CONTRACT_DASH[contract], lw=CONTRACT_LW[contract],
                solid_capstyle="round", zorder=3)
        # Mark the peak of every selectable curve; label only the winning one.
        # All three peaks sit within a couple of kWh of each other at the top of
        # the panel, so three labels collide with each other and with the title —
        # and the reader wants the one number anyway. The rest are printed below.
        if value == "Net_Annual_EUR" and contract in CURRENT_CONTRACT_ORDER:
            sized = series[series.index > 0]
            top_cap = sized.idxmax()
            peaks[contract] = (top_cap, float(series.loc[top_cap]))
            ax.plot([top_cap], [series.loc[top_cap]], marker="o", ms=8,
                    color=CONTRACT_COLOR[contract], mec=SURFACE, mew=2, zorder=4)
    ax.margins(x=0.03)

fig, ax, title, ylabel, export = axes["Cost_EUR"]
best_no_batt = float(no_batt[NO_BATTERY_CONTRACT_ORDER].min(axis=1).sum())
ax.axhline(best_no_batt, color=MUTED, lw=1.1, ls=(0, (5, 4)), zorder=2)
pf.edge_label(ax, best_no_batt,
              f"vsako gospodinjstvo na svojem najcenejšem paketu, brez baterije: "
              f"{best_no_batt:,.0f} EUR/a")
# No `title=` here: chart_frame carries the figure's one title, and a second
# one on the axes would be the same caption twice.
finish(ax, xlabel="Kapaciteta na gospodinjstvo [kWh]", ylabel=ylabel, yfmt=EUR)
pf.chart_frame(fig, title,
      f"Vsota po vseh {len(LABEL_ORDER)} gospodinjstvih, vsa na isti pogodbi in isti "
      f"kapaciteti. Črtkana črta je znesek, ki ga skupnost plača brez baterij, če vsako "
      f"gospodinjstvo izbere svoj najcenejši paket. Vsaka krivulja postavi celotno skupnost "
      f"na ENO pogodbo in ENO velikost; če vsako gospodinjstvo izbira zase, je izid boljši "
      f"in ta številka je izpisana spodaj.",
      handles=contract_handles())
pf.show(fig, export, layout="frame")

fig, ax, title, ylabel, export = axes["Net_Annual_EUR"]
ax.axhline(0, color=BASELINE, lw=1.0, zorder=1)
ax.margins(y=0.16)          # headroom for the label, which sits at the top
win_contract, (win_cap, win_net) = max(peaks.items(), key=lambda kv: kv[1][1])
ax.annotate(f"{win_contract}, po {win_cap:g} kWh: {win_net:+,.0f} EUR/a",
            xy=(win_cap, win_net), xytext=(10, 12), textcoords="offset points",
            ha="left", va="bottom", fontsize=8.5, color=INK_2, zorder=5)
finish(ax, xlabel="Kapaciteta na gospodinjstvo [kWh]", ylabel=ylabel, yfmt=EUR)
pf.chart_frame(fig, title,
      f"Skupna neto korist pri {CAPEX_EUR_PER_KWH:,.0f} EUR/kWh + {CAPEX_FIXED_EUR:,.0f} EUR "
      f"fiksno na gospodinjstvo, označena pri velikosti, ki je optimalna za skupnost — pri tej "
      f"ceni hrambe je to še vedno izguba, ker gospodinjstva nad ničlo ne pokrijejo tistih pod "
      f"njo. Podrobnosti po gospodinjstvih, vsako na svoji skali, so na spodnjih grafih.",
      handles=contract_handles())
pf.show(fig, export, layout="frame")

print(f"Community totals at the size that maximizes the community net benefit:")
for contract in CONTRACT_ORDER:
    series = totals["Net_Annual_EUR"].loc[contract]
    series = series[series.index > 0]
    cap = series.idxmax()
    cost0 = float(totals["Cost_EUR"].loc[(contract, 0.0)])
    tag = "  (legacy)" if contract in LEGACY_CONTRACTS else ""
    print(f"  {contract:>12}: {cap:5.1f} kWh each -> bill "
          f"{cost0:9,.0f} -> {float(totals['Cost_EUR'].loc[(contract, cap)]):9,.0f} EUR/a, "
          f"net {series.loc[cap]:+9,.0f} EUR/a across the community{tag}")
# The curves hold the community to one contract and one size. Each household is
# free to pick both, and that is the number a real community would reach.
print(f"  {'free choice':>12}: each household on its own best selectable contract and size -> "
      f"net {headline['Net_Annual_EUR'].sum():+,.0f} EUR/a, "
      f"{int((headline['Net_Annual_EUR'] > 0).sum())} of {len(LABEL_ORDER)} in profit")