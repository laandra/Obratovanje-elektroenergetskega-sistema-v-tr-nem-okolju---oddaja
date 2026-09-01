# share_sweep_energy_brez_baterije

Exported 2026-09-01T19:35:49+00:00
Files: share_sweep_energy_brez_baterije.pdf
Size: 7.16 x 3.58 in @ 600 dpi (exact figure size)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Koliko energije shema res prestavi — brez baterije — Polna črta = energija, ki jo je prejemnik dejansko porabil. Senčeno = prenesena energija, ki je prejemnik v istem 15-minutnem intervalu ni mogel porabiti; pri souporabi propade in se ne prenese naprej, pri skupnostni samooskrbi se vrne v odkup proizvajalca.

## Source

- notebook: /Users/summerscholl/Documents/Andraz/Energy_Community/Skupnostna_Samooskrba_vs_Souporaba.ipynb (via __vsc_ipynb_file__)
- cell execution count: 24
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 1b204c1ba8da6c4476e2896c4e22df5cc1e85268 (Development)
- subject: Also implemented new figure saving function in other notebooks.
- describe: 1b204c1-dirty

**Working tree was DIRTY (60 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
No_battery_comparison.ipynb                        | 216 +++++++++++----------
 .../catalogue_all_bill_ranking/SOURCE.md           |  70 +++++--
 .../catalogue_all_bill_ranking.pdf                 | Bin 24983 -> 24983 bytes
 .../catalogue_all_bill_ranking/source.json         |  78 +++++---
 .../catalogue_all_overpay_by_group/SOURCE.md       |  73 +++++--
 .../catalogue_all_overpay_by_group.pdf             | Bin 114684 -> 114684 bytes
 .../catalogue_all_overpay_by_group/source.json     |  81 +++++---
 .../catalogue_no_pv_bill_ranking/SOURCE.md         |  58 ++++--
 .../catalogue_no_pv_bill_ranking.pdf               | Bin 25016 -> 25016 bytes
 .../catalogue_no_pv_bill_ranking/source.json       |  66 ++++---
 .../catalogue_no_pv_overpay_by_group/SOURCE.md     |  61 ++++--
 .../catalogue_no_pv_overpay_by_group.pdf           | Bin 83217 -> 83217 bytes
 .../catalogue_no_pv_overpay_by_group/source.json   |  69 ++++---
 .../catalogue_premium_by_group/SOURCE.md           |  79 ++++++--
 .../catalogue_premium_by_group.pdf                 | Bin 59177 -> 59177 bytes
 .../catalogue_premium_by_group/source.json         |  82 +++++---
 .../catalogue_premium_by_supplier/SOURCE.md        |  76 ++++++--
 .../catalogue_premium_by_supplier.pdf              | Bin 28390 -> 28390 bytes
 .../catalogue_premium_by_supplier/source.json      |  82 +++++---
 .../catalogue_with_pv_bill_ranking/SOURCE.md       |  64 ++++--
 .../catalogue_with_pv_bill_ranking.pdf             | Bin 24911 -> 24911 bytes
 .../catalogue_with_pv_bill_ranking/source.json     |  72 ++++---
 .../catalogue_with_pv_overpay_by_group/SOURCE.md   |  67 +++++--
 .../catalogue_with_pv_overpay_by_group.pdf         | Bin 84072 -> 84072 bytes
 .../catalogue_with_pv_overpay_by_group/source.json |  75 ++++---
 .../no_battery/export_right_by_group/SOURCE.md     |  57 ++++--
 .../export_right_by_group.pdf                      | Bin 20105 -> 20105 bytes
 .../no_battery/export_right_by_group/source.json   |  65 ++++---
 .../no_battery/export_right_worth/SOURCE.md        |  57 ++++--
 .../export_right_worth/export_right_worth.pdf      | Bin 24115 -> 24115 bytes
 .../no_battery/export_right_worth/source.json      |  65 ++++---
 .../no_battery/no_pv_bill_by_group/SOURCE.md       |  57 ++++--
 .../Figures/no_battery/no_pv_bill_by_group/cell.py |   2 +-
 .../no_pv_bill_by_group/no_pv_bill_by_group.pdf    | Bin 17923 -> 17923 bytes
 .../no_battery/no_pv_bill_by_group/source.json     |  65 ++++---
 .../no_battery/no_pv_overpay_by_group/SOURCE.md    |  57 ++++--
 .../no_battery/no_pv_overpay_by_group/cell.py      |   2 +-
 .../no_pv_overpay_by_group.pdf                     | Bin 74006 -> 74006 bytes
 .../no_battery/no_pv_overpay_by_group/source.json  |  65 ++++---
 .../no_battery/pv_bill_composition/SOURCE.md       |  57 ++++--
 .../pv_bill_composition/pv_bill_composition.pdf    | Bin 15260 -> 15260 bytes
 .../no_battery/pv_bill_composition/source.json     |  65 ++++---
 .../Figures/no_battery/pv_bill_ranking/SOURCE.md   |  57 ++++--
 .../no_battery/pv_bill_ranking/pv_bill_ranking.pdf | Bin 19236 -> 19236 bytes
 .../Figures/no_battery/pv_bill_ranking/source.json |  65 ++++---
 .../pv_nosale_bill_composition/SOURCE.md           |  57 ++++--
 .../pv_nosale_bill_composition.pdf                 | Bin 18754 -> 18754 bytes
 .../pv_nosale_bill_composition/source.json         |  65 ++++---
 .../no_battery/pv_nosale_bill_ranking/SOURCE.md    |  57 ++++--
 .../pv_nosale_bill_ranking.pdf                     | Bin 19912 -> 19912 bytes
 .../no_battery/pv_nosale_bill_ranking/source.json  |  65 ++++---
 .../pv_nosale_overpay_by_group/SOURCE.md           |  57 ++++--
 .../pv_nosale_overpay_by_group.pdf                 | Bin 44407 -> 44407 bytes
 .../pv_nosale_overpay_by_group/source.json         |  65 ++++---
 .../no_battery/pv_overpay_by_group/SOURCE.md       |  57 ++++--
 .../pv_overpay_by_group/pv_overpay_by_group.pdf    | Bin 45177 -> 45177 bytes
 .../no_battery/pv_overpay_by_group/source.json     |  65 ++++---
 57 files changed, 1784 insertions(+), 809 deletions(-)
```
