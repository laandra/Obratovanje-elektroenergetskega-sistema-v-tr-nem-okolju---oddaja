### Net annual benefit — the optimal size is the peak of each curve
small_multiples(
    "Net_Annual_EUR",
    "Neto letna korist = prihranek MILP - letni strošek baterije",
    f"Oznaka = optimalna velikost pri tej pogodbi. Investicija {CAPEX_EUR_PER_KWH:,.0f} EUR/kWh "
    f"+ {CAPEX_FIXED_EUR:,.0f} EUR fiksno, {DISCOUNT_RATE:.0%} diskontna stopnja, življenjska "
    f"doba omejena z {BATTERY_CYCLE_LIMIT_EFC:,} cikli. Nad ničelno črto = nakup se izplača. "
    f"Vsak graf ima svojo skalo, zato berite predznak in lego vrha, ne višine glede na sosede; "
    f"ravni so v tabeli 8.3.",
    "Neto korist [EUR/a]",
    zero_line=True,
    mark_optimum=True,    export="net_benefit_panels",
)