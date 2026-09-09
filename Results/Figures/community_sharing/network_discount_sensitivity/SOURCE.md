# network_discount_sensitivity

Exported 2026-09-09T15:51:36+00:00
Files: network_discount_sensitivity.pdf
Size: 7.16 x 3.3652 in @ 600 dpi (exact figure size)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Prednost skupnostne samooskrbe je znižana distribucijska postavka — Pri značilnem primeru 4 je skupnostna distribucijska postavka praktično enaka polni (razlika je pod 0,0001 EUR/kWh), zato se prihranek skupnostne samooskrbe zoži na tisto, kar prihrani tudi souporaba — le da souporaba ob tem plača še nadomestilo organizatorju. Vsaka stopnja levo od 4 je omrežnina, ki je souporaba ne zniža.

## Source

- notebook: not detected
- cell execution count: 28
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 07aae07e717328104ffbc6c5a04c3fd8d9e7df4f (Development)
- subject: Multiuser_Battery_Size_Optimization.ipynb run is saved. The figure I want is set to central.
- describe: 07aae07-dirty

**Working tree was DIRTY (274 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff` (truncated), which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Battery_Size_Optimization.ipynb                    |    4 +-
 Energy_Community_Comparison.ipynb                  |   22 +-
 Extended_Multuser_Battery_Size_Optimization.ipynb  |   14 +-
 Household invoice generator.ipynb                  |  100 +-
 Household_local model.ipynb                        |   12 +-
 MILP_horizon_comparison.ipynb                      |  872 +++---
 Multi_household_baseline.ipynb                     |   70 +-
 Multuser_Battery_Size_Optimization.ipynb           |  598 ++--
 No_battery_comparison.ipynb                        | 2866 ++++++++++----------
 PLOTTING_GUIDE.txt                                 |   12 +-
 Plotting_Functions.py                              |   63 +-
 RBC_vs_MILP_Comparison.ipynb                       |  801 +++---
 Results/Community_Study/per_household.csv          |  210 +-
 .../SOURCE.md                                      |  402 +--
 .../cell.py                                        |    2 +-
 .../community_bill_by_scheme_10_kwh_pri_vsakem.pdf |  Bin 12167 -> 12326 bytes
 .../source.json                                    |   48 +-
 .../SOURCE.md                                      |  388 ++-
 .../community_bill_by_scheme_brez_baterije/cell.py |    2 +-
 .../community_bill_by_scheme_brez_baterije.pdf     |  Bin 12225 -> 12385 bytes
 .../source.json                                    |   44 +-
 .../SOURCE.md                                      |  395 ++-
 .../cell.py                                        |    2 +-
 ...community_bill_by_scheme_optimalna_baterija.pdf |  Bin 11861 -> 12029 bytes
 .../source.json                                    |   46 +-
 .../member_bill_change_10_kwh_pri_vsakem/SOURCE.md |  411 +--
 .../member_bill_change_10_kwh_pri_vsakem.pdf       |  Bin 14178 -> 14178 bytes
 .../source.json                                    |   50 +-
 .../member_bill_change_brez_baterije/SOURCE.md     |  407 +--
 .../member_bill_change_brez_baterije.pdf           |  Bin 14113 -> 14113 bytes
 .../member_bill_change_brez_baterije/source.json   |   50 +-
 .../network_discount_sensitivity.pdf               |  Bin 13565 -> 12764 bytes
 .../share_sweep_bill_10_kwh_pri_vsakem/SOURCE.md   |  367 ++-
 .../share_sweep_bill_10_kwh_pri_vsakem/cell.py     |    2 +-
 .../share_sweep_bill_10_kwh_pri_vsakem.pdf         |  Bin 18726 -> 18734 bytes
 .../share_sweep_bill_10_kwh_pri_vsakem/source.json |   38 +-
 .../share_sweep_bill_brez_baterije/SOURCE.md       |  360 ++-
 .../share_sweep_bill_brez_baterije/cell.py         |    2 +-
 .../share_sweep_bill_brez_baterije.pdf             |  Bin 18806 -> 18810 bytes
 .../share_sweep_bill_brez_baterije/source.json     |   36 +-
 .../share_sweep_energy_10_kwh_pri_vsakem/SOURCE.md |  381 ++-
 .../share_sweep_energy_10_kwh_pri_vsakem/cell.py   |    2 +-
 .../share_sweep_energy_10_kwh_pri_vsakem.pdf       |  Bin 13125 -> 13133 bytes
 .../source.json                                    |   42 +-
 .../share_sweep_energy_brez_baterije/SOURCE.md     |  374 ++-
 .../share_sweep_energy_brez_baterije/cell.py       |    2 +-
 .../share_sweep_energy_brez_baterije.pdf           |  Bin 12983 -> 12993 bytes
 .../share_sweep_energy_brez_baterije/source.json   |   40 +-
 .../Figures/horizon/achievable_saving/SOURCE.md    |  149 +-
 .../achievable_saving/achievable_saving.pdf        |  Bin 17606 -> 17235 bytes
 Results/Figures/horizon/achievable_saving/cell.py  |    2 +-
 .../Figures/horizon/achievable_saving/source.json  |   48 +-
 .../Figures/horizon/gap_by_consumer_type/SOURCE.md |  199 +-
 .../Figures/horizon/gap_by_consumer_type/cell.py   |    2 +-
 .../gap_by_consumer_type/gap_by_consumer_type.pdf  |  Bin 41176 -> 41176 bytes
 .../horizon/gap_by_consumer_type/source.json       |   44 +-
 .../horizon/gap_by_consumer_type_ratio/SOURCE.md   |  205 +-
 .../horizon/gap_by_consumer_type_ratio/cell.py     |    2 +-
 .../gap_by_consumer_type_ratio.pdf                 |  Bin 16074 -> 15983 bytes
 .../horizon/gap_by_consumer_type_ratio/source.json |   36 +-
 .../horizon/gap_by_group_and_tariff/SOURCE.md      |  195 +-
 .../gap_by_group_and_tariff.pdf                    |  Bin 80938 -> 80938 bytes
 .../horizon/gap_by_group_and_tariff/source.json    |   46 +-
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
 .../community_net_benefit/SOURCE.md                |  198 +-
 .../multiuser_sizing/community_net_benefit/cell.py |    4 +-
 .../community_net_benefit.pdf                      |  Bin 17272 -> 17341 bytes
 .../community_net_benefit/source.json              |  124 +-
 .../community_total_bill/SOURCE.md                 |  194 +-
 .../multiuser_sizing/community_total_bill/cell.py  |    4 +-
 .../community_total_bill/community_total_bill.pdf  |  Bin 16584 -> 16544 bytes
 .../community_total_bill/source.json               |  124 +-
 .../cost_vs_capacity_panels/SOURCE.md              |  202 +-
 .../cost_vs_capacity_panels.pdf                    |  Bin 38844 -> 38844 bytes
 .../cost_vs_capacity_panels/source.json            |  124 +-
 .../Figures/multiuser_sizing/curtailed/SOURCE.md   |  235 +-
 .../multiuser_sizing/curtailed/curtailed.pdf       |  Bin 14771 -> 14771 bytes
 .../Figures/multiuser_sizing/curtailed/source.json |  122 +-
 .../multiuser_sizing/cycles_median/SOURCE.md       |  222 +-
 .../Figures/multiuser_sizing/cycles_median/cell.py |    2 +-
 .../cycles_median/cycles_median.pdf                |  Bin 15888 -> 15882 bytes
 .../multiuser_sizing/cycles_median/source.json     |  122 +-
 .../multiuser_sizing/cycles_panels/SOURCE.md       |  220 +-
 .../Figures/multiuser_sizing/cycles_panels/cell.py |    2 +-
 .../cycles_panels/cycles_panels.pdf                |  Bin 37592 -> 37567 bytes
 .../multiuser_sizing/cycles_panels/source.json     |  124 +-
 .../multiuser_sizing/grid_charged/SOURCE.md        |  232 +-
 .../multiuser_sizing/grid_charged/grid_charged.pdf |  Bin 15430 -> 15430 bytes
 .../multiuser_sizing/grid_charged/source.json      |  122 +-
 .../headline_net_benefit/SOURCE.md                 |  226 +-
 .../headline_net_benefit/headline_net_benefit.pdf  |  Bin 18443 -> 18443 bytes
 .../headline_net_benefit/source.json               |  122 +-
 .../multiuser_sizing/headline_roi/SOURCE.md        |  229 +-
 .../multiuser_sizing/headline_roi/headline_roi.pdf |  Bin 18629 -> 18629 bytes
 .../multiuser_sizing/headline_roi/source.json      |  122 +-
 .../multiuser_sizing/inverter_fixed_fee/SOURCE.md  |  212 +-
 .../multiuser_sizing/inverter_fixed_fee/cell.py    |    2 +-
 .../inverter_fixed_fee/inverter_fixed_fee.pdf      |  Bin 16197 -> 16586 bytes
 .../inverter_fixed_fee/source.json                 |  124 +-
 .../multiuser_sizing/inverter_per_kw/SOURCE.md     |  216 +-
 .../multiuser_sizing/inverter_per_kw/cell.py       |    2 +-
 .../inverter_per_kw/inverter_per_kw.pdf            |  Bin 16949 -> 16949 bytes
 .../multiuser_sizing/inverter_per_kw/source.json   |  124 +-
 .../multiuser_sizing/marginal_value/SOURCE.md      |  210 +-
 .../multiuser_sizing/marginal_value/cell.py        |    2 +-
 .../marginal_value/marginal_value.pdf              |  Bin 39278 -> 20559 bytes
 .../multiuser_sizing/marginal_value/source.json    |  127 +-
 .../multiuser_sizing/net_benefit_panels/SOURCE.md  |  205 +-
 .../net_benefit_panels/net_benefit_panels.pdf      |  Bin 55822 -> 55822 bytes
 .../net_benefit_panels/source.json                 |  124 +-
 .../multiuser_sizing/peak_change_pct/SOURCE.md     |  241 +-
 .../peak_change_pct/peak_change_pct.pdf            |  Bin 16292 -> 16282 bytes
 .../multiuser_sizing/peak_change_pct/source.json   |  122 +-
 .../multiuser_sizing/peak_import_block_1/SOURCE.md |  247 +-
 .../peak_import_block_1/peak_import_block_1.pdf    |  Bin 15511 -> 15511 bytes
 .../peak_import_block_1/source.json                |  122 +-
 .../multiuser_sizing/peak_import_block_2/SOURCE.md |  250 +-
 .../peak_import_block_2/peak_import_block_2.pdf    |  Bin 15637 -> 15637 bytes
 .../peak_import_block_2/source.json                |  122 +-
 .../multiuser_sizing/peak_import_block_3/SOURCE.md |  253 +-
 .../peak_import_block_3/peak_import_block_3.pdf    |  Bin 15611 -> 15611 bytes
 .../peak_import_block_3/source.json                |  122 +-
 .../multiuser_sizing/peak_import_block_4/SOURCE.md |  256 +-
 .../peak_import_block_4/peak_import_block_4.pdf    |  Bin 15709 -> 15709 bytes
 .../peak_import_block_4/source.json                |  122 +-
 .../multiuser_sizing/peak_import_block_5/SOURCE.md |  259 +-
 .../peak_import_block_5/peak_import_block_5.pdf    |  Bin 15628 -> 15628 bytes
 .../peak_import_block_5/source.json                |  122 +-
 .../multiuser_sizing/peak_import_median/SOURCE.md  |  238 +-
 .../peak_import_median/peak_import_median.pdf      |  Bin 16156 -> 16156 bytes
 .../peak_import_median/source.json                 |  122 +-
 .../multiuser_sizing/peak_import_panels/SOURCE.md  |  244 +-
 .../peak_import_panels/peak_import_panels.pdf      |  Bin 31899 -> 31899 bytes
 .../peak_import_panels/source.json                 |  122 +-
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
 .../achievable_by_household_type/SOURCE.md         |  322 ++-
 .../achievable_by_household_type.pdf               |  Bin 11582 -> 11820 bytes
 .../achievable_by_household_type/cell.py           |    2 +-
 .../achievable_by_household_type/source.json       |   32 +-
 .../Figures/rbc_vs_milp/battery_earnings/SOURCE.md |  329 ++-
 .../battery_earnings/battery_earnings.pdf          |  Bin 16298 -> 16771 bytes
 .../Figures/rbc_vs_milp/battery_earnings/cell.py   |    6 +-
 .../rbc_vs_milp/battery_earnings/source.json       |   32 +-
 .../rbc_vs_milp/excess_power_charge/SOURCE.md      |  350 ++-
 .../rbc_vs_milp/excess_power_charge/cell.py        |    4 +-
 .../excess_power_charge/excess_power_charge.pdf    |  Bin 15801 -> 16156 bytes
 .../rbc_vs_milp/excess_power_charge/source.json    |   32 +-
 .../rbc_vs_milp/gap_by_household_type/SOURCE.md    |  317 ++-
 .../rbc_vs_milp/gap_by_household_type/cell.py      |    2 +-
 .../gap_by_household_type.pdf                      |  Bin 37483 -> 37618 bytes
 .../rbc_vs_milp/gap_by_household_type/source.json  |   34 +-
 .../rbc_vs_milp/gap_by_price_list/SOURCE.md        |  296 +-
 .../Figures/rbc_vs_milp/gap_by_price_list/cell.py  |    2 +-
 .../gap_by_price_list/gap_by_price_list.pdf        |  Bin 16280 -> 16455 bytes
 .../rbc_vs_milp/gap_by_price_list/source.json      |   34 +-
 Results/Figures/rbc_vs_milp/gap_by_rule/SOURCE.md  |  290 +-
 Results/Figures/rbc_vs_milp/gap_by_rule/cell.py    |    2 +-
 .../rbc_vs_milp/gap_by_rule/gap_by_rule.pdf        |  Bin 16411 -> 16543 bytes
 .../Figures/rbc_vs_milp/gap_by_rule/source.json    |   34 +-
 .../Figures/rbc_vs_milp/gap_vs_capacity/SOURCE.md  |  303 ++-
 .../Figures/rbc_vs_milp/gap_vs_capacity/cell.py    |    8 +-
 .../gap_vs_capacity/gap_vs_capacity.pdf            |  Bin 18510 -> 18786 bytes
 .../rbc_vs_milp/gap_vs_capacity/source.json        |   34 +-
 .../rbc_vs_milp/grid_charged_share/SOURCE.md       |  336 ++-
 .../Figures/rbc_vs_milp/grid_charged_share/cell.py |    6 +-
 .../grid_charged_share/grid_charged_share.pdf      |  Bin 16245 -> 16740 bytes
 .../rbc_vs_milp/grid_charged_share/source.json     |   32 +-
 .../Figures/rbc_vs_milp/peak_grid_import/SOURCE.md |  343 ++-
 .../Figures/rbc_vs_milp/peak_grid_import/cell.py   |    4 +-
 .../peak_grid_import/peak_grid_import.pdf          |  Bin 15789 -> 16124 bytes
 .../rbc_vs_milp/peak_grid_import/source.json       |   32 +-
 .../rbc_vs_milp/saving_vs_capacity/SOURCE.md       |  310 ++-
 .../Figures/rbc_vs_milp/saving_vs_capacity/cell.py |    8 +-
 .../saving_vs_capacity/saving_vs_capacity.pdf      |  Bin 19277 -> 19402 bytes
 .../rbc_vs_milp/saving_vs_capacity/source.json     |   34 +-
 Results/Figures/rbc_vs_milp/trace_day/SOURCE.md    |  283 +-
 Results/Figures/rbc_vs_milp/trace_day/cell.py      |    8 +-
 Results/Figures/rbc_vs_milp/trace_day/source.json  |   34 +-
 .../Figures/rbc_vs_milp/trace_day/trace_day.pdf    |  Bin 31149 -> 31670 bytes
 Skupnostna_Samooskrba_vs_Souporaba.ipynb           |   12 +-
 274 files changed, 15329 insertions(+), 10632 deletions(-)
```
