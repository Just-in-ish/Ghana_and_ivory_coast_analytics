import pandas as pd
import matplotlib.pyplot as plt


file_path = "FAOSTAT_data_7-23-2022.csv"  # adjust if needed
data = pd.read_csv(file_path)


filtered = data[(data["Area"].isin(["Ghana", "Côte d'Ivoire"])) & (data["Item"] == "Cocoa, beans")]


pivoted = filtered.pivot_table(
    index=["Area", "Year"],
    columns="Element",
    values="Value"
).reset_index()

pivoted = pivoted.rename(columns={
    "Area harvested": "Area harvested",
    "Yield": "Yield",
    "Production": "Production"
})

ghana_table = pivoted[pivoted["Area"] == "Ghana"].sort_values("Year")
ivory_table = pivoted[pivoted["Area"] == "Côte d'Ivoire"].sort_values("Year")

fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Scatter plot: Ghana Yield by Year
axs[0, 0].scatter(ghana_table["Year"], ghana_table["Yield"], color="blue", alpha=0.7)
axs[0, 0].set_title("Ghana Yield by Year")
axs[0, 0].set_xlabel("Year")
axs[0, 0].set_ylabel("Yield (hg/ha)")
axs[0, 0].grid(True, linestyle="--", alpha=0.6)

# Scatter plot: Ivory Coast Yield by Year
axs[0, 1].scatter(ivory_table["Year"], ivory_table["Yield"], color="green", alpha=0.7)
axs[0, 1].set_title("Ivory Coast Yield by Year")
axs[0, 1].set_xlabel("Year")
axs[0, 1].set_ylabel("Yield (hg/ha)")
axs[0, 1].grid(True, linestyle="--", alpha=0.6)

# Bar chart: Ghana Area harvested
axs[1, 0].bar(ghana_table["Year"], ghana_table["Area harvested"], color="orange")
axs[1, 0].set_title("Ghana Area Harvested by Year")
axs[1, 0].set_xlabel("Year")
axs[1, 0].set_ylabel("Area harvested (ha)")
axs[1, 0].tick_params(axis="x", labelrotation=45)

axs[1, 1].bar(ivory_table["Year"], ivory_table["Area harvested"], color="red")
axs[1, 1].set_title("Ivory Coast Area Harvested by Year")
axs[1, 1].set_xlabel("Year")
axs[1, 1].set_ylabel("Area harvested (ha)")
axs[1, 1].tick_params(axis="x", labelrotation=45)

fig.suptitle("Cocoa Production in Ghana and Ivory Coast", fontsize=18, fontweight="bold")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Save as PDF
fig.savefig("cocoa_production.pdf")
plt.show()
