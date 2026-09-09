# gap_by_group_and_tariff

Exported 2026-09-09T15:41:40+00:00
Files: gap_by_group_and_tariff.pdf
Size: 7.16 x 10.3104 in @ 600 dpi (exact figure size)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Vrzel po tipu gospodinjstva in ceniku, enaka skala 0-74 % na vseh grafih

## Source

- notebook: not detected
- cell execution count: 16
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 07aae07e717328104ffbc6c5a04c3fd8d9e7df4f (Development)
- subject: Multiuser_Battery_Size_Optimization.ipynb run is saved. The figure I want is set to central.
- describe: 07aae07-dirty

**Working tree was DIRTY (114 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Battery_Size_Optimization.ipynb                    |    4 +-
 Energy_Community_Comparison.ipynb                  |   22 +-
 Extended_Multuser_Battery_Size_Optimization.ipynb  |   14 +-
 Household invoice generator.ipynb                  |  100 +-
 Household_local model.ipynb                        |   12 +-
 MILP_horizon_comparison.ipynb                      |   16 +-
 Multi_household_baseline.ipynb                     |   70 +-
 Multuser_Battery_Size_Optimization.ipynb           |   10 +-
 No_battery_comparison.ipynb                        | 2866 ++++++++++----------
 PLOTTING_GUIDE.txt                                 |   12 +-
 Plotting_Functions.py                              |   63 +-
 RBC_vs_MILP_Comparison.ipynb                       |   34 +-
 .../Figures/horizon/achievable_saving/SOURCE.md    |  149 +-
 .../achievable_saving/achievable_saving.pdf        |  Bin 17606 -> 17235 bytes
 Results/Figures/horizon/achievable_saving/cell.py  |    2 +-
 .../Figures/horizon/achievable_saving/source.json  |   48 +-
 .../gap_by_group_and_tariff.pdf                    |  Bin 80938 -> 80938 bytes
 .../horizon/gap_means_all_tariffs/SOURCE.md        |  175 +-
 .../Figures/horizon/gap_means_all_tariffs/cell.py  |    4 +-
 .../gap_means_all_tariffs.pdf                      |  Bin 18190 -> 17500 bytes
 .../horizon/gap_means_all_tariffs/source.json      |   46 +-
 .../horizon/gap_means_all_tariffs_zoom/SOURCE.md   |  183 +-
 .../horizon/gap_means_all_tariffs_zoom/cell.py     |    4 +-
 .../gap_means_all_tariffs_zoom.pdf                 |  Bin 15499 -> 16000 bytes
 .../horizon/gap_means_all_tariffs_zoom/source.json |   46 +-
 .../horizon/gap_spread_households/SOURCE.md        |  169 +-
 .../gap_spread_households.pdf                      |  Bin 35136 -> 35136 bytes
 .../horizon/gap_spread_households/source.json      |   46 +-
 .../horizon/horizon_gap_by_tariff/SOURCE.md        |  155 +-
 .../Figures/horizon/horizon_gap_by_tariff/cell.py  |    4 +-
 .../horizon_gap_by_tariff.pdf                      |  Bin 14634 -> 13645 bytes
 .../horizon/horizon_gap_by_tariff/source.json      |   46 +-
 .../horizon/horizon_gap_by_tariff_zoom/SOURCE.md   |  163 +-
 .../horizon/horizon_gap_by_tariff_zoom/cell.py     |    4 +-
 .../horizon_gap_by_tariff_zoom.pdf                 |  Bin 11825 -> 11939 bytes
 .../horizon/horizon_gap_by_tariff_zoom/source.json |   46 +-
 Results/Figures/horizon/runtime_vs_gap/SOURCE.md   |  191 +-
 Results/Figures/horizon/runtime_vs_gap/cell.py     |    4 +-
 .../horizon/runtime_vs_gap/runtime_vs_gap.pdf      |  Bin 24148 -> 24392 bytes
 Results/Figures/horizon/runtime_vs_gap/source.json |   46 +-
 .../Figures/invoices/invoice_composition/SOURCE.md |   78 +-
 .../Figures/invoices/invoice_composition/cell.py   |    2 +-
 .../invoice_composition/invoice_composition.pdf    |  Bin 16447 -> 16678 bytes
 .../invoices/invoice_composition/source.json       |   58 +-
 .../group_total_cost/SOURCE.md                     |  110 +-
 .../group_total_cost/group_total_cost.pdf          |  Bin 11240 -> 11241 bytes
 .../group_total_cost/source.json                   |   67 +-
 .../catalogue_all_bill_ranking/SOURCE.md           |  133 +-
 .../catalogue_all_bill_ranking.pdf                 |  Bin 27354 -> 27354 bytes
 .../catalogue_all_bill_ranking/source.json         |   50 +-
 .../catalogue_all_overpay_by_group/SOURCE.md       |  139 +-
 .../catalogue_all_overpay_by_group.pdf             |  Bin 107977 -> 107783 bytes
 .../catalogue_all_overpay_by_group/source.json     |   50 +-
 .../catalogue_no_pv_bill_ranking/SOURCE.md         |  109 +-
 .../catalogue_no_pv_bill_ranking.pdf               |  Bin 27406 -> 27406 bytes
 .../catalogue_no_pv_bill_ranking/source.json       |   48 +-
 .../catalogue_no_pv_overpay_by_group/SOURCE.md     |  115 +-
 .../catalogue_no_pv_overpay_by_group.pdf           |  Bin 76824 -> 77476 bytes
 .../catalogue_no_pv_overpay_by_group/source.json   |   50 +-
 .../catalogue_premium_by_group/SOURCE.md           |  151 +-
 .../catalogue_premium_by_group.pdf                 |  Bin 60170 -> 59569 bytes
 .../no_battery/catalogue_premium_by_group/cell.py  |    4 +-
 .../catalogue_premium_by_group/source.json         |   50 +-
 .../catalogue_premium_by_supplier/SOURCE.md        |  145 +-
 .../catalogue_premium_by_supplier.pdf              |  Bin 26985 -> 26533 bytes
 .../catalogue_premium_by_supplier/cell.py          |    4 +-
 .../catalogue_premium_by_supplier/source.json      |   50 +-
 .../catalogue_with_pv_bill_ranking/SOURCE.md       |  121 +-
 .../catalogue_with_pv_bill_ranking.pdf             |  Bin 27296 -> 27296 bytes
 .../catalogue_with_pv_bill_ranking/source.json     |   50 +-
 .../catalogue_with_pv_overpay_by_group/SOURCE.md   |  127 +-
 .../catalogue_with_pv_overpay_by_group.pdf         |  Bin 77049 -> 77800 bytes
 .../catalogue_with_pv_overpay_by_group/source.json |   50 +-
 .../no_battery/export_right_by_group/SOURCE.md     |  102 +-
 .../no_battery/export_right_by_group/cell.py       |    2 +-
 .../export_right_by_group.pdf                      |  Bin 20116 -> 20642 bytes
 .../no_battery/export_right_by_group/source.json   |   43 +-
 .../no_battery/export_right_worth/SOURCE.md        |   95 +-
 .../Figures/no_battery/export_right_worth/cell.py  |    2 +-
 .../export_right_worth/export_right_worth.pdf      |  Bin 26945 -> 26945 bytes
 .../no_battery/export_right_worth/source.json      |   38 +-
 .../no_battery/no_pv_bill_by_group/SOURCE.md       |   45 +-
 .../Figures/no_battery/no_pv_bill_by_group/cell.py |    2 +-
 .../no_pv_bill_by_group/no_pv_bill_by_group.pdf    |  Bin 16668 -> 16432 bytes
 .../no_battery/no_pv_bill_by_group/source.json     |   33 +-
 .../no_battery/no_pv_overpay_by_group/SOURCE.md    |   51 +-
 .../no_battery/no_pv_overpay_by_group/cell.py      |    2 +-
 .../no_pv_overpay_by_group.pdf                     |  Bin 64336 -> 65385 bytes
 .../no_battery/no_pv_overpay_by_group/source.json  |   33 +-
 .../no_battery/pv_bill_composition/SOURCE.md       |   63 +-
 .../Figures/no_battery/pv_bill_composition/cell.py |    2 +-
 .../pv_bill_composition/pv_bill_composition.pdf    |  Bin 17423 -> 17920 bytes
 .../no_battery/pv_bill_composition/source.json     |   33 +-
 .../Figures/no_battery/pv_bill_ranking/SOURCE.md   |   55 +-
 Results/Figures/no_battery/pv_bill_ranking/cell.py |    2 +-
 .../no_battery/pv_bill_ranking/pv_bill_ranking.pdf |  Bin 21771 -> 21771 bytes
 .../Figures/no_battery/pv_bill_ranking/source.json |   33 +-
 .../pv_nosale_bill_composition/SOURCE.md           |   85 +-
 .../no_battery/pv_nosale_bill_composition/cell.py  |    4 +-
 .../pv_nosale_bill_composition.pdf                 |  Bin 17343 -> 17857 bytes
 .../pv_nosale_bill_composition/source.json         |   33 +-
 .../no_battery/pv_nosale_bill_ranking/SOURCE.md    |   79 +-
 .../no_battery/pv_nosale_bill_ranking/cell.py      |    4 +-
 .../pv_nosale_bill_ranking.pdf                     |  Bin 22461 -> 21756 bytes
 .../no_battery/pv_nosale_bill_ranking/source.json  |   33 +-
 .../pv_nosale_overpay_by_group/SOURCE.md           |   91 +-
 .../no_battery/pv_nosale_overpay_by_group/cell.py  |    4 +-
 .../pv_nosale_overpay_by_group.pdf                 |  Bin 42949 -> 42653 bytes
 .../pv_nosale_overpay_by_group/source.json         |   33 +-
 .../no_battery/pv_overpay_by_group/SOURCE.md       |   71 +-
 .../Figures/no_battery/pv_overpay_by_group/cell.py |    2 +-
 .../pv_overpay_by_group/pv_overpay_by_group.pdf    |  Bin 46157 -> 44004 bytes
 .../no_battery/pv_overpay_by_group/source.json     |   33 +-
 Skupnostna_Samooskrba_vs_Souporaba.ipynb           |   12 +-
 114 files changed, 3990 insertions(+), 3645 deletions(-)
```
