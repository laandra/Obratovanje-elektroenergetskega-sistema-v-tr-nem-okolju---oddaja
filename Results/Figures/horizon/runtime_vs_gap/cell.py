### What the extra compute buys, on each price list
fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.58))

for tariff in TARIFFS_READY:
    xs = np.array([summary.loc[(tariff, s), "Runtime_s"] for s in STRAT_ORDER], dtype=float)
    ys = np.array([summary.loc[(tariff, s), "Gap_pct"] for s in STRAT_ORDER], dtype=float)
    order = np.argsort(xs)
    # One list's trade-off curve, cheapest solve to most expensive.
    ax.plot(xs[order], ys[order], lw=2.0, color=TARIFF_COLOR[tariff], alpha=0.5, zorder=2)
    for strat, xi, yi in zip(STRAT_ORDER, xs, ys):
        ax.scatter([xi], [yi], s=95, marker=MODE_MARKER[hc.STRATEGIES[strat][2]],
                   color=strat_color(tariff, strat), zorder=3, lw=1.4, edgecolor=SURFACE)

# Label the strategies once, on the most spread-out list. Offsets alternate so
# the labels survive where three strategies collapse onto one corner.
anchor = max(TARIFFS_READY, key=lambda t: summary.loc[t, "Gap_pct"].max())
for k, strat in enumerate(STRAT_ORDER):
    ax.annotate(LABEL[strat],
                xy=(summary.loc[(anchor, strat), "Runtime_s"],
                    summary.loc[(anchor, strat), "Gap_pct"]),
                xytext=(10, 6 if k % 2 == 0 else -14), textcoords="offset points",
                color=INK, fontsize=9, fontweight="semibold", zorder=6,
                bbox=dict(boxstyle="round,pad=0.15", fc=SURFACE, ec="none", alpha=0.85))

ax.set_xscale("log")
ax.set_xlim(float(summary["Runtime_s"].min()) / 2.4, float(summary["Runtime_s"].max()) * 8.0)
ax.axhline(0, color=MUTED, lw=1.1, ls="--")
finish(ax, title="Porabljen računski čas proti prihranjenemu denarju",
       xlabel="Čas reševalnika [s/(gospodinjstvo·leto)]",
       ylabel="Vrzel [%]")
leg = tariff_legend(ax, where="upper right", title="Cenik")
if soc_mode_legend(ax, kind="marker", where="center right", title="Način SOC"):
    ax.add_artist(leg)
pf.show(fig, "runtime_vs_gap")