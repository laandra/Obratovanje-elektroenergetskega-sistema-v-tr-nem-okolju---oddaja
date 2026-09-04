### All 40 households at once, both catalogues, all 8 household types
# Pooling is legitimate because with the credit zeroed the two halves were billed
# on identical terms (check 2 above). It buys the 8-column heatmap, the only
# panel that can show whether a roof changes the answer rather than the bill.
#
# It costs the ranking column, which is a mean over households whose bills differ
# by 400 EUR/a, so it ranks price lists rather than describing a household. Every
# delta beside it is measured per household first.
rel_all = catalogue_figure(
    "all",
    "Oba kataloga, vseh 8 tipov: isti ceniki so poceni za vse -- streho občutijo le dinamični",
    "Vseh 40 gospodinjstev: preplačilo glede na najcenejši cenik te skupine [%]",
    "catalogue_all")

anonymise(rel_all).round(1)