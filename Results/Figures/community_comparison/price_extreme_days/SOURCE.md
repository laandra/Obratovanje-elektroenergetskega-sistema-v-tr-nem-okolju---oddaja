# price_extreme_days

Exported 2026-10-09T14:15:05+00:00
Files: price_extreme_days.pdf
Size: 3.5 x 2.8109 in @ 600 dpi (exact figure size)

> resized from 7.16x3.44 to 3.50x2.81 in; IEEE text applied to a figure drawn in the notebook style (scaled, not rebuilt); stroke weights scaled 0.49x to the narrower canvas

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Celotna skupnost ob cenovnih skrajnostih leta

## Source

- notebook: not detected
- cell execution count: 24
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 6d87e109cf31ccd8efe484ebfa7a7694d9052f31 (Development)
- subject: some documentation
- describe: 6d87e10-dirty

**Working tree was DIRTY (194 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff` (truncated), which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
.DS_Store                                          |  Bin 6148 -> 8196 bytes
 Battery_Size_Optimization.ipynb                    |  143 +-
 CLAUDE.md                                          |    4 +
 Community_Study.py                                 |    6 +-
 Energy_Community_Comparison.ipynb                  |    4 +-
 Extended_Multuser_Battery_Size_Optimization.ipynb  | 3854 ++++++++---------
 Horizon_Comparison.py                              |   17 +-
 Household invoice generator.ipynb                  |   98 +-
 Household_local model.ipynb                        |   16 +-
 MILP_Household.py                                  |   12 +
 MILP_horizon_comparison.ipynb                      |  211 +-
 Multi_household_baseline.ipynb                     |   72 +-
 ...r_Battery_Size_Optimization no cycle cost.ipynb |  101 +-
 Multuser_Battery_Size_Optimization.ipynb           |  101 +-
 No_battery_comparison.ipynb                        |  504 +--
 PLOTTING_GUIDE.txt                                 |   26 +
 Plotting_Functions.py                              |  218 +-
 RBC_vs_MILP_Comparison.ipynb                       |    2 +-
 Results/Community_Study/per_household.csv          |  100 +-
 .../battery_effect_by_item/SOURCE.md               |  195 +-
 .../battery_effect_by_item.pdf                     |  Bin 51540 -> 51754 bytes
 .../battery_effect_by_item/source.json             |   69 +-
 .../battery_saving_by_segment/SOURCE.md            |  221 +-
 .../battery_saving_by_segment.pdf                  |  Bin 28393 -> 28628 bytes
 .../battery_saving_by_segment/source.json          |   57 +-
 .../bill_composition/SOURCE.md                     |  189 +-
 .../bill_composition/bill_composition.pdf          |  Bin 49279 -> 49531 bytes
 .../bill_composition/source.json                   |   72 +-
 .../community_annual_cost/SOURCE.md                |  186 +-
 .../community_annual_cost.pdf                      |  Bin 51423 -> 51732 bytes
 .../community_annual_cost/source.json              |   76 +-
 .../household_cost_scatter/SOURCE.md               |  215 +-
 .../household_cost_scatter.pdf                     |  Bin 43763 -> 43772 bytes
 .../household_cost_scatter/source.json             |   60 +-
 .../import_duration_curve/SOURCE.md                |  201 +-
 .../import_duration_curve/cell.py                  |    2 +-
 .../import_duration_curve.pdf                      |  Bin 47647 -> 47887 bytes
 .../import_duration_curve/source.json              |   66 +-
 .../import_duration_curve_zoom/SOURCE.md           |  208 +-
 .../import_duration_curve_zoom/cell.py             |    2 +-
 .../import_duration_curve_zoom.pdf                 |  Bin 41704 -> 41938 bytes
 .../import_duration_curve_zoom/source.json         |   63 +-
 .../price_extreme_days/price_extreme_days.pdf      |  Bin 42097 -> 42113 bytes
 .../souporaba_shared_vs_forfeited/SOURCE.md        |  227 +-
 .../souporaba_shared_vs_forfeited.pdf              |  Bin 28261 -> 28261 bytes
 .../souporaba_shared_vs_forfeited/source.json      |   54 +-
 .../community_net_benefit/SOURCE.md                |  424 +-
 .../community_net_benefit.pdf                      |  Bin 37120 -> 37266 bytes
 .../community_net_benefit/source.json              |  104 +-
 .../community_total_bill/SOURCE.md                 |  415 +-
 .../community_total_bill/community_total_bill.pdf  |  Bin 35764 -> 36161 bytes
 .../community_total_bill/source.json               |  102 +-
 .../cost_vs_capacity_panels/SOURCE.md              |  429 +-
 .../cost_vs_capacity_panels.pdf                    |  Bin 70249 -> 71081 bytes
 .../cost_vs_capacity_panels/source.json            |  102 +-
 .../extended_multiuser_sizing/curtailed/SOURCE.md  |  487 +--
 .../curtailed/curtailed.pdf                        |  Bin 33156 -> 33218 bytes
 .../curtailed/source.json                          |  102 +-
 .../cycles_panels/SOURCE.md                        |  464 +--
 .../cycles_panels/cycles_panels.pdf                |  Bin 67739 -> 67829 bytes
 .../cycles_panels/source.json                      |  104 +-
 .../grid_charged/SOURCE.md                         |  481 +--
 .../grid_charged/grid_charged.pdf                  |  Bin 34404 -> 34537 bytes
 .../grid_charged/source.json                       |  102 +-
 .../headline_net_benefit/SOURCE.md                 |  471 +--
 .../headline_net_benefit/headline_net_benefit.pdf  |  Bin 38432 -> 39072 bytes
 .../headline_net_benefit/source.json               |  104 +-
 .../headline_roi/SOURCE.md                         |  477 +--
 .../headline_roi/headline_roi.pdf                  |  Bin 38646 -> 39279 bytes
 .../headline_roi/source.json                       |  104 +-
 .../inverter_fixed_fee/SOURCE.md                   |  448 +-
 .../inverter_fixed_fee/inverter_fixed_fee.pdf      |  Bin 33341 -> 33895 bytes
 .../inverter_fixed_fee/source.json                 |  102 +-
 .../inverter_per_kw/SOURCE.md                      |  457 +-
 .../inverter_per_kw/inverter_per_kw.pdf            |  Bin 33934 -> 34074 bytes
 .../inverter_per_kw/source.json                    |  104 +-
 .../marginal_value/SOURCE.md                       |  443 +-
 .../marginal_value/cell.py                         |   28 +-
 .../marginal_value/marginal_value.pdf              |  Bin 40771 -> 40929 bytes
 .../marginal_value/source.json                     |  104 +-
 .../net_benefit_panels/SOURCE.md                   |  437 +-
 .../net_benefit_panels/net_benefit_panels.pdf      |  Bin 90739 -> 92002 bytes
 .../net_benefit_panels/source.json                 |  104 +-
 .../peak_change_pct/SOURCE.md                      |  499 +--
 .../peak_change_pct/peak_change_pct.pdf            |  Bin 35173 -> 35205 bytes
 .../peak_change_pct/source.json                    |  102 +-
 .../peak_import_median/SOURCE.md                   |  495 +--
 .../peak_import_median/peak_import_median.pdf      |  Bin 34871 -> 34778 bytes
 .../peak_import_median/source.json                 |  104 +-
 .../peak_import_panels/SOURCE.md                   |  507 +--
 .../peak_import_panels/peak_import_panels.pdf      |  Bin 60339 -> 60348 bytes
 .../peak_import_panels/source.json                 |  104 +-
 .../Figures/horizon/achievable_saving/SOURCE.md    |  371 +-
 .../achievable_saving/achievable_saving.pdf        |  Bin 40115 -> 40115 bytes
 .../Figures/horizon/achievable_saving/source.json  |  100 +-
 .../Figures/horizon/gap_by_consumer_type/SOURCE.md |  395 +-
 .../gap_by_consumer_type/gap_by_consumer_type.pdf  |  Bin 56990 -> 56899 bytes
 .../horizon/gap_by_consumer_type/source.json       |  100 +-
 .../horizon/gap_by_consumer_type_ratio/SOURCE.md   |  398 +-
 .../gap_by_consumer_type_ratio.pdf                 |  Bin 33077 -> 32990 bytes
 .../horizon/gap_by_consumer_type_ratio/source.json |  100 +-
 .../horizon/gap_by_group_and_tariff/SOURCE.md      |  396 +-
 .../gap_by_group_and_tariff.pdf                    |  Bin 102886 -> 110408 bytes
 .../horizon/gap_by_group_and_tariff/source.json    |  104 +-
 .../horizon/gap_means_all_tariffs/SOURCE.md        |  383 +-
 .../gap_means_all_tariffs.pdf                      |  Bin 32999 -> 32900 bytes
 .../horizon/gap_means_all_tariffs/source.json      |  100 +-
 .../horizon/gap_means_all_tariffs_zoom/SOURCE.md   |  386 +-
 .../gap_means_all_tariffs_zoom.pdf                 |  Bin 30071 -> 29972 bytes
 .../horizon/gap_means_all_tariffs_zoom/source.json |  100 +-
 .../horizon/gap_spread_households/SOURCE.md        |  384 +-
 .../gap_spread_households.pdf                      |  Bin 55900 -> 55876 bytes
 .../horizon/gap_spread_households/source.json      |  104 +-
 .../horizon/horizon_gap_by_tariff/SOURCE.md        |  374 +-
 .../horizon_gap_by_tariff.pdf                      |  Bin 28945 -> 28804 bytes
 .../horizon/horizon_gap_by_tariff/source.json      |  100 +-
 .../horizon/horizon_gap_by_tariff_zoom/SOURCE.md   |  377 +-
 .../horizon_gap_by_tariff_zoom.pdf                 |  Bin 25378 -> 25284 bytes
 .../horizon/horizon_gap_by_tariff_zoom/source.json |  100 +-
 Results/Figures/horizon/runtime_vs_gap/SOURCE.md   |  389 +-
 .../horizon/runtime_vs_gap/runtime_vs_gap.pdf      |  Bin 48527 -> 48527 bytes
 Results/Figures/horizon/runtime_vs_gap/source.json |  100 +-
 .../Figures/invoices/invoice_composition/SOURCE.md |  401 +-
 .../invoice_composition/invoice_composition.pdf    |  Bin 34013 -> 34091 bytes
 .../invoices/invoice_composition/source.json       |  100 +-
 .../group_total_cost/SOURCE.md                     |  405 +-
 .../group_total_cost/group_total_cost.pdf          |  Bin 27016 -> 27118 bytes
 .../group_total_cost/source.json                   |   98 +-
 .../catalogue_all_bill_ranking/SOURCE.md           |  163 +-
 .../catalogue_all_bill_ranking.pdf                 |  Bin 50864 -> 50864 bytes
 .../catalogue_all_bill_ranking/source.json         |   86 +-
 .../catalogue_all_overpay_by_group/SOURCE.md       |  176 +-
 .../catalogue_all_overpay_by_group.pdf             |  Bin 134008 -> 134071 bytes
 .../catalogue_all_overpay_by_group.txt             |   62 +-
 .../catalogue_all_overpay_by_group/source.json     |   90 +-
 .../catalogue_no_pv_bill_ranking/SOURCE.md         |  135 +-
 .../catalogue_no_pv_bill_ranking.pdf               |  Bin 50877 -> 50877 bytes
 .../catalogue_no_pv_bill_ranking/source.json       |   88 +-
 .../catalogue_no_pv_overpay_by_group/SOURCE.md     |  148 +-
 .../catalogue_no_pv_overpay_by_group.pdf           |  Bin 103659 -> 103723 bytes
 .../catalogue_no_pv_overpay_by_group.txt           |   62 +-
 .../catalogue_no_pv_overpay_by_group/source.json   |   90 +-
 .../catalogue_premium_by_group/SOURCE.md           |  190 +-
 .../catalogue_premium_by_group.pdf                 |  Bin 75374 -> 75374 bytes
 .../catalogue_premium_by_group/source.json         |   92 +-
 .../catalogue_premium_by_supplier/SOURCE.md        |  178 +-
 .../catalogue_premium_by_supplier.pdf              |  Bin 55869 -> 55869 bytes
 .../catalogue_premium_by_supplier/source.json      |   90 +-
 .../catalogue_with_pv_bill_ranking/SOURCE.md       |  150 +-
 .../catalogue_with_pv_bill_ranking.pdf             |  Bin 50806 -> 50806 bytes
 .../catalogue_with_pv_bill_ranking/source.json     |   88 +-
 .../catalogue_with_pv_overpay_by_group/SOURCE.md   |  161 +-
 .../catalogue_with_pv_overpay_by_group.pdf         |  Bin 104261 -> 104324 bytes
 .../catalogue_with_pv_overpay_by_group.txt         |   62 +-
 .../catalogue_with_pv_overpay_by_group/source.json |   86 +-
 .../no_battery/export_right_by_group/SOURCE.md     |  129 +-
 .../export_right_by_group.pdf                      |  Bin 45015 -> 45065 bytes
 .../no_battery/export_right_by_group/source.json   |   90 +-
 .../no_battery/export_right_worth/SOURCE.md        |  123 +-
 .../export_right_worth/export_right_worth.pdf      |  Bin 49704 -> 49265 bytes
 .../no_battery/export_right_worth/source.json      |   91 +-
 .../no_battery/no_pv_bill_by_group/SOURCE.md       |   64 +-
 .../no_pv_bill_by_group/no_pv_bill_by_group.pdf    |  Bin 33773 -> 33773 bytes
 .../no_battery/no_pv_bill_by_group/source.json     |   74 +-
 .../no_battery/no_pv_overpay_by_group/SOURCE.md    |   77 +-
 .../no_pv_overpay_by_group.pdf                     |  Bin 93636 -> 93698 bytes
 .../no_pv_overpay_by_group.txt                     |   50 +-
 .../no_battery/no_pv_overpay_by_group/source.json  |   76 +-
 .../no_battery/pv_bill_composition/SOURCE.md       |   86 +-
 .../pv_bill_composition/pv_bill_composition.pdf    |  Bin 32101 -> 32101 bytes
 .../no_battery/pv_bill_composition/source.json     |   77 +-
 .../Figures/no_battery/pv_bill_ranking/SOURCE.md   |   79 +-
 .../no_battery/pv_bill_ranking/pv_bill_ranking.pdf |  Bin 41345 -> 41345 bytes
 .../Figures/no_battery/pv_bill_ranking/source.json |   76 +-
 .../pv_nosale_bill_composition/SOURCE.md           |  108 +-
 .../pv_nosale_bill_composition.pdf                 |  Bin 30852 -> 30852 bytes
 .../pv_nosale_bill_composition/source.json         |   84 +-
 .../no_battery/pv_nosale_bill_ranking/SOURCE.md    |  101 +-
 .../pv_nosale_bill_ranking.pdf                     |  Bin 41327 -> 41327 bytes
 .../no_battery/pv_nosale_bill_ranking/source.json  |   81 +-
 .../pv_nosale_overpay_by_group/SOURCE.md           |  121 +-
 .../pv_nosale_overpay_by_group.pdf                 |  Bin 62013 -> 62068 bytes
 .../pv_nosale_overpay_by_group.txt                 |   12 +-
 .../pv_nosale_overpay_by_group/source.json         |   90 +-
 .../no_battery/pv_overpay_by_group/SOURCE.md       |   99 +-
 .../pv_overpay_by_group/pv_overpay_by_group.pdf    |  Bin 62418 -> 62473 bytes
 .../pv_overpay_by_group/pv_overpay_by_group.txt    |   12 +-
 .../no_battery/pv_overpay_by_group/source.json     |   80 +-
 Results/multiuser_battery_sizing.csv               | 4354 ++++++++++----------
 Results/multiuser_battery_sizing_no_cycle_cost.csv | 3836 +++++++++--------
 190 files changed, 16009 insertions(+), 18285 deletions(-)
```
