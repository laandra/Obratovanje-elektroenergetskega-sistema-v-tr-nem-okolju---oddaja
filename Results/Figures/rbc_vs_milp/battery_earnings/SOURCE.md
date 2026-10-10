# battery_earnings

Exported 2026-10-09T16:03:04+00:00
Files: battery_earnings.pdf
Size: 7.16 x 3.938 in @ 600 dpi (exact figure size)

> IEEE text applied to a figure drawn in the notebook style (scaled, not rebuilt)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- What the battery earns

## Source

- notebook: not detected
- cell execution count: 16
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 6d87e109cf31ccd8efe484ebfa7a7694d9052f31 (Development)
- subject: some documentation
- describe: 6d87e10-dirty

**Working tree was DIRTY (370 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff` (truncated), which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
.DS_Store                                          |  Bin 6148 -> 8196 bytes
 Battery_Size_Optimization.ipynb                    |  458 +-
 CLAUDE.md                                          |    4 +
 Community_Study.py                                 |    6 +-
 Energy_Community_Comparison.ipynb                  |  798 ++--
 Extended_Multuser_Battery_Size_Optimization.ipynb  | 3854 ++++++++---------
 Horizon_Comparison.py                              |   17 +-
 Household invoice generator.ipynb                  |   98 +-
 Household_local model.ipynb                        |   16 +-
 MILP_Household.py                                  |   12 +
 MILP_horizon_comparison.ipynb                      |  211 +-
 Multi_household_baseline.ipynb                     |   72 +-
 ...r_Battery_Size_Optimization no cycle cost.ipynb |  557 +--
 Multuser_Battery_Size_Optimization.ipynb           |  502 ++-
 No_battery_comparison.ipynb                        |  504 +--
 PLOTTING_GUIDE.txt                                 |   26 +
 Plotting_Functions.py                              |  218 +-
 RBC_vs_MILP_Comparison.ipynb                       |    2 +-
 Results/Community_Study/per_household.csv          |  100 +-
 .../battery_sizing/cost_vs_capacity/SOURCE.md      |  361 +-
 .../cost_vs_capacity/cost_vs_capacity.pdf          |  Bin 39458 -> 39458 bytes
 .../battery_sizing/cost_vs_capacity/source.json    |   95 +-
 .../energy_through_battery/SOURCE.md               |  370 +-
 .../energy_through_battery.pdf                     |  Bin 29403 -> 29317 bytes
 .../energy_through_battery/source.json             |   79 +-
 .../equivalent_full_cycles/SOURCE.md               |  376 +-
 .../equivalent_full_cycles.pdf                     |  Bin 25018 -> 25018 bytes
 .../equivalent_full_cycles/source.json             |   67 +-
 .../battery_sizing/marginal_value/SOURCE.md        |  364 +-
 .../marginal_value/marginal_value.pdf              |  Bin 30157 -> 30235 bytes
 .../battery_sizing/marginal_value/source.json      |   91 +-
 .../battery_sizing/net_annual_benefit/SOURCE.md    |  367 +-
 .../net_annual_benefit/net_annual_benefit.pdf      |  Bin 43338 -> 43338 bytes
 .../battery_sizing/net_annual_benefit/source.json  |   85 +-
 .../battery_sizing/peak_grid_import/SOURCE.md      |  373 +-
 .../peak_grid_import/peak_grid_import.pdf          |  Bin 27258 -> 27322 bytes
 .../battery_sizing/peak_grid_import/source.json    |   73 +-
 .../Figures/battery_sizing/service_life/SOURCE.md  |  379 +-
 .../battery_sizing/service_life/service_life.pdf   |  Bin 30867 -> 30926 bytes
 .../battery_sizing/service_life/source.json        |   61 +-
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
 .../price_extreme_days/SOURCE.md                   |  233 +-
 .../price_extreme_days/price_extreme_days.pdf      |  Bin 42097 -> 42113 bytes
 .../price_extreme_days/source.json                 |   51 +-
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
 .../community_net_benefit/SOURCE.md                |  277 +-
 .../community_net_benefit.pdf                      |  Bin 40655 -> 36358 bytes
 .../community_net_benefit/source.json              |  124 +-
 .../community_total_bill/SOURCE.md                 |  272 +-
 .../community_total_bill/community_total_bill.pdf  |  Bin 40266 -> 35790 bytes
 .../community_total_bill/source.json               |  122 +-
 .../cost_vs_capacity_panels/SOURCE.md              |  278 +-
 .../cost_vs_capacity_panels.pdf                    |  Bin 72186 -> 66167 bytes
 .../cost_vs_capacity_panels/source.json            |  122 +-
 .../Figures/multiuser_sizing/curtailed/SOURCE.md   |  309 +-
 .../multiuser_sizing/curtailed/curtailed.pdf       |  Bin 36773 -> 32799 bytes
 .../Figures/multiuser_sizing/curtailed/source.json |  122 +-
 .../multiuser_sizing/cycles_median/SOURCE.md       |  244 +-
 .../cycles_median/cycles_median.pdf                |  Bin 29665 -> 25982 bytes
 .../multiuser_sizing/cycles_median/source.json     |   86 +-
 .../multiuser_sizing/cycles_panels/SOURCE.md       |  296 +-
 .../cycles_panels/cycles_panels.pdf                |  Bin 70357 -> 64427 bytes
 .../multiuser_sizing/cycles_panels/source.json     |  124 +-
 .../multiuser_sizing/grid_charged/SOURCE.md        |  306 +-
 .../multiuser_sizing/grid_charged/grid_charged.pdf |  Bin 38735 -> 33948 bytes
 .../multiuser_sizing/grid_charged/source.json      |  122 +-
 .../headline_net_benefit/SOURCE.md                 |  302 +-
 .../headline_net_benefit/headline_net_benefit.pdf  |  Bin 42767 -> 37922 bytes
 .../headline_net_benefit/source.json               |  124 +-
 .../multiuser_sizing/headline_roi/SOURCE.md        |  305 +-
 .../multiuser_sizing/headline_roi/headline_roi.pdf |  Bin 42874 -> 38116 bytes
 .../multiuser_sizing/headline_roi/source.json      |  124 +-
 .../multiuser_sizing/inverter_fixed_fee/SOURCE.md  |  243 +-
 .../inverter_fixed_fee/inverter_fixed_fee.pdf      |  Bin 34010 -> 30425 bytes
 .../inverter_fixed_fee/source.json                 |   94 +-
 .../multiuser_sizing/inverter_per_kw/SOURCE.md     |  246 +-
 .../inverter_per_kw/inverter_per_kw.pdf            |  Bin 37124 -> 33370 bytes
 .../multiuser_sizing/inverter_per_kw/source.json   |   94 +-
 .../multiuser_sizing/marginal_value/SOURCE.md      |  286 +-
 .../multiuser_sizing/marginal_value/cell.py        |   28 +-
 .../marginal_value/marginal_value.pdf              |  Bin 44012 -> 39372 bytes
 .../multiuser_sizing/marginal_value/source.json    |  124 +-
 .../multiuser_sizing/net_benefit_panels/SOURCE.md  |  283 +-
 .../net_benefit_panels/net_benefit_panels.pdf      |  Bin 89594 -> 83803 bytes
 .../net_benefit_panels/source.json                 |  124 +-
 .../multiuser_sizing/peak_change_pct/SOURCE.md     |  318 +-
 .../peak_change_pct/peak_change_pct.pdf            |  Bin 38450 -> 34559 bytes
 .../multiuser_sizing/peak_change_pct/source.json   |  124 +-
 .../multiuser_sizing/peak_import_block_1/SOURCE.md |  331 +-
 .../peak_import_block_1/peak_import_block_1.pdf    |  Bin 28662 -> 25353 bytes
 .../peak_import_block_1/source.json                |  126 +-
 .../multiuser_sizing/peak_import_block_2/SOURCE.md |  334 +-
 .../peak_import_block_2/peak_import_block_2.pdf    |  Bin 28558 -> 25318 bytes
 .../peak_import_block_2/source.json                |  126 +-
 .../multiuser_sizing/peak_import_block_3/SOURCE.md |  337 +-
 .../peak_import_block_3/peak_import_block_3.pdf    |  Bin 28527 -> 25290 bytes
 .../peak_import_block_3/source.json                |  126 +-
 .../multiuser_sizing/peak_import_block_4/SOURCE.md |  341 +-
 .../peak_import_block_4/peak_import_block_4.pdf    |  Bin 28512 -> 25268 bytes
 .../peak_import_block_4/source.json                |  124 +-
 .../multiuser_sizing/peak_import_block_5/SOURCE.md |  344 +-
 .../peak_import_block_5/peak_import_block_5.pdf    |  Bin 28029 -> 25019 bytes
 .../peak_import_block_5/source.json                |  124 +-
 .../multiuser_sizing/peak_import_median/SOURCE.md  |  323 +-
 .../peak_import_median/peak_import_median.pdf      |  Bin 31703 -> 28194 bytes
 .../peak_import_median/source.json                 |  124 +-
 .../multiuser_sizing/peak_import_panels/SOURCE.md  |  323 +-
 .../peak_import_panels/peak_import_panels.pdf      |  Bin 65066 -> 58640 bytes
 .../peak_import_panels/source.json                 |  126 +-
 .../community_net_benefit/SOURCE.md                |  301 +-
 .../community_net_benefit.pdf                      |  Bin 36138 -> 36143 bytes
 .../community_net_benefit/source.json              |   98 +-
 .../community_total_bill/SOURCE.md                 |  296 +-
 .../community_total_bill/community_total_bill.pdf  |  Bin 35463 -> 35471 bytes
 .../community_total_bill/source.json               |   96 +-
 .../cost_vs_capacity_panels/SOURCE.md              |  302 +-
 .../cost_vs_capacity_panels.pdf                    |  Bin 66079 -> 66142 bytes
 .../cost_vs_capacity_panels/source.json            |   96 +-
 .../curtailed/SOURCE.md                            |  333 +-
 .../curtailed/curtailed.pdf                        |  Bin 32832 -> 32832 bytes
 .../curtailed/source.json                          |   96 +-
 .../cycles_median/SOURCE.md                        |  306 +-
 .../cycles_median/cycles_median.pdf                |  Bin 26055 -> 25969 bytes
 .../cycles_median/source.json                      |   80 +-
 .../cycles_panels/SOURCE.md                        |  320 +-
 .../cycles_panels/cycles_panels.pdf                |  Bin 64972 -> 64972 bytes
 .../cycles_panels/source.json                      |   98 +-
 .../grid_charged/SOURCE.md                         |  330 +-
 .../grid_charged/grid_charged.pdf                  |  Bin 33944 -> 33948 bytes
 .../grid_charged/source.json                       |   96 +-
 .../headline_net_benefit/SOURCE.md                 |  326 +-
 .../headline_net_benefit/headline_net_benefit.pdf  |  Bin 37928 -> 37928 bytes
 .../headline_net_benefit/source.json               |   98 +-
 .../headline_roi/SOURCE.md                         |  329 +-
 .../headline_roi/headline_roi.pdf                  |  Bin 38129 -> 38129 bytes
 .../headline_roi/source.json                       |   98 +-
 .../inverter_fixed_fee/SOURCE.md                   |  314 +-
 .../inverter_fixed_fee/inverter_fixed_fee.pdf      |  Bin 33548 -> 33495 bytes
 .../inverter_fixed_fee/source.json                 |   98 +-
 .../inverter_per_kw/SOURCE.md                      |  317 +-
 .../inverter_per_kw/inverter_per_kw.pdf            |  Bin 33849 -> 33873 bytes
 .../inverter_per_kw/source.json                    |   98 +-
 .../marginal_value/SOURCE.md                       |  310 +-
 .../marginal_value/cell.py                         |   28 +-
 .../marginal_value/marginal_value.pdf              |  Bin 39475 -> 39360 bytes
 .../marginal_value/source.json                     |   98 +-
 .../net_benefit_panels/SOURCE.md                   |  307 +-
 .../net_benefit_panels/net_benefit_panels.pdf      |  Bin 83759 -> 83868 bytes
 .../net_benefit_panels/source.json                 |   98 +-
 .../peak_change_pct/SOURCE.md                      |  339 +-
 .../peak_change_pct/peak_change_pct.pdf            |  Bin 34830 -> 34830 bytes
 .../peak_change_pct/source.json                    |   96 +-
 .../peak_import_block_1/SOURCE.md                  |  347 +-
 .../peak_import_block_1/peak_import_block_1.pdf    |  Bin 25222 -> 25327 bytes
 .../peak_import_block_1/source.json                |   98 +-
 .../peak_import_block_2/SOURCE.md                  |  350 +-
 .../peak_import_block_2/peak_import_block_2.pdf    |  Bin 25242 -> 25345 bytes
 .../peak_import_block_2/source.json                |   98 +-
 .../peak_import_block_3/SOURCE.md                  |  353 +-
 .../peak_import_block_3/peak_import_block_3.pdf    |  Bin 25229 -> 25332 bytes
 .../peak_import_block_3/source.json                |   98 +-
 .../peak_import_block_4/SOURCE.md                  |  356 +-
 .../peak_import_block_4/peak_import_block_4.pdf    |  Bin 25285 -> 25385 bytes
 .../peak_import_block_4/source.json                |   98 +-
 .../peak_import_block_5/SOURCE.md                  |  359 +-
 .../peak_import_block_5/peak_import_block_5.pdf    |  Bin 25025 -> 25131 bytes
 .../peak_import_block_5/source.json                |   98 +-
 .../peak_import_median/SOURCE.md                   |  338 +-
 .../peak_import_median/peak_import_median.pdf      |  Bin 28183 -> 28285 bytes
 .../peak_import_median/source.json                 |   98 +-
 .../peak_import_panels/SOURCE.md                   |  344 +-
 .../peak_import_panels/peak_import_panels.pdf      |  Bin 59816 -> 59723 bytes
 .../peak_import_panels/source.json                 |   98 +-
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
 .../achievable_by_household_type/SOURCE.md         |  581 ++-
 .../achievable_by_household_type.pdf               |  Bin 25767 -> 25767 bytes
 .../achievable_by_household_type/source.json       |   54 +-
 .../battery_earnings/battery_earnings.pdf          |  Bin 35485 -> 40461 bytes
 .../rbc_vs_milp/gap_by_household_type/SOURCE.md    |  575 ++-
 .../gap_by_household_type.pdf                      |  Bin 64101 -> 64101 bytes
 .../rbc_vs_milp/gap_by_household_type/source.json  |   54 +-
 .../rbc_vs_milp/gap_by_price_list/SOURCE.md        |  557 ++-
 .../gap_by_price_list/gap_by_price_list.pdf        |  Bin 34234 -> 34234 bytes
 .../rbc_vs_milp/gap_by_price_list/source.json      |   54 +-
 Results/Figures/rbc_vs_milp/gap_by_rule/SOURCE.md  |  551 ++-
 .../rbc_vs_milp/gap_by_rule/gap_by_rule.pdf        |  Bin 34987 -> 34987 bytes
 .../Figures/rbc_vs_milp/gap_by_rule/source.json    |   54 +-
 .../Figures/rbc_vs_milp/gap_vs_capacity/SOURCE.md  |  563 ++-
 .../gap_vs_capacity/gap_vs_capacity.pdf            |  Bin 37102 -> 38826 bytes
 .../rbc_vs_milp/gap_vs_capacity/source.json        |   54 +-
 .../rbc_vs_milp/saving_vs_capacity/SOURCE.md       |  569 ++-
 .../saving_vs_capacity/saving_vs_capacity.pdf      |  Bin 38435 -> 42796 bytes
 .../rbc_vs_milp/saving_vs_capacity/source.json     |   54 +-
 Results/Figures/rbc_vs_milp/trace_day/SOURCE.md    |  549 ++-
 Results/Figures/rbc_vs_milp/trace_day/source.json  |   58 +-
 .../Figures/rbc_vs_milp/trace_day/trace_day.pdf    |  Bin 60087 -> 60414 bytes
 Results/multiuser_battery_sizing.csv               | 4354 ++++++++++----------
 Results/multiuser_battery_sizing_no_cycle_cost.csv | 3842 +++++++++--------
 363 files changed, 36622 insertions(+), 25163 deletions(-)
```
