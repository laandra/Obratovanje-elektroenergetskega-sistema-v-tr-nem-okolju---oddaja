# cost_vs_capacity_panels

Exported 2026-09-15T12:48:16+00:00
Files: cost_vs_capacity_panels.pdf
Size: 7.16 x 6.5753 in @ 600 dpi (exact figure size)

> resized from 12.20x10.00 to 7.16x6.58 in; IEEE text applied to a figure drawn in the notebook style (scaled, not rebuilt); stroke weights scaled 0.59x to the narrower canvas

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Letni strošek elektrike ob popolnem predvidevanju, po pogodbi in velikosti baterije — Celoletni MILP na točko, en graf na gospodinjstvo, vsak na svoji skali. NET meritve (sivo, pikčasto) so zaprta pogodba — obračun letno, za nove odjemalce ni več na voljo, prikazane so le kot strošek tistih, ki jo že imajo. Vsi drugi paketi priznavajo oddajo po intervalih. Pod ničlo gospodinjstvo za oddano energijo čez leto prejme več, kot plača za prevzeto. Vrednosti so v tabeli 8.2.

## Source

- notebook: C:\Users\HP\Documents\JupyterNotebook\Energy_Community\Multuser_Battery_Size_Optimization.ipynb (via __vsc_ipynb_file__)
- cell execution count: 20
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: d839d80046aa48d7eb20c079cb512fc0edf76e2c (Development)
- subject: Unifiing 2 graphs
- describe: d839d80-dirty

**Working tree was DIRTY (65 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff` (truncated), which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
PLOTTING_GUIDE.txt                                 |  77 +++-
 Plotting_Functions.py                              | 483 ++++++++++++++++++---
 .../community_net_benefit/SOURCE.md                | 363 ++++------------
 .../community_net_benefit.pdf                      | Bin 36265 -> 40655 bytes
 .../community_net_benefit/source.json              | 128 +++---
 .../community_total_bill/SOURCE.md                 | 363 ++++------------
 .../community_total_bill/community_total_bill.pdf  | Bin 35420 -> 40266 bytes
 .../community_total_bill/source.json               | 128 +++---
 .../cost_vs_capacity_panels/SOURCE.md              | 363 ++++------------
 .../cost_vs_capacity_panels.pdf                    | Bin 66002 -> 72186 bytes
 .../cost_vs_capacity_panels/source.json            | 128 +++---
 .../Figures/multiuser_sizing/curtailed/SOURCE.md   | 363 ++++------------
 .../multiuser_sizing/curtailed/curtailed.pdf       | Bin 32737 -> 36773 bytes
 .../Figures/multiuser_sizing/curtailed/source.json | 128 +++---
 .../multiuser_sizing/cycles_median/SOURCE.md       | 363 ++++------------
 .../cycles_median/cycles_median.pdf                | Bin 34504 -> 38882 bytes
 .../multiuser_sizing/cycles_median/source.json     | 128 +++---
 .../multiuser_sizing/cycles_panels/SOURCE.md       | 363 ++++------------
 .../cycles_panels/cycles_panels.pdf                | Bin 64329 -> 70357 bytes
 .../multiuser_sizing/cycles_panels/source.json     | 128 +++---
 .../multiuser_sizing/grid_charged/SOURCE.md        | 363 ++++------------
 .../multiuser_sizing/grid_charged/grid_charged.pdf | Bin 33835 -> 38735 bytes
 .../multiuser_sizing/grid_charged/source.json      | 128 +++---
 .../headline_net_benefit/SOURCE.md                 | 363 ++++------------
 .../headline_net_benefit/headline_net_benefit.pdf  | Bin 37491 -> 42767 bytes
 .../headline_net_benefit/source.json               | 128 +++---
 .../multiuser_sizing/headline_roi/SOURCE.md        | 363 ++++------------
 .../multiuser_sizing/headline_roi/headline_roi.pdf | Bin 37669 -> 42874 bytes
 .../multiuser_sizing/headline_roi/source.json      | 128 +++---
 .../multiuser_sizing/inverter_fixed_fee/SOURCE.md  | 363 ++++------------
 .../inverter_fixed_fee/inverter_fixed_fee.pdf      | Bin 33470 -> 37397 bytes
 .../inverter_fixed_fee/source.json                 | 128 +++---
 .../multiuser_sizing/inverter_per_kw/SOURCE.md     | 363 ++++------------
 .../inverter_per_kw/inverter_per_kw.pdf            | Bin 33457 -> 37514 bytes
 .../multiuser_sizing/inverter_per_kw/source.json   | 128 +++---
 .../multiuser_sizing/marginal_value/SOURCE.md      | 363 ++++------------
 .../marginal_value/marginal_value.pdf              | Bin 39278 -> 44012 bytes
 .../multiuser_sizing/marginal_value/source.json    | 128 +++---
 .../multiuser_sizing/net_benefit_panels/SOURCE.md  | 363 ++++------------
 .../net_benefit_panels/net_benefit_panels.pdf      | Bin 82672 -> 89594 bytes
 .../net_benefit_panels/source.json                 | 128 +++---
 .../multiuser_sizing/peak_change_pct/SOURCE.md     | 363 ++++------------
 .../peak_change_pct/peak_change_pct.pdf            | Bin 34506 -> 38450 bytes
 .../multiuser_sizing/peak_change_pct/source.json   | 128 +++---
 .../multiuser_sizing/peak_import_block_1/SOURCE.md | 363 ++++------------
 .../peak_import_block_1/peak_import_block_1.pdf    | Bin 33546 -> 37791 bytes
 .../peak_import_block_1/source.json                | 128 +++---
 .../multiuser_sizing/peak_import_block_2/SOURCE.md | 363 ++++------------
 .../peak_import_block_2/peak_import_block_2.pdf    | Bin 33667 -> 37933 bytes
 .../peak_import_block_2/source.json                | 128 +++---
 .../multiuser_sizing/peak_import_block_3/SOURCE.md | 363 ++++------------
 .../peak_import_block_3/peak_import_block_3.pdf    | Bin 33639 -> 37904 bytes
 .../peak_import_block_3/source.json                | 128 +++---
 .../multiuser_sizing/peak_import_block_4/SOURCE.md | 363 ++++------------
 .../peak_import_block_4/peak_import_block_4.pdf    | Bin 33874 -> 38324 bytes
 .../peak_import_block_4/source.json                | 128 +++---
 .../multiuser_sizing/peak_import_block_5/SOURCE.md | 363 ++++------------
 .../peak_import_block_5/peak_import_block_5.pdf    | Bin 33656 -> 37925 bytes
 .../peak_import_block_5/source.json                | 128 +++---
 .../multiuser_sizing/peak_import_median/SOURCE.md  | 363 ++++------------
 .../peak_import_median/peak_import_median.pdf      | Bin 34658 -> 39081 bytes
 .../peak_import_median/source.json                 | 128 +++---
 .../multiuser_sizing/peak_import_panels/SOURCE.md  | 363 ++++------------
 .../peak_import_panels/peak_import_panels.pdf      | Bin 58674 -> 65066 bytes
 .../peak_import_panels/source.json                 | 128 +++---
 65 files changed, 3412 insertions(+), 7459 deletions(-)
```
