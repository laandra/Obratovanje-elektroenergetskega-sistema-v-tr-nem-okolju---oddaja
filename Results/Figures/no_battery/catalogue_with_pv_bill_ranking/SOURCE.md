# catalogue_with_pv_bill_ranking

Exported 2026-09-09T15:41:26+00:00
Files: catalogue_with_pv_bill_ranking.pdf
Size: 7.16 x 9.3 in @ 600 dpi (tight)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- S PV in brez odkupa: cena samooskrbne police proti polici, ki je zanje zaprta

## Source

- notebook: not detected
- cell execution count: 20
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 07aae07e717328104ffbc6c5a04c3fd8d9e7df4f (Development)
- subject: Multiuser_Battery_Size_Optimization.ipynb run is saved. The figure I want is set to central.
- describe: 07aae07-dirty

**Working tree was DIRTY (67 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Battery_Size_Optimization.ipynb                    |   4 +-
 Energy_Community_Comparison.ipynb                  |  22 ++--
 Extended_Multuser_Battery_Size_Optimization.ipynb  |  14 +--
 Household invoice generator.ipynb                  | 100 +++++++++---------
 Household_local model.ipynb                        |  12 +--
 MILP_horizon_comparison.ipynb                      |  16 +--
 Multi_household_baseline.ipynb                     |  70 ++++++-------
 Multuser_Battery_Size_Optimization.ipynb           |  10 +-
 No_battery_comparison.ipynb                        |  18 ++--
 PLOTTING_GUIDE.txt                                 |  12 ++-
 Plotting_Functions.py                              |  63 +++++++++--
 RBC_vs_MILP_Comparison.ipynb                       |  34 +++---
 .../Figures/invoices/invoice_composition/SOURCE.md |  78 +++++---------
 .../Figures/invoices/invoice_composition/cell.py   |   2 +-
 .../invoice_composition/invoice_composition.pdf    | Bin 16447 -> 16678 bytes
 .../invoices/invoice_composition/source.json       |  58 +++--------
 .../group_total_cost/SOURCE.md                     | 110 ++++----------------
 .../group_total_cost/group_total_cost.pdf          | Bin 11240 -> 11241 bytes
 .../group_total_cost/source.json                   |  67 +++---------
 .../catalogue_no_pv_bill_ranking/SOURCE.md         | 109 ++++++++++---------
 .../catalogue_no_pv_bill_ranking.pdf               | Bin 27406 -> 27406 bytes
 .../catalogue_no_pv_bill_ranking/source.json       |  48 ++++-----
 .../catalogue_no_pv_overpay_by_group/SOURCE.md     | 115 ++++++++++++---------
 .../catalogue_no_pv_overpay_by_group.pdf           | Bin 76824 -> 77476 bytes
 .../catalogue_no_pv_overpay_by_group/source.json   |  50 ++++-----
 .../catalogue_with_pv_bill_ranking.pdf             | Bin 27296 -> 27296 bytes
 .../no_battery/export_right_by_group/SOURCE.md     | 102 ++++++++++--------
 .../no_battery/export_right_by_group/cell.py       |   2 +-
 .../export_right_by_group.pdf                      | Bin 20116 -> 20642 bytes
 .../no_battery/export_right_by_group/source.json   |  43 ++++----
 .../no_battery/export_right_worth/SOURCE.md        |  95 +++++++++--------
 .../Figures/no_battery/export_right_worth/cell.py  |   2 +-
 .../export_right_worth/export_right_worth.pdf      | Bin 26945 -> 26945 bytes
 .../no_battery/export_right_worth/source.json      |  38 ++++---
 .../no_battery/no_pv_bill_by_group/SOURCE.md       |  45 +++++---
 .../Figures/no_battery/no_pv_bill_by_group/cell.py |   2 +-
 .../no_pv_bill_by_group/no_pv_bill_by_group.pdf    | Bin 16668 -> 16432 bytes
 .../no_battery/no_pv_bill_by_group/source.json     |  33 ++++--
 .../no_battery/no_pv_overpay_by_group/SOURCE.md    |  51 +++++----
 .../no_battery/no_pv_overpay_by_group/cell.py      |   2 +-
 .../no_pv_overpay_by_group.pdf                     | Bin 64336 -> 65385 bytes
 .../no_battery/no_pv_overpay_by_group/source.json  |  33 ++++--
 .../no_battery/pv_bill_composition/SOURCE.md       |  63 ++++++-----
 .../Figures/no_battery/pv_bill_composition/cell.py |   2 +-
 .../pv_bill_composition/pv_bill_composition.pdf    | Bin 17423 -> 17920 bytes
 .../no_battery/pv_bill_composition/source.json     |  33 ++++--
 .../Figures/no_battery/pv_bill_ranking/SOURCE.md   |  55 ++++++----
 Results/Figures/no_battery/pv_bill_ranking/cell.py |   2 +-
 .../no_battery/pv_bill_ranking/pv_bill_ranking.pdf | Bin 21771 -> 21771 bytes
 .../Figures/no_battery/pv_bill_ranking/source.json |  33 ++++--
 .../pv_nosale_bill_composition/SOURCE.md           |  85 ++++++++-------
 .../no_battery/pv_nosale_bill_composition/cell.py  |   4 +-
 .../pv_nosale_bill_composition.pdf                 | Bin 17343 -> 17857 bytes
 .../pv_nosale_bill_composition/source.json         |  33 ++++--
 .../no_battery/pv_nosale_bill_ranking/SOURCE.md    |  79 ++++++++------
 .../no_battery/pv_nosale_bill_ranking/cell.py      |   4 +-
 .../pv_nosale_bill_ranking.pdf                     | Bin 22461 -> 21756 bytes
 .../no_battery/pv_nosale_bill_ranking/source.json  |  33 ++++--
 .../pv_nosale_overpay_by_group/SOURCE.md           |  91 +++++++++-------
 .../no_battery/pv_nosale_overpay_by_group/cell.py  |   4 +-
 .../pv_nosale_overpay_by_group.pdf                 | Bin 42949 -> 42653 bytes
 .../pv_nosale_overpay_by_group/source.json         |  33 ++++--
 .../no_battery/pv_overpay_by_group/SOURCE.md       |  71 +++++++------
 .../Figures/no_battery/pv_overpay_by_group/cell.py |   2 +-
 .../pv_overpay_by_group/pv_overpay_by_group.pdf    | Bin 46157 -> 44004 bytes
 .../no_battery/pv_overpay_by_group/source.json     |  33 ++++--
 Skupnostna_Samooskrba_vs_Souporaba.ipynb           |  12 ++-
 67 files changed, 1133 insertions(+), 999 deletions(-)
```
