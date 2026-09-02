### Community net-import duration curve, against the same year with no batteries
ZOOM_HOURS = 800
interval_hours = 24.0 / cs.STEPS_PER_DAY

# The full curve and its top-hours zoom are two figures, not two panels: the
# zoom is a second reading of the same axis and each needs the full width.
# The baseline is a reference, not a fifth scenario, so it is drawn underneath
# in ink. One curve covers all four scenarios (asserted in section 4).
base_sorted = np.sort(BASE_PROFILE["community_import_kw"].to_numpy(dtype=float))[::-1]
base_hours = (np.arange(len(base_sorted)) + 1) * interval_hours


def duration_curves(ax):
    """The baseline and the four scenarios, sorted descending, on one axes."""
    ax.plot(base_hours, base_sorted, color=MUTED, linewidth=3.2, zorder=1,
            label="brez baterij (enako v vseh scenarijih)")
    for scenario in SCEN_ORDER:
        profile = RESULTS[scenario]["community_profile"]["community_import_kw"]
        sorted_kw = np.sort(profile.to_numpy(dtype=float))[::-1]
        hours = (np.arange(len(sorted_kw)) + 1) * interval_hours
        # Souporaba runs the dinamicni dispatch, so its curve lies on top of it.
        ax.plot(hours, sorted_kw,
                color=SCEN_COLOR[scenario], linewidth=2, zorder=2,
                linestyle="--" if scenario == "souporaba" else "-",
                label=LABEL[scenario] + (" (= Dinamicni)" if scenario == "souporaba" else ""))
    return ax


fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.46))
duration_curves(ax)
ax.set_xlim(0, 8784)
ax.set_xticks(np.arange(0, 8785, 2000))
ax.legend(loc="upper right")
finish(ax, title="Kako pogosto skupnost odjema kolikšno moč",
       subtitle="neto odjem vseh 50 gospodinjstev, urejen padajoče; siva je leto brez baterij",
       xlabel="ur na leto pri tej moči ali več", ylabel="kW")
pf.show(fig, "import_duration_curve")

fig, axz = plt.subplots(figsize=pf.figsize(ratio=0.46))
duration_curves(axz)
peak_row = TOTALS.loc[TOTALS["Community_Peak_kW"].idxmax()]
axz.annotate(f"konica {peak_row['Community_Peak_kW']:.0f} kW, {peak_row['Scenario']}",
             (0, peak_row["Community_Peak_kW"]), xytext=(22, -16),
             textcoords="offset points", color=INK, fontsize=9)
axz.annotate(f"brez baterij {base_sorted[0]:.0f} kW",
             (0, base_sorted[0]), xytext=(22, -14),
             textcoords="offset points", color=MUTED, fontsize=9)

axz.set_xlim(0, ZOOM_HOURS)
axz.set_xticks(np.arange(0, ZOOM_HOURS + 1, 200))
axz.legend(loc="upper right")
finish(axz, title=f"Najvišjih {ZOOM_HOURS} ur, kjer se scenariji razidejo",
       xlabel="ur na leto pri tej moči ali več", ylabel="kW")
pf.show(fig, "import_duration_curve_zoom")

# The power exceeded 1, 10, 100 and 800 hours a year.
top_hours = [1, 10, 100, ZOOM_HOURS]

def top_of_curve(sorted_kw, label):
    return {"Scenario": label,
            **{f"presežena {h} h [kW]": sorted_kw[int(h / interval_hours) - 1]
               for h in top_hours}}

rows = [top_of_curve(
    np.sort(RESULTS[s]["community_profile"]["community_import_kw"].to_numpy(dtype=float))[::-1],
    LABEL[s],
) for s in SCEN_ORDER]
rows.append(top_of_curve(base_sorted, "Brez baterij"))
pd.DataFrame(rows).round(1)