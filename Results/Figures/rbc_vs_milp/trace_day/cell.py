# Sliced on the LOCAL day. The Fluvius stamps carry a `Z` suffix but are
# Brussels-local, so a window cut on the raw index starts two hours off and the
# hour axis would wrap mid-chart.
_, days_sorted, _ = milp_module.day_calendar(trace_env.dataset.index[:trace_sig.n_steps])
day = np.asarray(trace_sig.day_steps[days_sorted.index(pd.Timestamp(TRACE_DAY).date())])
hours = trace_sig.local_hour[day]
assert np.all(np.diff(hours) > 0), "the local day did not come out monotone"

# Three stacked rows sharing the hour axis: one figure, because the point is
# that the same day drives all three.
fig, axes = plt.subplots(3, 1, figsize=pf.figsize(ratio=0.91), sharex=True,
                         gridspec_kw={"height_ratios": [1.0, 1.3, 1.3]})

# --- what the day costs ----------------------------------------------------
ax = axes[0]
ax.plot(hours, trace_sig.import_rate[day], lw=2, color=INK, label="import")
ax.plot(hours, trace_sig.export_credit[day], lw=2, color=MUTED, ls="--", label="export credit")
ax.margins(y=0.30)                       # headroom, so the legend never sits on a line
ax.legend(loc="upper left", ncols=2)
panel_label(ax, "The price signal every rule is deciding against")
ax.set_ylabel("EUR / kWh")

# --- the household ---------------------------------------------------------
ax = axes[1]
ax.fill_between(hours, 0, trace_sig.generation[day] / trace_sig.hours,
                color=pf.mix(FAMILY_COLOR["roof"], "#ffffff", 0.6), lw=0, label="PV")
ax.plot(hours, trace_sig.consumption[day] / trace_sig.hours, lw=2, color=INK, label="load")
ax.margins(y=0.30)
ax.set_ylim(bottom=0)                    # a negative kW here would be a drawing artefact
ax.legend(loc="upper left", ncols=2)
panel_label(ax, "The household the rules are controlling")
ax.set_ylabel("kW")

# --- where the charge sits -------------------------------------------------
ax = axes[2]
for name in POLICIES:
    ax.plot(hours, traces[name]["soc"][day], lw=2, color=controller_color(name),
            label=CONTROLLER_LABEL[name])
ax.plot(hours, traces["milp_full_period"]["soc"][day], lw=2.2, ls="--", color=INK,
        label=CONTROLLER_LABEL["milp_full_period"])
ax.set_ylim(0, TRACE_CAPACITY_KWH * 1.02)
ax.set_xticks(range(0, 25, 3))
panel_label(ax, "State of charge — dashed = perfect foresight")
ax.set_xlabel("hour of the local day")
ax.set_ylabel("kWh stored")

# Ten traces will not fit beside the data, so the keys go under the figure --
# chart_frame measures the rows they need before it lays the axes out.
pf.chart_frame(fig, f"One day on {TRACE_TARIFF}: what every rule sees and what it does",
               handles=ax.get_legend_handles_labels()[0], ncol=4)
pf.show(fig, "trace_day", layout="frame")