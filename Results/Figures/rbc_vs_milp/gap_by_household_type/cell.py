by_group, _ = rbc.summarize(cross, by=["Dataset", "Controller"])
heat = (by_group["Gap_pct"].unstack("Controller")
        .reindex(index=[g for g in DATASET_GROUPS], columns=POLICIES))

fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.47))
values = heat.to_numpy(dtype=float)
# One hue, light -> dark: this panel encodes magnitude, not identity. The ramp
# is NEUTRAL rather than a family hue -- its columns span all three families,
# and a family hue here would read as a claim about which family a cell belongs
# to.
image = ax.imshow(values, aspect="auto", cmap=pf.ramp(INK_2, "gap"), vmin=0,
                  vmax=float(np.nanmax(values)))
ax.set_xticks(range(len(POLICIES)), [CONTROLLER_LABEL[c] for c in POLICIES],
              rotation=30, ha="right")
ax.set_yticks(range(len(heat.index)), [group_label(g) for g in heat.index])
ax.grid(False)
mid = float(np.nanmax(values)) * 0.55
for i in range(values.shape[0]):
    for j in range(values.shape[1]):
        v = values[i, j]
        if not np.isfinite(v):
            continue
        ax.text(j, i, f"{v:.0f}", ha="center", va="center", fontsize=9,
                color=SURFACE if v > mid else INK)
fig.colorbar(image, ax=ax, label="gap to the MILP [%]", pad=0.02)
finish(ax, title="Gap to the MILP by household type")
pf.show(fig, "gap_by_household_type")