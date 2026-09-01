# pv_bill_ranking

Exported 2026-09-01T19:02:47+00:00
Files: pv_bill_ranking.pdf
Size: 7.16 x 4.4 in @ 600 dpi (tight)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- S PV, brez baterije: cenik odloča o prevzemni ceni in o odkupu presežkov

## Source

- notebook: /Users/summerscholl/Documents/Andraz/Energy_Community/No_battery_comparison.ipynb (via __vsc_ipynb_file__)
- cell execution count: 9
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 1b204c1ba8da6c4476e2896c4e22df5cc1e85268 (Development)
- subject: Also implemented new figure saving function in other notebooks.
- describe: 1b204c1-dirty

**Working tree was DIRTY (33 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
No_battery_comparison.ipynb                        |  11 +++-
 .../no_battery/export_right_by_group/SOURCE.md     |  54 +++++++++++------
 .../export_right_by_group.pdf                      | Bin 20105 -> 20105 bytes
 .../no_battery/export_right_by_group/source.json   |  62 +++++++++++++-------
 .../no_battery/export_right_worth/SOURCE.md        |  51 ++++++++++------
 .../export_right_worth/export_right_worth.pdf      | Bin 24115 -> 24115 bytes
 .../no_battery/export_right_worth/source.json      |  59 ++++++++++++-------
 .../no_battery/no_pv_bill_by_group/SOURCE.md       |  57 ++++++++++++------
 .../Figures/no_battery/no_pv_bill_by_group/cell.py |   2 +-
 .../no_pv_bill_by_group/no_pv_bill_by_group.pdf    | Bin 17923 -> 17923 bytes
 .../no_battery/no_pv_bill_by_group/source.json     |  65 ++++++++++++++-------
 .../no_battery/no_pv_overpay_by_group/SOURCE.md    |  57 ++++++++++++------
 .../no_battery/no_pv_overpay_by_group/cell.py      |   2 +-
 .../no_pv_overpay_by_group.pdf                     | Bin 74006 -> 74006 bytes
 .../no_battery/no_pv_overpay_by_group/source.json  |  65 ++++++++++++++-------
 .../no_battery/pv_bill_composition/SOURCE.md       |  34 ++++++-----
 .../pv_bill_composition/pv_bill_composition.pdf    | Bin 15260 -> 15260 bytes
 .../no_battery/pv_bill_composition/source.json     |  42 ++++++-------
 .../Figures/no_battery/pv_bill_ranking/SOURCE.md   |  33 +++++------
 .../no_battery/pv_bill_ranking/pv_bill_ranking.pdf | Bin 19236 -> 19236 bytes
 .../Figures/no_battery/pv_bill_ranking/source.json |  41 ++++++-------
 .../pv_nosale_bill_composition/SOURCE.md           |  45 ++++++++------
 .../pv_nosale_bill_composition.pdf                 | Bin 18754 -> 18754 bytes
 .../pv_nosale_bill_composition/source.json         |  53 ++++++++++-------
 .../no_battery/pv_nosale_bill_ranking/SOURCE.md    |  42 +++++++------
 .../pv_nosale_bill_ranking.pdf                     | Bin 19912 -> 19912 bytes
 .../no_battery/pv_nosale_bill_ranking/source.json  |  50 +++++++++-------
 .../pv_nosale_overpay_by_group/SOURCE.md           |  48 +++++++++------
 .../pv_nosale_overpay_by_group.pdf                 | Bin 44407 -> 44407 bytes
 .../pv_nosale_overpay_by_group/source.json         |  56 +++++++++++-------
 .../no_battery/pv_overpay_by_group/SOURCE.md       |  39 +++++++------
 .../pv_overpay_by_group/pv_overpay_by_group.pdf    | Bin 45177 -> 45177 bytes
 .../no_battery/pv_overpay_by_group/source.json     |  47 ++++++++-------
 33 files changed, 623 insertions(+), 392 deletions(-)
```
