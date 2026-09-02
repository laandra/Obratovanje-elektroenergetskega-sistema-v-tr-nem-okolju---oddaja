# price_extreme_days

Exported 2026-09-02T06:49:59+00:00
Files: price_extreme_days.pdf
Size: 7.16 x 3.4368 in @ 600 dpi (exact figure size)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Celotna skupnost ob cenovnih skrajnostih leta

## Source

- notebook: not detected
- cell execution count: 24
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 13a96f887829200bcd1659b8ba56e381f9f992a1 (Development)
- subject: reruning the other notebook and fixing a bug
- describe: 13a96f8-dirty

**Working tree was DIRTY (62 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Energy_Community_Comparison.ipynb                  |  107 +-
 Extended_Multuser_Battery_Size_Optimization.ipynb  |    3 +-
 Household invoice generator.ipynb                  |   74 +-
 Household_local model.ipynb                        |    6 +-
 MILP_horizon_comparison.ipynb                      | 1460 +++++++++++++++-----
 Multi_household_baseline.ipynb                     |   59 +-
 Multuser_Battery_Size_Optimization.ipynb           |    3 +-
 No_battery_comparison.ipynb                        |    2 +-
 RBC_vs_MILP_Comparison.ipynb                       |    2 +-
 .../community_annual_cost/SOURCE.md                |  124 +-
 .../community_annual_cost.pdf                      |  Bin 23481 -> 23481 bytes
 .../community_annual_cost/source.json              |  122 +-
 .../Figures/horizon/achievable_saving/SOURCE.md    |   96 +-
 .../achievable_saving/achievable_saving.pdf        |  Bin 18168 -> 18168 bytes
 .../Figures/horizon/achievable_saving/source.json  |   25 +-
 .../Figures/horizon/gap_by_consumer_type/SOURCE.md |  124 +-
 .../gap_by_consumer_type/gap_by_consumer_type.pdf  |  Bin 41176 -> 41176 bytes
 .../horizon/gap_by_consumer_type/source.json       |   73 +-
 .../horizon/gap_by_consumer_type_ratio/SOURCE.md   |  127 +-
 .../gap_by_consumer_type_ratio.pdf                 |  Bin 16106 -> 16106 bytes
 .../horizon/gap_by_consumer_type_ratio/source.json |   79 +-
 .../horizon/gap_by_group_and_tariff/SOURCE.md      |  120 +-
 .../horizon/gap_by_group_and_tariff/cell.py        |    2 +-
 .../gap_by_group_and_tariff.pdf                    |  Bin 80946 -> 80946 bytes
 .../horizon/gap_by_group_and_tariff/source.json    |   65 +-
 .../horizon/gap_means_all_tariffs/SOURCE.md        |  111 +-
 .../gap_means_all_tariffs.pdf                      |  Bin 18381 -> 18381 bytes
 .../horizon/gap_means_all_tariffs/source.json      |   47 +-
 .../horizon/gap_means_all_tariffs_zoom/SOURCE.md   |  114 +-
 .../gap_means_all_tariffs_zoom.pdf                 |  Bin 15494 -> 15494 bytes
 .../horizon/gap_means_all_tariffs_zoom/source.json |   53 +-
 .../horizon/gap_spread_households/SOURCE.md        |  107 +-
 .../Figures/horizon/gap_spread_households/cell.py  |    2 +-
 .../gap_spread_households.pdf                      |  Bin 35145 -> 35145 bytes
 .../horizon/gap_spread_households/source.json      |   39 +-
 .../horizon/horizon_gap_by_tariff/SOURCE.md        |   97 +-
 .../Figures/horizon/horizon_gap_by_tariff/cell.py  |    2 +-
 .../horizon_gap_by_tariff.pdf                      |  Bin 14953 -> 14953 bytes
 .../horizon/horizon_gap_by_tariff/source.json      |   26 +-
 .../horizon/horizon_gap_by_tariff_zoom/SOURCE.md   |  103 +-
 .../horizon/horizon_gap_by_tariff_zoom/cell.py     |    2 +-
 .../horizon_gap_by_tariff_zoom.pdf                 |  Bin 11830 -> 11830 bytes
 .../horizon/horizon_gap_by_tariff_zoom/source.json |   32 +-
 Results/Figures/horizon/runtime_vs_gap/SOURCE.md   |  117 +-
 .../horizon/runtime_vs_gap/runtime_vs_gap.pdf      |  Bin 24287 -> 24287 bytes
 Results/Figures/horizon/runtime_vs_gap/source.json |   59 +-
 .../Figures/invoices/invoice_composition/SOURCE.md |   69 +-
 .../invoice_composition/invoice_composition.pdf    |  Bin 16447 -> 16447 bytes
 .../invoices/invoice_composition/source.json       |   64 +-
 .../group_total_cost/SOURCE.md                     |   66 +-
 .../group_total_cost/group_total_cost.pdf          |  Bin 11999 -> 11999 bytes
 .../group_total_cost/source.json                   |   61 +-
 Skupnostna_Samooskrba_vs_Souporaba.ipynb           | 1418 ++++++++++---------
 53 files changed, 3240 insertions(+), 2022 deletions(-)
```
