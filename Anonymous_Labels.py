"""One anonymised name per supplier, price list and sharing service.

The published study may not name the suppliers, so every label that reaches a
figure, a table or a printed line goes through here: a supplier becomes
"Ponudnik N" and a price list keeps only what it IS -- its tariff structure
(redni, fiksni, aktivni, dinamicni), whether it is a samooskrba list, and the
metering variant where the supplier publishes both.

The key is derived from the catalogue rather than typed out, so it is IDENTICAL
in every notebook that imports this module and cannot drift between them: N is
the supplier's position in the alphabetically sorted list of `PAKETI`
suppliers. Alphabetical order is independent of everything the studies compute,
so the numbering leaks no ranking, and it survives adding a price list to an
existing supplier.

    >>> supplier_label("GEN-I")
    'Ponudnik 3'
    >>> paket_label("GENI_SAMO_DINAMICNI")
    'Ponudnik 3 Samo Dinamični'
    >>> option_label("BISOL_FIKSNI99@1T")
    'Ponudnik 1 Fiksni akcijski [1T]'

`Household invoice generator.ipynb` deliberately does NOT import this module: an
invoice has to name the contract it was issued under.
"""
import sys

from Pricing_Functions import PAKETI

# `si_paketi` also catalogues the souporaba organizers, whose `organizator` is a
# supplier name. Importing `Pricing_Functions` is what puts `si_paketi` in
# sys.modules (its impl imports PAKETI from there), so read it back off that
# rather than re-loading the file under a second name and getting two catalogues.
STORITVE_SOUPORABE = getattr(sys.modules.get("si_paketi"),
                             "STORITVE_SOUPORABE", {})

VARIANT_SEP = "@"           # `GENI_REDNI@2T` -- a price list plus its meter
NO_VARIANT = "-"            # the list publishes no VT/MT-vs-ET choice

PONUDNIK = {name: f"Ponudnik {i}" for i, name in
            enumerate(sorted({p.dobavitelj for p in PAKETI.values()}), start=1)}

# What each catalogued list IS, once the brand name comes off it. Every entry is
# a tariff fact read off the package -- price structure, price guarantee, whether
# it is sold with a self-consumption device -- and never a product name.
CONTRACT_TYPE = {
    "GENI_REDNI":           "Redni",
    "GENI_FIKSNI":          "Fiksni",
    "GENI_AKTIVNI":         "Aktivni",
    "GENI_DINAMICNI":       "Dinamični",
    "GENI_SAMO_REDNI":      "Samo Redni",
    "GENI_SAMO_AKTIVNI":    "Samo Aktivni",
    "GENI_SAMO_FIKSNI":     "Samo Aktivni fiksni",
    "GENI_SAMO_DINAMICNI":  "Samo Dinamični",
    "GENI_NETMETERING":     "Samo Net metering",
    "BISOL_FIKSNI":         "Fiksni",
    "BISOL_FIKSNI_VEZAVA":  "Fiksni z vezavo",
    "BISOL_FIKSNI99":       "Fiksni akcijski",
    "BISOL_DINAMICNI":      "Dinamični",
    "BISOL_DINAMICNI_PLUS": "Dinamični zamejeni",
    "BISOL_SAMO_DINAMICNA": "Samo Dinamični",
    "PETROL_REDNI":         "Redni",
    "PETROL_AKCIJSKI":      "Akcijski",
    "PETROL_FIKS2026":      "Fiksni",
    "PETROL_SAMO_MESECNI":  "Samo Redni",
    "PETROL_SAMO_LETNI":    "Samo Net metering",
    "ELEN_ZANESLJIVA":      "Redni",
    "ELEN_FIKSNI":          "Fiksni",
    "ELEN_DINAMICNA":       "Dinamični",
}

_STRUCTURE = {"tarifni": "Tarifni", "aktivni": "Aktivni", "dinamicni": "Dinamični"}


def supplier_label(name):
    """"Ponudnik N" for a supplier name off a `Paket` or a summary column."""
    return PONUDNIK.get(name, str(name))


def base_id(option_id):
    """The catalogue key an option belongs to (`GENI_REDNI@2T` -> `GENI_REDNI`)."""
    return str(option_id).split(VARIANT_SEP, 1)[0]


def variant(option_id):
    """Which metering variant an option is: '2T', '1T', or '-' where there is none."""
    parts = str(option_id).split(VARIANT_SEP, 1)
    return parts[1] if len(parts) == 2 else NO_VARIANT


def paket_label(paket_id):
    """"Ponudnik N <what the list is>" for one catalogue key, no variant tag.

    An id this module has never seen falls back to the package's own fields --
    its price structure and whether it requires a self-consumption device -- so
    a new price list is anonymous by default rather than named by accident.
    """
    base = base_id(paket_id)
    paket = PAKETI.get(base)
    if paket is None:
        return str(paket_id)
    kind = CONTRACT_TYPE.get(base)
    if kind is None:
        kind = _STRUCTURE.get(paket.tip_cene.value, "Cenik")
        if paket.zahteva_pv:
            kind = f"Samo {kind}"
    return f"{supplier_label(paket.dobavitelj)} {kind}"


def option_label(option_id, with_variant=True):
    """Chart-axis label for one price OPTION, supplier anonymised.

    The metering variant is part of the identity, not a footnote: two rows that
    read "Ponudnik 3 Redni" and differ by 8 EUR/a would be unreadable, so a list
    that publishes both a VT/MT and an ET rate always carries its [2T]/[1T] tag.
    """
    tag = variant(option_id)
    name = paket_label(option_id)
    return f"{name} [{tag}]" if with_variant and tag != NO_VARIANT else name


def service_label(service_id):
    """"Ponudnik N" for a souporaba organizer, or a neutral name for none."""
    service = STORITVE_SOUPORABE.get(str(service_id))
    if service is None:
        return str(service_id)
    if service.organizator in PONUDNIK:
        return f"{PONUDNIK[service.organizator]} souporaba"
    return "Souporaba brez organizatorja"


def organizer_label(name):
    """"Ponudnik N" for a souporaba organizer NAME (the `organizator` field)."""
    return PONUDNIK.get(name, "brez organizatorja" if name in ("—", "-", "", None)
                        else str(name))


def anonymise(frame, index=True, columns=False, drop=("Supplier",)):
    """A copy of a summary or pivot table with every name replaced, for display.

    `drop` removes columns that only restate the anonymised index -- `Supplier`
    becomes the leading word of every row label, so keeping it prints "Ponudnik 1
    Fiksni akcijski [1T] | Ponudnik 1". The column is NOT redundant in the frame
    itself (chapter 5 of the no-battery study groups by it); it is redundant once
    the index carries the same name, which is only true at render time.
    """
    out = frame
    if index:
        out = out.rename(index=option_label)
    if columns:
        out = out.rename(columns=option_label)
    keep = [c for c in drop if c in getattr(out, "columns", ())]
    return out.drop(columns=keep) if keep else out


# Product names that appear inside free text rather than as a catalogue key --
# a package's `opombe`, say. Replaced by what the thing is, like every other
# label here.
BRANDS = {
    "Pametna samooskrba": "posebne samooskrbe",
}


def _aliases():
    """Every free-text form of a name -> its anonymous label, longest first.

    `si_obracun` writes an invoice's package as `f"{dobavitelj} – {ime}"`, and
    that string reaches a displayed frame, so the composite form is mapped as
    well as its parts. An `ime` shared by two suppliers ("Redni cenik za
    gospodinjske odjemalce" is both) is NOT mapped: it cannot be resolved to one
    supplier, and guessing would put the wrong Ponudnik on the row.
    """
    by_ime = {}
    for pid, p in PAKETI.items():
        by_ime.setdefault(p.ime, []).append(pid)

    out = dict(BRANDS)
    for pid, p in PAKETI.items():
        label = paket_label(pid)
        for dash in ("–", "-", "—"):
            out[f"{p.dobavitelj} {dash} {p.ime}"] = label
        if len(by_ime[p.ime]) == 1:
            out[p.ime] = label
    for service in STORITVE_SOUPORABE.values():
        if service.organizator in PONUDNIK:
            out[f"{service.organizator} – {service.ime}"] = (
                f"{PONUDNIK[service.organizator]} souporaba")
    out.update(PONUDNIK)                       # bare supplier names, last
    return sorted(out.items(), key=lambda kv: len(kv[0]), reverse=True)


_ALIASES = None


def scrub(text):
    """Every supplier, product and brand name in a free-text string replaced.

    Longest match first, so "GEN-I – GEN-I Dinamični – Gospodinjski odjemalci"
    becomes "Ponudnik 3 Dinamični" rather than a half-substituted mixture of the
    anonymous supplier and the real product.
    """
    global _ALIASES
    if _ALIASES is None:
        _ALIASES = _aliases()
    out = str(text)
    for name, label in _ALIASES:
        if name in out:
            out = out.replace(name, label)
    return out


def scrub_frame(frame, columns=None):
    """A copy of a frame with every name scrubbed out of its text cells.

    For frames a library built rather than the notebook -- invoice line items,
    say, whose package column carries `f"{dobavitelj} – {ime}"`. Numeric columns
    are untouched; `columns=None` means every column holding text.
    """
    # Column dtype is NOT the test: with pandas' string dtype enabled a text
    # column is StringDtype rather than object, and a `dtype == object` guard
    # silently skips exactly the columns this is for. What matters is whether the
    # cells hold strings, so ask the values.
    def _scrub_values(values):
        if not any(isinstance(v, str) for v in values):
            return None
        return [scrub(v) if isinstance(v, str) else v for v in values]

    out = frame.copy()
    cols = list(out.columns) if columns is None else list(columns)
    for col in cols:
        if col not in out.columns:
            continue
        scrubbed = _scrub_values(list(out[col]))
        if scrubbed is not None:
            out[col] = scrubbed
    scrubbed_index = _scrub_values(list(out.index))
    if scrubbed_index is not None:
        out.index = scrubbed_index
    return out


__all__ = ["PONUDNIK", "CONTRACT_TYPE", "BRANDS", "supplier_label", "base_id",
           "variant", "paket_label", "option_label", "service_label",
           "organizer_label", "anonymise", "scrub", "scrub_frame"]
