### The same peak as a change against the same household with no battery
# Its own figure: the axis is a percentage of each household's own peak and the
# band is the spread of the sixteen.
fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.61))
for contract in CONTRACT_ORDER:
    rel = by_cap["Peak_Change_pct"].median().loc[contract]
    lo = by_cap["Peak_Change_pct"].min().loc[contract]
    hi = by_cap["Peak_Change_pct"].max().loc[contract]
    # Band = the households' spread, so a median cannot hide one runaway.
    ax.fill_between(rel.index, lo.values, hi.values, color=CONTRACT_COLOR[contract],
                    alpha=0.10, lw=0, zorder=1)
    ax.plot(rel.index, rel.values, color=CONTRACT_COLOR[contract],
            ls=CONTRACT_DASH[contract], lw=CONTRACT_LW[contract], zorder=3)

ax.axhline(0, color=BASELINE, lw=1.2, zorder=2)
ax.margins(x=0.02)
finish(ax, xlabel="Kapaciteta baterije [kWh]",
       ylabel="Sprememba konice odjema [%]", yfmt=PCT_SIGNED)

pf.chart_frame(fig, "Sprememba konice odjema glede na isto gospodinjstvo brez baterije",
      f"Vsako gospodinjstvo je primerjano samo s seboj brez baterije in na isti pogodbi: črta "
      f"je mediana, pas je celoten razpon vseh {len(LABEL_ORDER)}. Nad ničelno črto je baterija "
      f"konico priključka poslabšala, ne izboljšala; pri 0 kWh je sprememba nič po definiciji.",
      handles=contract_handles(), ncol=3)
pf.show(fig, "peak_change_pct", layout="frame")