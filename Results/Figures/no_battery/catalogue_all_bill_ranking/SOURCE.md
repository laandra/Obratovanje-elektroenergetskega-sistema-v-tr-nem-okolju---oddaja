# catalogue_all_bill_ranking

Exported 2026-09-10T09:18:03+00:00
Files: catalogue_all_bill_ranking.pdf
Size: 7.16 x 9.3 in @ 600 dpi (exact figure size)

> IEEE text applied to a figure drawn in the notebook style (scaled, not rebuilt)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Oba kataloga, vseh 8 tipov: isti ceniki so poceni za vse -- streho občutijo le dinamični

## Source

- notebook: not detected
- cell execution count: 21
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: f6c343f6b3c6f94abe616b574949830b83ccff0f (Development)
- subject: Adding more updated graphs
- describe: f6c343f-dirty

**Working tree was DIRTY (278 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff` (truncated), which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Battery_Size_Optimization.ipynb                    | 176 ++++---
 Energy_Community_Comparison.ipynb                  | 263 +++++-----
 Extended_Multuser_Battery_Size_Optimization.ipynb  |  29 +-
 Household invoice generator.ipynb                  |  82 +--
 Household_local model.ipynb                        |   8 +-
 MILP_horizon_comparison.ipynb                      | 185 ++++---
 Multi_household_baseline.ipynb                     |  73 +--
 Multuser_Battery_Size_Optimization.ipynb           | 364 ++++++-------
 No_battery_comparison.ipynb                        | 226 ++++----
 PLOTTING_GUIDE.txt                                 |  31 +-
 Plotting_Functions.py                              |  33 ++
 RBC_vs_MILP_Comparison.ipynb                       | 220 ++++----
 .../battery_sizing/cost_vs_capacity/SOURCE.md      | 187 ++++++-
 .../cost_vs_capacity/cost_vs_capacity.pdf          | Bin 18668 -> 40037 bytes
 .../battery_sizing/cost_vs_capacity/source.json    |  74 ++-
 .../energy_through_battery/SOURCE.md               | 206 +++++++-
 .../energy_through_battery.pdf                     | Bin 12857 -> 29481 bytes
 .../energy_through_battery/source.json             |  68 ++-
 .../equivalent_full_cycles/SOURCE.md               | 218 +++++++-
 .../equivalent_full_cycles.pdf                     | Bin 11644 -> 25380 bytes
 .../equivalent_full_cycles/source.json             |  62 ++-
 .../battery_sizing/marginal_value/SOURCE.md        | 193 ++++++-
 .../marginal_value/marginal_value.pdf              | Bin 13952 -> 30063 bytes
 .../battery_sizing/marginal_value/source.json      |  73 ++-
 .../battery_sizing/net_annual_benefit/SOURCE.md    | 200 +++++++-
 .../net_annual_benefit/net_annual_benefit.pdf      | Bin 20475 -> 44605 bytes
 .../battery_sizing/net_annual_benefit/source.json  |  71 ++-
 .../battery_sizing/peak_grid_import/SOURCE.md      | 212 +++++++-
 .../peak_grid_import/peak_grid_import.pdf          | Bin 11663 -> 27140 bytes
 .../battery_sizing/peak_grid_import/source.json    |  65 ++-
 .../Figures/battery_sizing/service_life/SOURCE.md  | 225 ++++++--
 .../battery_sizing/service_life/service_life.pdf   | Bin 14688 -> 30900 bytes
 .../battery_sizing/service_life/source.json        |  60 ++-
 .../battery_effect_by_item/SOURCE.md               | 375 ++++++++++----
 .../battery_effect_by_item.pdf                     | Bin 23272 -> 51549 bytes
 .../battery_effect_by_item/source.json             |  43 +-
 .../battery_saving_by_segment/SOURCE.md            | 403 ++++++++++-----
 .../battery_saving_by_segment.pdf                  | Bin 12410 -> 28393 bytes
 .../battery_saving_by_segment/source.json          |  43 +-
 .../bill_composition/SOURCE.md                     | 368 +++++++++----
 .../bill_composition/bill_composition.pdf          | Bin 22332 -> 49565 bytes
 .../bill_composition/source.json                   |  43 +-
 .../community_annual_cost/SOURCE.md                | 361 +++++++++----
 .../community_annual_cost.pdf                      | Bin 24166 -> 52259 bytes
 .../community_annual_cost/source.json              |  43 +-
 .../household_cost_scatter/SOURCE.md               | 396 +++++++++-----
 .../household_cost_scatter.pdf                     | Bin 25951 -> 43763 bytes
 .../household_cost_scatter/source.json             |  43 +-
 .../import_duration_curve/SOURCE.md                | 382 ++++++++++----
 .../import_duration_curve.pdf                      | Bin 29943 -> 47647 bytes
 .../import_duration_curve/source.json              |  43 +-
 .../import_duration_curve_zoom/SOURCE.md           | 389 +++++++++-----
 .../import_duration_curve_zoom.pdf                 | Bin 24699 -> 41704 bytes
 .../import_duration_curve_zoom/source.json         |  43 +-
 .../price_extreme_days/SOURCE.md                   | 415 ++++++++++-----
 .../price_extreme_days/price_extreme_days.pdf      | Bin 36036 -> 64988 bytes
 .../price_extreme_days/source.json                 |  41 +-
 .../souporaba_shared_vs_forfeited/SOURCE.md        | 410 ++++++++++-----
 .../souporaba_shared_vs_forfeited.pdf              | Bin 12907 -> 28261 bytes
 .../souporaba_shared_vs_forfeited/source.json      |  43 +-
 .../SOURCE.md                                      | 334 ++++++++----
 .../community_bill_by_scheme_10_kwh_pri_vsakem.pdf | Bin 12326 -> 27728 bytes
 .../source.json                                    |  41 +-
 .../SOURCE.md                                      | 324 +++++++++---
 .../community_bill_by_scheme_brez_baterije.pdf     | Bin 12385 -> 27283 bytes
 .../source.json                                    |  49 +-
 .../SOURCE.md                                      | 328 +++++++++---
 ...community_bill_by_scheme_optimalna_baterija.pdf | Bin 12029 -> 27256 bytes
 .../source.json                                    |  41 +-
 .../member_bill_change_10_kwh_pri_vsakem/SOURCE.md | 346 +++++++++----
 .../member_bill_change_10_kwh_pri_vsakem.pdf       | Bin 14178 -> 31086 bytes
 .../source.json                                    |  41 +-
 .../member_bill_change_brez_baterije/SOURCE.md     | 340 ++++++++----
 .../member_bill_change_brez_baterije.pdf           | Bin 14113 -> 31026 bytes
 .../member_bill_change_brez_baterije/source.json   |  41 +-
 .../network_discount_sensitivity/SOURCE.md         | 352 +++++++++----
 .../network_discount_sensitivity.pdf               | Bin 12764 -> 28732 bytes
 .../network_discount_sensitivity/source.json       |  41 +-
 .../share_sweep_bill_10_kwh_pri_vsakem/SOURCE.md   | 305 ++++++++---
 .../share_sweep_bill_10_kwh_pri_vsakem.pdf         | Bin 18461 -> 40647 bytes
 .../share_sweep_bill_10_kwh_pri_vsakem/source.json |  67 +--
 .../share_sweep_bill_brez_baterije/SOURCE.md       | 298 ++++++++---
 .../share_sweep_bill_brez_baterije.pdf             | Bin 18528 -> 40645 bytes
 .../share_sweep_bill_brez_baterije/source.json     |  73 +--
 .../share_sweep_energy_10_kwh_pri_vsakem/SOURCE.md | 318 +++++++++---
 .../share_sweep_energy_10_kwh_pri_vsakem.pdf       | Bin 13133 -> 29366 bytes
 .../source.json                                    |  55 +-
 .../share_sweep_energy_brez_baterije/SOURCE.md     | 312 ++++++++---
 .../share_sweep_energy_brez_baterije.pdf           | Bin 12993 -> 29142 bytes
 .../share_sweep_energy_brez_baterije/source.json   |  61 +--
 .../Figures/horizon/achievable_saving/SOURCE.md    | 383 ++++++++++----
 .../achievable_saving/achievable_saving.pdf        | Bin 17235 -> 40115 bytes
 .../Figures/horizon/achievable_saving/source.json  |  99 ++--
 .../Figures/horizon/gap_by_consumer_type/SOURCE.md | 413 ++++++++++-----
 .../gap_by_consumer_type/gap_by_consumer_type.pdf  | Bin 41176 -> 56990 bytes
 .../horizon/gap_by_consumer_type/source.json       |  99 ++--
 .../horizon/gap_by_consumer_type_ratio/SOURCE.md   | 417 ++++++++++-----
 .../gap_by_consumer_type_ratio.pdf                 | Bin 15983 -> 33077 bytes
 .../horizon/gap_by_consumer_type_ratio/source.json |  99 ++--
 .../horizon/gap_by_group_and_tariff/SOURCE.md      | 408 ++++++++++-----
 .../gap_by_group_and_tariff.pdf                    | Bin 80938 -> 102886 bytes
 .../horizon/gap_by_group_and_tariff/source.json    |  97 ++--
 .../horizon/gap_means_all_tariffs/SOURCE.md        | 398 ++++++++++----
 .../gap_means_all_tariffs.pdf                      | Bin 17500 -> 32999 bytes
 .../horizon/gap_means_all_tariffs/source.json      |  99 ++--
 .../horizon/gap_means_all_tariffs_zoom/SOURCE.md   | 402 +++++++++++----
 .../gap_means_all_tariffs_zoom.pdf                 | Bin 16000 -> 30071 bytes
 .../horizon/gap_means_all_tariffs_zoom/source.json |  99 ++--
 .../horizon/gap_spread_households/SOURCE.md        | 393 ++++++++++----
 .../gap_spread_households.pdf                      | Bin 35136 -> 55900 bytes
 .../horizon/gap_spread_households/source.json      |  96 ++--
 .../horizon/horizon_gap_by_tariff/SOURCE.md        | 387 ++++++++++----
 .../horizon_gap_by_tariff.pdf                      | Bin 13645 -> 28945 bytes
 .../horizon/horizon_gap_by_tariff/source.json      |  99 ++--
 .../horizon/horizon_gap_by_tariff_zoom/SOURCE.md   | 391 ++++++++++----
 .../horizon_gap_by_tariff_zoom.pdf                 | Bin 11939 -> 25378 bytes
 .../horizon/horizon_gap_by_tariff_zoom/source.json |  99 ++--
 Results/Figures/horizon/runtime_vs_gap/SOURCE.md   | 406 ++++++++++-----
 .../horizon/runtime_vs_gap/runtime_vs_gap.pdf      | Bin 24392 -> 48527 bytes
 Results/Figures/horizon/runtime_vs_gap/source.json |  99 ++--
 .../Figures/invoices/invoice_composition/SOURCE.md | 313 ++++++++++-
 .../invoice_composition/invoice_composition.pdf    | Bin 16678 -> 34013 bytes
 .../invoices/invoice_composition/source.json       |  66 ++-
 .../group_total_cost/SOURCE.md                     | 309 ++++++++++-
 .../group_total_cost/group_total_cost.pdf          | Bin 11241 -> 27016 bytes
 .../group_total_cost/source.json                   |  64 ++-
 .../community_net_benefit/SOURCE.md                | 571 +++++++++++----------
 .../community_net_benefit.pdf                      | Bin 17341 -> 36265 bytes
 .../community_net_benefit/source.json              |  99 ++--
 .../community_total_bill/SOURCE.md                 | 571 +++++++++++----------
 .../community_total_bill/community_total_bill.pdf  | Bin 16544 -> 35420 bytes
 .../community_total_bill/source.json               |  99 ++--
 .../cost_vs_capacity_panels/SOURCE.md              | 571 +++++++++++----------
 .../cost_vs_capacity_panels.pdf                    | Bin 38844 -> 66002 bytes
 .../cost_vs_capacity_panels/source.json            |  98 ++--
 .../Figures/multiuser_sizing/curtailed/SOURCE.md   | 570 ++++++++++----------
 .../multiuser_sizing/curtailed/curtailed.pdf       | Bin 14771 -> 32737 bytes
 .../Figures/multiuser_sizing/curtailed/source.json |  99 ++--
 .../multiuser_sizing/cycles_median/SOURCE.md       | 570 ++++++++++----------
 .../cycles_median/cycles_median.pdf                | Bin 15882 -> 34504 bytes
 .../multiuser_sizing/cycles_median/source.json     |  99 ++--
 .../multiuser_sizing/cycles_panels/SOURCE.md       | 570 ++++++++++----------
 .../cycles_panels/cycles_panels.pdf                | Bin 37567 -> 64329 bytes
 .../multiuser_sizing/cycles_panels/source.json     |  98 ++--
 .../multiuser_sizing/grid_charged/SOURCE.md        | 570 ++++++++++----------
 .../multiuser_sizing/grid_charged/grid_charged.pdf | Bin 15430 -> 33835 bytes
 .../multiuser_sizing/grid_charged/source.json      |  99 ++--
 .../headline_net_benefit/SOURCE.md                 | 570 ++++++++++----------
 .../headline_net_benefit/headline_net_benefit.pdf  | Bin 18443 -> 37491 bytes
 .../headline_net_benefit/source.json               |  99 ++--
 .../multiuser_sizing/headline_roi/SOURCE.md        | 570 ++++++++++----------
 .../multiuser_sizing/headline_roi/headline_roi.pdf | Bin 18629 -> 37669 bytes
 .../multiuser_sizing/headline_roi/source.json      |  99 ++--
 .../multiuser_sizing/inverter_fixed_fee/SOURCE.md  | 570 ++++++++++----------
 .../inverter_fixed_fee/inverter_fixed_fee.pdf      | Bin 16586 -> 33470 bytes
 .../inverter_fixed_fee/source.json                 |  99 ++--
 .../multiuser_sizing/inverter_per_kw/SOURCE.md     | 570 ++++++++++----------
 .../inverter_per_kw/inverter_per_kw.pdf            | Bin 16949 -> 33457 bytes
 .../multiuser_sizing/inverter_per_kw/source.json   |  99 ++--
 .../multiuser_sizing/marginal_value/SOURCE.md      | 569 ++++++++++----------
 .../multiuser_sizing/marginal_value/cell.py        |   2 +-
 .../marginal_value/marginal_value.pdf              | Bin 39278 -> 39278 bytes
 .../multiuser_sizing/marginal_value/source.json    |  96 ++--
 .../multiuser_sizing/net_benefit_panels/SOURCE.md  | 571 +++++++++++----------
 .../net_benefit_panels/net_benefit_panels.pdf      | Bin 55822 -> 82672 bytes
 .../net_benefit_panels/source.json                 |  98 ++--
 .../multiuser_sizing/peak_change_pct/SOURCE.md     | 570 ++++++++++----------
 .../peak_change_pct/peak_change_pct.pdf            | Bin 16282 -> 34506 bytes
 .../multiuser_sizing/peak_change_pct/source.json   |  99 ++--
 .../multiuser_sizing/peak_import_block_1/SOURCE.md | 570 ++++++++++----------
 .../peak_import_block_1/peak_import_block_1.pdf    | Bin 15511 -> 33546 bytes
 .../peak_import_block_1/source.json                |  99 ++--
 .../multiuser_sizing/peak_import_block_2/SOURCE.md | 570 ++++++++++----------
 .../peak_import_block_2/peak_import_block_2.pdf    | Bin 15637 -> 33667 bytes
 .../peak_import_block_2/source.json                |  99 ++--
 .../multiuser_sizing/peak_import_block_3/SOURCE.md | 570 ++++++++++----------
 .../peak_import_block_3/peak_import_block_3.pdf    | Bin 15611 -> 33639 bytes
 .../peak_import_block_3/source.json                |  99 ++--
 .../multiuser_sizing/peak_import_block_4/SOURCE.md | 570 ++++++++++----------
 .../peak_import_block_4/peak_import_block_4.pdf    | Bin 15709 -> 33874 bytes
 .../peak_import_block_4/source.json                |  99 ++--
 .../multiuser_sizing/peak_import_block_5/SOURCE.md | 570 ++++++++++----------
 .../peak_import_block_5/peak_import_block_5.pdf    | Bin 15628 -> 33656 bytes
 .../peak_import_block_5/source.json                |  99 ++--
 .../multiuser_sizing/peak_import_median/SOURCE.md  | 570 ++++++++++----------
 .../peak_import_median/peak_import_median.pdf      | Bin 16156 -> 34658 bytes
 .../peak_import_median/source.json                 |  99 ++--
 .../multiuser_sizing/peak_import_panels/SOURCE.md  | 570 ++++++++++----------
 .../peak_import_panels/peak_import_panels.pdf      | Bin 31899 -> 58674 bytes
 .../peak_import_panels/source.json                 |  98 ++--
 .../catalogue_all_bill_ranking/SOURCE.md           | 246 ++++++---
 .../catalogue_all_bill_ranking.pdf                 | Bin 27354 -> 50864 bytes
 .../catalogue_all_bill_ranking/source.json         |  89 ++--
 .../catalogue_all_overpay_by_group/SOURCE.md       | 252 ++++++---
 .../catalogue_all_overpay_by_group.pdf             | Bin 107783 -> 134008 bytes
 .../catalogue_all_overpay_by_group/source.json     |  89 ++--
 .../catalogue_no_pv_bill_ranking/SOURCE.md         | 357 ++++++++++---
 .../catalogue_no_pv_bill_ranking.pdf               | Bin 27406 -> 50877 bytes
 .../catalogue_no_pv_bill_ranking/source.json       |  99 ++--
 .../catalogue_no_pv_overpay_by_group/SOURCE.md     | 360 ++++++++++---
 .../catalogue_no_pv_overpay_by_group.pdf           | Bin 77476 -> 103659 bytes
 .../catalogue_no_pv_overpay_by_group/source.json   |  99 ++--
 .../catalogue_premium_by_group/SOURCE.md           | 265 ++++++----
 .../catalogue_premium_by_group.pdf                 | Bin 59569 -> 75374 bytes
 .../catalogue_premium_by_group/source.json         |  89 ++--
 .../catalogue_premium_by_supplier/SOURCE.md        | 258 ++++++----
 .../catalogue_premium_by_supplier.pdf              | Bin 26533 -> 55869 bytes
 .../catalogue_premium_by_supplier/source.json      |  89 ++--
 .../catalogue_with_pv_bill_ranking/SOURCE.md       | 363 ++++++++++---
 .../catalogue_with_pv_bill_ranking.pdf             | Bin 27296 -> 50806 bytes
 .../catalogue_with_pv_bill_ranking/source.json     |  99 ++--
 .../catalogue_with_pv_overpay_by_group/SOURCE.md   | 366 ++++++++++---
 .../catalogue_with_pv_overpay_by_group.pdf         | Bin 77800 -> 104261 bytes
 .../catalogue_with_pv_overpay_by_group/source.json |  99 ++--
 .../no_battery/export_right_by_group/SOURCE.md     | 353 ++++++++++---
 .../export_right_by_group.pdf                      | Bin 20642 -> 45015 bytes
 .../no_battery/export_right_by_group/source.json   |  99 ++--
 .../no_battery/export_right_worth/SOURCE.md        | 349 ++++++++++---
 .../export_right_worth/export_right_worth.pdf      | Bin 26945 -> 49704 bytes
 .../no_battery/export_right_worth/source.json      |  99 ++--
 .../no_battery/no_pv_bill_by_group/SOURCE.md       | 317 ++++++++++--
 .../no_pv_bill_by_group/no_pv_bill_by_group.pdf    | Bin 16432 -> 33773 bytes
 .../no_battery/no_pv_bill_by_group/source.json     |  70 ++-
 .../no_battery/no_pv_overpay_by_group/SOURCE.md    | 321 ++++++++++--
 .../no_pv_overpay_by_group.pdf                     | Bin 65385 -> 93636 bytes
 .../no_battery/no_pv_overpay_by_group/source.json  |  74 ++-
 .../no_battery/pv_bill_composition/SOURCE.md       | 329 ++++++++++--
 .../pv_bill_composition/pv_bill_composition.pdf    | Bin 17920 -> 32101 bytes
 .../no_battery/pv_bill_composition/source.json     |  82 +--
 .../Figures/no_battery/pv_bill_ranking/SOURCE.md   | 325 ++++++++++--
 .../no_battery/pv_bill_ranking/pv_bill_ranking.pdf | Bin 21771 -> 41345 bytes
 .../Figures/no_battery/pv_bill_ranking/source.json |  78 ++-
 .../pv_nosale_bill_composition/SOURCE.md           | 341 ++++++++++--
 .../pv_nosale_bill_composition.pdf                 | Bin 17857 -> 30852 bytes
 .../pv_nosale_bill_composition/source.json         |  94 ++--
 .../no_battery/pv_nosale_bill_ranking/SOURCE.md    | 337 ++++++++++--
 .../pv_nosale_bill_ranking.pdf                     | Bin 21756 -> 41327 bytes
 .../no_battery/pv_nosale_bill_ranking/source.json  |  90 ++--
 .../pv_nosale_overpay_by_group/SOURCE.md           | 345 +++++++++++--
 .../pv_nosale_overpay_by_group.pdf                 | Bin 42653 -> 62013 bytes
 .../pv_nosale_overpay_by_group/source.json         |  98 ++--
 .../no_battery/pv_overpay_by_group/SOURCE.md       | 333 ++++++++++--
 .../pv_overpay_by_group/pv_overpay_by_group.pdf    | Bin 44004 -> 62418 bytes
 .../no_battery/pv_overpay_by_group/source.json     |  86 ++--
 .../achievable_by_household_type/SOURCE.md         | 269 ++++++++--
 .../achievable_by_household_type.pdf               | Bin 11820 -> 25767 bytes
 .../achievable_by_household_type/source.json       |  73 +--
 .../Figures/rbc_vs_milp/battery_earnings/SOURCE.md | 275 ++++++++--
 .../battery_earnings/battery_earnings.pdf          | Bin 16771 -> 35485 bytes
 .../rbc_vs_milp/battery_earnings/source.json       |  76 +--
 .../rbc_vs_milp/excess_power_charge/SOURCE.md      | 293 ++++++++---
 .../excess_power_charge/excess_power_charge.pdf    | Bin 16156 -> 34771 bytes
 .../rbc_vs_milp/excess_power_charge/source.json    |  79 +--
 .../rbc_vs_milp/gap_by_household_type/SOURCE.md    | 263 ++++++++--
 .../gap_by_household_type.pdf                      | Bin 37618 -> 64101 bytes
 .../rbc_vs_milp/gap_by_household_type/source.json  |  70 +--
 .../rbc_vs_milp/gap_by_price_list/SOURCE.md        | 245 +++++++--
 .../gap_by_price_list/gap_by_price_list.pdf        | Bin 16455 -> 34234 bytes
 .../rbc_vs_milp/gap_by_price_list/source.json      |  61 ++-
 Results/Figures/rbc_vs_milp/gap_by_rule/SOURCE.md  | 238 +++++++--
 .../rbc_vs_milp/gap_by_rule/gap_by_rule.pdf        | Bin 16542 -> 34987 bytes
 .../Figures/rbc_vs_milp/gap_by_rule/source.json    |  57 +-
 .../Figures/rbc_vs_milp/gap_vs_capacity/SOURCE.md  | 251 +++++++--
 .../gap_vs_capacity/gap_vs_capacity.pdf            | Bin 18786 -> 37102 bytes
 .../rbc_vs_milp/gap_vs_capacity/source.json        |  64 ++-
 .../rbc_vs_milp/grid_charged_share/SOURCE.md       | 281 +++++++---
 .../grid_charged_share/grid_charged_share.pdf      | Bin 16740 -> 34988 bytes
 .../rbc_vs_milp/grid_charged_share/source.json     |  79 +--
 .../Figures/rbc_vs_milp/peak_grid_import/SOURCE.md | 287 ++++++++---
 .../peak_grid_import/peak_grid_import.pdf          | Bin 16124 -> 34516 bytes
 .../rbc_vs_milp/peak_grid_import/source.json       |  79 +--
 .../rbc_vs_milp/saving_vs_capacity/SOURCE.md       | 257 ++++++++--
 .../saving_vs_capacity/saving_vs_capacity.pdf      | Bin 19402 -> 38435 bytes
 .../rbc_vs_milp/saving_vs_capacity/source.json     |  67 ++-
 Results/Figures/rbc_vs_milp/trace_day/SOURCE.md    | 230 +++++++--
 Results/Figures/rbc_vs_milp/trace_day/source.json  |  52 +-
 .../Figures/rbc_vs_milp/trace_day/trace_day.pdf    | Bin 31670 -> 60087 bytes
 Skupnostna_Samooskrba_vs_Souporaba.ipynb           | 268 +++++-----
 278 files changed, 27634 insertions(+), 14756 deletions(-)
```
