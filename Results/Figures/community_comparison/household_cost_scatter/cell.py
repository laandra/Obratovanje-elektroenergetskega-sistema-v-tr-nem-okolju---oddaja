### Per-household annual cost, by scenario, against the same year with no batteries
fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.53))
rng = np.random.default_rng(0)

# One jitter per household, reused in every column, so the with/without pair
# reads as one vertical segment.
ids = sorted(HOUSEHOLDS["household_id"].unique())
JITTER = dict(zip(ids, rng.uniform(-0.17, 0.17, len(ids))))

BASE_COST = HOUSEHOLDS_BASE.set_index(["scenario", "household_id"])["total_cost_eur"]
MOVED_EUR = 1.0   # below this the ring lands on the dot and says nothing

for i, scenario in enumerate(SCEN_ORDER):
    subset = HOUSEHOLDS[HOUSEHOLDS["scenario"] == scenario]
    cost = subset.set_index("household_id")["total_cost_eur"]
    base = BASE_COST[scenario].reindex(cost.index)

    # A ring wherever removing the batteries moves the bill by over a euro: the
    # ten battery households under redni/aktivni/dinamicni, all fifty under
    # souporaba, where the senders' surplus changes every receiver's share.
    moved = base[(base - cost).abs() > MOVED_EUR]
    for hid in moved.index:
        xb = i + JITTER[hid]
        ax.plot([xb, xb], [base[hid], cost[hid]], color=MUTED, linewidth=1, zorder=1)
    ax.scatter([i + JITTER[h] for h in moved.index], moved.to_numpy(dtype=float),
               s=34, facecolor="none", edgecolor=MUTED, linewidth=1.1, zorder=2,
               label="isto gospodinjstvo brez baterij" if i == 0 else None)

    for seg in SEGMENTS:
        seg_rows = subset[subset["segment"] == seg]
        ax.scatter([i + JITTER[h] for h in seg_rows["household_id"]],
                   seg_rows["total_cost_eur"], s=26, color=SEG_COLOR[seg],
                   alpha=0.85, linewidth=0, zorder=3, label=seg if i == 0 else None)

    ax.scatter([i], [base.mean()], marker="_", s=900, color=MUTED, linewidth=2,
               zorder=4, label="povprečje brez baterij" if i == 0 else None)
    ax.scatter([i], [cost.mean()], marker="_", s=900, color=INK, linewidth=2,
               zorder=5, label="povprečje" if i == 0 else None)

for _, row in EXTREMES.iterrows():
    xi = SCEN_ORDER.index(row["scenario"]) + JITTER[row["household_id"]]
    ax.annotate(row["household_id"], (xi, row["Cost_EUR"]), xytext=(12, 0),
                textcoords="offset points", fontsize=8, color=INK_2, va="center")

ax.set_xticks(range(len(SCEN_ORDER)))
ax.set_xticklabels([LABEL[s] for s in SCEN_ORDER])
ax.legend(ncol=4, loc="upper left", bbox_to_anchor=(0, -0.10), fontsize=9)
finish(ax, title="Vsako gospodinjstvo, vsak scenarij",
       subtitle="obroč je isto gospodinjstvo brez baterij; skrajna primera sta označena",
       ylabel="EUR / leto", yfmt=EUR)
pf.show(fig, "household_cost_scatter")

# What the ten batteries moved, on their own bills and on everybody else's.
moved_all = HOUSEHOLDS[["scenario", "household_id", "battery_kwh", "total_cost_eur"]].copy()
moved_all["Brez baterij [EUR]"] = [
    BASE_COST[(s, h)] for s, h in zip(moved_all["scenario"], moved_all["household_id"])
]
moved_all["Premik [EUR]"] = moved_all["Brez baterij [EUR]"] - moved_all["total_cost_eur"]
moved_all["Scenario"] = moved_all["scenario"].map(LABEL)
moved_all["Baterija"] = np.where(moved_all["battery_kwh"] > 0, "z baterijo", "brez baterije")
print("Premik > 0 pomeni, da bi gospodinjstvo brez baterij v skupnosti plačalo več.")
moved_all.groupby(["Scenario", "Baterija"], sort=False)["Premik [EUR]"].agg(
    ["count", "mean", "min", "max", "sum"]).round(1)