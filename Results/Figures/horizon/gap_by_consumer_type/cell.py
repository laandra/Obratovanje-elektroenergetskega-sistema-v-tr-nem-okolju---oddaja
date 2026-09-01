### Kaj tip odjemalca naredi kakovosti MILP, po algoritmih
# The list is averaged out so the consumer is the only thing varying, over the
# lists every group may sign. Redni 2T is scoped to the no-PV groups, so leaving
# it in would read a contract difference as a household difference.
UNIVERSAL = [t for t in TARIFFS_READY
             if all(hc.tariff_allowed(t, g) for g in hc.DATASET_GROUPS)]
df_g = df_scored[df_scored["Tariff"].isin(UNIVERSAL)]
GROUPS = [g for g in hc.DATASET_GROUPS if g in set(df_g["Dataset"])]

gap_group = (df_g.pivot_table(index="Dataset", columns="Strategy", values="Gap_pct",
                              aggfunc="mean")
             .reindex(index=GROUPS, columns=STRAT_ORDER))
# Pooled per (group, strategy): summed gap over summed achievable.
gap_group_pooled = (
    df_g.groupby(["Dataset", "Strategy"])[["Gap_to_Optimum_EUR", "Achievable_EUR"]]
    .apply(hc._pooled_gap_pct).unstack("Strategy")
    .reindex(index=GROUPS, columns=STRAT_ORDER)
)
gap_eur_group = (df_g.pivot_table(index="Dataset", columns="Strategy",
                                  values="Gap_to_Optimum_EUR", aggfunc="mean")
                 .reindex(index=GROUPS, columns=STRAT_ORDER))

# Every algorithm is scored against its own column mean: the question is which
# consumer type an algorithm handles badly.
col_mean = gap_group.mean(axis=0)
rel = gap_group.div(col_mean.where(col_mean > 1e-9))     # 1.0 = that algorithm's average consumer
pv_mask = np.array([hc.has_pv(g) for g in GROUPS])


def short_group(g):
    """Fluvius_PV_HP_EV -> PV+HP+EV, and the bare group -> 'osnovni'."""
    return "osnovni" if g == "Fluvius" else g.replace("Fluvius_", "").replace("_", "+")

# --- the numbers themselves, colour-normalised per algorithm -----------------
# Each column is scaled to its own maximum; the printed number carries the
# magnitude. A neutral ramp: these rows pool the price lists, so neither list
# hue may claim them.
fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.52))
norm = gap_group.div(gap_group.max(axis=0).where(lambda s: s > 1e-9)).fillna(0.0)
ax.imshow(norm.to_numpy(), cmap=pf.ramp(INK_2, "spread"), aspect="auto", vmin=0, vmax=1)
ax.set_xticks(range(len(STRAT_ORDER)), [LABEL[s] for s in STRAT_ORDER],
              rotation=25, ha="right", fontsize=9)
ax.set_yticks(range(len(GROUPS)), [short_group(g) for g in GROUPS], fontsize=9)
ax.grid(False)
for r in range(len(GROUPS)):
    for c in range(len(STRAT_ORDER)):
        v = gap_group.iat[r, c]
        ax.text(c, r, fmt_pct(v, 2), ha="center", va="center", fontsize=8,
                color="#ffffff" if norm.iat[r, c] > 0.62 else INK)
finish(ax, title="Povprečna vrzel [%] po skupinah; senčenje je normirano po stolpcu, "
                 "temno = najtežji odjemalec za ta algoritem")
pf.show(fig, "gap_by_consumer_type")

# --- the same rows as a ratio, so the algorithms share one axis --------------
fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.52))
GROUP_SHADE = [pf.mix(INK_2, "#ffffff", t) for t in np.linspace(0.72, 0.05, len(GROUPS))]
base = np.arange(len(STRAT_ORDER))[::-1]
flat_rows = []
for j, strat in enumerate(STRAT_ORDER):
    y = base[j]
    vals = rel[strat].to_numpy()
    if not np.isfinite(vals).any():
        # The whole-year solve is 0 % on every type by construction, so there is
        # no ratio to draw.
        flat_rows.append(y)
        continue
    ax.plot([np.nanmin(vals), np.nanmax(vals)], [y, y], color=MUTED, lw=1.2,
            alpha=0.45, zorder=2)
    for i, g in enumerate(GROUPS):
        ax.scatter([vals[i]], [y], s=62, marker="o" if pv_mask[i] else "s",
                   color=GROUP_SHADE[i], edgecolor=SURFACE, lw=0.8, zorder=3)
ax.axvline(1.0, color=MUTED, lw=1.1, ls="--")
for y in flat_rows:
    ax.annotate("0 % pri vseh tipih", xy=(1.0, y), xycoords=("axes fraction", "data"),
                xytext=(-6, 0), textcoords="offset points", ha="right", va="center",
                fontsize=8, color=MUTED)
ax.set_yticks(base, [LABEL[s] for s in STRAT_ORDER])
finish(ax, title="Tip odjemalca proti kakovosti MILP: krog = s PV, kvadrat = brez PV",
       xlabel="Vrzel skupine / povprečje tega algoritma  (1,0 = povprečen odjemalec)")
ax.grid(axis="y", visible=False)
pf.key_legend(ax, [plt.Line2D([], [], marker="o" if pv_mask[i] else "s", ls="", ms=7,
                              color=GROUP_SHADE[i]) for i in range(len(GROUPS))],
              where="lower left", ncol=4,
              labels=[short_group(g) for g in GROUPS], fontsize=8,
              title="tip gospodinjstva", title_fontsize=8, columnspacing=1.0,
              handletextpad=0.4)
pf.show(fig, "gap_by_consumer_type_ratio")

# --- read-out -------------------------------------------------------------
lines = [
    f"{len(GROUPS)} tipov gospodinjstev x {len(STRAT_ORDER)} algoritmov, "
    f"ceniki {', '.join(UNIVERSAL)} (skupine s PV in brez njega so na njih enako zastopane)",
    "",
    f"{'algoritem':16s}{'najtežji tip':>18s}{'vrzel':>8s}{'najlažji tip':>18s}{'vrzel':>8s}"
    f"{'razpon':>9s}{'PV / brez PV':>14s}",
]
for strat in STRAT_ORDER:
    col = gap_group[strat].dropna()
    if col.empty or col.max() <= 1e-9:
        lines.append(f"{LABEL[strat]:16s}{'--':>18s}{0.0:7.2f}%{'--':>18s}{0.0:7.2f}%"
                     f"{0.0:8.2f}{'--':>14s}")
        continue
    hi, lo = col.idxmax(), col.idxmin()
    pv_mean = float(gap_group.loc[pv_mask, strat].mean())
    no_pv_mean = float(gap_group.loc[~pv_mask, strat].mean())
    ratio = pv_mean / no_pv_mean if no_pv_mean > 1e-9 else float("nan")
    lines.append(
        f"{LABEL[strat]:16s}{short_group(hi):>18s}{col[hi]:7.2f}%"
        f"{short_group(lo):>18s}{col[lo]:7.2f}%"
        f"{col.max() - col.min():8.2f}{ratio:13.2f}x"
    )

# Is "hard household" a property of the household? A high rank correlation
# across algorithms means the consumer type is a fixed handicap.
ranks = gap_group[[s for s in STRAT_ORDER if gap_group[s].max() > 1e-9]].rank(axis=0)
corr = ranks.corr(method="spearman")
off = corr.to_numpy()[np.triu_indices(len(corr), k=1)] if len(corr) > 1 else np.array([])
worst_each = {s: gap_group[s].idxmax() for s in ranks.columns}
lines += [
    "",
    f"Spearman med algoritmi po uvrstitvi skupin: povprečno {np.nanmean(off):.2f} "
    f"(min {np.nanmin(off):.2f}) -- "
    + ("isti tipi so težki za vse algoritme" if np.nanmean(off) > 0.6
       else "vsak algoritem se lomi na svojem tipu odjemalca"),
    f"Najtežji tip po algoritmih: "
    + ", ".join(f"{LABEL[s]} -> {short_group(g)}" for s, g in worst_each.items()),
]
# Where the mean of percentages and the pooled gap disagree about which type is
# hardest, the disagreement is printed rather than averaged away.
disagree = [(s_, worst_each[s_], gap_group_pooled[s_].idxmax()) for s_ in ranks.columns
            if gap_group_pooled[s_].notna().any()
            and gap_group_pooled[s_].idxmax() != worst_each[s_]]
lines += [
    ("Združeno po evrih (pooled) je najtežji tip drugje: "
     + ", ".join(f"{LABEL[s_]} -> {short_group(p_)} (namesto {short_group(m_)})"
                 for s_, m_, p_ in disagree))
    if disagree else
    "Združeno po evrih (pooled) je najtežji tip povsod isti kot po povprečju odstotkov",
    "",
    "V evrih (povprečna zamujena letna korist na gospodinjstvo tega tipa):",
    f"{'algoritem':16s}" + "".join(f"{short_group(g):>16s}" for g in GROUPS[:4]),
]
for strat in STRAT_ORDER:
    lines.append(f"{LABEL[strat]:16s}"
                 + "".join(f"{gap_eur_group.loc[g, strat]:15.2f}" for g in GROUPS[:4]))
lines.append(f"{'algoritem':16s}" + "".join(f"{short_group(g):>16s}" for g in GROUPS[4:]))
for strat in STRAT_ORDER:
    lines.append(f"{LABEL[strat]:16s}"
                 + "".join(f"{gap_eur_group.loc[g, strat]:15.2f}" for g in GROUPS[4:]))

print("\n".join(lines))

gap_group.rename(columns=LABEL).round(2)