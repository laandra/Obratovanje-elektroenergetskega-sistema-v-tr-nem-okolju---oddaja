# community_annual_cost

Exported 2026-09-04T09:08:27+00:00
Files: community_annual_cost.pdf
Size: 7.16 x 3.6516 in @ 600 dpi (tight)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Kolikšen je letni strošek skupnosti — 50 gospodinjstev, z DDV; postavke nad črto, dobropis pod njo

## Source

- notebook: not detected
- cell execution count: 18
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 7d7dbc1e3272f9f1e0fcb3305e503472b8188cca (Development)
- subject: Fixed a 2T bug and rerun the notebooks
- describe: 7d7dbc1-dirty

**Working tree was DIRTY (108 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Battery_Size_Optimization.ipynb                    |  611 ++--
 Energy_Community_Comparison.ipynb                  |   14 +-
 Extended_Multuser_Battery_Size_Optimization.ipynb  |   52 +-
 MILP_horizon_comparison.ipynb                      |   29 +-
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
 .../community_annual_cost.pdf                      |  Bin 23481 -> 23481 bytes
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
 Skupnostna_Samooskrba_vs_Souporaba.ipynb           |   25 +-
 107 files changed, 4690 insertions(+), 3692 deletions(-)
```
