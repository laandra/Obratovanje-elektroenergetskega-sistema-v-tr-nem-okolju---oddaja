# headline_net_benefit

Exported 2026-09-09T12:47:09+00:00
Files: headline_net_benefit.pdf
Size: 7.16 x 15.48 in @ 600 dpi (exact figure size)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Pri kateri pogodbi se nakup baterije izplača — neto letna korist pri optimalni velikosti — Vsako gospodinjstvo pri svoji najboljši velikosti na vsaki pogodbi. Stolpci levo od ničle pri 250 EUR/kWh + 1,000 EUR pomenijo izgubo. Vsak produkt nastopa dvakrat, enkrat v obliki samooskrba in enkrat brez odkupa; par si deli barvo. Sivi stolpec je zaprta pogodba NET meritve, za gospodinjstva, ki jo že imajo — ni med paketi v ponudbi, gospodinjstva brez proizvodnje pa zanjo nimajo stolpca. Vrednosti so v tabeli 8.2.

## Source

- notebook: /Users/summerscholl/Documents/Andraz/Energy_Community/Multuser_Battery_Size_Optimization.ipynb (via __vsc_ipynb_file__)
- cell execution count: 26
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 586530e0e06e4c329f2341bc378502fd21980e9e (Development)
- subject: Adding a missing file
- describe: 586530e-dirty

**Working tree was DIRTY (52 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff` (truncated), which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Multi_household_baseline.ipynb                     |  445 +--
 .../community_net_benefit/SOURCE.md                |   69 +-
 .../community_net_benefit/cell.py                  |    4 +-
 .../community_net_benefit.pdf                      |  Bin 17942 -> 17924 bytes
 .../community_net_benefit/source.json              |   73 +-
 .../community_total_bill/SOURCE.md                 |   65 +-
 .../community_total_bill/cell.py                   |    4 +-
 .../community_total_bill/community_total_bill.pdf  |  Bin 16820 -> 16798 bytes
 .../community_total_bill/source.json               |   69 +-
 .../cost_vs_capacity_panels/SOURCE.md              |   73 +-
 .../cost_vs_capacity_panels.pdf                    |  Bin 43185 -> 43185 bytes
 .../cost_vs_capacity_panels/source.json            |   77 +-
 .../extended_multiuser_sizing/curtailed/SOURCE.md  |  102 +-
 .../curtailed/curtailed.pdf                        |  Bin 15033 -> 15033 bytes
 .../curtailed/source.json                          |  106 +-
 .../cycles_panels/SOURCE.md                        |   90 +-
 .../cycles_panels/cycles_panels.pdf                |  Bin 42213 -> 42213 bytes
 .../cycles_panels/source.json                      |   94 +-
 .../grid_charged/SOURCE.md                         |   99 +-
 .../grid_charged/grid_charged.pdf                  |  Bin 15806 -> 15806 bytes
 .../grid_charged/source.json                       |  103 +-
 .../headline_net_benefit/SOURCE.md                 |   93 +-
 .../headline_net_benefit/headline_net_benefit.pdf  |  Bin 19421 -> 19421 bytes
 .../headline_net_benefit/source.json               |   97 +-
 .../headline_roi/SOURCE.md                         |   96 +-
 .../headline_roi/headline_roi.pdf                  |  Bin 19619 -> 19619 bytes
 .../headline_roi/source.json                       |  100 +-
 .../inverter_fixed_fee/SOURCE.md                   |   82 +-
 .../inverter_fixed_fee/cell.py                     |    4 +-
 .../inverter_fixed_fee/inverter_fixed_fee.pdf      |  Bin 20262 -> 20260 bytes
 .../inverter_fixed_fee/source.json                 |   86 +-
 .../inverter_per_kw/SOURCE.md                      |   86 +-
 .../inverter_per_kw/cell.py                        |    4 +-
 .../inverter_per_kw/inverter_per_kw.pdf            |  Bin 20653 -> 20196 bytes
 .../inverter_per_kw/source.json                    |   90 +-
 .../marginal_value/SOURCE.md                       |   79 +-
 .../marginal_value/marginal_value.pdf              |  Bin 21829 -> 21829 bytes
 .../marginal_value/source.json                     |   83 +-
 .../net_benefit_panels/SOURCE.md                   |   76 +-
 .../net_benefit_panels/net_benefit_panels.pdf      |  Bin 63809 -> 63809 bytes
 .../net_benefit_panels/source.json                 |   80 +-
 .../peak_change_pct/SOURCE.md                      |  108 +-
 .../peak_change_pct/peak_change_pct.pdf            |  Bin 17017 -> 17017 bytes
 .../peak_change_pct/source.json                    |  112 +-
 .../peak_import_median/SOURCE.md                   |  105 +-
 .../peak_import_median/peak_import_median.pdf      |  Bin 16362 -> 16362 bytes
 .../peak_import_median/source.json                 |  109 +-
 .../peak_import_panels/SOURCE.md                   |  111 +-
 .../peak_import_panels/peak_import_panels.pdf      |  Bin 34551 -> 34551 bytes
 .../peak_import_panels/source.json                 |  115 +-
 Results/multiuser_battery_sizing.csv               | 3860 ++++++++++----------
 51 files changed, 3151 insertions(+), 3898 deletions(-)
```
