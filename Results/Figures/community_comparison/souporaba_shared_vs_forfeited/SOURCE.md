# souporaba_shared_vs_forfeited

Exported 2026-09-16T10:25:24+00:00
Files: souporaba_shared_vs_forfeited.pdf
Size: 7.16 x 3.5084 in @ 600 dpi (exact figure size)

> IEEE text applied to a figure drawn in the notebook style (scaled, not rebuilt)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Koliko deljene energije dejansko pride do prejemnikov — oznaka je delež neizrabljene energije

## Source

- notebook: C:\Users\HP\Documents\JupyterNotebook\Energy_Community\Energy_Community_Comparison.ipynb (via __vsc_ipynb_file__)
- cell execution count: 23
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: d5900b29f97249fb6e20a20fc33375950474a3da (Development)
- subject: Puhing after merge
- describe: d5900b2-dirty

**Working tree was DIRTY (28 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Anonymous_Labels.py                                |  77 ++++-
 No_battery_comparison.ipynb                        | 172 +++++++----
 PLOTTING_GUIDE.txt                                 |  52 +++-
 Plotting_Functions.py                              | 316 ++++++++++++++++++++-
 .../battery_effect_by_item/SOURCE.md               |  74 ++---
 .../battery_effect_by_item.pdf                     | Bin 57939 -> 57947 bytes
 .../battery_effect_by_item/cell.py                 |  10 +-
 .../battery_effect_by_item/source.json             |  64 +----
 .../battery_saving_by_segment/SOURCE.md            |  74 +++--
 .../battery_saving_by_segment.pdf                  | Bin 32769 -> 32769 bytes
 .../battery_saving_by_segment/source.json          |  42 ++-
 .../bill_composition/SOURCE.md                     |  74 ++---
 .../bill_composition/bill_composition.pdf          | Bin 55127 -> 55215 bytes
 .../community_comparison/bill_composition/cell.py  |  10 +-
 .../bill_composition/source.json                   |  72 ++---
 .../community_annual_cost/SOURCE.md                |  35 +--
 .../community_annual_cost.pdf                      | Bin 58931 -> 58931 bytes
 .../community_annual_cost/source.json              |  39 +--
 .../household_cost_scatter/SOURCE.md               |  79 ++----
 .../household_cost_scatter.pdf                     | Bin 47503 -> 47503 bytes
 .../household_cost_scatter/source.json             |  53 ++--
 .../import_duration_curve/SOURCE.md                |  55 ++--
 .../import_duration_curve.pdf                      | Bin 51366 -> 51366 bytes
 .../import_duration_curve/source.json              |  41 ++-
 .../import_duration_curve_zoom/SOURCE.md           |  61 ++--
 .../import_duration_curve_zoom.pdf                 | Bin 45875 -> 45875 bytes
 .../import_duration_curve_zoom/source.json         |  41 ++-
 .../souporaba_shared_vs_forfeited.pdf              | Bin 32261 -> 32261 bytes
 28 files changed, 830 insertions(+), 611 deletions(-)
```
