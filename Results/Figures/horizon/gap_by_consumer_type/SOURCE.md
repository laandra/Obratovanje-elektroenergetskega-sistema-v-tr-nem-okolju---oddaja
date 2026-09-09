# gap_by_consumer_type

Exported 2026-09-08T12:50:45+00:00
Files: gap_by_consumer_type.pdf
Size: 7.16 x 3.7232 in @ 600 dpi (tight)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Povprečna vrzel [%] po skupinah; senčenje je normirano po stolpcu, temno = najtežji odjemalec za ta algoritem

## Source

- notebook: not detected
- cell execution count: 16
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: e27b8705358a3c54beba1329067f42f895d682fd (Development)
- subject: Update Slovenian graphics
- describe: e27b870-dirty

**Working tree was DIRTY (105 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Battery_Size_Optimization.ipynb                    |    2 +-
 Energy_Community_Comparison.ipynb                  |    2 +-
 Extended_Multuser_Battery_Size_Optimization.ipynb  |   10 +-
 Household_local model.ipynb                        |    2 +-
 MILP_horizon_comparison.ipynb                      |   12 +-
 Multuser_Battery_Size_Optimization.ipynb           |    6 +-
 No_battery_comparison.ipynb                        | 2341 ++++++++++----------
 RBC_vs_MILP_Comparison.ipynb                       |    2 +-
 .../Figures/horizon/achievable_saving/SOURCE.md    |  216 +-
 .../achievable_saving/achievable_saving.pdf        |  Bin 17857 -> 17606 bytes
 Results/Figures/horizon/achievable_saving/cell.py  |    2 +-
 .../Figures/horizon/achievable_saving/source.json  |  104 +-
 .../gap_by_consumer_type/gap_by_consumer_type.pdf  |  Bin 41176 -> 41176 bytes
 .../horizon/gap_by_group_and_tariff/SOURCE.md      |  256 +--
 .../gap_by_group_and_tariff.pdf                    |  Bin 80938 -> 80938 bytes
 .../horizon/gap_by_group_and_tariff/source.json    |  104 +-
 .../horizon/gap_means_all_tariffs/SOURCE.md        |  239 +-
 .../Figures/horizon/gap_means_all_tariffs/cell.py  |    2 +-
 .../gap_means_all_tariffs.pdf                      |  Bin 18394 -> 18190 bytes
 .../horizon/gap_means_all_tariffs/source.json      |  104 +-
 .../horizon/gap_means_all_tariffs_zoom/SOURCE.md   |  244 +-
 .../horizon/gap_means_all_tariffs_zoom/cell.py     |    2 +-
 .../gap_means_all_tariffs_zoom.pdf                 |  Bin 15499 -> 15499 bytes
 .../horizon/gap_means_all_tariffs_zoom/source.json |  104 +-
 .../horizon/gap_spread_households/SOURCE.md        |  233 +-
 .../gap_spread_households.pdf                      |  Bin 35136 -> 35136 bytes
 .../horizon/gap_spread_households/source.json      |  104 +-
 .../horizon/horizon_gap_by_tariff/SOURCE.md        |  223 +-
 .../Figures/horizon/horizon_gap_by_tariff/cell.py  |    2 +-
 .../horizon_gap_by_tariff.pdf                      |  Bin 14949 -> 14634 bytes
 .../horizon/horizon_gap_by_tariff/source.json      |  104 +-
 .../horizon/horizon_gap_by_tariff_zoom/SOURCE.md   |  228 +-
 .../horizon/horizon_gap_by_tariff_zoom/cell.py     |    2 +-
 .../horizon_gap_by_tariff_zoom.pdf                 |  Bin 11825 -> 11825 bytes
 .../horizon/horizon_gap_by_tariff_zoom/source.json |  104 +-
 Results/Figures/horizon/runtime_vs_gap/SOURCE.md   |  251 +--
 Results/Figures/horizon/runtime_vs_gap/cell.py     |    4 +-
 .../horizon/runtime_vs_gap/runtime_vs_gap.pdf      |  Bin 24286 -> 24148 bytes
 Results/Figures/horizon/runtime_vs_gap/source.json |  104 +-
 .../catalogue_all_bill_ranking/SOURCE.md           |  105 +-
 .../catalogue_all_bill_ranking.pdf                 |  Bin 27460 -> 27354 bytes
 .../catalogue_all_bill_ranking/source.json         |   49 +-
 .../catalogue_all_overpay_by_group/SOURCE.md       |  107 +-
 .../catalogue_all_overpay_by_group.pdf             |  Bin 107977 -> 107977 bytes
 .../catalogue_all_overpay_by_group/source.json     |   50 +-
 .../catalogue_no_pv_bill_ranking/SOURCE.md         |   85 +-
 .../catalogue_no_pv_bill_ranking.pdf               |  Bin 27528 -> 27406 bytes
 .../catalogue_no_pv_bill_ranking/source.json       |   45 +-
 .../catalogue_no_pv_overpay_by_group/SOURCE.md     |   89 +-
 .../catalogue_no_pv_overpay_by_group.pdf           |  Bin 76824 -> 76824 bytes
 .../catalogue_no_pv_overpay_by_group/source.json   |   42 +-
 .../catalogue_premium_by_group/SOURCE.md           |  122 +-
 .../catalogue_premium_by_group.pdf                 |  Bin 60174 -> 60170 bytes
 .../no_battery/catalogue_premium_by_group/cell.py  |    4 +-
 .../catalogue_premium_by_group/source.json         |   50 +-
 .../catalogue_premium_by_supplier/SOURCE.md        |  115 +-
 .../catalogue_premium_by_supplier.pdf              |  Bin 27076 -> 26985 bytes
 .../catalogue_premium_by_supplier/cell.py          |    4 +-
 .../catalogue_premium_by_supplier/source.json      |   50 +-
 .../catalogue_with_pv_bill_ranking/SOURCE.md       |   95 +-
 .../catalogue_with_pv_bill_ranking.pdf             |  Bin 27416 -> 27296 bytes
 .../catalogue_with_pv_bill_ranking/source.json     |   45 +-
 .../catalogue_with_pv_overpay_by_group/SOURCE.md   |   99 +-
 .../catalogue_with_pv_overpay_by_group.pdf         |  Bin 77049 -> 77049 bytes
 .../catalogue_with_pv_overpay_by_group/source.json |   46 +-
 .../no_battery/export_right_by_group/SOURCE.md     |   78 +-
 .../export_right_by_group.pdf                      |  Bin 20116 -> 20116 bytes
 .../no_battery/export_right_by_group/source.json   |   44 +-
 .../no_battery/export_right_worth/SOURCE.md        |   73 +-
 .../export_right_worth/export_right_worth.pdf      |  Bin 26945 -> 26945 bytes
 .../no_battery/export_right_worth/source.json      |   43 +-
 .../no_battery/no_pv_bill_by_group/SOURCE.md       |   27 +-
 .../Figures/no_battery/no_pv_bill_by_group/cell.py |    2 +-
 .../no_pv_bill_by_group/no_pv_bill_by_group.pdf    |  Bin 16664 -> 16668 bytes
 .../no_battery/no_pv_bill_by_group/source.json     |   33 +-
 .../no_battery/no_pv_overpay_by_group/SOURCE.md    |   32 +-
 .../no_battery/no_pv_overpay_by_group/cell.py      |    2 +-
 .../no_pv_overpay_by_group.pdf                     |  Bin 64336 -> 64336 bytes
 .../no_battery/no_pv_overpay_by_group/source.json  |   36 +-
 .../no_battery/pv_bill_composition/SOURCE.md       |   44 +-
 .../Figures/no_battery/pv_bill_composition/cell.py |    6 +-
 .../pv_bill_composition/pv_bill_composition.pdf    |  Bin 17919 -> 17423 bytes
 .../no_battery/pv_bill_composition/source.json     |   38 +-
 .../Figures/no_battery/pv_bill_ranking/SOURCE.md   |   37 +-
 Results/Figures/no_battery/pv_bill_ranking/cell.py |    6 +-
 .../no_battery/pv_bill_ranking/pv_bill_ranking.pdf |  Bin 21771 -> 21771 bytes
 .../Figures/no_battery/pv_bill_ranking/source.json |   37 +-
 .../pv_nosale_bill_composition/SOURCE.md           |   61 +-
 .../no_battery/pv_nosale_bill_composition/cell.py  |    4 +-
 .../pv_nosale_bill_composition.pdf                 |  Bin 17691 -> 17343 bytes
 .../pv_nosale_bill_composition/source.json         |   41 +-
 .../no_battery/pv_nosale_bill_ranking/SOURCE.md    |   54 +-
 .../no_battery/pv_nosale_bill_ranking/cell.py      |    4 +-
 .../pv_nosale_bill_ranking.pdf                     |  Bin 22461 -> 22461 bytes
 .../no_battery/pv_nosale_bill_ranking/source.json  |   40 +-
 .../pv_nosale_overpay_by_group/SOURCE.md           |   66 +-
 .../no_battery/pv_nosale_overpay_by_group/cell.py  |    4 +-
 .../pv_nosale_overpay_by_group.pdf                 |  Bin 42949 -> 42949 bytes
 .../pv_nosale_overpay_by_group/source.json         |   42 +-
 .../no_battery/pv_overpay_by_group/SOURCE.md       |   49 +-
 .../Figures/no_battery/pv_overpay_by_group/cell.py |    6 +-
 .../pv_overpay_by_group/pv_overpay_by_group.pdf    |  Bin 46157 -> 46157 bytes
 .../no_battery/pv_overpay_by_group/source.json     |   39 +-
 Skupnostna_Samooskrba_vs_Souporaba.ipynb           |    5 +-
 104 files changed, 3644 insertions(+), 3624 deletions(-)
```
