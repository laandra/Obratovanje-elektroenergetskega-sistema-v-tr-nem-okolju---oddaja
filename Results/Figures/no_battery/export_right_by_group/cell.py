### The two contracts on the same axis: one row per contract, one dot per regime
# A dumbbell rather than paired bars: the quantity of interest is the distance
# between two states of the same household. Both dots are labelled.
fig, ax = plt.subplots(figsize=pf.figsize(
    ratio=rows_ratio(len(head), per_row=0.62, floor=3.6)))

ypos = np.arange(len(head))[::-1]
span = head["NoSale_EUR"].max()
for y, (opt, row) in zip(ypos, head.iterrows()):
    ax.plot([row["Credited_EUR"], row["NoSale_EUR"]], [y, y],
            color=MUTED, lw=2.0, zorder=1, solid_capstyle="round")
    if row["Worth_EUR"] < 0.5:
        # A list that never bought surpluses lands both regimes on the same
        # euro, so the marker is split in half rather than overdrawn.
        for regime, side in (("credited", "left"), ("nosale", "right")):
            ax.plot(row["Credited_EUR"], y, marker="o", ms=11, ls="",
                    color=REGIME_COLOR[regime], fillstyle=side,
                    mec=SURFACE, mew=1.2, zorder=3)
    else:
        # 2 px surface ring on each mark so a dot never dissolves into the connector
        for value, regime in ((row["Credited_EUR"], "credited"),
                              (row["NoSale_EUR"], "nosale")):
            ax.plot(value, y, marker="o", ms=11, color=REGIME_COLOR[regime],
                    mec=SURFACE, mew=2.0, zorder=3)
    ax.text(row["Credited_EUR"] - span * 0.010, y, f"{row['Credited_EUR']:.0f}",
            va="center", ha="right", fontsize=8.5, color=INK_2)
    if row["Worth_EUR"] >= 0.5:
        worth_pct = row["Worth_EUR"] / row["Credited_EUR"] * 100 if row["Credited_EUR"] else 0
        ax.text(row["NoSale_EUR"] + span * 0.010, y, f"{row['NoSale_EUR']:.0f}",
                va="center", ha="left", fontsize=8.5, color=INK_2)
        ax.text((row["Credited_EUR"] + row["NoSale_EUR"]) / 2, y + 0.20,
                f"+{row['Worth_EUR']:.0f} (+{worth_pct:.1f}%)",
                va="bottom", ha="center", fontsize=8.5, color=INK,
                fontweight="semibold")
    else:
        ax.text((row["Credited_EUR"] + row["NoSale_EUR"]) / 2, y + 0.20,
                "brez odkupa",
                va="bottom", ha="center", fontsize=8.5, color=INK,
                fontweight="semibold")

# The row label carries the contract, the meter variant and the billing scheme.
ax.set_yticks(ypos, [f"{short_list_name(o)}\n{head.loc[o, 'Structure']}"
                     for o in head.index], fontsize=8)
# A rule between the best and worst blocks: the middle of the ranking is
# missing, and a continuous axis would imply it is not.
if len(best) < len(head):
    ax.axhline(ypos[len(best) - 1] - 0.5, color=MUTED, lw=1.0, ls=(0, (4, 3)))
    ax.text(head["Credited_EUR"].min() * 0.955, ypos[len(best) - 1] - 0.42,
            f"najboljši {len(best)}", va="bottom", ha="left", fontsize=8,
            color=MUTED, style="italic")
    ax.text(head["Credited_EUR"].min() * 0.955, ypos[len(best) - 1] - 0.58,
            f"najslabši {len(worst)}" + (f"  ({len(middle)} vmesnih ni prikazanih)"
                                         if middle else ""),
            va="top", ha="left", fontsize=8, color=MUTED, style="italic")
ax.set_xlim(head["Credited_EUR"].min() * 0.94, span * 1.05)
ax.set_ylim(-0.7, len(head) - 0.3)
finish(ax, title="Kolikšna je vrednost pravice do prodaje presežkov",
       xlabel="Letni račun [EUR/a]")
ax.grid(axis="x")
ax.spines["left"].set_visible(False)
key_below(ax,
          [plt.Line2D([], [], marker="o", ls="", ms=10, mec=SURFACE, mew=2.0,
                      color=REGIME_COLOR[r]) for r in ("credited", "nosale")],
          [REGIME_LABEL[r] for r in ("credited", "nosale")], ncol=2)
pf.show(fig, "export_right_worth")

# Per household type, on the best contract of each regime: who the buyback
# matters to.
best_pair = {"credited": (pv_best, df_pv), "nosale": (pv0_best, df_pv0)}
groups_pv = list(hc.PV_GROUPS)
by_group_regime = pd.DataFrame({
    regime: (frame[frame["Option"] == opt]
             .groupby("Dataset")["Cost_EUR"].mean().reindex(groups_pv))
    for regime, (opt, frame) in best_pair.items()
})

fig, ax = plt.subplots()
xpos = np.arange(len(groups_pv))
bar_w = 0.38
credited_values = by_group_regime["credited"].to_numpy()
for i, regime in enumerate(("credited", "nosale")):
    ax.bar(xpos + (i - 0.5) * (bar_w + 0.02), by_group_regime[regime],
           width=bar_w,
           color=REGIME_COLOR[regime], label=REGIME_LABEL[regime])
    for x, v, base in zip(xpos + (i - 0.5) * (bar_w + 0.02),
                          by_group_regime[regime], credited_values):
        pct = v / base * 100 if base else 0
        ax.text(x, v - by_group_regime.to_numpy().max() * 0.035,
                f"{v:.0f}\n({pct:.1f}%)", ha="center",
                va="top", fontsize=8, color=SURFACE)
# The delta is written above the pair, with a dedicated band clear of the
# two-line values inside the columns.
for x, (lo, hi) in zip(xpos, zip(by_group_regime["credited"],
                                 by_group_regime["nosale"])):
    pct = (hi - lo) / lo * 100 if lo else 0
    ax.text(x, hi + by_group_regime.to_numpy().max() * 0.075,
            f"+{hi - lo:.0f} (+{pct:.1f}%)", ha="center", va="bottom", fontsize=8.5,
            color=INK, fontweight="semibold")
ax.set_xticks(xpos, [group_label(g) for g in groups_pv],
              rotation=20, ha="right", fontsize=9)
ax.set_ylim(0, by_group_regime.to_numpy().max() * 1.26)
finish(ax,
       title=(f"{short_list_name(pv_best)} z odkupom in brez, po tipu gospodinjstva"
              if pv_best == pv0_best else
              "Na najcenejšem ceniku vsake možnosti, po tipu gospodinjstva"),
       ylabel="EUR/a", yfmt=EUR)
ax.legend(fontsize=8.5, loc="upper left")
ax.grid(axis="y")
pf.show(fig, "export_right_by_group")

by_group_regime.assign(
    Worth_EUR=lambda d: d["nosale"] - d["credited"],
    Export_kWh=df_pv.groupby("Dataset")["Export_kWh"].mean().reindex(groups_pv),
).round(1)