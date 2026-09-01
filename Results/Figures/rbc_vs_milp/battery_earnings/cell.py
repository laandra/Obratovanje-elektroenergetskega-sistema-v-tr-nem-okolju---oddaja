share = (
    scored.assign(
        Grid_Share=lambda d: np.where(d["Charged_kWh"] > 1e-9,
                                      100.0 * d["Grid_Charged_kWh"] / d["Charged_kWh"],
                                      np.nan))
    .groupby(["Tariff", "Controller"])
    .agg(Saving_EUR=("Savings_EUR", "mean"),
         Grid_Share_pct=("Grid_Share", "mean"),
         Cycles=("Equivalent_Full_Cycles", "mean"))
)
grid_share = share["Grid_Share_pct"].unstack("Tariff").reindex(
    index=POLICIES + ["milp_full_period"], columns=TARIFF_ORDER)
saving = share["Saving_EUR"].unstack("Tariff").reindex(
    index=POLICIES + ["milp_full_period"], columns=TARIFF_ORDER)

y = np.arange(len(grid_share.index))
labels = [CONTROLLER_LABEL[c] for c in grid_share.index]

# One figure each: these two axes have different units and different stories,
# and side by side neither survives \columnwidth.
for frame, title, formatter, unit, export in (
    (saving, "What the battery earns", EUR, "EUR/a", "battery_earnings"),
    (grid_share, "How much of it was bought from the grid", PCT, "%", "grid_charged_share"),
):
    fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.55))
    height = 0.8 / len(TARIFF_ORDER)
    for k, tariff in enumerate(TARIFF_ORDER):
        offset = (k - (len(TARIFF_ORDER) - 1) / 2) * height
        # The price list is the SECOND categorical question these panels ask, and
        # the hue channel is already spoken for by the controller family, so it
        # gets a neutral ramp plus a legend rather than four more hues.
        ax.barh(y + offset, frame[tariff].to_numpy(dtype=float), height=height * 0.9,
                color=pf.mix(INK_2, "#ffffff", 0.72 - 0.22 * k), label=tariff)
    ax.axvline(0, color=MUTED, lw=1)
    ax.set_yticks(y, labels)
    finish(ax, title=title, xlabel=unit, xfmt=formatter)
    # Under the axes: the bars run the full width, so a legend placed inside
    # would sit on top of four of them.
    pf.key_legend(ax, [Patch(facecolor=pf.mix(INK_2, "#ffffff", 0.72 - 0.22 * k),
                             label=t) for k, t in enumerate(TARIFF_ORDER)],
                  ncol=len(TARIFF_ORDER), title="price list")
    pf.show(fig, export)

display(saving.round(0))
print("A controller that never grid-charges shows a zero-length bar on the right: "
      "self-consumption and delayed PV charge store only what the roof gave them.")