### Aging: how the cycle limit's bite depends on battery size illustrative

cap_life = df_sizing.loc[df_sizing["Capacity_kWh"] > 0, "Capacity_kWh"].to_numpy()
efc_life = df_sizing.loc[df_sizing["Capacity_kWh"] > 0, "Equivalent_Full_Cycles"].to_numpy()
cycle_life_y = np.where(efc_life > 0, BATTERY_CYCLE_LIMIT_EFC / efc_life, np.inf)
service_life_y = np.minimum(cycle_life_y, BATTERY_LIFETIME_YEARS)

finite_cycle_life = cycle_life_y[np.isfinite(cycle_life_y)]
y_top = max(
    BATTERY_LIFETIME_YEARS,
    np.percentile(finite_cycle_life, 90) if finite_cycle_life.size else BATTERY_LIFETIME_YEARS,
) * 1.15

fig, ax = plt.subplots()
ax.plot(cap_life, cycle_life_y, color=MUTED, lw=1.3, ls=":", marker="o", ms=4,
        mfc=SURFACE, mew=1.4, label="samo cikli (EFC limit)")
ax.axhline(BATTERY_LIFETIME_YEARS, color=MUTED, lw=1.3, ls="--", label="samo starost (koledarsko)")
ax.plot(cap_life, service_life_y, color=SERIES[2], lw=2.4,
        label="dejanska življenjska doba (nižje od obeh)")

size_C_life = float(np.interp(size_C, cap_life, service_life_y))
ax.scatter([size_C], [size_C_life], color=INK_2, zorder=5, s=45)
ax.annotate(f"scenarij C: {size_C:g} kWh -> {size_C_life:.1f} let",
            xy=(size_C, size_C_life), xytext=(8, -14), textcoords="offset points")

ax.set_ylim(0, y_top)
finish(ax, title="Kako velikost baterije premakne konec življenjske dobe",
       xlabel="Kapaciteta baterije [kWh]", ylabel="Življenjska doba [let]", yfmt=YEARS)
ax.legend(loc="lower right")
pf.show(fig, "service_life")

crossover = cap_life[cycle_life_y >= BATTERY_LIFETIME_YEARS]
if len(crossover):
    print(f"Nad {crossover.min():.1f} kWh cikli ne omejujejo več -- prevzame koledarska "
          f"starost ({BATTERY_LIFETIME_YEARS:.0f} let).")
else:
    print(f"V celotnem prikazanem razponu velikosti cikli omejujejo pred koledarskim "
          f"staranjem ({BATTERY_LIFETIME_YEARS:.0f} let).")