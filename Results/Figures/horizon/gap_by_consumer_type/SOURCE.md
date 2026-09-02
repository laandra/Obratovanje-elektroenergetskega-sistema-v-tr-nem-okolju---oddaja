# gap_by_consumer_type

Exported 2026-09-01T19:58:24+00:00
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

- commit: 13a96f887829200bcd1659b8ba56e381f9f992a1 (Development)
- subject: reruning the other notebook and fixing a bug
- describe: 13a96f8-dirty

**Working tree was DIRTY (70 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Energy_Community_Comparison.ipynb                  |   95 +-
 Extended_Multuser_Battery_Size_Optimization.ipynb  |    3 +-
 Household invoice generator.ipynb                  |    2 +-
 MILP_horizon_comparison.ipynb                      |    2 +-
 Multi_household_baseline.ipynb                     |    3 +-
 Multuser_Battery_Size_Optimization.ipynb           |    3 +-
 No_battery_comparison.ipynb                        |    2 +-
 RBC_vs_MILP_Comparison.ipynb                       |    2 +-
 .../Figures/horizon/achievable_saving/SOURCE.md    |   96 +-
 .../achievable_saving/achievable_saving.pdf        |  Bin 18168 -> 18168 bytes
 .../Figures/horizon/achievable_saving/source.json  |   25 +-
 .../gap_by_consumer_type/gap_by_consumer_type.pdf  |  Bin 41176 -> 41176 bytes
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
 .../Fluvius_HP_EV_user_003.csv                     |    2 +-
 .../Fluvius_PV_EV_user_003.csv                     |    2 +-
 .../Fluvius_PV_EV_user_005_redni1t.csv             |    2 +-
 .../Fluvius_PV_HP_EV_user_001.csv                  |   10 +-
 .../Fluvius_PV_HP_EV_user_001_aktivni.csv          |   10 +-
 .../Fluvius_PV_HP_EV_user_001_redni1t.csv          |    6 +-
 .../Fluvius_PV_HP_EV_user_002.csv                  |   10 +-
 .../Fluvius_PV_HP_EV_user_002_aktivni.csv          |   10 +-
 .../Fluvius_PV_HP_EV_user_002_redni1t.csv          |   10 +-
 .../Fluvius_PV_HP_EV_user_003.csv                  |   10 +-
 .../Fluvius_PV_HP_EV_user_003_aktivni.csv          |    8 +-
 .../Fluvius_PV_HP_EV_user_003_redni1t.csv          |    8 +-
 .../Fluvius_PV_HP_EV_user_004.csv                  |    6 +-
 .../Fluvius_PV_HP_EV_user_004_aktivni.csv          |   10 +-
 .../Fluvius_PV_HP_EV_user_004_redni1t.csv          |   10 +-
 .../Fluvius_PV_HP_EV_user_005.csv                  |   10 +-
 .../Fluvius_PV_HP_EV_user_005_aktivni.csv          |   10 +-
 .../Fluvius_PV_HP_EV_user_005_redni1t.csv          |    6 +-
 .../Fluvius_PV_HP_user_001_aktivni.csv             |    2 +-
 .../Fluvius_PV_HP_user_002_aktivni.csv             |    2 +-
 .../Fluvius_PV_HP_user_002_redni1t.csv             |    8 +-
 .../Fluvius_PV_HP_user_003.csv                     |    6 +-
 .../Fluvius_PV_HP_user_003_aktivni.csv             |    6 +-
 .../Fluvius_PV_HP_user_003_redni1t.csv             |    6 +-
 .../Fluvius_PV_HP_user_004.csv                     |    8 +-
 .../Fluvius_PV_HP_user_004_aktivni.csv             |    4 +-
 .../Fluvius_PV_HP_user_004_redni1t.csv             |    8 +-
 .../Fluvius_PV_HP_user_005.csv                     |    8 +-
 .../Fluvius_PV_HP_user_005_aktivni.csv             |    8 +-
 .../Fluvius_PV_HP_user_005_redni1t.csv             |    8 +-
 .../Fluvius_PV_user_002.csv                        |    2 +-
 .../Fluvius_PV_user_004_redni1t.csv                |    2 +-
 Skupnostna_Samooskrba_vs_Souporaba.ipynb           | 1418 +++++++++++---------
 70 files changed, 1585 insertions(+), 1382 deletions(-)
```
