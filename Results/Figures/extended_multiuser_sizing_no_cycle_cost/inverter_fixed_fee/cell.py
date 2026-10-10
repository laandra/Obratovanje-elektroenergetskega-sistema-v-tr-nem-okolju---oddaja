### What the inverter costs the case for a battery
# Two deliberately different x axes: a flat fee and a per-kW price do different
# things, and that difference is the point. A flat fee only moves the vertical
# position of the curve, so it decides HOW MANY households clear zero; a per-kW
# price is charged on power, which scales with capacity, so it also moves WHERE
# the peak sits. Tables 8.5a-c.
#
# Two questions, two figures: they do not share an axis, and neither reads at
# half of \textwidth.

# One solve of the capex model per x value, read off for all three contracts,
# rather than one per (contract, x).
n_profit = {c: [] for c in CURRENT_CONTRACT_ORDER}
med_kwh = {c: [] for c in CURRENT_CONTRACT_ORDER}
for fixed_eur in INVERTER_FIXED_FINE_EUR:
    top = optimum_capex(CAPEX_EUR_PER_KWH, fixed_eur)
    for contract in CURRENT_CONTRACT_ORDER:
        n_profit[contract].append(int((top.xs(contract, level="Contract")["Net"] > 0).sum()))
for per_kw in INVERTER_PER_KW_FINE:
    top = optimum_capex(CAPEX_EUR_PER_KWH, fixed_eur=0.0, eur_per_kw=per_kw)
    for contract in CURRENT_CONTRACT_ORDER:
        med_kwh[contract].append(
            float(top.xs(contract, level="Contract")["Capacity_kWh"].median())
        )

# Legend keys from the shared helper, so both figures carry the same
# colour = product / dash = odkup encoding as every other figure.
keys = contract_handles(contracts=CURRENT_CONTRACT_ORDER)

### A flat fee decides IF, never HOW BIG
fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.55))
for contract in CURRENT_CONTRACT_ORDER:
    ax.plot(INVERTER_FIXED_FINE_EUR, n_profit[contract], color=CONTRACT_COLOR[contract],
            ls=CONTRACT_DASH[contract], lw=CONTRACT_LW[contract],
            marker="o", ms=5, mfc=SURFACE, mew=1.4, zorder=3)
ax.axvline(CAPEX_FIXED_EUR, color=MUTED, lw=1.1, ls=(0, (5, 4)), zorder=2)
ax.annotate(f"predpostavljeno\n{CAPEX_FIXED_EUR:,.0f} EUR", xy=(CAPEX_FIXED_EUR, 0.97),
            xycoords=("data", "axes fraction"), xytext=(6, 0),
            textcoords="offset points", ha="left", va="top",
            fontsize=8.5, color=INK_2, zorder=5)
ax.set_ylim(-0.5, len(LABEL_ORDER) + 0.5)
ax.margins(x=0.03)
finish(ax, xlabel="Enkratni strošek razsmernika in montaže [EUR]",
       ylabel="Število gospodinjstev", yfmt=PLAIN)
pf.chart_frame(fig, "Fiksna cena razsmernika in vgradnje določa, koliko gospodinjstev "
                    "preseže ničlo",
      f"Hramba je ves čas pri {CAPEX_EUR_PER_KWH:,.0f} EUR/kWh; zaprta pogodba je izpuščena, "
      f"ker gre za izbiro med paketi v ponudbi. Višji fiksni znesek zniža vsako krivuljo za "
      f"enak letni znesek, zato gospodinjstva padejo iz dobička, najboljša velikost pa ostane "
      f"ista.", handles=keys, ncol=3)
pf.show(fig, "inverter_fixed_fee", layout="frame")

### A per-kW price decides HOW BIG
fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.55))
for contract in CURRENT_CONTRACT_ORDER:
    ax.plot(INVERTER_PER_KW_FINE, med_kwh[contract], color=CONTRACT_COLOR[contract],
            ls=CONTRACT_DASH[contract], lw=CONTRACT_LW[contract],
            marker="o", ms=5, mfc=SURFACE, mew=1.4, zorder=3)
ax.axvline(EQUAL_MONEY_EUR_PER_KW, color=MUTED, lw=1.1, ls=(0, (5, 4)), zorder=2)
ax.annotate(f"enak znesek kot\n{CAPEX_FIXED_EUR:,.0f} EUR fiksno",
            xy=(EQUAL_MONEY_EUR_PER_KW, 0.97), xycoords=("data", "axes fraction"),
            xytext=(6, 0), textcoords="offset points", ha="left", va="top",
            fontsize=8.5, color=INK_2, zorder=5)
ax.set_ylim(bottom=0)
ax.margins(x=0.03)
# Kapacitete ležijo na polkilovatni mreži: PLAIN bi 7.5 kWh izpisal kot 8.
finish(ax, xlabel="Cena razsmernika [EUR/kW]",
       ylabel="Mediana optimalne kapacitete [kWh]", yfmt=KW)
pf.chart_frame(fig, "Cena na kW premakne tudi optimalno velikost",
      f"Moč je {C_RATE:g} kW na kWh do meje {INVERTER_MAX_KW:g} kW, zato cena na kW vsaki kWh "
      f"doda {C_RATE:g}-kratnik te cene in zmanjša baterijo — "
      f"{C_RATE * EQUAL_MONEY_EUR_PER_KW:,.0f} EUR/kWh pri enakovrednem znesku. Hramba je pri "
      f"{CAPEX_EUR_PER_KWH:,.0f} EUR/kWh in brez fiksnega dela.",
      handles=keys, ncol=3)
pf.show(fig, "inverter_per_kw", layout="frame")