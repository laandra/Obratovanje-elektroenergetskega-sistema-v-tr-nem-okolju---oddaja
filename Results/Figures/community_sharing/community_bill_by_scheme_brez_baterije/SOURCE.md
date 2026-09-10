# community_bill_by_scheme_brez_baterije

Exported 2026-09-09T17:04:49+00:00
Files: community_bill_by_scheme_brez_baterije.pdf
Size: 7.16 x 3.7232 in @ 600 dpi (exact figure size)

## Caption

The title text for this figure, for the article's `\caption{...}`:

- Letni račun šestnajstih gospodinjstev, po shemi in ceniku — brez baterije — Prosta razdelitev deljene energije po intervalih, interna cena 0.050 EUR/kWh, značilni primer 2. Šrafirano = skupnostna samooskrba na ceniku, ki je izrecno ne dovoli (izračun je protidejstven). Manjkajoč stolpec = kombinacija, ki v tej študiji ni rešena (dinamični cenik se rešuje le brez hrambe, razdelek 7).

## Source

- notebook: not detected
- cell execution count: 26
- caller: <frozen runpy>:198
- cell source: cell.py

## Git

- commit: c946279b7af58519c80f4c1da1d35a4dc4c0b426 (Development)
- subject: Rerun after some graph fixes
- describe: c946279-dirty

**Working tree was DIRTY (74 files) — the commit above does NOT reproduce this figure on its own.**
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
 .../community_bill_by_scheme_brez_baterije.pdf     | Bin 12385 -> 12385 bytes
 .../share_sweep_bill_10_kwh_pri_vsakem/SOURCE.md   | 322 ++-------
 .../share_sweep_bill_10_kwh_pri_vsakem/cell.py     |   3 +-
 .../share_sweep_bill_10_kwh_pri_vsakem.pdf         | Bin 18734 -> 18461 bytes
 .../share_sweep_bill_10_kwh_pri_vsakem/source.json | 104 +--
 .../share_sweep_bill_brez_baterije/SOURCE.md       | 314 ++-------
 .../share_sweep_bill_brez_baterije/cell.py         |   3 +-
 .../share_sweep_bill_brez_baterije.pdf             | Bin 18810 -> 18528 bytes
 .../share_sweep_bill_brez_baterije/source.json     | 112 +--
 .../share_sweep_energy_10_kwh_pri_vsakem/SOURCE.md | 337 +++------
 .../share_sweep_energy_10_kwh_pri_vsakem.pdf       | Bin 13133 -> 13133 bytes
 .../source.json                                    |  90 +--
 .../share_sweep_energy_brez_baterije/SOURCE.md     | 330 ++-------
 .../share_sweep_energy_brez_baterije.pdf           | Bin 12993 -> 12993 bytes
 .../share_sweep_energy_brez_baterije/source.json   |  96 +--
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
 74 files changed, 2254 insertions(+), 6472 deletions(-)
```
