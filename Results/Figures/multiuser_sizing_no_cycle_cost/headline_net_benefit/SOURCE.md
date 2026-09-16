# headline_net_benefit

Exported 2026-09-15T23:23:38+00:00
Files: headline_net_benefit.pdf
Size: 7.16 x 16.1864 in @ 600 dpi (exact figure size)

> resized from 7.16x15.48 to 7.16x16.19 in; IEEE text applied to a figure drawn in the notebook style (scaled, not rebuilt)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Pri kateri pogodbi se nakup baterije izplača — neto letna korist pri optimalni velikosti — Vsako gospodinjstvo pri svoji najboljši velikosti na vsaki pogodbi. Stolpci levo od ničle pri 250 EUR/kWh + 1,000 EUR pomenijo izgubo. Vsak produkt nastopa dvakrat, enkrat v obliki samooskrba in enkrat brez odkupa; par si deli barvo. Sivi stolpec je zaprta pogodba NET meritve, za gospodinjstva, ki jo že imajo — ni med paketi v ponudbi, gospodinjstva brez proizvodnje pa zanjo nimajo stolpca. Vrednosti so v tabeli 8.2.

## Source

- notebook: /Users/summerscholl/Documents/Andraz/Energy_Community/Multuser_Battery_Size_Optimization no cycle cost.ipynb (via __vsc_ipynb_file__)
- cell execution count: 26
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: f7d2f9c7fae6e24b4f3b615be90ae8644c63491c (Development)
- subject: Changing graphs
- describe: f7d2f9c-dirty

**Working tree was DIRTY (26 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Battery_Size_Optimization.ipynb                    | 1381 ++++++++++----------
 .../battery_sizing/cost_vs_capacity/SOURCE.md      |  208 +--
 .../cost_vs_capacity/cost_vs_capacity.pdf          |  Bin 40037 -> 39458 bytes
 .../battery_sizing/cost_vs_capacity/source.json    |   95 +-
 .../energy_through_battery/SOURCE.md               |  217 +--
 .../energy_through_battery.pdf                     |  Bin 29481 -> 29403 bytes
 .../energy_through_battery/source.json             |   79 +-
 .../equivalent_full_cycles/SOURCE.md               |  223 +---
 .../equivalent_full_cycles.pdf                     |  Bin 25380 -> 25018 bytes
 .../equivalent_full_cycles/source.json             |   67 +-
 .../battery_sizing/marginal_value/SOURCE.md        |  211 +--
 .../marginal_value/marginal_value.pdf              |  Bin 30063 -> 30157 bytes
 .../battery_sizing/marginal_value/source.json      |   91 +-
 .../battery_sizing/net_annual_benefit/SOURCE.md    |  214 +--
 .../net_annual_benefit/net_annual_benefit.pdf      |  Bin 44605 -> 43338 bytes
 .../battery_sizing/net_annual_benefit/source.json  |   85 +-
 .../battery_sizing/peak_grid_import/SOURCE.md      |  220 +---
 .../peak_grid_import/peak_grid_import.pdf          |  Bin 27140 -> 27258 bytes
 .../battery_sizing/peak_grid_import/source.json    |   73 +-
 .../Figures/battery_sizing/service_life/SOURCE.md  |  226 +---
 .../battery_sizing/service_life/service_life.pdf   |  Bin 30900 -> 30867 bytes
 .../battery_sizing/service_life/source.json        |   61 +-
 Results/battery_size_optimization.csv              |   68 +-
 23 files changed, 1138 insertions(+), 2381 deletions(-)
```
