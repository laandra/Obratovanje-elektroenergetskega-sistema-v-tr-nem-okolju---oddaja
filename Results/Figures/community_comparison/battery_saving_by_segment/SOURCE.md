# battery_saving_by_segment

Exported 2026-09-02T08:44:21+00:00
Files: battery_saving_by_segment.pdf
Size: 7.16 x 3.7232 in @ 600 dpi (tight)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Letni prihranek s 30 kWh baterijo — isto gospodinjstvo, obračunano brez baterije, vse drugo nespremenjeno

## Source

- notebook: /Users/summerscholl/Documents/Andraz/Energy_Community/Energy_Community_Comparison.ipynb (via __vsc_ipynb_file__)
- cell execution count: 58
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 7940b1377d833816b4278c4c3f71855080b2f016 (Development)
- subject: Mostly rerun evrything and implemented new ploting function on the whole notebook.     An error remaining in RBC
- describe: 7940b13-dirty

**Working tree was DIRTY (30 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
DQN/dqn_model                                      | Bin 223465 -> 223465 bytes
 Environment.py                                     |  23 +-
 Horizon_Comparison.py                              |  28 +
 Household_local model.ipynb                        | 647 +++++++++++++---
 RBC_vs_MILP_Comparison.ipynb                       | 819 +++++++++++----------
 .../battery_effect_by_item/SOURCE.md               |  87 +--
 .../battery_effect_by_item.pdf                     | Bin 23266 -> 23266 bytes
 .../battery_effect_by_item/source.json             |  80 +-
 .../battery_saving_by_segment.pdf                  | Bin 12677 -> 12677 bytes
 .../bill_composition/SOURCE.md                     |  84 +--
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
 .../import_duration_curve/source.json              |  83 +--
 .../import_duration_curve_zoom/SOURCE.md           |  93 +--
 .../import_duration_curve_zoom.pdf                 | Bin 24231 -> 24231 bytes
 .../import_duration_curve_zoom/source.json         |  86 +--
 Results/Figures/rbc_vs_milp/trace_day/SOURCE.md    |  76 +-
 Results/Figures/rbc_vs_milp/trace_day/source.json  |  69 +-
 .../Figures/rbc_vs_milp/trace_day/trace_day.pdf    | Bin 31141 -> 31149 bytes
 Rule_Based_Control.py                              | 100 ++-
 Rule_Based_Control_Check.py                        |  59 ++
 __pycache__/Environment.cpython-314.pyc            | Bin 82365 -> 82554 bytes
 30 files changed, 1513 insertions(+), 1330 deletions(-)
```
