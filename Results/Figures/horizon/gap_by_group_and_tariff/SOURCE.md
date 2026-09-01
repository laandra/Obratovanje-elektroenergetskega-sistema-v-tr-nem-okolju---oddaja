# gap_by_group_and_tariff

Exported 2026-09-01T15:00:37+00:00
Files: gap_by_group_and_tariff.pdf
Size: 7.16 x 10.3104 in @ 600 dpi (exact figure size)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Vrzel po tipu gospodinjstva in ceniku, enaka skala 0-74 % na vseh grafih

## Source

- notebook: not detected
- cell execution count: 15
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 3c6b7c9f845a0f4987657e0f9fa0e4956f6c6cfd (Development)
- subject: New ploting function
- describe: 3c6b7c9-dirty

**Working tree was DIRTY (45 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Battery_Size_Optimization.ipynb                    |  88 ++--
 Energy_Community_Comparison.ipynb                  | 228 +++++----
 Extended_Multuser_Battery_Size_Optimization.ipynb  | 520 +++++++++-----------
 Household invoice generator.ipynb                  |  62 +--
 MILP_horizon_comparison.ipynb                      | 331 ++++++-------
 Multi_household_baseline.ipynb                     |  27 +-
 Multuser_Battery_Size_Optimization.ipynb           | 412 +++++++---------
 No_battery_comparison.ipynb                        | 542 ++++++++++-----------
 RBC_vs_MILP_Comparison.ipynb                       | 253 +++++-----
 .../Fluvius_HP_EV_user_003.csv                     |   2 +-
 .../Fluvius_PV_EV_user_003.csv                     |   2 +-
 .../Fluvius_PV_EV_user_005_redni1t.csv             |   2 +-
 .../Fluvius_PV_HP_EV_user_001.csv                  |  10 +-
 .../Fluvius_PV_HP_EV_user_001_aktivni.csv          |  10 +-
 .../Fluvius_PV_HP_EV_user_001_redni1t.csv          |   6 +-
 .../Fluvius_PV_HP_EV_user_002.csv                  |  10 +-
 .../Fluvius_PV_HP_EV_user_002_aktivni.csv          |  10 +-
 .../Fluvius_PV_HP_EV_user_002_redni1t.csv          |  10 +-
 .../Fluvius_PV_HP_EV_user_003.csv                  |  10 +-
 .../Fluvius_PV_HP_EV_user_003_aktivni.csv          |   8 +-
 .../Fluvius_PV_HP_EV_user_003_redni1t.csv          |   8 +-
 .../Fluvius_PV_HP_EV_user_004.csv                  |   6 +-
 .../Fluvius_PV_HP_EV_user_004_aktivni.csv          |  10 +-
 .../Fluvius_PV_HP_EV_user_004_redni1t.csv          |  10 +-
 .../Fluvius_PV_HP_EV_user_005.csv                  |  10 +-
 .../Fluvius_PV_HP_EV_user_005_aktivni.csv          |  10 +-
 .../Fluvius_PV_HP_EV_user_005_redni1t.csv          |   6 +-
 .../Fluvius_PV_HP_user_001_aktivni.csv             |   2 +-
 .../Fluvius_PV_HP_user_002_aktivni.csv             |   2 +-
 .../Fluvius_PV_HP_user_002_redni1t.csv             |   8 +-
 .../Fluvius_PV_HP_user_003.csv                     |   6 +-
 .../Fluvius_PV_HP_user_003_aktivni.csv             |   6 +-
 .../Fluvius_PV_HP_user_003_redni1t.csv             |   6 +-
 .../Fluvius_PV_HP_user_004.csv                     |   8 +-
 .../Fluvius_PV_HP_user_004_aktivni.csv             |   4 +-
 .../Fluvius_PV_HP_user_004_redni1t.csv             |   8 +-
 .../Fluvius_PV_HP_user_005.csv                     |   8 +-
 .../Fluvius_PV_HP_user_005_aktivni.csv             |   8 +-
 .../Fluvius_PV_HP_user_005_redni1t.csv             |   8 +-
 .../Fluvius_PV_user_002.csv                        |   2 +-
 .../Fluvius_PV_user_004_redni1t.csv                |   2 +-
 Skupnostna_Samooskrba_vs_Souporaba.ipynb           | 221 +++++----
 42 files changed, 1382 insertions(+), 1520 deletions(-)
```
