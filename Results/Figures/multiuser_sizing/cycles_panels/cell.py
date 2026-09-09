### Equivalent full cycles per year
# The curve starts at the 0 kWh solve, so the first segment is a steep climb into
# the 1 kWh point: the first kWh of storage is cycled hardest.
small_multiples(
    "Equivalent_Full_Cycles",
    "Kako močno vsaka pogodba obremeni baterijo",
    f"Ekvivalentni polni cikli na leto glede na shranjeno energijo, (noter + ven) / (2 x "
    f"kapaciteta). Baterija z oceno {BATTERY_CYCLE_LIMIT_EFC:,} EFC je izrabljena pri "
    f"{BATTERY_CYCLE_LIMIT_EFC // BATTERY_CALENDAR_LIFE_Y} ciklih/leto, zato krivulja nad to "
    f"ravnjo kupuje prihranke na račun življenjske dobe baterije. Krivulje se začnejo pri "
    f"izračunu brez baterije, kjer je ciklov po definiciji nič. Vsako gospodinjstvo ima svojo "
    f"skalo; mediane po vseh so v tabeli 8.6.",
    "Ekvivalentni polni cikli [1/leto]",
    fmt=PLAIN,    export="cycles_panels",
)