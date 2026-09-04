### Both catalogues on one axis: the households with no roof
# Hue is spent on the catalogue rather than on magnitude, because every row here
# is under the same zeroed export regime and the regime channel is free.
def catalogue_bill_panel(ax, summary, title, xlabel="Letni račun [EUR/a]"):
    """Ranked annual bill, one bar per option, hue = which catalogue sells it."""
    ypos = np.arange(len(summary))[::-1]
    ax.barh(ypos, summary["Cost_EUR"], height=0.74,
            color=[CATALOGUE_COLOR[c] for c in summary["Catalogue"]])
    ax.set_yticks(ypos, [short_list_name(o) for o in summary.index], fontsize=7.5)
    bar_labels(ax, ypos, summary["Cost_EUR"].to_numpy(), fontsize=7.5)
    # The cheapest row of each catalogue is named inside its own bar.
    for catalogue in ("dobava", "samooskrba"):
        opt = cheapest_of(summary, catalogue)
        ax.text(summary.loc[opt, "Cost_EUR"] * 0.5,
                ypos[list(summary.index).index(opt)],
                f"najcenejši – {CATALOGUE_SHORT[catalogue]}", va="center",
                ha="center", fontsize=7.5, color="#ffffff", fontweight="semibold")
    ax.set_xlim(0, summary["Cost_EUR"].max() * 1.12)
    ax.set_ylim(-0.8, len(summary) - 0.2)
    finish(ax, title=title, xlabel=xlabel)
    ax.grid(axis="x")
    ax.spines["left"].set_visible(False)
    key_below(ax, [Patch(facecolor=CATALOGUE_COLOR[c]) for c in CATALOGUE_ORDER],
              [CATALOGUE_LABEL[c] for c in CATALOGUE_ORDER], ncol=1)
    return ypos


def catalogue_figure(name, bill_title, heat_title, export):
    """The chapter's two figures for one household set.

    First: every option ranked by its own bill. Second: the same rows against the
    cheapest option for each household TYPE -- the ranking is a mean and can hide
    a list that suits one kind of household and no other.

    They are two figures rather than two panels of one: at 31 price lists a row
    shared between them is unreadable at half of \\textwidth.

    The heatmap ramp is NEUTRAL rather than either catalogue's hue: its rows come
    from both shelves, and giving the magnitude one of the two categorical hues
    would read as a claim about which shelf the cell belongs to.
    """
    summary, rel = cat_summary[name], by_group_cat_rel[name]

    fig, ax = plt.subplots(figsize=pf.figsize(ratio=rows_ratio(len(summary),
                                                               per_row=0.30)))
    catalogue_bill_panel(ax, summary, bill_title)
    pf.show(fig, f"{export}_bill_ranking")

    fig, ax = plt.subplots(figsize=pf.figsize(ratio=rows_ratio(len(rel),
                                                               per_row=0.28)))
    overpay_heatmap(ax, rel, INK_2, heat_title, fig=fig,
                    cell_fontsize=6.5 if rel.shape[1] > 5 else 7.0,
                    label_fontsize=7.5)
    pf.show(fig, f"{export}_overpay_by_group")
    return rel


rel_no_pv = catalogue_figure(
    "no PV",
    "Brez PV: samooskrbni ceniki so cenovno v igri, čeprav jih tak odjemalec ne sme podpisati",
    "Brez PV, oba kataloga: preplačilo glede na najcenejši cenik te skupine [%]",
    "catalogue_no_pv")

anonymise(rel_no_pv).round(2)