import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = "data/FAOSTAT_data_7-23-2022.csv"
data = pd.read_csv(file_path)

# Filter for Ghana and Ivory Coast cocoa beans
filtered = data[
    (data["Area"].isin(["Ghana", "Côte d'Ivoire"])) &
    (data["Item"] == "Cocoa, beans")
]

# Pivot to get Year, Area harvested, Yield, Production
pivoted = filtered.pivot_table(
    index=["Area", "Year"],
    columns="Element",
    values="Value"
).reset_index()

# Two separate tables
ghana_table = pivoted[pivoted["Area"] == "Ghana"].sort_values("Year")
ivory_table = pivoted[pivoted["Area"] == "Côte d'Ivoire"].sort_values("Year")

# -------------------------------
# Step 1: Ghana Yield scatter
plt.figure(figsize=(7,5))
plt.scatter(ghana_table["Year"], ghana_table["Yield"], color="blue", alpha=0.7)
plt.title("Ghana Yield by Year")
plt.xlabel("Year")
plt.ylabel("Yield (hg/ha)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

# Step 2: Ivory Coast Yield scatter
plt.figure(figsize=(7,5))
plt.scatter(ivory_table["Year"], ivory_table["Yield"], color="green", alpha=0.7)
plt.title("Ivory Coast Yield by Year")
plt.xlabel("Year")
plt.ylabel("Yield (hg/ha)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

# Step 3: Ghana Area harvested bar chart
plt.figure(figsize=(7,5))
plt.bar(ghana_table["Year"], ghana_table["Area harvested"], color="orange")
plt.title("Ghana Area Harvested by Year")
plt.xlabel("Year")
plt.ylabel("Area harvested (ha)")
plt.xticks(rotation=45)
plt.show()

# Step 4: Ivory Coast Area harvested bar chart
plt.figure(figsize=(7,5))
plt.bar(ivory_table["Year"], ivory_table["Area harvested"], color="red")
plt.title("Ivory Coast Area Harvested by Year")
plt.xlabel("Year")
plt.ylabel("Area harvested (ha)")
plt.xticks(rotation=45)
plt.show()

# -------------------------------
# Step 5: Combine all plots into one figure with 4 panels
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Ghana Yield
axs[0, 0].scatter(ghana_table["Year"], ghana_table["Yield"], color="blue", alpha=0.7)
axs[0, 0].set_title("Ghana Yield by Year")
axs[0, 0].set_xlabel("Year")
axs[0, 0].set_ylabel("Yield (hg/ha)")
axs[0, 0].grid(True, linestyle="--", alpha=0.6)

# Ivory Coast Yield
axs[0, 1].scatter(ivory_table["Year"], ivory_table["Yield"], color="green", alpha=0.7)
axs[0, 1].set_title("Ivory Coast Yield by Year")
axs[0, 1].set_xlabel("Year")
axs[0, 1].set_ylabel("Yield (hg/ha)")
axs[0, 1].grid(True, linestyle="--", alpha=0.6)

# Ghana Area harvested
axs[1, 0].bar(ghana_table["Year"], ghana_table["Area harvested"], color="orange")
axs[1, 0].set_title("Ghana Area Harvested by Year")
axs[1, 0].set_xlabel("Year")
axs[1, 0].set_ylabel("Area harvested (ha)")
axs[1, 0].tick_params(axis="x", labelrotation=45)

# Ivory Coast Area harvested
axs[1, 1].bar(ivory_table["Year"], ivory_table["Area harvested"], color="red")
axs[1, 1].set_title("Ivory Coast Area Harvested by Year")
axs[1, 1].set_xlabel("Year")
axs[1, 1].set_ylabel("Area harvested (ha)")
axs[1, 1].tick_params(axis="x", labelrotation=45)

# Overall title
fig.suptitle("Cocoa Production in Ghana and Ivory Coast", fontsize=18, fontweight="bold")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Save and show
fig.savefig("cocoa_production.pdf")
plt.show()
