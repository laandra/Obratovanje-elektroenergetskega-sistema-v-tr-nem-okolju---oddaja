# share_sweep_bill_10_kwh_pri_vsakem

Exported 2026-09-03T07:57:28+00:00
Files: share_sweep_bill_10_kwh_pri_vsakem.pdf
Size: 7.16 x 3.938 in @ 600 dpi (exact figure size)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Optimalni delež deljene energije — 10 kWh pri vsakem — Cenik Redni, 16 gospodinjstev, celo leto 2024, interna cena 0.050 EUR/kWh, značilni primer 2. Polna črta = pogodbeni (statični) delež, črtkano = prosta razdelitev po intervalih. Oznaka = delež z najnižjim računom skupnosti. Razmik med polno in črtkano črto je cena tega, da je delež v pogodbi fiksen.

## Source

- notebook: /Users/summerscholl/Documents/Andraz/Energy_Community/Skupnostna_Samooskrba_vs_Souporaba.ipynb (via __vsc_ipynb_file__)
- cell execution count: 23
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 7d7dbc1e3272f9f1e0fcb3305e503472b8188cca (Development)
- subject: Fixed a 2T bug and rerun the notebooks
- describe: 7d7dbc1-dirty

**Working tree was DIRTY (8 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
.../__pycache__/si_obracun.cpython-314.pyc         | Bin 50361 -> 50361 bytes
 .../share_sweep_bill_10_kwh_pri_vsakem.pdf         | Bin 18726 -> 18726 bytes
 .../share_sweep_bill_brez_baterije/SOURCE.md       |  74 +++------------------
 .../share_sweep_bill_brez_baterije.pdf             | Bin 18806 -> 18806 bytes
 .../share_sweep_bill_brez_baterije/source.json     |  71 ++++----------------
 __pycache__/Data_Loader.cpython-314.pyc            | Bin 10140 -> 10140 bytes
 __pycache__/Environment.cpython-314.pyc            | Bin 82599 -> 82599 bytes
 __pycache__/Pricing_Functions.cpython-314.pyc      | Bin 4925 -> 4979 bytes
 8 files changed, 24 insertions(+), 121 deletions(-)
```
