# cycles_median

Exported 2026-09-15T13:33:52+00:00
Files: cycles_median.pdf
Size: 3.5 x 2.01 in @ 600 dpi (exact figure size)

> resized from 7.16x3.15 to 3.50x2.01 in; IEEE text applied to a figure drawn in the notebook style (scaled, not rebuilt); stroke weights scaled 0.49x to the narrower canvas

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Koliko je baterija sploh v uporabi — Mediana po 16 gospodinjstvih, z začetkom pri izračunu brez baterije pri 0 kWh, kjer je ciklov po definiciji nič. Redni 1T leži tik nad ničlo: enotna tarifa nima cenovnega razpona čez dan, ki bi pokril 10.8 % izgube krožnega cikla, zato baterijo poganja le lastna raba PV — 8 gospodinjstev brez PV je na tej pogodbi tako rekoč ne uporabi. Pari krivulj se prekrivajo (Aktivni s Fiksni, Redni 2T s Fiksni BO): dispečiranje določa razpon cen čez dan in ne njihova raven, razpon pa je pri teh cenikih isti — kjer sta krivulji povsem enaki, je črtkanje zamaknjeno, da se vidita obe barvi. Redni + NM je sklenljiv le s PV, zato je njegova mediana po 8 gospodinjstvih in ne po vseh.

## Source

- notebook: C:\Users\HP\Documents\JupyterNotebook\Energy_Community\Multuser_Battery_Size_Optimization.ipynb (via __vsc_ipynb_file__)
- cell execution count: 49
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: f7d2f9c7fae6e24b4f3b615be90ae8644c63491c (Development)
- subject: Changing graphs
- describe: f7d2f9c-dirty

**Working tree was DIRTY (6 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Multuser_Battery_Size_Optimization.ipynb           |  49 ++++++++---
 .../multiuser_sizing/cycles_median/SOURCE.md       |  91 ++++-----------------
 .../Figures/multiuser_sizing/cycles_median/cell.py |   5 +-
 .../cycles_median/cycles_median.pdf                | Bin 38882 -> 29665 bytes
 .../multiuser_sizing/cycles_median/source.json     |  76 ++++-------------
 Results/battery_size_optimization.csv              |  50 +++++------
 6 files changed, 99 insertions(+), 172 deletions(-)
```
