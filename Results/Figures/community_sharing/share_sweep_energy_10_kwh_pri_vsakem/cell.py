### What souporaba throws away, and community self-supply does not
SUBTITLE = ("Polna črta = energija, ki jo je prejemnik dejansko porabil. Senčeno = "
            "prenesena energija, ki je prejemnik v istem 15-minutnem intervalu ni mogel "
            "porabiti; pri souporabi propade in se ne prenese naprej, pri skupnostni "
            "samooskrbi se vrne v odkup proizvajalca.")

for battery in SWEEP_BATTERIES:
    fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.50))
    handles = []
    for scheme in (ccm.SCHEME_SOUPORABA, ccm.SCHEME_SKUPNOST):
        sub = sweep[(sweep["battery"] == battery) & (sweep["scheme"] == scheme)
                    ].sort_values("share")
        color = SCHEME_COLOR[scheme]
        ax.plot(sub["share"], sub["Shared_kWh"], color=color, linewidth=2.0, zorder=3)
        handles.append(plt.Line2D([], [], color=color, lw=2.0,
                                  label=f"{SCHEME_LABEL[scheme]} — porabljeno"))
        if sub["Wasted_kWh"].abs().max() > 1.0:
            ax.fill_between(sub["share"], sub["Shared_kWh"],
                            sub["Shared_kWh"] + sub["Wasted_kWh"], color=color, alpha=0.16,
                            linewidth=0, zorder=2)
            handles.append(Patch(facecolor=color, alpha=0.16,
                                 label=f"{SCHEME_LABEL[scheme]} — propade"))
    ax.axhline(SHARING_CEILING_KWH, color=MUTED, linestyle=":", linewidth=1.0)
    ax.annotate("sočasna zgornja meja (brez hrambe)", (0.02, SHARING_CEILING_KWH),
                xytext=(0, 4), textcoords="offset points", color=MUTED, fontsize=8)
    ax.grid(axis="y", linewidth=0.6)
    ax.set_axisbelow(True)
    finish(ax, xlabel="Pogodbeni delež deljene energije", ylabel="Energija [kWh/a]",
           yfmt=PLAIN, xfmt=SHARE)
    pf.chart_frame(fig, f"Koliko energije shema res prestavi — {battery}", SUBTITLE,
                   handles=handles, ncol=2)
    pf.show(fig, f"share_sweep_energy_{pf.slug(battery)}", layout="frame")