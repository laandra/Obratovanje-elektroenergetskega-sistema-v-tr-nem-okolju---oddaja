# network_discount_sensitivity

Exported 2026-09-03T07:57:30+00:00
Files: network_discount_sensitivity.pdf
Size: 7.16 x 3.3652 in @ 600 dpi (exact figure size)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Prednost skupnostne samooskrbe je znižana distribucijska postavka — Pri značilnem primeru 4 je skupnostna distribucijska postavka praktično enaka polni (razlika je pod 0,0001 EUR/kWh), zato se prihranek skupnostne samooskrbe zoži na tisto, kar prihrani tudi souporaba — le da souporaba ob tem plača še nadomestilo organizatorju. Vsaka stopnja levo od 4 je omrežnina, ki je souporaba ne zniža.

## Source

- notebook: /Users/summerscholl/Documents/Andraz/Energy_Community/Skupnostna_Samooskrba_vs_Souporaba.ipynb (via __vsc_ipynb_file__)
- cell execution count: 27
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 7d7dbc1e3272f9f1e0fcb3305e503472b8188cca (Development)
- subject: Fixed a 2T bug and rerun the notebooks
- describe: 7d7dbc1-dirty

**Working tree was DIRTY (32 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
.../__pycache__/si_obracun.cpython-314.pyc         | Bin 50361 -> 50361 bytes
 .../SOURCE.md                                      |  92 ++++++-------------
 .../community_bill_by_scheme_10_kwh_pri_vsakem.pdf | Bin 12167 -> 12167 bytes
 .../source.json                                    |  89 +++++++------------
 .../SOURCE.md                                      |  86 +++++-------------
 .../community_bill_by_scheme_brez_baterije.pdf     | Bin 12225 -> 12225 bytes
 .../source.json                                    |  83 ++++++-----------
 .../SOURCE.md                                      |  89 ++++++-------------
 ...community_bill_by_scheme_optimalna_baterija.pdf | Bin 11861 -> 11861 bytes
 .../source.json                                    |  86 ++++++------------
 .../member_bill_change_10_kwh_pri_vsakem/SOURCE.md |  98 ++++++++-------------
 .../member_bill_change_10_kwh_pri_vsakem.pdf       | Bin 14178 -> 14178 bytes
 .../source.json                                    |  95 ++++++++------------
 .../member_bill_change_brez_baterije/SOURCE.md     |  95 +++++++-------------
 .../member_bill_change_brez_baterije.pdf           | Bin 14113 -> 14113 bytes
 .../member_bill_change_brez_baterije/source.json   |  92 +++++++------------
 .../network_discount_sensitivity.pdf               | Bin 14247 -> 14247 bytes
 .../share_sweep_bill_10_kwh_pri_vsakem/SOURCE.md   |  77 +++-------------
 .../share_sweep_bill_10_kwh_pri_vsakem.pdf         | Bin 18726 -> 18726 bytes
 .../share_sweep_bill_10_kwh_pri_vsakem/source.json |  74 ++++------------
 .../share_sweep_bill_brez_baterije/SOURCE.md       |  74 +++-------------
 .../share_sweep_bill_brez_baterije.pdf             | Bin 18806 -> 18806 bytes
 .../share_sweep_bill_brez_baterije/source.json     |  71 +++------------
 .../share_sweep_energy_10_kwh_pri_vsakem/SOURCE.md |  83 +++++------------
 .../share_sweep_energy_10_kwh_pri_vsakem.pdf       | Bin 13125 -> 13125 bytes
 .../source.json                                    |  80 +++++------------
 .../share_sweep_energy_brez_baterije/SOURCE.md     |  80 ++++-------------
 .../share_sweep_energy_brez_baterije.pdf           | Bin 12983 -> 12983 bytes
 .../share_sweep_energy_brez_baterije/source.json   |  77 ++++------------
 __pycache__/Data_Loader.cpython-314.pyc            | Bin 10140 -> 10140 bytes
 __pycache__/Environment.cpython-314.pyc            | Bin 82599 -> 82599 bytes
 __pycache__/Pricing_Functions.cpython-314.pyc      | Bin 4925 -> 4979 bytes
 32 files changed, 432 insertions(+), 1089 deletions(-)
```
