# share_sweep_bill_brez_baterije

Exported 2026-09-09T17:04:48+00:00
Files: share_sweep_bill_brez_baterije.pdf
Size: 7.16 x 3.938 in @ 600 dpi (exact figure size)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Optimalni delež deljene energije — brez baterije — Cenik Redni, 16 gospodinjstev, celo leto 2024, interna cena 0.050 EUR/kWh, značilni primer 2. Polna črta = pogodbeni (statični) delež, črtkano = prosta razdelitev po intervalih. Oznaka = delež z najnižjim računom skupnosti. Razmik med polno in črtkano črto je cena tega, da je delež v pogodbi fiksen.

## Source

- notebook: not detected
- cell execution count: 24
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: c946279b7af58519c80f4c1da1d35a4dc4c0b426 (Development)
- subject: Rerun after some graph fixes
- describe: c946279-dirty

**Working tree was DIRTY (60 files) — the commit above does NOT reproduce this figure on its own.**
See `uncommitted.diff`, which excludes :(exclude)*.ipynb — the notebook side is in `cell.py`.

```
Battery_Size_Optimization.ipynb                    | 755 +++++++++++----------
 RBC_vs_MILP_Comparison.ipynb                       | 178 ++---
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
 .../share_sweep_bill_brez_baterije.pdf             | Bin 18810 -> 18528 bytes
 .../achievable_by_household_type/SOURCE.md         | 277 ++------
 .../achievable_by_household_type.pdf               | Bin 11820 -> 11820 bytes
 .../achievable_by_household_type/source.json       | 110 ++-
 .../Figures/rbc_vs_milp/battery_earnings/SOURCE.md | 284 ++------
 .../battery_earnings/battery_earnings.pdf          | Bin 16771 -> 16771 bytes
 .../rbc_vs_milp/battery_earnings/source.json       | 113 ++-
 .../rbc_vs_milp/excess_power_charge/SOURCE.md      | 305 ++-------
 .../excess_power_charge/excess_power_charge.pdf    | Bin 16156 -> 16156 bytes
 .../rbc_vs_milp/excess_power_charge/source.json    | 116 ++--
 .../rbc_vs_milp/gap_by_household_type/SOURCE.md    | 270 ++------
 .../gap_by_household_type.pdf                      | Bin 37618 -> 37618 bytes
 .../rbc_vs_milp/gap_by_household_type/source.json  | 107 ++-
 .../rbc_vs_milp/gap_by_price_list/SOURCE.md        | 249 ++-----
 .../gap_by_price_list/gap_by_price_list.pdf        | Bin 16455 -> 16455 bytes
 .../rbc_vs_milp/gap_by_price_list/source.json      |  98 ++-
 Results/Figures/rbc_vs_milp/gap_by_rule/SOURCE.md  | 241 +------
 Results/Figures/rbc_vs_milp/gap_by_rule/cell.py    |   2 +-
 .../rbc_vs_milp/gap_by_rule/gap_by_rule.pdf        | Bin 16543 -> 16542 bytes
 .../Figures/rbc_vs_milp/gap_by_rule/source.json    |  94 +--
 .../Figures/rbc_vs_milp/gap_vs_capacity/SOURCE.md  | 256 ++-----
 .../gap_vs_capacity/gap_vs_capacity.pdf            | Bin 18786 -> 18786 bytes
 .../rbc_vs_milp/gap_vs_capacity/source.json        | 101 ++-
 .../rbc_vs_milp/grid_charged_share/SOURCE.md       | 291 ++------
 .../grid_charged_share/grid_charged_share.pdf      | Bin 16740 -> 16740 bytes
 .../rbc_vs_milp/grid_charged_share/source.json     | 116 ++--
 .../Figures/rbc_vs_milp/peak_grid_import/SOURCE.md | 298 ++------
 .../peak_grid_import/peak_grid_import.pdf          | Bin 16124 -> 16124 bytes
 .../rbc_vs_milp/peak_grid_import/source.json       | 116 ++--
 .../rbc_vs_milp/saving_vs_capacity/SOURCE.md       | 263 ++-----
 .../saving_vs_capacity/saving_vs_capacity.pdf      | Bin 19402 -> 19402 bytes
 .../rbc_vs_milp/saving_vs_capacity/source.json     | 104 ++-
 Results/Figures/rbc_vs_milp/trace_day/SOURCE.md    | 234 +------
 Results/Figures/rbc_vs_milp/trace_day/source.json  |  91 +--
 .../Figures/rbc_vs_milp/trace_day/trace_day.pdf    | Bin 31670 -> 31670 bytes
 60 files changed, 1758 insertions(+), 5257 deletions(-)
```
