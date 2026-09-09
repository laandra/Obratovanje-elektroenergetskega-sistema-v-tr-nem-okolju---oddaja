### The community bill, by scheme and price list
order = [ccm.SCHEME_INDIVIDUAL, ccm.SCHEME_SOUPORABA, ccm.SCHEME_SKUPNOST]
width = 0.26
SUBTITLE = (f"Prosta razdelitev deljene energije po intervalih, interna cena "
            f"{INTERNAL_PRICE:.3f} EUR/kWh, značilni primer {ZNACILNI_PRIMER}. Šrafirano = "
            f"skupnostna samooskrba na ceniku, ki je izrecno ne dovoli (izračun je "
            f"protidejstven). Manjkajoč stolpec = kombinacija, ki v tej študiji ni rešena "
            f"(dinamični cenik se rešuje le brez hrambe, razdelek 7).")

for battery in BATTERY_SCENARIOS:
    fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.52))
    configs = list(LIST_CONFIGS)
    x = np.arange(len(configs))
    for i, scheme in enumerate(order):
        sub = headline[(headline["battery"] == battery) & (headline["scheme"] == scheme)
                       & (headline["sharing"] != ccm.SHARING_STATIC)]
        vals, hatches = [], []
        for c in configs:
            row = sub[sub["config"] == c]
            vals.append(float(row["Community_cost_EUR"].iloc[0]) if len(row) else np.nan)
            hatches.append(scheme == ccm.SCHEME_SKUPNOST and not SKUPNOST_ALLOWED[c])
        bars = ax.bar(x + (i - 1) * width, vals, width * 0.92, color=SCHEME_COLOR[scheme],
                      label=SCHEME_LABEL[scheme], zorder=3, edgecolor=SURFACE, linewidth=1.2)
        for bar, hatched, v in zip(bars, hatches, vals):
            # A missing bar is a configuration this notebook did not solve at
            # this battery scenario (the SIPX-linked pairing, section 7); a
            # hatched one is a configuration the price list forbids.
            if not np.isfinite(v):
                continue
            if hatched:
                bar.set_hatch("///")
                bar.set_alpha(0.55)
                ax.annotate("cenik ne dovoli", (bar.get_x() + bar.get_width() / 2, v),
                            xytext=(0, 4), textcoords="offset points", ha="center",
                            fontsize=7.2, color=SCHEME_COLOR[scheme], rotation=90, va="bottom")
    ax.set_xticks(x)
    ax.set_xticklabels(configs)
    ax.grid(axis="y", linewidth=0.6)
    ax.set_axisbelow(True)
    finish(ax, xlabel="Cenik", ylabel="Letni račun skupnosti [EUR/a]", yfmt=EUR)
    pf.chart_frame(fig, f"Letni račun šestnajstih gospodinjstev, po shemi in ceniku — {battery}",
                   SUBTITLE, handles=[Patch(facecolor=SCHEME_COLOR[s], label=SCHEME_LABEL[s])
                                      for s in order], ncol=3)
    pf.show(fig, f"community_bill_by_scheme_{pf.slug(battery)}", layout="frame")