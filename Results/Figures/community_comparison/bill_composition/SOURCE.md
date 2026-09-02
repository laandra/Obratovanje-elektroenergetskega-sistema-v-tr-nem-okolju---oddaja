# bill_composition

Exported 2026-09-02T08:44:19+00:00
Files: bill_composition.pdf
Size: 7.16 x 3.938 in @ 600 dpi (tight)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Iz česa je račun sestavljen — delež bruto računa, z baterijami

## Source

- notebook: /Users/summerscholl/Documents/Andraz/Energy_Community/Energy_Community_Comparison.ipynb (via __vsc_ipynb_file__)
- cell execution count: 55
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 7940b1377d833816b4278c4c3f71855080b2f016 (Development)
- subject: Mostly rerun evrything and implemented new ploting function on the whole notebook.     An error remaining in RBC
- describe: 7940b13-dirty

**Working tree was DIRTY (15 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
DQN/dqn_model                                      | Bin 223465 -> 223465 bytes
 Environment.py                                     |  23 +-
 Horizon_Comparison.py                              |  28 +
 Household_local model.ipynb                        | 647 +++++++++++++---
 RBC_vs_MILP_Comparison.ipynb                       | 819 +++++++++++----------
 .../bill_composition/bill_composition.pdf          | Bin 22190 -> 22190 bytes
 .../community_annual_cost/SOURCE.md                |  79 +-
 .../community_annual_cost.pdf                      | Bin 23481 -> 23481 bytes
 .../community_annual_cost/source.json              |  78 +-
 Results/Figures/rbc_vs_milp/trace_day/SOURCE.md    |  76 +-
 Results/Figures/rbc_vs_milp/trace_day/source.json  |  69 +-
 .../Figures/rbc_vs_milp/trace_day/trace_day.pdf    | Bin 31141 -> 31149 bytes
 Rule_Based_Control.py                              | 100 ++-
 Rule_Based_Control_Check.py                        |  59 ++
 __pycache__/Environment.cpython-314.pyc            | Bin 82365 -> 82554 bytes
 15 files changed, 1233 insertions(+), 745 deletions(-)
```
