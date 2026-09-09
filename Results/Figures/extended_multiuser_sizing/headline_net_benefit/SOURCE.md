# headline_net_benefit

Exported 2026-09-09T07:04:08+00:00
Files: headline_net_benefit.pdf
Size: 7.16 x 19.16 in @ 600 dpi (exact figure size)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Pri kateri pogodbi se nakup baterije izplača — neto letna korist pri optimalni velikosti — Vsako gospodinjstvo pri svoji najboljši velikosti na vsaki pogodbi. Stolpci levo od ničle pri 250 EUR/kWh + 1,000 EUR pomenijo izgubo. Vsak produkt nastopa dvakrat, enkrat v obliki samooskrba in enkrat brez odkupa; par si deli barvo. Sivi stolpec je zaprta pogodba NET meritve, za gospodinjstva, ki jo že imajo — ni med paketi v ponudbi, gospodinjstva brez proizvodnje pa zanjo nimajo stolpca. Vrednosti so v tabeli 8.2.

## Source

- notebook: /Users/summerscholl/Documents/Andraz/Energy_Community/Extended_Multuser_Battery_Size_Optimization.ipynb (via __vsc_ipynb_file__)
- cell execution count: 24
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 586530e0e06e4c329f2341bc378502fd21980e9e (Development)
- subject: Adding a missing file
- describe: 586530e-dirty

**Working tree was DIRTY (29 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
.../community_net_benefit/SOURCE.md                |  69 +++------------
 .../community_net_benefit/cell.py                  |   4 +-
 .../community_net_benefit.pdf                      | Bin 17942 -> 17924 bytes
 .../community_net_benefit/source.json              |  73 +++-------------
 .../community_total_bill/SOURCE.md                 |  65 ++------------
 .../community_total_bill/cell.py                   |   4 +-
 .../community_total_bill/community_total_bill.pdf  | Bin 16820 -> 16798 bytes
 .../community_total_bill/source.json               |  69 +++------------
 .../cost_vs_capacity_panels/SOURCE.md              |  73 ++++------------
 .../cost_vs_capacity_panels.pdf                    | Bin 43185 -> 43185 bytes
 .../cost_vs_capacity_panels/source.json            |  77 ++++-------------
 .../cycles_panels/SOURCE.md                        |  90 ++++++++------------
 .../cycles_panels/cycles_panels.pdf                | Bin 42213 -> 42213 bytes
 .../cycles_panels/source.json                      |  94 ++++++++-------------
 .../headline_net_benefit/headline_net_benefit.pdf  | Bin 19421 -> 19421 bytes
 .../inverter_fixed_fee/SOURCE.md                   |  82 ++++++------------
 .../inverter_fixed_fee/cell.py                     |   4 +-
 .../inverter_fixed_fee/inverter_fixed_fee.pdf      | Bin 20262 -> 20260 bytes
 .../inverter_fixed_fee/source.json                 |  86 ++++++-------------
 .../inverter_per_kw/SOURCE.md                      |  86 +++++++------------
 .../inverter_per_kw/cell.py                        |   4 +-
 .../inverter_per_kw/inverter_per_kw.pdf            | Bin 20653 -> 20196 bytes
 .../inverter_per_kw/source.json                    |  90 +++++++-------------
 .../marginal_value/SOURCE.md                       |  79 +++++------------
 .../marginal_value/marginal_value.pdf              | Bin 21829 -> 21829 bytes
 .../marginal_value/source.json                     |  83 ++++++------------
 .../net_benefit_panels/SOURCE.md                   |  76 +++++------------
 .../net_benefit_panels/net_benefit_panels.pdf      | Bin 63809 -> 63809 bytes
 .../net_benefit_panels/source.json                 |  80 +++++-------------
 29 files changed, 352 insertions(+), 936 deletions(-)
```
