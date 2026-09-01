### Who wins and who loses
labels_order = [LABELS[k] for k in HOUSEHOLD_KEYS]
y = np.arange(len(labels_order))
SUBTITLE = (f"Levo od ničle = cenejši račun. Črne oznake so oddajniki (s PV), sive "
            f"prejemniki. Interna cena {INTERNAL_PRICE:.3f} EUR/kWh — ta cena je edino, kar "
            f"premika delitev med vlogama; skupni znesek se z njo skoraj ne spremeni.")

for battery in SWEEP_BATTERIES:
    fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.70))
    base = sel[(sel["battery"] == battery) & (sel["scheme"] == ccm.SCHEME_INDIVIDUAL)
               ].set_index("Member")["Cost_EUR"]
    for i, scheme in enumerate((ccm.SCHEME_SOUPORABA, ccm.SCHEME_SKUPNOST)):
        sub = sel[(sel["battery"] == battery) & (sel["scheme"] == scheme)].set_index("Member")
        delta = (sub["Cost_EUR"] - base).reindex(labels_order)
        ax.barh(y + (i - 0.5) * 0.38, delta, 0.35, color=SCHEME_COLOR[scheme],
                label=SCHEME_LABEL[scheme], zorder=3, edgecolor=SURFACE, linewidth=1.0)
    ax.axvline(0, color=BASELINE, linewidth=1.2)
    ax.set_yticks(y)
    ax.set_yticklabels(labels_order, fontsize=8)
    ax.invert_yaxis()
    ax.grid(axis="x", linewidth=0.6)
    ax.set_axisbelow(True)
    # The role is carried by the tick label's ink, so it survives being read in
    # black and white.
    for tick, k in zip(ax.get_yticklabels(), HOUSEHOLD_KEYS):
        tick.set_color(INK if HAS_PV[k] else MUTED)
    finish(ax, xlabel="Sprememba letnega računa [EUR/a]", xfmt=EUR)
    pf.chart_frame(fig, f"Kdo plača manj in kdo več kot brez delitve — {battery}", SUBTITLE,
                   handles=[Patch(facecolor=SCHEME_COLOR[s], label=SCHEME_LABEL[s])
                            for s in (ccm.SCHEME_SOUPORABA, ccm.SCHEME_SKUPNOST)], ncol=2)
    pf.show(fig, f"member_bill_change_{pf.slug(battery)}", layout="frame")