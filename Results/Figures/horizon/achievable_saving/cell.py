### What one point of gap is worth: the achievable saving on each list
fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.36))

vals = [achievable[t] for t in TARIFFS_READY]
ypos = np.arange(len(TARIFFS_READY))[::-1]

ax.barh(ypos, vals, height=0.62, color=[TARIFF_COLOR[t] for t in TARIFFS_READY])
for y, v in zip(ypos, vals):
    ax.annotate(f"{v:,.0f} EUR/a", xy=(v, y), xytext=(7, 0), textcoords="offset points",
                va="center", color=INK, fontsize=9, fontweight="semibold")

ax.set_yticks(ypos, TARIFFS_READY)
ax.set_xlim(0, max(vals) * 1.28)
finish(ax, title="Imenovalec vseh spodnjih odstotkov",
       xlabel="Prihranek celoletnega optimuma glede na isto gospodinjstvo brez baterije [EUR/a]")
ax.grid(axis="y", visible=False)
pf.show(fig, "achievable_saving")