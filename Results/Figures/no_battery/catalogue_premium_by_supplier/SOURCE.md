# catalogue_premium_by_supplier

Exported 2026-09-16T09:15:14+00:00
Files: catalogue_premium_by_supplier.pdf
Size: 7.16 x 3.6 in @ 600 dpi (exact figure size)

> IEEE text applied to a figure drawn in the notebook style (scaled, not rebuilt)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Najboljša ponudba istega dobavitelja, s samooskrbo in brez

## Source

- notebook: C:\Users\HP\Documents\JupyterNotebook\Energy_Community\No_battery_comparison.ipynb (via __vsc_ipynb_file__)
- cell execution count: 22
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: f7d2f9c7fae6e24b4f3b615be90ae8644c63491c (Development)
- subject: Changing graphs
- describe: f7d2f9c-dirty

**Working tree was DIRTY (102 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff` (truncated), which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Battery_Size_Optimization.ipynb                    |  56 +--
 Energy_Community_Comparison.ipynb                  | 464 ++++-----------------
 Multuser_Battery_Size_Optimization.ipynb           |  65 ++-
 PLOTTING_GUIDE.txt                                 |  33 +-
 Plotting_Functions.py                              | 114 ++++-
 Results/Community_Study/per_household.csv          | 210 +++++-----
 .../battery_effect_by_item/SOURCE.md               | 324 +++-----------
 .../battery_effect_by_item.pdf                     | Bin 51549 -> 57939 bytes
 .../battery_effect_by_item/cell.py                 |   2 +-
 .../battery_effect_by_item/source.json             | 106 +++--
 .../battery_saving_by_segment/SOURCE.md            | 321 ++------------
 .../battery_saving_by_segment.pdf                  | Bin 28393 -> 32769 bytes
 .../battery_saving_by_segment/source.json          |  79 ++--
 .../bill_composition/SOURCE.md                     | 325 +++------------
 .../bill_composition/bill_composition.pdf          | Bin 49565 -> 55127 bytes
 .../community_comparison/bill_composition/cell.py  |   2 +-
 .../bill_composition/source.json                   | 118 +++---
 .../community_annual_cost/SOURCE.md                | 284 ++-----------
 .../community_annual_cost.pdf                      | Bin 52259 -> 58931 bytes
 .../community_annual_cost/source.json              |  90 ++--
 .../household_cost_scatter/SOURCE.md               | 328 +++------------
 .../household_cost_scatter.pdf                     | Bin 43763 -> 47503 bytes
 .../household_cost_scatter/source.json             |  89 ++--
 .../import_duration_curve/SOURCE.md                | 302 ++------------
 .../import_duration_curve.pdf                      | Bin 47647 -> 51366 bytes
 .../import_duration_curve/source.json              |  81 ++--
 .../import_duration_curve_zoom/SOURCE.md           | 308 ++------------
 .../import_duration_curve_zoom.pdf                 | Bin 41704 -> 45875 bytes
 .../import_duration_curve_zoom/source.json         |  78 ++--
 .../price_extreme_days/SOURCE.md                   | 346 +++------------
 .../price_extreme_days/cell.py                     |  12 +-
 .../price_extreme_days/price_extreme_days.pdf      | Bin 64988 -> 45821 bytes
 .../price_extreme_days/source.json                 |  94 ++---
 .../souporaba_shared_vs_forfeited/SOURCE.md        | 327 ++-------------
 .../souporaba_shared_vs_forfeited.pdf              | Bin 28261 -> 32261 bytes
 .../souporaba_shared_vs_forfeited/source.json      |  82 ++--
 .../multiuser_sizing/cycles_median/SOURCE.md       |  91 +---
 .../Figures/multiuser_sizing/cycles_median/cell.py |   5 +-
 .../cycles_median/cycles_median.pdf                | Bin 38882 -> 29665 bytes
 .../multiuser_sizing/cycles_median/source.json     |  76 +---
 .../multiuser_sizing/inverter_fixed_fee/SOURCE.md  |  99 ++---
 .../multiuser_sizing/inverter_fixed_fee/cell.py    |   6 +-
 .../inverter_fixed_fee/inverter_fixed_fee.pdf      | Bin 37397 -> 34010 bytes
 .../inverter_fixed_fee/source.json                 |  72 +---
 .../multiuser_sizing/inverter_per_kw/SOURCE.md     |  99 ++---
 .../multiuser_sizing/inverter_per_kw/cell.py       |   6 +-
 .../inverter_per_kw/inverter_per_kw.pdf            | Bin 37514 -> 37124 bytes
 .../multiuser_sizing/inverter_per_kw/source.json   |  72 +---
 .../catalogue_all_bill_ranking/SOURCE.md           | 388 +++++------------
 .../catalogue_all_bill_ranking.pdf                 | Bin 50864 -> 55973 bytes
 .../catalogue_all_bill_ranking/source.json         |  82 ++--
 .../catalogue_all_overpay_by_group/SOURCE.md       | 391 +++++------------
 .../catalogue_all_overpay_by_group.pdf             | Bin 134008 -> 138592 bytes
 .../catalogue_all_overpay_by_group/source.json     |  82 ++--
 .../catalogue_no_pv_bill_ranking/SOURCE.md         | 376 ++++-------------
 .../catalogue_no_pv_bill_ranking.pdf               | Bin 50877 -> 55986 bytes
 .../catalogue_no_pv_bill_ranking/source.json       |  82 ++--
 .../catalogue_no_pv_overpay_by_group/SOURCE.md     | 379 +++++------------
 .../catalogue_no_pv_overpay_by_group.pdf           | Bin 103659 -> 108243 bytes
 .../catalogue_no_pv_overpay_by_group/source.json   |  82 ++--
 .../catalogue_premium_by_supplier.pdf              | Bin 55869 -> 62770 bytes
 .../catalogue_with_pv_bill_ranking/SOURCE.md       | 382 +++++------------
 .../catalogue_with_pv_bill_ranking.pdf             | Bin 50806 -> 55915 bytes
 .../catalogue_with_pv_bill_ranking/source.json     |  82 ++--
 .../catalogue_with_pv_overpay_by_group/SOURCE.md   | 385 +++++------------
 .../catalogue_with_pv_overpay_by_group.pdf         | Bin 104261 -> 108845 bytes
 .../catalogue_with_pv_overpay_by_group/source.json |  82 ++--
 .../no_battery/export_right_by_group/SOURCE.md     | 373 ++++-------------
 .../export_right_by_group.pdf                      | Bin 45015 -> 51567 bytes
 .../no_battery/export_right_by_group/source.json   |  82 ++--
 .../no_battery/export_right_worth/SOURCE.md        | 370 ++++------------
 .../export_right_worth/export_right_worth.pdf      | Bin 49704 -> 56389 bytes
 .../no_battery/export_right_worth/source.json      |  82 ++--
 .../no_battery/no_pv_bill_by_group/SOURCE.md       | 345 +++------------
 .../no_pv_bill_by_group/no_pv_bill_by_group.pdf    | Bin 33773 -> 37712 bytes
 .../no_battery/no_pv_bill_by_group/source.json     |  84 ++--
 .../no_battery/no_pv_overpay_by_group/SOURCE.md    | 348 +++-------------
 .../no_pv_overpay_by_group.pdf                     | Bin 93636 -> 98166 bytes
 .../no_battery/no_pv_overpay_by_group/source.json  |  84 ++--
 .../no_battery/pv_bill_composition/SOURCE.md       | 355 +++-------------
 .../Figures/no_battery/pv_bill_composition/cell.py |   2 +-
 .../pv_bill_composition/pv_bill_composition.pdf    | Bin 32101 -> 36584 bytes
 .../no_battery/pv_bill_composition/source.json     |  84 ++--
 .../Figures/no_battery/pv_bill_ranking/SOURCE.md   | 351 +++-------------
 Results/Figures/no_battery/pv_bill_ranking/cell.py |   2 +-
 .../no_battery/pv_bill_ranking/pv_bill_ranking.pdf | Bin 41345 -> 46020 bytes
 .../Figures/no_battery/pv_bill_ranking/source.json |  84 ++--
 .../pv_nosale_bill_composition/SOURCE.md           | 364 ++++------------
 .../pv_nosale_bill_composition.pdf                 | Bin 30852 -> 35311 bytes
 .../pv_nosale_bill_composition/source.json         |  82 ++--
 .../no_battery/pv_nosale_bill_ranking/SOURCE.md    | 363 ++++------------
 .../pv_nosale_bill_ranking.pdf                     | Bin 41327 -> 46002 bytes
 .../no_battery/pv_nosale_bill_ranking/source.json  |  84 ++--
 .../pv_nosale_overpay_by_group/SOURCE.md           | 367 ++++------------
 .../pv_nosale_overpay_by_group.pdf                 | Bin 62013 -> 66555 bytes
 .../pv_nosale_overpay_by_group/source.json         |  82 ++--
 .../no_battery/pv_overpay_by_group/SOURCE.md       | 363 ++++------------
 .../Figures/no_battery/pv_overpay_by_group/cell.py |   2 +-
 .../pv_overpay_by_group/pv_overpay_by_group.pdf    | Bin 62418 -> 43172 bytes
 .../no_battery/pv_overpay_by_group/source.json     |  90 ++--
 Results/battery_size_optimization.csv              |  50 +--
 Skupnostna_Samooskrba_vs_Souporaba.ipynb           |   2 +-
 102 files changed, 3313 insertions(+), 9141 deletions(-)
```
