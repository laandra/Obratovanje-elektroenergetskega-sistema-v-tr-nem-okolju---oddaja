### What the samooskrba shelf costs: against the whole supply shelf, and per supplier
# A difference between two contracts for the same household, so it is computed
# per household and then averaged, never as a difference of two group means.
cat_all = df_cat_all.assign(Catalogue=[catalogue_of(o) for o in df_cat_all["Option"]])
best_supply = (cat_all[cat_all["Catalogue"] == "dobava"]
               .groupby(["Dataset", "Household"])["Cost_EUR"].min())
samo = cat_all[cat_all["Catalogue"] == "samooskrba"].copy()
samo["Premium_EUR"] = samo["Cost_EUR"] - samo.set_index(
    ["Dataset", "Household"]).index.map(best_supply)
premium_by_group = (samo.pivot_table(index="Option", columns="Dataset",
                                     values="Premium_EUR")
                    .reindex([o for o in cat_summary["all"].index
                              if catalogue_of(o) == "samooskrba"]))

# Per supplier, on the households held to this choice: the cheapest thing it will
# sell a roof against the cheapest thing it would sell the same house without
# one. A comparison of shelves, best offer against best offer.
pv_summary_cat = cat_summary["with PV"]
supplier_rows = []
for supplier in sorted(pv_summary_cat["Supplier"].unique()):
    shelf = pv_summary_cat[pv_summary_cat["Supplier"] == supplier]
    dobava = shelf[shelf["Catalogue"] == "dobava"]
    samoo = shelf[shelf["Catalogue"] == "samooskrba"]
    supplier_rows.append({
        "Supplier": supplier,
        "Dobava_Option": dobava.index[0] if len(dobava) else None,
        "Dobava_EUR": float(dobava["Cost_EUR"].iloc[0]) if len(dobava) else np.nan,
        "Samooskrba_Option": samoo.index[0] if len(samoo) else None,
        "Samooskrba_EUR": float(samoo["Cost_EUR"].iloc[0]) if len(samoo) else np.nan,
        "Lists_Dobava": len(dobava), "Lists_Samooskrba": len(samoo),
    })
supplier_premium = pd.DataFrame(supplier_rows).set_index("Supplier")
supplier_premium["Premium_EUR"] = (supplier_premium["Samooskrba_EUR"]
                                   - supplier_premium["Dobava_EUR"])
supplier_premium = supplier_premium.sort_values("Premium_EUR", na_position="last")

# --- one row per supplier, one dot per shelf ---------------------------------
# A dumbbell, as in chapter 4: the finding is the distance between two contracts
# for the same household.
fig, ax = plt.subplots(figsize=pf.figsize(
    ratio=rows_ratio(len(supplier_premium), per_row=0.66, floor=3.6)))
ypos = np.arange(len(supplier_premium))[::-1]
bills = supplier_premium[["Dobava_EUR", "Samooskrba_EUR"]].to_numpy()
lo_x, hi_x = float(np.nanmin(bills)), float(np.nanmax(bills))
span = hi_x - lo_x
for y, (supplier, row) in zip(ypos, supplier_premium.iterrows()):
    dob, sam = row["Dobava_EUR"], row["Samooskrba_EUR"]
    ax.plot(dob, y, marker="o", ms=11, color=CATALOGUE_COLOR["dobava"],
            mec=SURFACE, mew=2.0, zorder=3)
    if np.isnan(sam):
        # A supplier with no samooskrba list is a closed door, not a zero
        # premium: one dot, said in words rather than drawn as a gap.
        ax.text(dob + span * 0.03, y, f"{dob:.0f}    ni samooskrbnega cenika",
                va="center", ha="left", fontsize=8.5, color=MUTED, style="italic")
        continue
    ax.plot([dob, sam], [y, y], color=MUTED, lw=2.0, zorder=1,
            solid_capstyle="round")
    ax.plot(sam, y, marker="o", ms=11, color=CATALOGUE_COLOR["samooskrba"],
            mec=SURFACE, mew=2.0, zorder=3)
    left, right = min(dob, sam), max(dob, sam)
    ax.text(left - span * 0.025, y, f"{left:.0f}", va="center", ha="right",
            fontsize=8.5, color=INK_2)
    ax.text(right + span * 0.025, y, f"{right:.0f}", va="center", ha="left",
            fontsize=8.5, color=INK_2)
    ax.text((dob + sam) / 2, y + 0.16, f"{row['Premium_EUR']:+.0f}",
            va="bottom", ha="center", fontsize=9.5, color=INK,
            fontweight="semibold")
# Which two lists a row compares belongs in the row label: at 20 EUR/a apart the
# two names would overlap under the dots.
ax.set_yticks(ypos, [
    f"{supplier_label(s)}\ndobava: {short_list_name(r['Dobava_Option'])}\n"
    + (f"samooskrba: {short_list_name(r['Samooskrba_Option'])}"
       if pd.notna(r["Samooskrba_Option"]) else "samooskrba: ni cenika")
    for s, r in supplier_premium.iterrows()], fontsize=8)
ax.set_xlim(lo_x - span * 0.22, hi_x + span * 0.30)
ax.set_ylim(-0.75, len(supplier_premium) - 0.35)
finish(ax, title="Najboljša ponudba istega dobavitelja, s samooskrbo in brez",
       xlabel="Letni račun s PV, brez odkupa [EUR/a]")
ax.grid(axis="x")
ax.spines["left"].set_visible(False)
key_below(ax,
          [plt.Line2D([], [], marker="o", ls="", ms=10, mec=SURFACE, mew=2.0,
                      color=CATALOGUE_COLOR[c]) for c in CATALOGUE_ORDER],
          ["najcenejši cenik za dobavo", "najcenejši samooskrbni cenik"], ncol=2)
pf.show(fig, "catalogue_premium_by_supplier")

# --- the premium itself, per option and per household type -------------------
# A signed quantity with a meaningful zero, so the one diverging scale here:
# purple where the supply shelf wins, green where this samooskrba list beats
# everything on it, neutral at the tie. `TwoSlopeNorm` keeps the zero on the
# neutral colour, the negative side being too small for a symmetric scale.
fig, ax = plt.subplots(figsize=pf.figsize(
    ratio=rows_ratio(len(premium_by_group), per_row=0.30)))
values = premium_by_group.to_numpy()
diverging = LinearSegmentedColormap.from_list("catalogue_div", [
    pf.mix(CATALOGUE_COLOR["samooskrba"], "#0b0b0b", 0.30),
    CATALOGUE_COLOR["samooskrba"],
    pf.mix(CATALOGUE_COLOR["samooskrba"], "#ffffff", 0.72),
    "#f0efec",
    pf.mix(CATALOGUE_COLOR["dobava"], "#ffffff", 0.72),
    CATALOGUE_COLOR["dobava"],
    pf.mix(CATALOGUE_COLOR["dobava"], "#0b0b0b", 0.30)])
norm = TwoSlopeNorm(vmin=float(np.nanmin(values)), vcenter=0.0,
                    vmax=float(np.nanmax(values)))
im = ax.imshow(values, cmap=diverging, norm=norm, aspect="auto")
ax.set_xticks(range(premium_by_group.shape[1]),
              [group_label(c) for c in premium_by_group.columns],
              rotation=30, ha="right", fontsize=8)
ax.set_yticks(range(premium_by_group.shape[0]),
              [short_list_name(o) for o in premium_by_group.index], fontsize=8)
ax.grid(False)
for r in range(values.shape[0]):
    for c in range(values.shape[1]):
        strong = norm(values[r, c]) > 0.86 or norm(values[r, c]) < 0.14
        ax.text(c, r, f"{values[r, c]:+.0f}", ha="center", va="center",
                fontsize=7.5, color="#ffffff" if strong else INK)
finish(ax, title="Koliko dražji je samooskrbni cenik od najcenejšega cenika za dobavo "
                 "[EUR/a]")
fig.colorbar(im, ax=ax, fraction=0.045, pad=0.02,
             label="EUR/a  (zeleno: samooskrba cenejša)")
pf.show(fig, "catalogue_premium_by_group")

supplier_premium[["Dobava_EUR", "Samooskrba_EUR", "Premium_EUR",
                  "Lists_Dobava", "Lists_Samooskrba"]].rename(
    index=supplier_label).rename(columns={
    "Dobava_EUR": "najcenejša dobava [EUR/a]",
    "Samooskrba_EUR": "najcenejša samooskrba [EUR/a]",
    "Premium_EUR": "razlika [EUR/a]",
    "Lists_Dobava": "cenikov za dobavo",
    "Lists_Samooskrba": "samooskrbnih cenikov",
}).round(2)