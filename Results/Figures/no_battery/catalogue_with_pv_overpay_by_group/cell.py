### The same 32 options on the households that actually have a roof
# The half that is a real decision: these households are confined to the green
# rows by `dovoljuje_pv`, and the purple rows are what they are kept from.
rel_pv = catalogue_figure(
    "with PV",
    "S PV in brez odkupa: cena samooskrbne police proti polici, ki je zanje zaprta",
    "S PV, presežki po 0 EUR: preplačilo glede na najcenejši cenik te skupine [%]",
    "catalogue_with_pv")

rel_pv.round(2)