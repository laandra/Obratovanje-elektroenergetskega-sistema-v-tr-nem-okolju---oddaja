# gap_by_rule

Exported 2026-09-09T17:02:52+00:00
Files: gap_by_rule.pdf
Size: 7.16 x 3.2936 in @ 600 dpi (tight)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- How much of the achievable saving each rule gives up

## Source

- notebook: not detected
- cell execution count: 11
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: c946279b7af58519c80f4c1da1d35a4dc4c0b426 (Development)
- subject: Rerun after some graph fixes
- describe: c946279-dirty

**Working tree was DIRTY (28 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Battery_Size_Optimization.ipynb                    | 755 +++++++++++----------
 .../battery_sizing/cost_vs_capacity/SOURCE.md      | 192 +-----
 .../cost_vs_capacity/cost_vs_capacity.pdf          | Bin 18668 -> 18668 bytes
 .../battery_sizing/cost_vs_capacity/source.json    |  73 +-
 .../energy_through_battery/SOURCE.md               | 211 +-----
 .../energy_through_battery.pdf                     | Bin 12857 -> 12857 bytes
 .../energy_through_battery/source.json             |  67 +-
 .../equivalent_full_cycles/SOURCE.md               | 223 +-----
 .../battery_sizing/equivalent_full_cycles/cell.py  |   2 +-
 .../equivalent_full_cycles.pdf                     | Bin 11509 -> 11644 bytes
 .../equivalent_full_cycles/source.json             |  61 +-
 .../battery_sizing/marginal_value/SOURCE.md        | 198 +-----
 .../Figures/battery_sizing/marginal_value/cell.py  |   2 +-
 .../marginal_value/marginal_value.pdf              | Bin 13939 -> 13952 bytes
 .../battery_sizing/marginal_value/source.json      |  72 +-
 .../battery_sizing/net_annual_benefit/SOURCE.md    | 205 +-----
 .../net_annual_benefit/net_annual_benefit.pdf      | Bin 20475 -> 20475 bytes
 .../battery_sizing/net_annual_benefit/source.json  |  70 +-
 .../battery_sizing/peak_grid_import/SOURCE.md      | 217 +-----
 .../peak_grid_import/peak_grid_import.pdf          | Bin 11663 -> 11663 bytes
 .../battery_sizing/peak_grid_import/source.json    |  64 +-
 .../Figures/battery_sizing/service_life/SOURCE.md  | 230 +------
 .../battery_sizing/service_life/service_life.pdf   | Bin 14688 -> 14688 bytes
 .../battery_sizing/service_life/source.json        |  59 +-
 .../rbc_vs_milp/gap_by_rule/gap_by_rule.pdf        | Bin 16543 -> 16542 bytes
 Results/Figures/rbc_vs_milp/trace_day/SOURCE.md    | 234 +------
 Results/Figures/rbc_vs_milp/trace_day/source.json  |  91 +--
 .../Figures/rbc_vs_milp/trace_day/trace_day.pdf    | Bin 31670 -> 31670 bytes
 28 files changed, 679 insertions(+), 2347 deletions(-)
```
