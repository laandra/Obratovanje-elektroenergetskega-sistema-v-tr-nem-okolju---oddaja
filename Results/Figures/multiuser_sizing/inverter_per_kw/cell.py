### What the inverter costs the case for a battery
# Two effects, two figures: a flat fee moves the zero-profit threshold without
# touching the optimal size, a per-kW price moves the size itself. One solve of
# the capex model per x value, read off for all contracts.

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

# Legend keys from the shared helper, so these two carry the same
# colour = product / dash = odkup encoding as every other figure.
keys = contract_handles(contracts=CURRENT_CONTRACT_ORDER)
# The sweep is 4x denser than the markers, so a marker every fourth sample still
# lands on the round 200 EUR / 50 EUR-per-kW values a reader would look up.
MARK_EVERY = 4


def vline_note(ax, x, text, x_max):
    """Label pinned to a vertical reference line, flipped to the other side once
    the line sits in the right third. The equal-money rate is computed from the
    data, not fixed, so it moves — and a label that runs off the axes is worse
    than no label. Surface-coloured pad, as edge_label does, so it never sits on
    a curve."""
    right = x > 0.66 * x_max
    ax.annotate(text, xy=(x, 0.97), xycoords=("data", "axes fraction"),
                xytext=(-6 if right else 6, 0), textcoords="offset points",
                ha="right" if right else "left", va="top",
                fontsize=8.5, color=INK_2, zorder=5,
                bbox=dict(facecolor=SURFACE, edgecolor="none", pad=1.6))


### 9a A flat fee decides IF, never HOW BIG
fig1, ax1 = plt.subplots(figsize=pf.figsize(ratio=0.61))
for contract in CURRENT_CONTRACT_ORDER:
    ax1.plot(INVERTER_FIXED_FINE_EUR, n_profit[contract], color=CONTRACT_COLOR[contract],
             ls=CONTRACT_DASH[contract], lw=CONTRACT_LW[contract],
             marker="o", ms=5, mfc=SURFACE, mew=1.4, markevery=MARK_EVERY,
             solid_capstyle="round", zorder=3)

ax1.axvline(CAPEX_FIXED_EUR, color=MUTED, lw=1.1, ls=(0, (5, 4)), zorder=2)
vline_note(ax1, CAPEX_FIXED_EUR, f"privzeto\n{CAPEX_FIXED_EUR:,.0f} EUR",
           float(INVERTER_FIXED_FINE_EUR[-1]))
finish(ax1, xlabel="Enkratni strošek razsmernika in montaže [EUR]",
       ylabel=f"Gospodinjstva, od {len(LABEL_ORDER)}", yfmt=PLAIN)
ax1.set_ylim(-0.5, len(LABEL_ORDER) + 0.5)
# A count of households is a whole number; the default locator puts ticks at 2.5
# gospodinjstva. Step chosen to keep roughly eight ticks whatever the panel size.
ax1.set_yticks(range(0, len(LABEL_ORDER) + 1, max(1, round(len(LABEL_ORDER) / 8))))
ax1.margins(x=0.03)

pf.chart_frame(fig1, "Koliko gospodinjstvom se baterija izplača pri danem enkratnem strošku",
      f"Vsako gospodinjstvo pri svoji najboljši kapaciteti na dani pogodbi, pri hrambi "
      f"{CAPEX_EUR_PER_KWH:,.0f} EUR/kWh. Šteta so tista, pri katerih je neto korist nad "
      f"ničlo. Enkratni strošek — razsmernik, montaža, dela na merilnem mestu — se zaračuna "
      f"ne glede na velikost paketa, zato optimalne kapacitete ne premakne: vse krivulje "
      f"zniža za enako letno anuiteto in odloča samo o tem, ali se nakup sploh izplača. "
      f"Navpičnica je privzetih {CAPEX_FIXED_EUR:,.0f} EUR.", handles=keys, ncol=4)
pf.show(fig1, "inverter_fixed_fee", layout="frame")

### 9b A per-kW price decides HOW BIG
fig2, ax2 = plt.subplots(figsize=pf.figsize(ratio=0.61))
for contract in CURRENT_CONTRACT_ORDER:
    ax2.plot(INVERTER_PER_KW_FINE, med_kwh[contract], color=CONTRACT_COLOR[contract],
             ls=CONTRACT_DASH[contract], lw=CONTRACT_LW[contract],
             marker="o", ms=5, mfc=SURFACE, mew=1.4, markevery=MARK_EVERY,
             solid_capstyle="round", zorder=3)

ax2.axvline(EQUAL_MONEY_EUR_PER_KW, color=MUTED, lw=1.1, ls=(0, (5, 4)), zorder=2)
vline_note(ax2, EQUAL_MONEY_EUR_PER_KW,
           f"enak denar kot\n{CAPEX_FIXED_EUR:,.0f} EUR pavšala\n"
           f"({EQUAL_MONEY_EUR_PER_KW:,.0f} EUR/kW)",
           float(INVERTER_PER_KW_FINE[-1]))
finish(ax2, xlabel="Cena razsmernika [EUR/kW]",
       ylabel="Mediana optimalne kapacitete [kWh]", yfmt=KW)
ax2.set_ylim(bottom=0)
ax2.margins(x=0.03)
# Kapacitete ležijo na polkilovatni mreži: PLAIN bi 7.5 kWh izpisal kot 8,
# zato KW zgoraj.

pf.chart_frame(fig2, "Optimalna velikost baterije, ko je razsmernik zaračunan na kW",
      f"Mediana najboljših kapacitet po {len(LABEL_ORDER)} gospodinjstvih, pri hrambi "
      f"{CAPEX_EUR_PER_KWH:,.0f} EUR/kWh in brez enkratnega stroška. Moč paketa je "
      f"min({C_RATE:g} x kapaciteta, {INVERTER_MAX_KW:,.0f} kW), zato cena na kW ni pavšal: "
      f"pod mejo razsmernika vsaki kWh hrambe doda {C_RATE:g}-kratnik cene na kW in optimum "
      f"potisne navzdol, nad njo pa ne več. Navpičnica je {EQUAL_MONEY_EUR_PER_KW:,.0f} "
      f"EUR/kW — enak denar kot {CAPEX_FIXED_EUR:,.0f} EUR pavšala pri moči, ki jo črpa "
      f"današnji mediani optimum.", handles=keys, ncol=4)
pf.show(fig2, "inverter_per_kw", layout="frame")