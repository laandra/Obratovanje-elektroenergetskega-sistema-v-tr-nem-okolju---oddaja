# battery_saving_by_segment

Exported 2026-09-16T07:00:50+00:00
Files: battery_saving_by_segment.pdf
Size: 7.16 x 3.7232 in @ 600 dpi (exact figure size)

> IEEE text applied to a figure drawn in the notebook style (scaled, not rebuilt)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Letni prihranek s 30 kWh baterijo — isto gospodinjstvo, obračunano brez baterije, vse drugo nespremenjeno

## Source

- notebook: C:\Users\HP\Documents\JupyterNotebook\Energy_Community\Energy_Community_Comparison.ipynb (via __vsc_ipynb_file__)
- cell execution count: 23
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: f7d2f9c7fae6e24b4f3b615be90ae8644c63491c (Development)
- subject: Changing graphs
- describe: f7d2f9c-dirty

**Working tree was DIRTY (35 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Multuser_Battery_Size_Optimization.ipynb           |  49 +++-
 Results/Community_Study/per_household.csv          | 210 +++++++-------
 .../battery_effect_by_item/SOURCE.md               | 296 ++-----------------
 .../battery_effect_by_item.pdf                     | Bin 51549 -> 57939 bytes
 .../battery_effect_by_item/source.json             |  84 ++----
 .../battery_saving_by_segment.pdf                  | Bin 28393 -> 32769 bytes
 .../bill_composition/SOURCE.md                     | 290 ++-----------------
 .../bill_composition/bill_composition.pdf          | Bin 49565 -> 55370 bytes
 .../bill_composition/source.json                   |  87 ++----
 .../community_annual_cost/SOURCE.md                | 284 ++----------------
 .../community_annual_cost.pdf                      | Bin 52259 -> 58931 bytes
 .../community_annual_cost/source.json              |  90 ++----
 .../household_cost_scatter/SOURCE.md               | 318 +++------------------
 .../household_cost_scatter/cell.py                 |   2 +-
 .../household_cost_scatter.pdf                     | Bin 43763 -> 46633 bytes
 .../household_cost_scatter/source.json             |  81 ++----
 .../import_duration_curve/SOURCE.md                | 302 +++----------------
 .../import_duration_curve.pdf                      | Bin 47647 -> 51366 bytes
 .../import_duration_curve/source.json              |  81 ++----
 .../import_duration_curve_zoom/SOURCE.md           | 308 +++-----------------
 .../import_duration_curve_zoom.pdf                 | Bin 41704 -> 45875 bytes
 .../import_duration_curve_zoom/source.json         |  78 ++---
 .../multiuser_sizing/cycles_median/SOURCE.md       |  91 ++----
 .../Figures/multiuser_sizing/cycles_median/cell.py |   5 +-
 .../cycles_median/cycles_median.pdf                | Bin 38882 -> 29665 bytes
 .../multiuser_sizing/cycles_median/source.json     |  76 ++---
 .../multiuser_sizing/inverter_fixed_fee/SOURCE.md  |  99 ++-----
 .../multiuser_sizing/inverter_fixed_fee/cell.py    |   6 +-
 .../inverter_fixed_fee/inverter_fixed_fee.pdf      | Bin 37397 -> 34010 bytes
 .../inverter_fixed_fee/source.json                 |  72 ++---
 .../multiuser_sizing/inverter_per_kw/SOURCE.md     |  99 ++-----
 .../multiuser_sizing/inverter_per_kw/cell.py       |   6 +-
 .../inverter_per_kw/inverter_per_kw.pdf            | Bin 37514 -> 37124 bytes
 .../multiuser_sizing/inverter_per_kw/source.json   |  72 ++---
 Results/battery_size_optimization.csv              |  50 ++--
 35 files changed, 657 insertions(+), 2479 deletions(-)
```
