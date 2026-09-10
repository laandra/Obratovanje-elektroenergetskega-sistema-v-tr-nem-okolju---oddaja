### Souporaba: shared energy used vs forfeited, by month
monthly = RESULTS["souporaba"]["monthly"]
recv = monthly[monthly["role"] == "prejemnik"].groupby("month")[
    ["deljeno_kwh", "neizrabljeno_kwh"]
].sum()

fig, ax = plt.subplots(figsize=pf.figsize(ratio=0.49))
ax.bar(recv.index, recv["deljeno_kwh"], width=0.68, color=SERIES[0],
       edgecolor=SURFACE, linewidth=2, label="porabijo prejemniki")
ax.bar(recv.index, recv["neizrabljeno_kwh"], bottom=recv["deljeno_kwh"], width=0.68,
       color=BLUES[1], edgecolor=SURFACE, linewidth=2, label="neizrabljeno")

share = 100 * recv["neizrabljeno_kwh"] / (recv["deljeno_kwh"] + recv["neizrabljeno_kwh"])
for m, pct in share.items():
    total = recv.loc[m].sum()
    ax.annotate(f"{pct:.0f}%", (m, total), xytext=(0, 5), textcoords="offset points",
                ha="center", fontsize=9, color=INK_2)

ax.set_xticks(range(1, 13))
ax.legend(ncol=2, loc="upper left")
finish(ax, title="Koliko deljene energije dejansko pride do prejemnikov",
       subtitle="oznaka je delež neizrabljene energije",
       xlabel="Mesec", ylabel="Deljena energija [kWh]")
pf.show(fig, "souporaba_shared_vs_forfeited")