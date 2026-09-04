# pv_overpay_by_group

Exported 2026-09-04T07:07:18+00:00
Files: pv_overpay_by_group.pdf
Size: 7.16 x 4.4 in @ 600 dpi (tight)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- S PV, presežke odkupi dobavitelj: preplačilo po tipu gospodinjstva [%]

## Source

- notebook: not detected
- cell execution count: 9
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 7d7dbc1e3272f9f1e0fcb3305e503472b8188cca (Development)
- subject: Fixed a 2T bug and rerun the notebooks
- describe: 7d7dbc1-dirty

**Working tree was DIRTY (19 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
No_battery_comparison.ipynb                        | 237 ++++++++++++++-------
 Plotting_Functions.py                              |  13 +-
 .../no_battery/no_pv_bill_by_group/SOURCE.md       |  58 ++---
 .../Figures/no_battery/no_pv_bill_by_group/cell.py |   2 +-
 .../no_pv_bill_by_group/no_pv_bill_by_group.pdf    | Bin 17923 -> 16664 bytes
 .../no_battery/no_pv_bill_by_group/source.json     |  48 ++---
 .../no_battery/no_pv_overpay_by_group/SOURCE.md    |  58 ++---
 .../no_battery/no_pv_overpay_by_group/cell.py      |   2 +-
 .../no_pv_overpay_by_group.pdf                     | Bin 74006 -> 64336 bytes
 .../no_battery/no_pv_overpay_by_group/source.json  |  48 ++---
 .../no_battery/pv_bill_composition/SOURCE.md       |  58 ++---
 .../Figures/no_battery/pv_bill_composition/cell.py |   2 +-
 .../pv_bill_composition/pv_bill_composition.pdf    | Bin 15260 -> 17919 bytes
 .../no_battery/pv_bill_composition/source.json     |  48 ++---
 .../Figures/no_battery/pv_bill_ranking/SOURCE.md   |  58 ++---
 Results/Figures/no_battery/pv_bill_ranking/cell.py |   2 +-
 .../no_battery/pv_bill_ranking/pv_bill_ranking.pdf | Bin 19236 -> 21771 bytes
 .../Figures/no_battery/pv_bill_ranking/source.json |  48 ++---
 .../pv_overpay_by_group/pv_overpay_by_group.pdf    | Bin 45177 -> 46157 bytes
 19 files changed, 316 insertions(+), 366 deletions(-)
```
