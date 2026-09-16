# cycles_median

Exported 2026-09-16T09:11:18+00:00
Files: cycles_median.pdf
Size: 3.5 x 1.8 in @ 600 dpi (exact figure size)

> resized from 7.16x3.15 to 3.50x1.80 in; IEEE text applied to a figure drawn in the notebook style (scaled, not rebuilt); stroke weights scaled 0.49x to the narrower canvas

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Koliko je baterija sploh v uporabi — Mediana po 16 gospodinjstvih, z začetkom pri izračunu brez baterije pri 0 kWh, kjer je ciklov po definiciji nič. Redni 1T leži tik nad ničlo: enotna tarifa nima cenovnega razpona čez dan, ki bi pokril 10.8 % izgube krožnega cikla, zato baterijo poganja le lastna raba PV — 8 gospodinjstev brez PV je na tej pogodbi tako rekoč ne uporabi. Pari krivulj se prekrivajo (Aktivni s Fiksni, Redni 2T s Fiksni BO): dispečiranje določa razpon cen čez dan in ne njihova raven, razpon pa je pri teh cenikih isti — kjer sta krivulji povsem enaki, je črtkanje zamaknjeno, da se vidita obe barvi. Redni + NM je sklenljiv le s PV, zato je njegova mediana po 8 gospodinjstvih in ne po vseh.

## Source

- notebook: /Users/summerscholl/Documents/Andraz/Energy_Community/Multuser_Battery_Size_Optimization no cycle cost.ipynb (via __vsc_ipynb_file__)
- cell execution count: 35
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: 7fbf9fb85d766d1a7a473f931f551e8dd103b354 (Development)
- subject: Adding no cicle cost optimization for comparison
- describe: 7fbf9fb-dirty

**Working tree was DIRTY (4 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
.../cycles_median/SOURCE.md                        |  42 ++++-------------
 .../cycles_median/cell.py                          |   3 +-
 .../cycles_median/cycles_median.pdf                | Bin 34686 -> 26055 bytes
 .../cycles_median/source.json                      |  51 ++++++---------------
 4 files changed, 25 insertions(+), 71 deletions(-)
```
