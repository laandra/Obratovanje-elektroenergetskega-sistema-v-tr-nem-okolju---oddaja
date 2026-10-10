# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repository is

A research codebase for an academic study of **Slovenian household and energy-community
electricity billing, battery dispatch and tariff choice**. It models the real Slovenian
tariff regime (network power/energy charges per time block, presežna moč ratchet,
OVE+SPTE / URE / operater trga levies, trošarina, DDV, samooskrba credit netting) at
15-minute resolution, dispatches household batteries against it with a perfect-foresight
MILP (PuLP/CBC) and rule-based controllers, and produces the figures and LaTeX tables for
the publication.

Outputs are **figures and tables for an IEEE two-column article**, mostly in Slovenian.
There is no application to deploy and no service to run.

## Environment

Python 3.14 in a local venv. Always invoke it explicitly:

```bash
.venv/bin/python <script>
.venv/bin/python -m jupyter execute --inplace --timeout=3600 <notebook>.ipynb
```

Dependencies are pinned in `requirements.txt` (numpy, pandas, matplotlib, PuLP, gymnasium,
holidays, torch, optuna, ...). Long solves parallelize with `--workers` (the machine has
~10 usable cores).

## Layer map

The repo is layered; each layer owns one thing and the layer above never re-implements it.

**1. Tariff and billing — [New pricing functions/](New pricing functions/)** (Slovenian
domain layer, docstrings in Slovene, every constant sourced to a published act or price
list):

| file | owns |
|---|---|
| [si_tarife.py](New pricing functions/si_tarife.py) | tariff constants (network rates, levies, excise, DDV), with regulatory sources |
| [si_cas.py](New pricing functions/si_cas.py) | calendar, seasons, the 5 time blocks, holidays, Europe/Ljubljana local time |
| [si_paketi.py](New pricing functions/si_paketi.py) | the price-list catalogue (`PAKETI`), souporaba services, package/household compatibility rules |
| [si_obracun.py](New pricing functions/si_obracun.py) | the monthly bill: `dobava`, `samooskrba`, `obracun_souporabe`, `MesecniObracun`, `Racun` |
| [si_moc.py](New pricing functions/si_moc.py) | dogovorjena obračunska moč — the per-block agreed-power vector and the rules that constrain it |
| [si_konica.py](New pricing functions/si_konica.py) | the running-maximum ratchet proxy used by the MILP/RL paths |
| [si_invoice.py](New pricing functions/si_invoice.py) | line-item invoices (`InvoiceBuilder`) from per-interval results |
| [si_poraba_doma.py](New pricing functions/si_poraba_doma.py) | bills real meter exports under `Input data/Poraba doma/` (has a CLI) |
| [test_primer.py](New pricing functions/test_primer.py), [test_souporaba.py](New pricing functions/test_souporaba.py) | print-driven self-tests, run directly |

[Pricing_Functions.py](Pricing_Functions.py) at the repo root is an **import shim** that
re-exports that folder under a package-safe name (the folder name has a space in it).
Import `Pricing_Functions`, not the files, from root-level code.

**2. Physics and data**

- [Data_Loader.py](Data_Loader.py) — loads profiles from `Input data/` and SMP prices.
- [Basic_Functions.py](Basic_Functions.py) — battery envelope primitives shared by MILP and RL.
- [Environment.py](Environment.py) — `HouseholdEnvironment` / `CommunityEnvironment`
  (gymnasium), plus the agreed-power schedule machinery (`agreed_power_schedule_for_profile`,
  `converge_agreed_power`).
- [Battery_Economics.py](Battery_Economics.py) — CAPEX/OPEX/discounting/IRR and the cycle
  wear price. Kept apart from dispatch on purpose: the wear price steers the MILP, it is
  never a line on a bill.

**3. Optimization**

- [MILP_Household.py](MILP_Household.py) — the single-household MILP: physics blocks
  (`add_household_physics`), the ratchet (`add_excess_power_ratchet`), endogenous agreed
  power (`add_endogenous_agreed_power`) and its causal shadow-price surrogate
  (`add_online_agreed_power_surrogate`), the price vectors (`interval_rate_vectors`), and
  the solver entry point `solve_household`. Also `build_household_env`, the one env factory.
- [Community_MILP.py](Community_MILP.py) — one MILP over every community member, solving
  batteries and shared-energy splits jointly under `individualno` / `souporaba` /
  `skupnostna_samooskrba`. Decomposed by calendar month.
- [Rule_Based_Control.py](Rule_Based_Control.py) — eight deployable controllers and the
  runner that prices them through exactly the same settlement as the MILP (has a CLI).

**4. Study drivers** (each writes per-unit CSV caches under `Results/` and has a CLI):

- [Horizon_Comparison.py](Horizon_Comparison.py) — horizon × execution × SOC mode × tariff,
  over 8 Fluvius groups. Also the home of the shared study configuration
  (`DATASET_GROUPS`, `TARIFFS`, `PEAK_RESET_MONTHS`, `AGREED_POWER_*`, `FULL_PERIOD_GAP_REL`).
- [Community_Study.py](Community_Study.py) — a 50-household community under four commercial arrangements.
- [multi_household_tools.py](multi_household_tools.py) — interval/souporaba scenario runners for the baseline notebooks.
- [Anonymous_Labels.py](Anonymous_Labels.py) — the publication may not name suppliers;
  every label reaching a figure, table or printed line goes through here
  (`supplier_label`, `option_label`, `short_option_label`, `anonymise`, `scrub`).

**5. Presentation — [Plotting_Functions.py](Plotting_Functions.py).** See below.

**6. Notebooks** — the studies themselves. Each one loads a `Results/*.csv` cache by
default and only re-solves when its `RUN_*` flag is flipped to `True`:

| notebook | question | figure subdir | run flag |
|---|---|---|---|
| [Energy_Community_Comparison.ipynb](Energy_Community_Comparison.ipynb) | what does a 50-household community pay, under which tariff | `community_comparison` | `RUN_DISPATCH` |
| [Skupnostna_Samooskrba_vs_Souporaba.ipynb](Skupnostna_Samooskrba_vs_Souporaba.ipynb) | the two Slovenian sharing schemes, head to head | `community_sharing` | — |
| [No_battery_comparison.ipynb](No_battery_comparison.ipynb) | which contract should a household with no battery sign | `no_battery` | `RUN_PV`, `RUN_NO_PV`, `RUN_PV_NOSALE`, `RUN_CATALOGUE` |
| [MILP_horizon_comparison.ipynb](MILP_horizon_comparison.ipynb) | how far ahead must the optimizer look | `horizon` | `RUN_BATCH` |
| [RBC_vs_MILP_Comparison.ipynb](RBC_vs_MILP_Comparison.ipynb) | what perfect foresight is worth against a real rule | `rbc_vs_milp` | `RUN_BATCH` |
| [Battery_Size_Optimization.ipynb](Battery_Size_Optimization.ipynb) | one household, capacity sweep | `battery_sizing` | `RUN_KEYS` |
| [Multuser_Battery_Size_Optimization.ipynb](Multuser_Battery_Size_Optimization.ipynb) | 16 households × 9 price lists × capacity | `multiuser_sizing` | `RUN_KEYS` |
| [Multuser_Battery_Size_Optimization no cycle cost.ipynb](Multuser_Battery_Size_Optimization no cycle cost.ipynb) | the same, wear price off | `multiuser_sizing_no_cycle_cost` | `RUN_KEYS` |
| [Extended_Multuser_Battery_Size_Optimization.ipynb](Extended_Multuser_Battery_Size_Optimization.ipynb) | the extended variant | `extended_multiuser_sizing` | `RUN_KEYS` |
| [Household invoice generator.ipynb](Household invoice generator.ipynb) | real invoices for the `Poraba doma` meters | `invoices` | — |
| [Multi_household_baseline.ipynb](Multi_household_baseline.ipynb) | no-PV baseline vs PV scenarios | `multi_household_baseline` | — |
| [Household_local model.ipynb](Household_local model.ipynb) | DQN against the MILP | `dqn_household` | — |

[Archive/](Archive/) holds superseded work (SARSA, clustering, old notebooks) — do not
extend it. `Claude outputs/` holds generated poster/LaTeX artefacts.

## Plotting — the rule

**Every new graph goes through the unified plotting module,
[Plotting_Functions.py](Plotting_Functions.py). If it cannot express what the figure needs,
EXTEND `Plotting_Functions.py` — never work around it with a local helper, a private
rcParams block, or a bare `plt.savefig`.**

There is exactly one plotting module. Nothing else sets rcParams and nothing else writes
into `Results/Figures`. It owns the style, the IEEE geometry, the Slovenian/English
glossary, the export backend and the provenance capture, because those are properties of
the *article* rather than of any one chart. A local helper that duplicates one of them is
how the nine copy-pasted style cells this module replaced drifted apart.

Notebook preamble, once:

```python
import importlib
import Plotting_Functions as pf
pf = importlib.reload(pf)                       # the reload is load-bearing: `import`
pf.use(subdir="<notebook_subdir>", titles=False, preset="page")   # returns the kernel's
from Plotting_Functions import INK, INK_2, MUTED, SURFACE, SERIES, EUR, finish  # first cache
```

End of every figure cell, once — this replaces `plt.tight_layout(); plt.show()`:

```python
pf.show(fig, "figure_name")
```

Practical rules:

- Build with a bare `plt.subplots()`; `pf.use` already set the standard figsize. No
  `figsize=` literals in cells — use `pf.figsize(ratio=...)` for a taller/shorter figure.
- Width comes from the preset (`page` 7.16 in, `column` 3.5 in, `screen` preview,
  `as_built` opt-out). Retarget a figure by changing the preset and nothing else.
- Never put two panels side by side for a two-column article — split into two figures with
  one `pf.show` each.
- Labels are written in Slovenian; `pf.LANG = "en"` translates through `GLOSSARY` /
  `GLOSSARY_PARTS`. Untranslated strings collect in `pf.MISSING_TRANSLATIONS` — that list
  is the glossary to-do. Use `pf.t(sl, en)` in new code.
- Numbers: in a Slovenian figure `pf.show` rewrites every number to a decimal comma
  and a U+202F thousands space (ticks, annotations, legends, LaTeX tables). Write plain
  English f-strings in cells; never hand-format "0,5" (the pass would misread it).
  English-text notebooks declare `lang="en"`.
- Use the shared helpers rather than re-rolling them: `finish`, `chart_frame`
  (+ `layout="frame"`), `key_legend`, `panel_grid`, `edge_label`, `mix`, `ramp`, and the
  formatters `EUR`, `PLAIN`, `KW`, `PCT`, `PCT_SIGNED`, `YEARS`. An axis on a percent
  formatter must carry `[%]` in its label — the formatters draw no units.
- Tables that are really heatmaps go out as LaTeX: `pf.latex_heatmap_table` +
  `pf.show_table`. `pf.latex_figure` emits the float block.
- Semantics stay in the notebook: colour *dictionaries* (`TARIFF_COLOR`, ...) belong to the
  study; only the palette (`SERIES`) is shared.
- The alias `pf` is conventional but not universal: `Household invoice generator.ipynb`
  binds `pf` to `Pricing_Functions` and imports the plotting module as `plots`, because
  the whole notebook is a pricing notebook. Do not shadow one with the other.
- Each export writes `Results/Figures/<subdir>/<name>/` with the PDF, `source.json`,
  `SOURCE.md` (carrying the caption text, since `titles=False`), `cell.py` and — when the
  tree was dirty — a gitignored `uncommitted.diff`. Keep `name` stable; LaTeX depends on it.

`PLOTTING_GUIDE.txt` is the long-form reference (geometry, layout ordering, translation,
troubleshooting). **Read it before changing `Plotting_Functions.py`**, and update it when
you extend the module.

## Working conventions

**Import constants, never retype them.** A value that two studies must share lives in one
module and is imported: the solver gap is `Horizon_Comparison.FULL_PERIOD_GAP_REL`, battery
physics are `MILP_Household.{C_RATE, CHARGE_EFFICIENCY, INVERTER_MAX_KW, SOC_FRACTION}`,
capital costs are `Battery_Economics.*`, price lists are `si_paketi.PAKETI`. A re-typed
number is a bug waiting for the two studies to disagree.

**One price signal.** `MILP_Household.interval_rate_vectors` is the single per-interval
import/export rate source; rules, the MILP and the evaluators all read it. Do not rebuild
rates locally.

**Caching.** Study drivers write one CSV per unit under `Results/<Study>/` and notebooks
read them. Result rows are stamped with configuration tags (`PEAK_RESET_TAG`,
`AGREED_POWER_TAG`, `SETTLEMENT_TAG`); a cache written under a different tag holds a
*different quantity*, not an older one, and is rejected rather than merged. If you change
a tagged rule, the cache is void and must be regenerated.

**Validation is print-driven, not pytest.** Run the check scripts directly; each has a
`--quick` mode:

```bash
.venv/bin/python Rule_Based_Control_Check.py --quick
.venv/bin/python Battery_Envelope_Check.py --quick
.venv/bin/python Agreed_Power_Check.py --quick
.venv/bin/python "New pricing functions/test_primer.py"
.venv/bin/python "New pricing functions/test_souporaba.py"
```

The invariant they exist to protect: **the perfect-foresight MILP is a lower bound.** A
rule-based controller that comes out cheaper than the MILP on the objective the MILP
minimized is a pricing bug, never a better policy.

**Anonymisation.** Everything published goes through `Anonymous_Labels`; a supplier is
"Ponudnik N" and a price list keeps only its tariff structure. The one deliberate
exception is `Household invoice generator.ipynb` — a real invoice must name its contract.

**Documentation style.** Modules carry long explanatory docstrings saying *why* a rule is
shaped the way it is and what would break otherwise. Match that when editing; a comment
here is usually load-bearing.

## Domain gotchas

- **Fluvius timestamps are Brussels-local despite the `Z` suffix.** Any calendar or clock
  decision must go through `si_cas.v_lokalni_cas` / `MILP_Household.month_calendar` /
  `day_calendar`. A rule read off the raw index fires 1–2 h off the tariff clock.
- **The agreed power is endogenous.** Month *M*'s dogovorjena obračunska moč is the mean of
  the top-5 15-minute peaks per block over the window ending at *M* − lag, derived from the
  profile the *dispatch* achieved. A month legitimately carries no agreed power in a block
  it is not billed for, so never index a block directly.
- **Two excess-power rules coexist.** `si_obracun` bills the statutory
  `sqrt(sum of squared exceedances)` with VAT; the MILP path bills the linear running-maximum
  ratchet (`si_konica`) without. They are comparable only once that item is lifted out.
- **Exports are not symmetric with imports.** The samooskrba buyback credit is *not* subject
  to DDV and is subtracted after VAT. A price list with `tip_odkupa=NI` credits exports zero.
- **Price-list eligibility is real.** `si_paketi.preveri_paket` rejects a samooskrba list for
  a household with no PV device and vice versa; two-tariff plain lists are scoped to the
  no-PV groups. A job that ignores this solves fine and then fails at invoicing.
- **Only price *spreads* drive dispatch.** Two lists a flat amount apart produce identical
  trajectories — overlapping curves in a usage chart are correct, not a bug.

## Git

Work happens on `Development`; `main` is the PR target. Figure PDFs and their provenance are
tracked; `uncommitted.diff` is not. A figure exported from a dirty tree is not reproducible
from the commit id alone — commit before the final export run for the paper.
