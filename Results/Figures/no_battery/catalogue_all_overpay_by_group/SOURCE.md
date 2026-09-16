# catalogue_all_overpay_by_group

Exported 2026-09-16T11:38:22+00:00
Files: catalogue_all_overpay_by_group.pdf
Size: 7.16 x 8.68 in @ 600 dpi (exact figure size)

> IEEE text applied to a figure drawn in the notebook style (scaled, not rebuilt)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Vseh 40 gospodinjstev: preplačilo glede na najcenejši cenik te skupine [%]

## Source

- notebook: /Users/summerscholl/Documents/Andraz/Energy_Community/No_battery_comparison.ipynb (via __vsc_ipynb_file__)
- cell execution count: 20
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: c134bcae1736c41e670854eb0cdccc05fbbb135d (Development)
- subject: Tables converted to latex format. More work on graphs
- describe: c134bca-dirty

**Working tree was DIRTY (95 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Results/Community_Study/per_household.csv          | 210 ++++++++++-----------
 .../battery_effect_by_item/SOURCE.md               |  60 ++----
 .../battery_effect_by_item.pdf                     | Bin 57947 -> 51540 bytes
 .../battery_effect_by_item/source.json             |  56 ++----
 .../battery_saving_by_segment/SOURCE.md            |  60 +++---
 .../battery_saving_by_segment.pdf                  | Bin 32769 -> 28393 bytes
 .../battery_saving_by_segment/source.json          |  30 ++-
 .../bill_composition/SOURCE.md                     |  57 ++----
 .../bill_composition/bill_composition.pdf          | Bin 54897 -> 49279 bytes
 .../bill_composition/source.json                   |  59 ++----
 .../community_annual_cost/SOURCE.md                |  57 ++----
 .../community_annual_cost/cell.py                  |  86 ++++++---
 .../community_annual_cost.pdf                      | Bin 58596 -> 51423 bytes
 .../community_annual_cost/source.json              |  65 ++-----
 .../household_cost_scatter/SOURCE.md               |  54 +++---
 .../household_cost_scatter.pdf                     | Bin 47503 -> 43763 bytes
 .../household_cost_scatter/source.json             |  30 ++-
 .../import_duration_curve/SOURCE.md                |  42 ++---
 .../import_duration_curve.pdf                      | Bin 51366 -> 47647 bytes
 .../import_duration_curve/source.json              |  30 ++-
 .../import_duration_curve_zoom/SOURCE.md           |  48 +++--
 .../import_duration_curve_zoom.pdf                 | Bin 45875 -> 41704 bytes
 .../import_duration_curve_zoom/source.json         |  30 ++-
 .../price_extreme_days/SOURCE.md                   |  72 ++++---
 .../price_extreme_days/price_extreme_days.pdf      | Bin 45821 -> 42097 bytes
 .../price_extreme_days/source.json                 |  30 ++-
 .../souporaba_shared_vs_forfeited/SOURCE.md        |  66 +++----
 .../souporaba_shared_vs_forfeited.pdf              | Bin 32261 -> 28261 bytes
 .../souporaba_shared_vs_forfeited/source.json      |  30 ++-
 .../catalogue_all_bill_ranking/SOURCE.md           | 196 +++++++++----------
 .../catalogue_all_bill_ranking.pdf                 | Bin 55973 -> 50864 bytes
 .../no_battery/catalogue_all_bill_ranking/cell.py  |   2 +-
 .../catalogue_all_bill_ranking/source.json         |  70 +++----
 .../catalogue_all_overpay_by_group/SOURCE.md       | 207 ++++++++++----------
 .../catalogue_all_overpay_by_group.pdf             | Bin 138592 -> 134008 bytes
 .../catalogue_all_overpay_by_group/cell.py         |   2 +-
 .../catalogue_all_overpay_by_group/source.json     |  83 ++++----
 .../catalogue_no_pv_bill_ranking/SOURCE.md         | 170 ++++++++---------
 .../catalogue_no_pv_bill_ranking.pdf               | Bin 55986 -> 50877 bytes
 .../catalogue_no_pv_bill_ranking/cell.py           |  20 +-
 .../catalogue_no_pv_bill_ranking/source.json       |  70 +++----
 .../catalogue_no_pv_overpay_by_group/SOURCE.md     | 180 +++++++++---------
 .../catalogue_no_pv_overpay_by_group.pdf           | Bin 108243 -> 103659 bytes
 .../catalogue_no_pv_overpay_by_group/cell.py       |  20 +-
 .../catalogue_no_pv_overpay_by_group/source.json   |  70 +++----
 .../catalogue_with_pv_bill_ranking/SOURCE.md       | 184 +++++++++---------
 .../catalogue_with_pv_bill_ranking.pdf             | Bin 55915 -> 50806 bytes
 .../catalogue_with_pv_bill_ranking/source.json     |  70 +++----
 .../catalogue_with_pv_overpay_by_group/SOURCE.md   | 192 +++++++++----------
 .../catalogue_with_pv_overpay_by_group.pdf         | Bin 108845 -> 104261 bytes
 .../catalogue_with_pv_overpay_by_group/source.json |  70 +++----
 .../no_battery/export_right_by_group/SOURCE.md     | 164 ++++++++--------
 .../export_right_by_group.pdf                      | Bin 51567 -> 45015 bytes
 .../no_battery/export_right_by_group/source.json   |  70 +++----
 .../no_battery/export_right_worth/SOURCE.md        | 158 +++++++---------
 .../export_right_worth/export_right_worth.pdf      | Bin 56389 -> 49704 bytes
 .../no_battery/export_right_worth/source.json      |  70 +++----
 .../no_battery/no_pv_bill_by_group/SOURCE.md       |  97 ++++------
 .../Figures/no_battery/no_pv_bill_by_group/cell.py |  13 +-
 .../no_pv_bill_by_group/no_pv_bill_by_group.pdf    | Bin 37712 -> 33773 bytes
 .../no_battery/no_pv_bill_by_group/source.json     |  50 ++---
 .../no_battery/no_pv_overpay_by_group/SOURCE.md    | 107 +++++------
 .../no_battery/no_pv_overpay_by_group/cell.py      |  13 +-
 .../no_pv_overpay_by_group.pdf                     | Bin 98166 -> 93636 bytes
 .../no_battery/no_pv_overpay_by_group/source.json  |  56 +++---
 .../no_battery/pv_bill_composition/SOURCE.md       | 119 +++++-------
 .../Figures/no_battery/pv_bill_composition/cell.py |   9 +-
 .../pv_bill_composition/pv_bill_composition.pdf    | Bin 36584 -> 32101 bytes
 .../no_battery/pv_bill_composition/source.json     |  61 +++---
 .../Figures/no_battery/pv_bill_ranking/SOURCE.md   | 111 +++++------
 Results/Figures/no_battery/pv_bill_ranking/cell.py |   9 +-
 .../no_battery/pv_bill_ranking/pv_bill_ranking.pdf | Bin 46020 -> 41345 bytes
 .../Figures/no_battery/pv_bill_ranking/source.json |  57 +++---
 .../pv_nosale_bill_composition/SOURCE.md           | 144 +++++++-------
 .../no_battery/pv_nosale_bill_composition/cell.py  |   8 +-
 .../pv_nosale_bill_composition.pdf                 | Bin 35311 -> 30852 bytes
 .../pv_nosale_bill_composition/source.json         |  70 +++----
 .../no_battery/pv_nosale_bill_ranking/SOURCE.md    | 135 ++++++-------
 .../no_battery/pv_nosale_bill_ranking/cell.py      |   8 +-
 .../pv_nosale_bill_ranking.pdf                     | Bin 46002 -> 41327 bytes
 .../no_battery/pv_nosale_bill_ranking/source.json  |  68 +++----
 .../pv_nosale_overpay_by_group/SOURCE.md           | 154 +++++++--------
 .../no_battery/pv_nosale_overpay_by_group/cell.py  |   8 +-
 .../pv_nosale_overpay_by_group.pdf                 | Bin 66555 -> 62013 bytes
 .../pv_nosale_overpay_by_group/source.json         |  70 +++----
 .../no_battery/pv_overpay_by_group/SOURCE.md       | 134 ++++++-------
 .../Figures/no_battery/pv_overpay_by_group/cell.py |   9 +-
 .../pv_overpay_by_group/pv_overpay_by_group.pdf    | Bin 43172 -> 62418 bytes
 .../no_battery/pv_overpay_by_group/source.json     |  74 ++++----
 89 files changed, 2141 insertions(+), 2683 deletions(-)
```
