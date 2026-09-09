### Annual electricity cost vs battery size
# Independent y per panel, as everywhere in section 9: the comparison is between
# contracts within a panel, not between panels. The 0 kWh-only lists are shown
# here and nowhere else, this being the figure about the bill; on the net-benefit
# and cycle figures that point is 0 by construction.
small_multiples(
    "Cost_EUR",
    "Letni strošek elektrike ob popolnem predvidevanju, po pogodbi in velikosti baterije",
    "Celoletni MILP na točko, en graf na gospodinjstvo, vsak na svoji skali. NET meritve (sivo, "
    "pikčasto) so zaprta pogodba — obračun letno, za nove odjemalce ni več na voljo, prikazane "
    "so le kot strošek tistih, ki jo že imajo. Vsi drugi paketi priznavajo oddajo po "
    "intervalih. Pod ničlo gospodinjstvo za oddano energijo čez leto prejme več, kot plača za "
    "prevzeto. Vrednosti so v tabeli 8.2.",
    "Letni strošek [EUR/a]",
    zero_line=True,
    baselines=BASELINE_CONTRACTS,    export="cost_vs_capacity_panels",
)