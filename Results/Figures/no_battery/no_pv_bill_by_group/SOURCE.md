# no_pv_bill_by_group

Exported 2026-09-09T15:41:04+00:00
Files: no_pv_bill_by_group.pdf
Size: 7.16 x 8.5 in @ 600 dpi (tight)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Brez PV, brez baterije: edini vzvod je pogodba

## Source

- notebook: not detected
- cell execution count: 7
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 07aae07e717328104ffbc6c5a04c3fd8d9e7df4f (Development)
- subject: Multiuser_Battery_Size_Optimization.ipynb run is saved. The figure I want is set to central.
- describe: 07aae07-dirty

**Working tree was DIRTY (21 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Battery_Size_Optimization.ipynb                    |   4 +-
 Energy_Community_Comparison.ipynb                  |  22 ++---
 Extended_Multuser_Battery_Size_Optimization.ipynb  |  14 +--
 Household invoice generator.ipynb                  | 100 +++++++++----------
 Household_local model.ipynb                        |  12 +--
 MILP_horizon_comparison.ipynb                      |  16 +--
 Multi_household_baseline.ipynb                     |  70 ++++++-------
 Multuser_Battery_Size_Optimization.ipynb           |  10 +-
 No_battery_comparison.ipynb                        |  18 ++--
 PLOTTING_GUIDE.txt                                 |  12 ++-
 Plotting_Functions.py                              |  63 ++++++++++--
 RBC_vs_MILP_Comparison.ipynb                       |  34 ++++---
 .../Figures/invoices/invoice_composition/SOURCE.md |  78 +++++----------
 .../Figures/invoices/invoice_composition/cell.py   |   2 +-
 .../invoice_composition/invoice_composition.pdf    | Bin 16447 -> 16678 bytes
 .../invoices/invoice_composition/source.json       |  58 +++--------
 .../group_total_cost/SOURCE.md                     | 110 ++++-----------------
 .../group_total_cost/group_total_cost.pdf          | Bin 11240 -> 11241 bytes
 .../group_total_cost/source.json                   |  67 +++----------
 .../no_pv_bill_by_group/no_pv_bill_by_group.pdf    | Bin 16668 -> 16432 bytes
 Skupnostna_Samooskrba_vs_Souporaba.ipynb           |  12 ++-
 21 files changed, 298 insertions(+), 404 deletions(-)
```
