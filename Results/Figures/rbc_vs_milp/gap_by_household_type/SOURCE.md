# gap_by_household_type

Exported 2026-09-02T12:53:27+00:00
Files: gap_by_household_type.pdf
Size: 7.16 x 3.3652 in @ 600 dpi (tight)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Gap to the MILP by household type

## Source

- notebook: /Users/summerscholl/Documents/Andraz/Energy_Community/RBC_vs_MILP_Comparison.ipynb (via __vsc_ipynb_file__)
- cell execution count: 21
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 7940b1377d833816b4278c4c3f71855080b2f016 (Development)
- subject: Mostly rerun evrything and implemented new ploting function on the whole notebook.     An error remaining in RBC
- describe: 7940b13-dirty

**Working tree was DIRTY (217 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff` (truncated), which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
DQN/dqn_model                                      | Bin 223465 -> 223465 bytes
 Energy_Community_Comparison.ipynb                  | 457 ++---------
 Environment.py                                     |  32 +-
 Extended_Multuser_Battery_Size_Optimization.ipynb  |  59 +-
 Horizon_Comparison.py                              |  37 +-
 Household_local model.ipynb                        | 647 ++++++++++++---
 MILP_Household.py                                  |   4 +-
 Multuser_Battery_Size_Optimization.ipynb           |  38 +-
 .../__pycache__/si_obracun.cpython-314.pyc         | Bin 49552 -> 50361 bytes
 New pricing functions/si_obracun.py                |  26 +-
 RBC_vs_MILP_Comparison.ipynb                       | 877 +++++++++++----------
 .../battery_effect_by_item/SOURCE.md               |  87 +-
 .../battery_effect_by_item.pdf                     | Bin 23266 -> 23266 bytes
 .../battery_effect_by_item/source.json             |  80 +-
 .../battery_saving_by_segment/SOURCE.md            |  99 +--
 .../battery_saving_by_segment.pdf                  | Bin 12677 -> 12677 bytes
 .../battery_saving_by_segment/source.json          |  92 +--
 .../bill_composition/SOURCE.md                     |  84 +-
 .../bill_composition/bill_composition.pdf          | Bin 22190 -> 22190 bytes
 .../bill_composition/source.json                   |  77 +-
 .../community_annual_cost/SOURCE.md                |  79 +-
 .../community_annual_cost.pdf                      | Bin 23481 -> 23481 bytes
 .../community_annual_cost/source.json              |  78 +-
 .../household_cost_scatter/SOURCE.md               |  96 +--
 .../household_cost_scatter.pdf                     | Bin 25359 -> 25359 bytes
 .../household_cost_scatter/source.json             |  89 +--
 .../import_duration_curve/SOURCE.md                |  90 +--
 .../import_duration_curve.pdf                      | Bin 30012 -> 30012 bytes
 .../import_duration_curve/source.json              |  83 +-
 .../import_duration_curve_zoom/SOURCE.md           |  93 +--
 .../import_duration_curve_zoom.pdf                 | Bin 24231 -> 24231 bytes
 .../import_duration_curve_zoom/source.json         |  86 +-
 .../price_extreme_days/SOURCE.md                   | 105 ++-
 .../price_extreme_days/price_extreme_days.pdf      | Bin 36454 -> 36454 bytes
 .../price_extreme_days/source.json                 |  98 +--
 .../souporaba_shared_vs_forfeited/SOURCE.md        | 102 +--
 .../souporaba_shared_vs_forfeited.pdf              | Bin 11890 -> 11890 bytes
 .../souporaba_shared_vs_forfeited/source.json      |  95 +--
 .../gap_by_household_type.pdf                      | Bin 37188 -> 37483 bytes
 .../rbc_vs_milp/gap_by_price_list/SOURCE.md        | 285 +++++--
 .../gap_by_price_list/gap_by_price_list.pdf        | Bin 16277 -> 16280 bytes
 .../rbc_vs_milp/gap_by_price_list/source.json      | 102 +--
 Results/Figures/rbc_vs_milp/gap_by_rule/SOURCE.md  | 279 +++++--
 .../rbc_vs_milp/gap_by_rule/gap_by_rule.pdf        | Bin 16358 -> 16418 bytes
 .../Figures/rbc_vs_milp/gap_by_rule/source.json    | 102 +--
 .../Figures/rbc_vs_milp/gap_vs_capacity/SOURCE.md  | 291 +++++--
 .../gap_vs_capacity/gap_vs_capacity.pdf            | Bin 18510 -> 18510 bytes
 .../rbc_vs_milp/gap_vs_capacity/source.json        | 102 +--
 .../rbc_vs_milp/saving_vs_capacity/SOURCE.md       | 297 +++++--
 .../saving_vs_capacity/saving_vs_capacity.pdf      | Bin 19284 -> 19279 bytes
 .../rbc_vs_milp/saving_vs_capacity/source.json     | 102 +--
 Results/Figures/rbc_vs_milp/trace_day/SOURCE.md    | 108 ++-
 Results/Figures/rbc_vs_milp/trace_day/source.json  |  95 +--
 .../Figures/rbc_vs_milp/trace_day/trace_day.pdf    | Bin 31141 -> 31149 bytes
 .../Fluvius_EV_user_001_redni2t.csv                |   6 -
 .../Fluvius_EV_user_002_redni2t.csv                |   6 -
 .../Fluvius_EV_user_003_redni2t.csv                |   6 -
 .../Fluvius_EV_user_004_redni2t.csv                |   6 -
 .../Fluvius_EV_user_005_redni2t.csv                |   6 -
 .../Fluvius_HP_EV_user_001_redni2t.csv             |   6 -
 .../Fluvius_HP_EV_user_002_redni2t.csv             |   6 -
 .../Fluvius_HP_EV_user_003_redni2t.csv             |   6 -
 .../Fluvius_HP_EV_user_004_redni2t.csv             |   6 -
 .../Fluvius_HP_EV_user_005_redni2t.csv             |   6 -
 .../Fluvius_HP_user_001_redni2t.csv                |   6 -
 .../Fluvius_HP_user_002_redni2t.csv                |   6 -
 .../Fluvius_HP_user_003_redni2t.csv                |   6 -
 .../Fluvius_HP_user_004_redni2t.csv                |   6 -
 .../Fluvius_HP_user_005_redni2t.csv                |   6 -
 .../Fluvius_user_001_redni2t.csv                   |   6 -
 .../Fluvius_user_002_redni2t.csv                   |   6 -
 .../Fluvius_user_003_redni2t.csv                   |   6 -
 .../Fluvius_user_004_redni2t.csv                   |   6 -
 .../Fluvius_user_005_redni2t.csv                   |   6 -
 Results/RBC_Comparison/Fluvius_EV_user_001.csv     |  82 +-
 .../RBC_Comparison/Fluvius_EV_user_001_aktivni.csv |  82 +-
 .../RBC_Comparison/Fluvius_EV_user_001_redni1t.csv |  82 +-
 .../RBC_Comparison/Fluvius_EV_user_001_redni2t.csv |  82 +-
 Results/RBC_Comparison/Fluvius_EV_user_002.csv     |  82 +-
 .../RBC_Comparison/Fluvius_EV_user_002_aktivni.csv |  82 +-
 .../RBC_Comparison/Fluvius_EV_user_002_redni1t.csv |  82 +-
 .../RBC_Comparison/Fluvius_EV_user_002_redni2t.csv |  82 +-
 Results/RBC_Comparison/Fluvius_EV_user_003.csv     |  82 +-
 .../RBC_Comparison/Fluvius_EV_user_003_aktivni.csv |  82 +-
 .../RBC_Comparison/Fluvius_EV_user_003_redni1t.csv |  82 +-
 .../RBC_Comparison/Fluvius_EV_user_003_redni2t.csv |  82 +-
 Results/RBC_Comparison/Fluvius_EV_user_004.csv     |  82 +-
 .../RBC_Comparison/Fluvius_EV_user_004_aktivni.csv |  82 +-
 .../RBC_Comparison/Fluvius_EV_user_004_redni1t.csv |  82 +-
 .../RBC_Comparison/Fluvius_EV_user_004_redni2t.csv |  82 +-
 Results/RBC_Comparison/Fluvius_EV_user_005.csv     |  82 +-
 .../RBC_Comparison/Fluvius_EV_user_005_aktivni.csv |  82 +-
 .../RBC_Comparison/Fluvius_EV_user_005_redni1t.csv |  82 +-
 .../RBC_Comparison/Fluvius_EV_user_005_redni2t.csv |  82 +-
 Results/RBC_Comparison/Fluvius_HP_EV_user_001.csv  |  82 +-
 .../Fluvius_HP_EV_user_001_aktivni.csv             |  82 +-
 .../Fluvius_HP_EV_user_001_redni1t.csv             |  82 +-
 .../Fluvius_HP_EV_user_001_redni2t.csv             |  82 +-
 Results/RBC_Comparison/Fluvius_HP_EV_user_002.csv  |  82 +-
 .../Fluvius_HP_EV_user_002_aktivni.csv             |  82 +-
 .../Fluvius_HP_EV_user_002_redni1t.csv             |  82 +-
 .../Fluvius_HP_EV_user_002_redni2t.csv             |  82 +-
 Results/RBC_Comparison/Fluvius_HP_EV_user_003.csv  |  82 +-
 .../Fluvius_HP_EV_user_003_aktivni.csv             |  82 +-
 .../Fluvius_HP_EV_user_003_redni1t.csv             |  82 +-
 .../Fluvius_HP_EV_user_003_redni2t.csv             |  82 +-
 Results/RBC_Comparison/Fluvius_HP_EV_user_004.csv  |  82 +-
 .../Fluvius_HP_EV_user_004_aktivni.csv             |  82 +-
 .../Fluvius_HP_EV_user_004_redni1t.csv             |  82 +-
 .../Fluvius_HP_EV_user_004_redni2t.csv             |  82 +-
 Results/RBC_Comparison/Fluvius_HP_EV_user_005.csv  |  82 +-
 .../Fluvius_HP_EV_user_005_aktivni.csv             |  82 +-
 .../Fluvius_HP_EV_user_005_redni1t.csv             |  82 +-
 .../Fluvius_HP_EV_user_005_redni2t.csv             |  82 +-
 Results/RBC_Comparison/Fluvius_HP_user_001.csv     |  82 +-
 .../RBC_Comparison/Fluvius_HP_user_001_aktivni.csv |  82 +-
 .../RBC_Comparison/Fluvius_HP_user_001_redni1t.csv |  82 +-
 .../RBC_Comparison/Fluvius_HP_user_001_redni2t.csv |  82 +-
 Results/RBC_Comparison/Fluvius_HP_user_002.csv     |  82 +-
 .../RBC_Comparison/Fluvius_HP_user_002_aktivni.csv |  82 +-
 .../RBC_Comparison/Fluvius_HP_user_002_redni1t.csv |  82 +-
 .../RBC_Comparison/Fluvius_HP_user_002_redni2t.csv |  82 +-
 Results/RBC_Comparison/Fluvius_HP_user_003.csv     |  82 +-
 .../RBC_Comparison/Fluvius_HP_user_003_aktivni.csv |  82 +-
 .../RBC_Comparison/Fluvius_HP_user_003_redni1t.csv |  82 +-
 .../RBC_Comparison/Fluvius_HP_user_003_redni2t.csv |  82 +-
 Results/RBC_Comparison/Fluvius_HP_user_004.csv     |  82 +-
 .../RBC_Comparison/Fluvius_HP_user_004_aktivni.csv |  82 +-
 .../RBC_Comparison/Fluvius_HP_user_004_redni1t.csv |  82 +-
 .../RBC_Comparison/Fluvius_HP_user_004_redni2t.csv |  82 +-
 Results/RBC_Comparison/Fluvius_HP_user_005.csv     |  82 +-
 .../RBC_Comparison/Fluvius_HP_user_005_aktivni.csv |  82 +-
 .../RBC_Comparison/Fluvius_HP_user_005_redni1t.csv |  82 +-
 .../RBC_Comparison/Fluvius_HP_user_005_redni2t.csv |  82 +-
 Results/RBC_Comparison/Fluvius_PV_EV_user_001.csv  |  82 +-
 .../Fluvius_PV_EV_user_001_aktivni.csv             |  82 +-
 .../Fluvius_PV_EV_user_001_redni1t.csv             |  82 +-
 Results/RBC_Comparison/Fluvius_PV_EV_user_002.csv  |  82 +-
 .../Fluvius_PV_EV_user_002_aktivni.csv             |  82 +-
 .../Fluvius_PV_EV_user_002_redni1t.csv             |  82 +-
 Results/RBC_Comparison/Fluvius_PV_EV_user_003.csv  |  82 +-
 .../Fluvius_PV_EV_user_003_aktivni.csv             |  82 +-
 .../Fluvius_PV_EV_user_003_redni1t.csv             |  82 +-
 Results/RBC_Comparison/Fluvius_PV_EV_user_004.csv  |  82 +-
 .../Fluvius_PV_EV_user_004_aktivni.csv             |  82 +-
 .../Fluvius_PV_EV_user_004_redni1t.csv             |  82 +-
 Results/RBC_Comparison/Fluvius_PV_EV_user_005.csv  |  82 +-
 .../Fluvius_PV_EV_user_005_aktivni.csv             |  82 +-
 .../Fluvius_PV_EV_user_005_redni1t.csv             |  82 +-
 .../RBC_Comparison/Fluvius_PV_HP_EV_user_001.csv   |  82 +-
 .../Fluvius_PV_HP_EV_user_001_aktivni.csv          |  82 +-
 .../Fluvius_PV_HP_EV_user_001_redni1t.csv          |  82 +-
 .../RBC_Comparison/Fluvius_PV_HP_EV_user_002.csv   |  82 +-
 .../Fluvius_PV_HP_EV_user_002_aktivni.csv          |  82 +-
 .../Fluvius_PV_HP_EV_user_002_redni1t.csv          |  82 +-
 .../RBC_Comparison/Fluvius_PV_HP_EV_user_003.csv   |  82 +-
 .../Fluvius_PV_HP_EV_user_003_aktivni.csv          |  82 +-
 .../Fluvius_PV_HP_EV_user_003_redni1t.csv          |  82 +-
 .../RBC_Comparison/Fluvius_PV_HP_EV_user_004.csv   |  82 +-
 .../Fluvius_PV_HP_EV_user_004_aktivni.csv          |  82 +-
 .../Fluvius_PV_HP_EV_user_004_redni1t.csv          |  82 +-
 .../RBC_Comparison/Fluvius_PV_HP_EV_user_005.csv   |  82 +-
 .../Fluvius_PV_HP_EV_user_005_aktivni.csv          |  82 +-
 .../Fluvius_PV_HP_EV_user_005_redni1t.csv          |  82 +-
 Results/RBC_Comparison/Fluvius_PV_HP_user_001.csv  |  82 +-
 .../Fluvius_PV_HP_user_001_aktivni.csv             |  82 +-
 .../Fluvius_PV_HP_user_001_redni1t.csv             |  82 +-
 Results/RBC_Comparison/Fluvius_PV_HP_user_002.csv  |  82 +-
 .../Fluvius_PV_HP_user_002_aktivni.csv             |  82 +-
 .../Fluvius_PV_HP_user_002_redni1t.csv             |  82 +-
 Results/RBC_Comparison/Fluvius_PV_HP_user_003.csv  |  82 +-
 .../Fluvius_PV_HP_user_003_aktivni.csv             |  82 +-
 .../Fluvius_PV_HP_user_003_redni1t.csv             |  82 +-
 Results/RBC_Comparison/Fluvius_PV_HP_user_004.csv  |  82 +-
 .../Fluvius_PV_HP_user_004_aktivni.csv             |  82 +-
 .../Fluvius_PV_HP_user_004_redni1t.csv             |  82 +-
 Results/RBC_Comparison/Fluvius_PV_HP_user_005.csv  |  82 +-
 .../Fluvius_PV_HP_user_005_aktivni.csv             |  82 +-
 .../Fluvius_PV_HP_user_005_redni1t.csv             |  82 +-
 Results/RBC_Comparison/Fluvius_PV_user_001.csv     |  82 +-
 .../RBC_Comparison/Fluvius_PV_user_001_aktivni.csv |  82 +-
 .../RBC_Comparison/Fluvius_PV_user_001_redni1t.csv |  82 +-
 Results/RBC_Comparison/Fluvius_PV_user_002.csv     |  82 +-
 .../RBC_Comparison/Fluvius_PV_user_002_aktivni.csv |  82 +-
 .../RBC_Comparison/Fluvius_PV_user_002_redni1t.csv |  82 +-
 Results/RBC_Comparison/Fluvius_PV_user_003.csv     |  82 +-
 .../RBC_Comparison/Fluvius_PV_user_003_aktivni.csv |  82 +-
 .../RBC_Comparison/Fluvius_PV_user_003_redni1t.csv |  82 +-
 Results/RBC_Comparison/Fluvius_PV_user_004.csv     |  82 +-
 .../RBC_Comparison/Fluvius_PV_user_004_aktivni.csv |  82 +-
 .../RBC_Comparison/Fluvius_PV_user_004_redni1t.csv |  82 +-
 Results/RBC_Comparison/Fluvius_PV_user_005.csv     |  82 +-
 .../RBC_Comparison/Fluvius_PV_user_005_aktivni.csv |  82 +-
 .../RBC_Comparison/Fluvius_PV_user_005_redni1t.csv |  82 +-
 Results/RBC_Comparison/Fluvius_user_001.csv        |  82 +-
 .../RBC_Comparison/Fluvius_user_001_aktivni.csv    |  82 +-
 .../RBC_Comparison/Fluvius_user_001_redni1t.csv    |  82 +-
 .../RBC_Comparison/Fluvius_user_001_redni2t.csv    |  82 +-
 Results/RBC_Comparison/Fluvius_user_002.csv        |  82 +-
 .../RBC_Comparison/Fluvius_user_002_aktivni.csv    |  82 +-
 .../RBC_Comparison/Fluvius_user_002_redni1t.csv    |  82 +-
 .../RBC_Comparison/Fluvius_user_002_redni2t.csv    |  82 +-
 Results/RBC_Comparison/Fluvius_user_003.csv        |  82 +-
 .../RBC_Comparison/Fluvius_user_003_aktivni.csv    |  82 +-
 .../RBC_Comparison/Fluvius_user_003_redni1t.csv    |  82 +-
 .../RBC_Comparison/Fluvius_user_003_redni2t.csv    |  82 +-
 Results/RBC_Comparison/Fluvius_user_004.csv        |  82 +-
 .../RBC_Comparison/Fluvius_user_004_aktivni.csv    |  82 +-
 .../RBC_Comparison/Fluvius_user_004_redni1t.csv    |  82 +-
 .../RBC_Comparison/Fluvius_user_004_redni2t.csv    |  82 +-
 Results/RBC_Comparison/Fluvius_user_005.csv        |  82 +-
 .../RBC_Comparison/Fluvius_user_005_aktivni.csv    |  82 +-
 .../RBC_Comparison/Fluvius_user_005_redni1t.csv    |  82 +-
 .../RBC_Comparison/Fluvius_user_005_redni2t.csv    |  82 +-
 Rule_Based_Control.py                              | 100 ++-
 Rule_Based_Control_Check.py                        |  59 ++
 __pycache__/Environment.cpython-314.pyc            | Bin 82365 -> 82599 bytes
 217 files changed, 8834 insertions(+), 8478 deletions(-)
```
