# catalogue_no_pv_bill_ranking

Exported 2026-09-08T07:35:14+00:00
Files: catalogue_no_pv_bill_ranking.pdf
Size: 7.16 x 9.3 in @ 600 dpi (tight)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Brez PV: samooskrbni ceniki so cenovno v igri, čeprav jih tak odjemalec ne sme podpisati

## Source

- notebook: C:\Users\HP\Documents\JupyterNotebook\Energy_Community\No_battery_comparison.ipynb (via __vsc_ipynb_file__)
- cell execution count: 25
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 1b43677d1afb3f2de4e6ca23fc165a66c2ed9249 (Development)
- subject: Anonimized the electricity providers
- describe: 1b43677-dirty

**Working tree was DIRTY (34 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
No_battery_comparison.ipynb                        | 2849 ++++++++++----------
 .../catalogue_no_pv_bill_ranking.pdf               |  Bin 27528 -> 27528 bytes
 .../no_battery/export_right_by_group/SOURCE.md     |   84 +-
 .../no_battery/export_right_by_group/cell.py       |    7 +-
 .../export_right_by_group.pdf                      |  Bin 20105 -> 20116 bytes
 .../no_battery/export_right_by_group/source.json   |   32 +-
 .../no_battery/export_right_worth/SOURCE.md        |   77 +-
 .../Figures/no_battery/export_right_worth/cell.py  |    7 +-
 .../export_right_worth/export_right_worth.pdf      |  Bin 26945 -> 26945 bytes
 .../no_battery/export_right_worth/source.json      |   31 +-
 .../no_battery/no_pv_bill_by_group/SOURCE.md       |   38 +-
 .../no_pv_bill_by_group/no_pv_bill_by_group.pdf    |  Bin 16664 -> 16664 bytes
 .../no_battery/no_pv_bill_by_group/source.json     |   40 +-
 .../no_battery/no_pv_overpay_by_group/SOURCE.md    |   36 +-
 .../no_pv_overpay_by_group.pdf                     |  Bin 64336 -> 64336 bytes
 .../no_battery/no_pv_overpay_by_group/source.json  |   34 +-
 .../no_battery/pv_bill_composition/SOURCE.md       |   42 +-
 .../pv_bill_composition/pv_bill_composition.pdf    |  Bin 17919 -> 17919 bytes
 .../no_battery/pv_bill_composition/source.json     |   26 +-
 .../Figures/no_battery/pv_bill_ranking/SOURCE.md   |   39 +-
 .../no_battery/pv_bill_ranking/pv_bill_ranking.pdf |  Bin 21771 -> 21771 bytes
 .../Figures/no_battery/pv_bill_ranking/source.json |   31 +-
 .../pv_nosale_bill_composition/SOURCE.md           |   63 +-
 .../pv_nosale_bill_composition.pdf                 |  Bin 17691 -> 17691 bytes
 .../pv_nosale_bill_composition/source.json         |   29 +-
 .../no_battery/pv_nosale_bill_ranking/SOURCE.md    |   56 +-
 .../pv_nosale_bill_ranking.pdf                     |  Bin 22461 -> 22461 bytes
 .../no_battery/pv_nosale_bill_ranking/source.json  |   28 +-
 .../pv_nosale_overpay_by_group/SOURCE.md           |   70 +-
 .../pv_nosale_overpay_by_group.pdf                 |  Bin 42949 -> 42949 bytes
 .../pv_nosale_overpay_by_group/source.json         |   30 +-
 .../no_battery/pv_overpay_by_group/SOURCE.md       |   49 +-
 .../pv_overpay_by_group/pv_overpay_by_group.pdf    |  Bin 46157 -> 46157 bytes
 .../no_battery/pv_overpay_by_group/source.json     |   27 +-
 34 files changed, 1780 insertions(+), 1945 deletions(-)
```
