### Annual electricity cost vs battery size
# Independent y per panel, as everywhere in section 9: these households run from
# a ~400 EUR/a bill to a ~1,300 EUR/a one, and a common scale would flatten the
# small ones into straight lines. The comparison this figure is for is between
# contracts within a panel, not between panels.
# The 0 kWh-only lists are shown HERE and nowhere else in section 9: this is the
# figure about the bill, and for a household with no self-supply device the
# plain two-tariff point at x = 0 is the bill it actually pays today. On the
# net-benefit and cycle figures that point is 0 by construction and would only
# add a dot on the zero line.
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