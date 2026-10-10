# headline_net_benefit

Exported 2026-10-09T22:05:09+00:00
Files: headline_net_benefit.pdf
Size: 7.16 x 16.1864 in @ 600 dpi (exact figure size)

> resized from 7.16x15.48 to 7.16x16.19 in; IEEE text applied to a figure drawn in the notebook style (scaled, not rebuilt)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Pri kateri pogodbi se nakup baterije izplača — neto letna korist pri optimalni velikosti — Vsako gospodinjstvo pri svoji najboljši velikosti na vsaki pogodbi. Stolpci levo od ničle pri 250 EUR/kWh + 1 000 EUR pomenijo izgubo. Vsak produkt nastopa dvakrat, enkrat v obliki samooskrba in enkrat brez odkupa; par si deli barvo. Sivi stolpec je zaprta pogodba NET meritve, za gospodinjstva, ki jo že imajo — ni med paketi v ponudbi, gospodinjstva brez proizvodnje pa zanjo nimajo stolpca. Vrednosti so v tabeli 8.2.

## Source

- notebook: not detected
- cell execution count: 26
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 6d87e109cf31ccd8efe484ebfa7a7694d9052f31 (Development)
- subject: some documentation
- describe: 6d87e10-dirty

**Working tree was DIRTY (411 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff` (truncated), which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
.DS_Store                                          |  Bin 6148 -> 8196 bytes
 Battery_Size_Optimization.ipynb                    |  528 +-
 CLAUDE.md                                          |    4 +
 Community_Study.py                                 |   25 +-
 Energy_Community_Comparison.ipynb                  |  798 ++-
 Extended_Multuser_Battery_Size_Optimization.ipynb  | 3847 ++++++------
 Horizon_Comparison.py                              |   28 +-
 Household invoice generator.ipynb                  |   98 +-
 Household_local model.ipynb                        |   16 +-
 MILP_Household.py                                  |   17 +
 MILP_horizon_comparison.ipynb                      |  211 +-
 Multi_household_baseline.ipynb                     |   72 +-
 ...r_Battery_Size_Optimization no cycle cost.ipynb |  537 +-
 Multuser_Battery_Size_Optimization.ipynb           |  455 +-
 No_battery_comparison.ipynb                        |  504 +-
 PLOTTING_GUIDE.txt                                 |   26 +
 Plotting_Functions.py                              |  218 +-
 RBC_vs_MILP_Comparison.ipynb                       |  241 +-
 Results/Community_Study/per_household.csv          |  100 +-
 .../battery_sizing/cost_vs_capacity/SOURCE.md      |  444 +-
 .../cost_vs_capacity/cost_vs_capacity.pdf          |  Bin 39458 -> 39458 bytes
 .../battery_sizing/cost_vs_capacity/source.json    |   57 +-
 .../energy_through_battery/SOURCE.md               |  444 +-
 .../energy_through_battery.pdf                     |  Bin 29403 -> 29317 bytes
 .../energy_through_battery/source.json             |   57 +-
 .../equivalent_full_cycles/SOURCE.md               |  444 +-
 .../equivalent_full_cycles.pdf                     |  Bin 25018 -> 25018 bytes
 .../equivalent_full_cycles/source.json             |   57 +-
 .../battery_sizing/marginal_value/SOURCE.md        |  444 +-
 .../marginal_value/marginal_value.pdf              |  Bin 30157 -> 30235 bytes
 .../battery_sizing/marginal_value/source.json      |   57 +-
 .../battery_sizing/net_annual_benefit/SOURCE.md    |  444 +-
 .../net_annual_benefit/net_annual_benefit.pdf      |  Bin 43338 -> 43338 bytes
 .../battery_sizing/net_annual_benefit/source.json  |   57 +-
 .../battery_sizing/peak_grid_import/SOURCE.md      |  444 +-
 .../peak_grid_import/peak_grid_import.pdf          |  Bin 27258 -> 27322 bytes
 .../battery_sizing/peak_grid_import/source.json    |   57 +-
 .../Figures/battery_sizing/service_life/SOURCE.md  |  444 +-
 .../battery_sizing/service_life/service_life.pdf   |  Bin 30867 -> 30926 bytes
 .../battery_sizing/service_life/source.json        |   57 +-
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
 .../SOURCE.md                                      |  423 +-
 .../community_bill_by_scheme_10_kwh_pri_vsakem.pdf |  Bin 31364 -> 27679 bytes
 .../source.json                                    |   96 +-
 .../SOURCE.md                                      |  411 +-
 .../community_bill_by_scheme_brez_baterije.pdf     |  Bin 30239 -> 27980 bytes
 .../source.json                                    |   90 +-
 .../SOURCE.md                                      |  417 +-
 ...community_bill_by_scheme_optimalna_baterija.pdf |  Bin 30543 -> 27709 bytes
 .../source.json                                    |   93 +-
 .../member_bill_change_10_kwh_pri_vsakem/SOURCE.md |  435 +-
 .../member_bill_change_10_kwh_pri_vsakem.pdf       |  Bin 35560 -> 31095 bytes
 .../source.json                                    |  102 +-
 .../member_bill_change_brez_baterije/SOURCE.md     |  429 +-
 .../member_bill_change_brez_baterije.pdf           |  Bin 35500 -> 31021 bytes
 .../member_bill_change_brez_baterije/source.json   |   99 +-
 .../network_discount_sensitivity/SOURCE.md         |  439 +-
 .../network_discount_sensitivity.pdf               |  Bin 32555 -> 28730 bytes
 .../network_discount_sensitivity/source.json       |  103 +-
 .../community_sharing/share_sweep_bill/SOURCE.md   |  425 +-
 .../community_sharing/share_sweep_bill/cell.py     |    4 +-
 .../share_sweep_bill/share_sweep_bill.pdf          |  Bin 50047 -> 44449 bytes
 .../community_sharing/share_sweep_bill/source.json |  114 +-
 .../share_sweep_energy_10_kwh_pri_vsakem/SOURCE.md |  631 +-
 .../share_sweep_energy_10_kwh_pri_vsakem.pdf       |  Bin 29366 -> 28932 bytes
 .../source.json                                    |   58 +-
 .../share_sweep_energy_brez_baterije/SOURCE.md     |  625 +-
 .../share_sweep_energy_brez_baterije.pdf           |  Bin 29142 -> 29414 bytes
 .../share_sweep_energy_brez_baterije/source.json   |   58 +-
 .../community_net_benefit/SOURCE.md                |  708 ++-
 .../community_net_benefit.pdf                      |  Bin 37120 -> 37266 bytes
 .../community_net_benefit/source.json              |   44 +-
 .../community_total_bill/SOURCE.md                 |  702 ++-
 .../community_total_bill/community_total_bill.pdf  |  Bin 35764 -> 36161 bytes
 .../community_total_bill/source.json               |   42 +-
 .../cost_vs_capacity_panels/SOURCE.md              |  710 ++-
 .../cost_vs_capacity_panels.pdf                    |  Bin 70249 -> 71081 bytes
 .../cost_vs_capacity_panels/source.json            |   42 +-
 .../extended_multiuser_sizing/curtailed/SOURCE.md  |  739 +--
 .../curtailed/curtailed.pdf                        |  Bin 33156 -> 33218 bytes
 .../curtailed/source.json                          |   42 +-
 .../cycles_panels/SOURCE.md                        |  729 ++-
 .../cycles_panels/cycles_panels.pdf                |  Bin 67739 -> 67829 bytes
 .../cycles_panels/source.json                      |   44 +-
 .../grid_charged/SOURCE.md                         |  736 ++-
 .../grid_charged/grid_charged.pdf                  |  Bin 34404 -> 34537 bytes
 .../grid_charged/source.json                       |   42 +-
 .../headline_net_benefit/SOURCE.md                 |  733 ++-
 .../headline_net_benefit/headline_net_benefit.pdf  |  Bin 38432 -> 39072 bytes
 .../headline_net_benefit/source.json               |   44 +-
 .../headline_roi/SOURCE.md                         |  735 ++-
 .../headline_roi/headline_roi.pdf                  |  Bin 38646 -> 39279 bytes
 .../headline_roi/source.json                       |   44 +-
 .../inverter_fixed_fee/SOURCE.md                   |  719 ++-
 .../inverter_fixed_fee/inverter_fixed_fee.pdf      |  Bin 33341 -> 33895 bytes
 .../inverter_fixed_fee/source.json                 |   42 +-
 .../inverter_per_kw/SOURCE.md                      |  725 ++-
 .../inverter_per_kw/inverter_per_kw.pdf            |  Bin 33934 -> 34074 bytes
 .../inverter_per_kw/source.json                    |   44 +-
 .../marginal_value/SOURCE.md                       |  718 ++-
 .../marginal_value/cell.py                         |   30 +-
 .../marginal_value/marginal_value.pdf              |  Bin 40771 -> 40929 bytes
 .../marginal_value/source.json                     |   44 +-
 .../net_benefit_panels/SOURCE.md                   |  715 ++-
 .../net_benefit_panels/net_benefit_panels.pdf      |  Bin 90739 -> 92002 bytes
 .../net_benefit_panels/source.json                 |   44 +-
 .../peak_change_pct/SOURCE.md                      |  745 +--
 .../peak_change_pct/peak_change_pct.pdf            |  Bin 35173 -> 35205 bytes
 .../peak_change_pct/source.json                    |   42 +-
 .../peak_import_median/SOURCE.md                   |  744 +--
 .../peak_import_median/peak_import_median.pdf      |  Bin 34871 -> 34778 bytes
 .../peak_import_median/source.json                 |   44 +-
 .../peak_import_panels/SOURCE.md                   |  750 +--
 .../peak_import_panels/peak_import_panels.pdf      |  Bin 60339 -> 60348 bytes
 .../peak_import_panels/source.json                 |   44 +-
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
 .../community_net_benefit/SOURCE.md                |  485 +-
 .../community_net_benefit.pdf                      |  Bin 40655 -> 36357 bytes
 .../community_net_benefit/source.json              |  124 +-
 .../community_total_bill/SOURCE.md                 |  483 +-
 .../community_total_bill/community_total_bill.pdf  |  Bin 40266 -> 35792 bytes
 .../community_total_bill/source.json               |  122 +-
 .../cost_vs_capacity_panels/SOURCE.md              |  483 +-
 .../cost_vs_capacity_panels.pdf                    |  Bin 72186 -> 66168 bytes
 .../cost_vs_capacity_panels/source.json            |  122 +-
 .../Figures/multiuser_sizing/curtailed/SOURCE.md   |  482 +-
 .../multiuser_sizing/curtailed/curtailed.pdf       |  Bin 36773 -> 32799 bytes
 .../Figures/multiuser_sizing/curtailed/source.json |  122 +-
 .../multiuser_sizing/cycles_median/SOURCE.md       |  430 +-
 .../cycles_median/cycles_median.pdf                |  Bin 29665 -> 25982 bytes
 .../multiuser_sizing/cycles_median/source.json     |   86 +-
 .../multiuser_sizing/cycles_panels/SOURCE.md       |  485 +-
 .../cycles_panels/cycles_panels.pdf                |  Bin 70357 -> 64420 bytes
 .../multiuser_sizing/cycles_panels/source.json     |  124 +-
 .../multiuser_sizing/grid_charged/SOURCE.md        |  482 +-
 .../multiuser_sizing/grid_charged/grid_charged.pdf |  Bin 38735 -> 33949 bytes
 .../multiuser_sizing/grid_charged/source.json      |  122 +-
 .../headline_net_benefit/SOURCE.md                 |  484 +-
 .../headline_net_benefit/headline_net_benefit.pdf  |  Bin 42767 -> 37922 bytes
 .../headline_net_benefit/source.json               |  124 +-
 .../multiuser_sizing/headline_roi/SOURCE.md        |  484 +-
 .../multiuser_sizing/headline_roi/headline_roi.pdf |  Bin 42874 -> 38116 bytes
 .../multiuser_sizing/headline_roi/source.json      |  124 +-
 .../multiuser_sizing/inverter_fixed_fee/SOURCE.md  |  438 +-
 .../inverter_fixed_fee/inverter_fixed_fee.pdf      |  Bin 34010 -> 30425 bytes
 .../inverter_fixed_fee/source.json                 |   94 +-
 .../multiuser_sizing/inverter_per_kw/SOURCE.md     |  438 +-
 .../inverter_per_kw/inverter_per_kw.pdf            |  Bin 37124 -> 33370 bytes
 .../multiuser_sizing/inverter_per_kw/source.json   |   94 +-
 .../multiuser_sizing/marginal_value/SOURCE.md      |  485 +-
 .../multiuser_sizing/marginal_value/cell.py        |   30 +-
 .../marginal_value/marginal_value.pdf              |  Bin 44012 -> 39374 bytes
 .../multiuser_sizing/marginal_value/source.json    |  124 +-
 .../multiuser_sizing/net_benefit_panels/SOURCE.md  |  485 +-
 .../net_benefit_panels/net_benefit_panels.pdf      |  Bin 89594 -> 83800 bytes
 .../net_benefit_panels/source.json                 |  124 +-
 .../multiuser_sizing/peak_change_pct/SOURCE.md     |  485 +-
 .../peak_change_pct/peak_change_pct.pdf            |  Bin 38450 -> 34559 bytes
 .../multiuser_sizing/peak_change_pct/source.json   |  124 +-
 .../multiuser_sizing/peak_import_block_1/SOURCE.md |  492 +-
 .../peak_import_block_1/peak_import_block_1.pdf    |  Bin 28662 -> 25353 bytes
 .../peak_import_block_1/source.json                |  126 +-
 .../multiuser_sizing/peak_import_block_2/SOURCE.md |  492 +-
 .../peak_import_block_2/peak_import_block_2.pdf    |  Bin 28558 -> 25319 bytes
 .../peak_import_block_2/source.json                |  126 +-
 .../multiuser_sizing/peak_import_block_3/SOURCE.md |  492 +-
 .../peak_import_block_3/peak_import_block_3.pdf    |  Bin 28527 -> 25290 bytes
 .../peak_import_block_3/source.json                |  126 +-
 .../multiuser_sizing/peak_import_block_4/SOURCE.md |  493 +-
 .../peak_import_block_4/peak_import_block_4.pdf    |  Bin 28512 -> 25266 bytes
 .../peak_import_block_4/source.json                |  124 +-
 .../multiuser_sizing/peak_import_block_5/SOURCE.md |  493 +-
 .../peak_import_block_5/peak_import_block_5.pdf    |  Bin 28029 -> 25020 bytes
 .../peak_import_block_5/source.json                |  124 +-
 .../multiuser_sizing/peak_import_median/SOURCE.md  |  493 +-
 .../peak_import_median/peak_import_median.pdf      |  Bin 31703 -> 28194 bytes
 .../peak_import_median/source.json                 |  124 +-
 .../multiuser_sizing/peak_import_panels/SOURCE.md  |  487 +-
 .../peak_import_panels/peak_import_panels.pdf      |  Bin 65066 -> 58640 bytes
 .../peak_import_panels/source.json                 |  126 +-
 .../community_net_benefit/SOURCE.md                |  445 +-
 .../community_net_benefit.pdf                      |  Bin 36138 -> 36145 bytes
 .../community_net_benefit/source.json              |   58 +-
 .../community_total_bill/SOURCE.md                 |  443 +-
 .../community_total_bill/community_total_bill.pdf  |  Bin 35463 -> 35478 bytes
 .../community_total_bill/source.json               |   56 +-
 .../cost_vs_capacity_panels/SOURCE.md              |  443 +-
 .../cost_vs_capacity_panels.pdf                    |  Bin 66079 -> 66134 bytes
 .../cost_vs_capacity_panels/source.json            |   56 +-
 .../curtailed/SOURCE.md                            |  428 +-
 .../curtailed/curtailed.pdf                        |  Bin 32832 -> 32832 bytes
 .../curtailed/source.json                          |   56 +-
 .../cycles_median/SOURCE.md                        |  428 +-
 .../cycles_median/cycles_median.pdf                |  Bin 26055 -> 25970 bytes
 .../cycles_median/source.json                      |   80 +-
 .../cycles_panels/SOURCE.md                        |  445 +-
 .../cycles_panels/cycles_panels.pdf                |  Bin 64972 -> 64977 bytes
 .../cycles_panels/source.json                      |   58 +-
 .../grid_charged/SOURCE.md                         |  428 +-
 .../grid_charged/grid_charged.pdf                  |  Bin 33944 -> 33948 bytes
 .../grid_charged/source.json                       |   56 +-
 .../headline_net_benefit/SOURCE.md                 |  430 +-
 .../headline_net_benefit/headline_net_benefit.pdf  |  Bin 37928 -> 37928 bytes
 .../headline_net_benefit/source.json               |   58 +-
 .../headline_roi/SOURCE.md                         |  430 +-
 .../headline_roi/headline_roi.pdf                  |  Bin 38129 -> 38129 bytes
 .../headline_roi/source.json                       |   58 +-
 .../inverter_fixed_fee/SOURCE.md                   |  445 +-
 .../inverter_fixed_fee/inverter_fixed_fee.pdf      |  Bin 33548 -> 33495 bytes
 .../inverter_fixed_fee/source.json                 |   58 +-
 .../inverter_per_kw/SOURCE.md                      |  445 +-
 .../inverter_per_kw/inverter_per_kw.pdf            |  Bin 33849 -> 33873 bytes
 .../inverter_per_kw/source.json                    |   58 +-
 .../marginal_value/SOURCE.md                       |  445 +-
 .../marginal_value/cell.py                         |   30 +-
 .../marginal_value/marginal_value.pdf              |  Bin 39475 -> 39355 bytes
 .../marginal_value/source.json                     |   58 +-
 .../net_benefit_panels/SOURCE.md                   |  445 +-
 .../net_benefit_panels/net_benefit_panels.pdf      |  Bin 83759 -> 83854 bytes
 .../net_benefit_panels/source.json                 |   58 +-
 .../peak_change_pct/SOURCE.md                      |  428 +-
 .../peak_change_pct/peak_change_pct.pdf            |  Bin 34830 -> 34838 bytes
 .../peak_change_pct/source.json                    |   56 +-
 .../peak_import_block_1/SOURCE.md                  |  430 +-
 .../peak_import_block_1/peak_import_block_1.pdf    |  Bin 25222 -> 25326 bytes
 .../peak_import_block_1/source.json                |   58 +-
 .../peak_import_block_2/SOURCE.md                  |  430 +-
 .../peak_import_block_2/peak_import_block_2.pdf    |  Bin 25242 -> 25345 bytes
 .../peak_import_block_2/source.json                |   58 +-
 .../peak_import_block_3/SOURCE.md                  |  430 +-
 .../peak_import_block_3/peak_import_block_3.pdf    |  Bin 25229 -> 25333 bytes
 .../peak_import_block_3/source.json                |   58 +-
 .../peak_import_block_4/SOURCE.md                  |  430 +-
 .../peak_import_block_4/peak_import_block_4.pdf    |  Bin 25285 -> 25385 bytes
 .../peak_import_block_4/source.json                |   58 +-
 .../peak_import_block_5/SOURCE.md                  |  430 +-
 .../peak_import_block_5/peak_import_block_5.pdf    |  Bin 25025 -> 25131 bytes
 .../peak_import_block_5/source.json                |   58 +-
 .../peak_import_median/SOURCE.md                   |  430 +-
 .../peak_import_median/peak_import_median.pdf      |  Bin 28183 -> 28283 bytes
 .../peak_import_median/source.json                 |   58 +-
 .../peak_import_panels/SOURCE.md                   |  430 +-
 .../peak_import_panels/peak_import_panels.pdf      |  Bin 59816 -> 59706 bytes
 .../peak_import_panels/source.json                 |   58 +-
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
 .../achievable_by_household_type/SOURCE.md         |  581 +-
 .../achievable_by_household_type.pdf               |  Bin 25767 -> 25767 bytes
 .../achievable_by_household_type/source.json       |   54 +-
 .../Figures/rbc_vs_milp/battery_earnings/SOURCE.md |  587 +-
 .../battery_earnings/battery_earnings.pdf          |  Bin 35485 -> 40461 bytes
 .../rbc_vs_milp/battery_earnings/source.json       |   54 +-
 .../rbc_vs_milp/excess_power_charge/SOURCE.md      |  605 +-
 .../excess_power_charge/excess_power_charge.pdf    |  Bin 34771 -> 34771 bytes
 .../rbc_vs_milp/excess_power_charge/source.json    |   54 +-
 .../rbc_vs_milp/gap_by_household_type/SOURCE.md    |  575 +-
 .../gap_by_household_type.pdf                      |  Bin 64101 -> 64101 bytes
 .../rbc_vs_milp/gap_by_household_type/source.json  |   54 +-
 .../rbc_vs_milp/gap_by_price_list/SOURCE.md        |  557 +-
 .../gap_by_price_list/gap_by_price_list.pdf        |  Bin 34234 -> 34234 bytes
 .../rbc_vs_milp/gap_by_price_list/source.json      |   54 +-
 Results/Figures/rbc_vs_milp/gap_by_rule/SOURCE.md  |  551 +-
 .../rbc_vs_milp/gap_by_rule/gap_by_rule.pdf        |  Bin 34987 -> 34987 bytes
 .../Figures/rbc_vs_milp/gap_by_rule/source.json    |   54 +-
 .../Figures/rbc_vs_milp/gap_vs_capacity/SOURCE.md  |  563 +-
 .../gap_vs_capacity/gap_vs_capacity.pdf            |  Bin 37102 -> 38826 bytes
 .../rbc_vs_milp/gap_vs_capacity/source.json        |   54 +-
 .../rbc_vs_milp/grid_charged_share/SOURCE.md       |  593 +-
 .../grid_charged_share/grid_charged_share.pdf      |  Bin 34988 -> 39973 bytes
 .../rbc_vs_milp/grid_charged_share/source.json     |   54 +-
 .../Figures/rbc_vs_milp/peak_grid_import/SOURCE.md |  599 +-
 .../peak_grid_import/peak_grid_import.pdf          |  Bin 34516 -> 34516 bytes
 .../rbc_vs_milp/peak_grid_import/source.json       |   54 +-
 .../rbc_vs_milp/saving_vs_capacity/SOURCE.md       |  569 +-
 .../saving_vs_capacity/saving_vs_capacity.pdf      |  Bin 38435 -> 42796 bytes
 .../rbc_vs_milp/saving_vs_capacity/source.json     |   54 +-
 Results/Figures/rbc_vs_milp/trace_day/SOURCE.md    |  549 +-
 Results/Figures/rbc_vs_milp/trace_day/source.json  |   58 +-
 .../Figures/rbc_vs_milp/trace_day/trace_day.pdf    |  Bin 60087 -> 60414 bytes
 Results/multiuser_battery_sizing.csv               | 4354 +++++++-------
 Results/multiuser_battery_sizing_no_cycle_cost.csv | 3842 ++++++------
 Rule_Based_Control.py                              |    1 +
 Skupnostna_Samooskrba_vs_Souporaba.ipynb           | 6157 +++++++-------------
 404 files changed, 54371 insertions(+), 30174 deletions(-)
```
