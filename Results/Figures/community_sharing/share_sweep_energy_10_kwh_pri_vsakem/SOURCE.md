# share_sweep_energy_10_kwh_pri_vsakem

Exported 2026-09-03T07:57:28+00:00
Files: share_sweep_energy_10_kwh_pri_vsakem.pdf
Size: 7.16 x 3.58 in @ 600 dpi (exact figure size)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Koliko energije shema res prestavi — 10 kWh pri vsakem — Polna črta = energija, ki jo je prejemnik dejansko porabil. Senčeno = prenesena energija, ki je prejemnik v istem 15-minutnem intervalu ni mogel porabiti; pri souporabi propade in se ne prenese naprej, pri skupnostni samooskrbi se vrne v odkup proizvajalca.

## Source

- notebook: /Users/summerscholl/Documents/Andraz/Energy_Community/Skupnostna_Samooskrba_vs_Souporaba.ipynb (via __vsc_ipynb_file__)
- cell execution count: 24
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 7d7dbc1e3272f9f1e0fcb3305e503472b8188cca (Development)
- subject: Fixed a 2T bug and rerun the notebooks
- describe: 7d7dbc1-dirty

**Working tree was DIRTY (14 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
.../__pycache__/si_obracun.cpython-314.pyc         | Bin 50361 -> 50361 bytes
 .../share_sweep_bill_10_kwh_pri_vsakem/SOURCE.md   |  77 ++++----------------
 .../share_sweep_bill_10_kwh_pri_vsakem.pdf         | Bin 18726 -> 18726 bytes
 .../share_sweep_bill_10_kwh_pri_vsakem/source.json |  74 +++++--------------
 .../share_sweep_bill_brez_baterije/SOURCE.md       |  74 +++----------------
 .../share_sweep_bill_brez_baterije.pdf             | Bin 18806 -> 18806 bytes
 .../share_sweep_bill_brez_baterije/source.json     |  71 ++++--------------
 .../share_sweep_energy_10_kwh_pri_vsakem.pdf       | Bin 13125 -> 13125 bytes
 .../share_sweep_energy_brez_baterije/SOURCE.md     |  80 +++++----------------
 .../share_sweep_energy_brez_baterije.pdf           | Bin 12983 -> 12983 bytes
 .../share_sweep_energy_brez_baterije/source.json   |  77 +++++---------------
 __pycache__/Data_Loader.cpython-314.pyc            | Bin 10140 -> 10140 bytes
 __pycache__/Environment.cpython-314.pyc            | Bin 82599 -> 82599 bytes
 __pycache__/Pricing_Functions.cpython-314.pyc      | Bin 4925 -> 4979 bytes
 14 files changed, 90 insertions(+), 363 deletions(-)
```
