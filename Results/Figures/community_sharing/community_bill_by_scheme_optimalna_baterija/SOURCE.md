# community_bill_by_scheme_optimalna_baterija

Exported 2026-09-04T10:48:51+00:00
Files: community_bill_by_scheme_optimalna_baterija.pdf
Size: 7.16 x 3.7232 in @ 600 dpi (exact figure size)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Letni račun šestnajstih gospodinjstev, po shemi in ceniku — optimalna baterija — Prosta razdelitev deljene energije po intervalih, interna cena 0.050 EUR/kWh, značilni primer 2. Šrafirano = skupnostna samooskrba na ceniku, ki je izrecno ne dovoli (izračun je protidejstven). Manjkajoč stolpec = kombinacija, ki v tej študiji ni rešena (dinamični cenik se rešuje le brez hrambe, razdelek 7).

## Source

- notebook: not detected
- cell execution count: 25
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 7d7dbc1e3272f9f1e0fcb3305e503472b8188cca (Development)
- subject: Fixed a 2T bug and rerun the notebooks
- describe: 7d7dbc1-dirty

**Working tree was DIRTY (194 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Battery_Size_Optimization.ipynb                    |  611 ++--
 Energy_Community_Comparison.ipynb                  | 1003 +++----
 Extended_Multuser_Battery_Size_Optimization.ipynb  |   52 +-
 MILP_horizon_comparison.ipynb                      |  982 +++----
 Multi_household_baseline.ipynb                     |  511 ++--
 Multuser_Battery_Size_Optimization.ipynb           |   42 +-
 No_battery_comparison.ipynb                        | 2939 +++++++++++---------
 Plotting_Functions.py                              |   13 +-
 RBC_vs_MILP_Comparison.ipynb                       |    4 +-
 Results/Community_Study/per_household.csv          |  210 +-
 .../battery_sizing/cost_vs_capacity/SOURCE.md      |  114 +-
 .../cost_vs_capacity/cost_vs_capacity.pdf          |  Bin 18668 -> 18668 bytes
 .../battery_sizing/cost_vs_capacity/source.json    |   76 +-
 .../energy_through_battery/SOURCE.md               |  123 +-
 .../energy_through_battery.pdf                     |  Bin 12857 -> 12857 bytes
 .../energy_through_battery/source.json             |   76 +-
 .../equivalent_full_cycles/SOURCE.md               |  129 +-
 .../equivalent_full_cycles.pdf                     |  Bin 11509 -> 11509 bytes
 .../equivalent_full_cycles/source.json             |   76 +-
 .../battery_sizing/marginal_value/SOURCE.md        |  117 +-
 .../marginal_value/marginal_value.pdf              |  Bin 13939 -> 13939 bytes
 .../battery_sizing/marginal_value/source.json      |   76 +-
 .../battery_sizing/net_annual_benefit/SOURCE.md    |  119 +-
 .../net_annual_benefit/net_annual_benefit.pdf      |  Bin 20475 -> 20475 bytes
 .../battery_sizing/net_annual_benefit/source.json  |   75 +-
 .../battery_sizing/peak_grid_import/SOURCE.md      |  126 +-
 .../peak_grid_import/peak_grid_import.pdf          |  Bin 11663 -> 11663 bytes
 .../battery_sizing/peak_grid_import/source.json    |   76 +-
 .../Figures/battery_sizing/service_life/SOURCE.md  |  132 +-
 .../Figures/battery_sizing/service_life/cell.py    |    8 +-
 .../battery_sizing/service_life/service_life.pdf   |  Bin 14689 -> 14689 bytes
 .../battery_sizing/service_life/source.json        |   76 +-
 .../battery_effect_by_item/SOURCE.md               |  147 +-
 .../battery_effect_by_item.pdf                     |  Bin 23266 -> 23266 bytes
 .../battery_effect_by_item/source.json             |   78 +-
 .../battery_saving_by_segment/SOURCE.md            |  171 +-
 .../battery_saving_by_segment.pdf                  |  Bin 12677 -> 12673 bytes
 .../battery_saving_by_segment/source.json          |   70 +-
 .../bill_composition/SOURCE.md                     |  141 +-
 .../bill_composition/bill_composition.pdf          |  Bin 22190 -> 22190 bytes
 .../bill_composition/source.json                   |   81 +-
 .../community_annual_cost/SOURCE.md                |  135 +-
 .../community_annual_cost.pdf                      |  Bin 23481 -> 23481 bytes
 .../community_annual_cost/source.json              |   84 +-
 .../household_cost_scatter/SOURCE.md               |  165 +-
 .../household_cost_scatter.pdf                     |  Bin 25359 -> 25349 bytes
 .../household_cost_scatter/source.json             |   69 +-
 .../import_duration_curve/SOURCE.md                |  153 +-
 .../import_duration_curve.pdf                      |  Bin 30012 -> 30012 bytes
 .../import_duration_curve/source.json              |   75 +-
 .../import_duration_curve_zoom/SOURCE.md           |  159 +-
 .../import_duration_curve_zoom.pdf                 |  Bin 24231 -> 24231 bytes
 .../import_duration_curve_zoom/source.json         |   72 +-
 .../price_extreme_days/SOURCE.md                   |  183 +-
 .../price_extreme_days/price_extreme_days.pdf      |  Bin 36454 -> 36454 bytes
 .../price_extreme_days/source.json                 |   76 +-
 .../souporaba_shared_vs_forfeited/SOURCE.md        |  177 +-
 .../souporaba_shared_vs_forfeited.pdf              |  Bin 11890 -> 11890 bytes
 .../souporaba_shared_vs_forfeited/source.json      |   73 +-
 .../SOURCE.md                                      |  253 +-
 .../community_bill_by_scheme_10_kwh_pri_vsakem.pdf |  Bin 12167 -> 12167 bytes
 .../source.json                                    |  124 +-
 .../SOURCE.md                                      |  264 +-
 .../community_bill_by_scheme_brez_baterije.pdf     |  Bin 12225 -> 12225 bytes
 .../source.json                                    |  124 +-
 .../SOURCE.md                                      |  250 +-
 ...community_bill_by_scheme_optimalna_baterija.pdf |  Bin 11861 -> 11861 bytes
 .../source.json                                    |  124 +-
 .../member_bill_change_10_kwh_pri_vsakem/SOURCE.md |  259 +-
 .../member_bill_change_10_kwh_pri_vsakem.pdf       |  Bin 14178 -> 14178 bytes
 .../source.json                                    |  124 +-
 .../member_bill_change_brez_baterije/SOURCE.md     |  256 +-
 .../member_bill_change_brez_baterije.pdf           |  Bin 14113 -> 14113 bytes
 .../member_bill_change_brez_baterije/source.json   |  124 +-
 .../network_discount_sensitivity/SOURCE.md         |  262 +-
 .../network_discount_sensitivity.pdf               |  Bin 14247 -> 14247 bytes
 .../network_discount_sensitivity/source.json       |  124 +-
 .../share_sweep_bill_10_kwh_pri_vsakem/SOURCE.md   |  264 +-
 .../share_sweep_bill_10_kwh_pri_vsakem.pdf         |  Bin 18726 -> 18726 bytes
 .../share_sweep_bill_10_kwh_pri_vsakem/source.json |  124 +-
 .../share_sweep_bill_brez_baterije/SOURCE.md       |  264 +-
 .../share_sweep_bill_brez_baterije.pdf             |  Bin 18806 -> 18806 bytes
 .../share_sweep_bill_brez_baterije/source.json     |  124 +-
 .../share_sweep_energy_10_kwh_pri_vsakem/SOURCE.md |  264 +-
 .../share_sweep_energy_10_kwh_pri_vsakem.pdf       |  Bin 13125 -> 13125 bytes
 .../source.json                                    |  124 +-
 .../share_sweep_energy_brez_baterije/SOURCE.md     |  264 +-
 .../share_sweep_energy_brez_baterije.pdf           |  Bin 12983 -> 12983 bytes
 .../share_sweep_energy_brez_baterije/source.json   |  124 +-
 .../Figures/horizon/achievable_saving/SOURCE.md    |  406 +--
 .../achievable_saving/achievable_saving.pdf        |  Bin 17857 -> 17857 bytes
 .../Figures/horizon/achievable_saving/source.json  |   84 +-
 .../Figures/horizon/gap_by_consumer_type/SOURCE.md |  452 ++-
 .../gap_by_consumer_type/gap_by_consumer_type.pdf  |  Bin 41176 -> 41176 bytes
 .../horizon/gap_by_consumer_type/source.json       |   84 +-
 .../horizon/gap_by_consumer_type_ratio/SOURCE.md   |  456 ++-
 .../gap_by_consumer_type_ratio.pdf                 |  Bin 16106 -> 16106 bytes
 .../horizon/gap_by_consumer_type_ratio/source.json |   84 +-
 .../horizon/gap_by_group_and_tariff/SOURCE.md      |  448 ++-
 .../gap_by_group_and_tariff.pdf                    |  Bin 80938 -> 80938 bytes
 .../horizon/gap_by_group_and_tariff/source.json    |   84 +-
 .../horizon/gap_means_all_tariffs/SOURCE.md        |  430 +--
 .../gap_means_all_tariffs.pdf                      |  Bin 18394 -> 18394 bytes
 .../horizon/gap_means_all_tariffs/source.json      |   84 +-
 .../horizon/gap_means_all_tariffs_zoom/SOURCE.md   |  436 +--
 .../gap_means_all_tariffs_zoom.pdf                 |  Bin 15499 -> 15499 bytes
 .../horizon/gap_means_all_tariffs_zoom/source.json |   84 +-
 .../horizon/gap_spread_households/SOURCE.md        |  424 +--
 .../gap_spread_households.pdf                      |  Bin 35136 -> 35136 bytes
 .../horizon/gap_spread_households/source.json      |   84 +-
 .../horizon/horizon_gap_by_tariff/SOURCE.md        |  412 +--
 .../horizon_gap_by_tariff.pdf                      |  Bin 14949 -> 14949 bytes
 .../horizon/horizon_gap_by_tariff/source.json      |   84 +-
 .../horizon/horizon_gap_by_tariff_zoom/SOURCE.md   |  418 +--
 .../horizon_gap_by_tariff_zoom.pdf                 |  Bin 11825 -> 11825 bytes
 .../horizon/horizon_gap_by_tariff_zoom/source.json |   84 +-
 Results/Figures/horizon/runtime_vs_gap/SOURCE.md   |  442 +--
 .../horizon/runtime_vs_gap/runtime_vs_gap.pdf      |  Bin 24286 -> 24286 bytes
 Results/Figures/horizon/runtime_vs_gap/source.json |   84 +-
 .../group_total_cost/SOURCE.md                     |  139 +-
 .../group_total_cost/group_total_cost.pdf          |  Bin 11999 -> 11240 bytes
 .../group_total_cost/source.json                   |  100 +-
 .../catalogue_all_bill_ranking/SOURCE.md           |  111 +-
 .../catalogue_all_bill_ranking.pdf                 |  Bin 24983 -> 27460 bytes
 .../no_battery/catalogue_all_bill_ranking/cell.py  |    2 +-
 .../catalogue_all_bill_ranking/source.json         |   40 +-
 .../catalogue_all_overpay_by_group/SOURCE.md       |  118 +-
 .../catalogue_all_overpay_by_group.pdf             |  Bin 114684 -> 107977 bytes
 .../catalogue_all_overpay_by_group/cell.py         |    2 +-
 .../catalogue_all_overpay_by_group/source.json     |   43 +-
 .../catalogue_no_pv_bill_ranking/SOURCE.md         |   83 +-
 .../catalogue_no_pv_bill_ranking.pdf               |  Bin 25016 -> 27528 bytes
 .../catalogue_no_pv_bill_ranking/cell.py           |    2 +-
 .../catalogue_no_pv_bill_ranking/source.json       |   31 +-
 .../catalogue_no_pv_overpay_by_group/SOURCE.md     |   90 +-
 .../catalogue_no_pv_overpay_by_group.pdf           |  Bin 83217 -> 76824 bytes
 .../catalogue_no_pv_overpay_by_group/cell.py       |    2 +-
 .../catalogue_no_pv_overpay_by_group/source.json   |   32 +-
 .../catalogue_premium_by_group/SOURCE.md           |  132 +-
 .../catalogue_premium_by_group.pdf                 |  Bin 59177 -> 60174 bytes
 .../no_battery/catalogue_premium_by_group/cell.py  |    5 +-
 .../catalogue_premium_by_group/source.json         |   44 +-
 .../catalogue_premium_by_supplier/SOURCE.md        |  125 +-
 .../catalogue_premium_by_supplier.pdf              |  Bin 28390 -> 27076 bytes
 .../catalogue_premium_by_supplier/cell.py          |    5 +-
 .../catalogue_premium_by_supplier/source.json      |   44 +-
 .../catalogue_with_pv_bill_ranking/SOURCE.md       |   97 +-
 .../catalogue_with_pv_bill_ranking.pdf             |  Bin 24911 -> 27416 bytes
 .../catalogue_with_pv_bill_ranking/cell.py         |    2 +-
 .../catalogue_with_pv_bill_ranking/source.json     |   33 +-
 .../catalogue_with_pv_overpay_by_group/SOURCE.md   |  104 +-
 .../catalogue_with_pv_overpay_by_group.pdf         |  Bin 84072 -> 77049 bytes
 .../catalogue_with_pv_overpay_by_group/cell.py     |    2 +-
 .../catalogue_with_pv_overpay_by_group/source.json |   37 +-
 .../no_battery/export_right_by_group/SOURCE.md     |   81 +-
 .../export_right_by_group.pdf                      |  Bin 20105 -> 20105 bytes
 .../no_battery/export_right_by_group/source.json   |   35 +-
 .../no_battery/export_right_worth/SOURCE.md        |   78 +-
 .../export_right_worth/export_right_worth.pdf      |  Bin 24115 -> 26945 bytes
 .../no_battery/export_right_worth/source.json      |   36 +-
 .../no_battery/no_pv_bill_by_group/SOURCE.md       |   65 +-
 .../Figures/no_battery/no_pv_bill_by_group/cell.py |    2 +-
 .../no_pv_bill_by_group/no_pv_bill_by_group.pdf    |  Bin 17923 -> 16664 bytes
 .../no_battery/no_pv_bill_by_group/source.json     |   41 +-
 .../no_battery/no_pv_overpay_by_group/SOURCE.md    |   58 +-
 .../no_battery/no_pv_overpay_by_group/cell.py      |    2 +-
 .../no_pv_overpay_by_group.pdf                     |  Bin 74006 -> 64336 bytes
 .../no_battery/no_pv_overpay_by_group/source.json  |   48 +-
 .../no_battery/pv_bill_composition/SOURCE.md       |   58 +-
 .../Figures/no_battery/pv_bill_composition/cell.py |    2 +-
 .../pv_bill_composition/pv_bill_composition.pdf    |  Bin 15260 -> 17919 bytes
 .../no_battery/pv_bill_composition/source.json     |   48 +-
 .../Figures/no_battery/pv_bill_ranking/SOURCE.md   |   58 +-
 Results/Figures/no_battery/pv_bill_ranking/cell.py |    2 +-
 .../no_battery/pv_bill_ranking/pv_bill_ranking.pdf |  Bin 19236 -> 21771 bytes
 .../Figures/no_battery/pv_bill_ranking/source.json |   48 +-
 .../pv_nosale_bill_composition/SOURCE.md           |   70 +-
 .../no_battery/pv_nosale_bill_composition/cell.py  |    2 +-
 .../pv_nosale_bill_composition.pdf                 |  Bin 18754 -> 17691 bytes
 .../pv_nosale_bill_composition/source.json         |   40 +-
 .../no_battery/pv_nosale_bill_ranking/SOURCE.md    |   66 +-
 .../no_battery/pv_nosale_bill_ranking/cell.py      |    2 +-
 .../pv_nosale_bill_ranking.pdf                     |  Bin 19912 -> 22461 bytes
 .../no_battery/pv_nosale_bill_ranking/source.json  |   42 +-
 .../pv_nosale_overpay_by_group/SOURCE.md           |   74 +-
 .../no_battery/pv_nosale_overpay_by_group/cell.py  |    2 +-
 .../pv_nosale_overpay_by_group.pdf                 |  Bin 44407 -> 42949 bytes
 .../pv_nosale_overpay_by_group/source.json         |   38 +-
 .../no_battery/pv_overpay_by_group/SOURCE.md       |   62 +-
 .../Figures/no_battery/pv_overpay_by_group/cell.py |    2 +-
 .../pv_overpay_by_group/pv_overpay_by_group.pdf    |  Bin 45177 -> 46157 bytes
 .../no_battery/pv_overpay_by_group/source.json     |   46 +-
 Skupnostna_Samooskrba_vs_Souporaba.ipynb           |  988 ++++---
 193 files changed, 12109 insertions(+), 10291 deletions(-)
```
