# inverter_per_kw

Exported 2026-09-15T15:23:05+00:00
Files: inverter_per_kw.pdf
Size: 3.5 x 2.8414 in @ 600 dpi (exact figure size)

> resized from 7.16x4.37 to 3.50x2.84 in; IEEE text applied to a figure drawn in the notebook style (scaled, not rebuilt); stroke weights scaled 0.49x to the narrower canvas

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Optimalna velikost baterije, ko je razsmernik zaračunan na kW — Mediana najboljših kapacitet po 16 gospodinjstvih, pri hrambi 250 EUR/kWh in brez enkratnega stroška. Moč paketa je min(0.5 x kapaciteta, 11 kW), zato cena na kW ni pavšal: pod mejo razsmernika vsaki kWh hrambe doda 0.5-kratnik cene na kW in optimum potisne navzdol, nad njo pa ne več. Navpičnica je 333 EUR/kW — enak denar kot 1,000 EUR pavšala pri moči, ki jo črpa današnji mediani optimum.

## Source

- notebook: C:\Users\HP\Documents\JupyterNotebook\Energy_Community\Multuser_Battery_Size_Optimization.ipynb (via __vsc_ipynb_file__)
- cell execution count: 52
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: f7d2f9c7fae6e24b4f3b615be90ae8644c63491c (Development)
- subject: Changing graphs
- describe: f7d2f9c-dirty

**Working tree was DIRTY (14 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Multuser_Battery_Size_Optimization.ipynb           |  49 +++++++---
 .../multiuser_sizing/cycles_median/SOURCE.md       |  91 ++++---------------
 .../Figures/multiuser_sizing/cycles_median/cell.py |   5 +-
 .../cycles_median/cycles_median.pdf                | Bin 38882 -> 29665 bytes
 .../multiuser_sizing/cycles_median/source.json     |  76 ++++------------
 .../multiuser_sizing/inverter_fixed_fee/SOURCE.md  |  99 +++++----------------
 .../multiuser_sizing/inverter_fixed_fee/cell.py    |   6 +-
 .../inverter_fixed_fee/inverter_fixed_fee.pdf      | Bin 37397 -> 34010 bytes
 .../inverter_fixed_fee/source.json                 |  72 ++++-----------
 .../multiuser_sizing/inverter_per_kw/SOURCE.md     |  99 +++++----------------
 .../multiuser_sizing/inverter_per_kw/cell.py       |   4 +-
 .../inverter_per_kw/inverter_per_kw.pdf            | Bin 37514 -> 37124 bytes
 .../multiuser_sizing/inverter_per_kw/source.json   |  72 ++++-----------
 Results/battery_size_optimization.csv              |  50 ++++++-----
 14 files changed, 188 insertions(+), 435 deletions(-)
```
