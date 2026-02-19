# ======================================
# TASK 2: BREAST CANCER DATA VISUALIZATION
# ======================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

# Load dataset
bc = pd.read_csv("Untitled spreadsheet - Sheet1.csv")

# --------------------------------------
# 2a. Scatter plot: Radius vs Texture
# --------------------------------------

sns.scatterplot(
    data=bc,
    x="radius_mean",
    y="texture_mean",
    hue="diagnosis"
)

plt.title("Radius Mean vs Texture Mean by Diagnosis")
plt.xlabel("Radius Mean")
plt.ylabel("Texture Mean")

plt.savefig("task2_scatter_radius_texture.png", dpi=300, bbox_inches="tight")
plt.show()

# --------------------------------------
# 2b. Correlation heatmap
# --------------------------------------

features = [
    "radius_mean",
    "texture_mean",
    "perimeter_mean",
    "area_mean",
    "smoothness_mean",
    "compactness_mean"
]

corr = bc[features].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Heatmap of Breast Cancer Features")

plt.savefig("task2_correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()

# --------------------------------------
# TASK 2c: SCATTER (Radius vs Texture)

plt.figure(figsize=(6, 5))  # <-- goes FIRST

sns.scatterplot(
    data=bc,
    x="radius_mean",
    y="texture_mean",
    hue="diagnosis"
)

plt.xlabel("Radius Mean")
plt.ylabel("Texture Mean")
plt.title("Texture Mean vs Radius Mean by Diagnosis")
plt.grid(True)

plt.savefig("task2_scatter_radius_texture.png", dpi=300, bbox_inches="tight")
plt.close()  # <-- goes LAST

# --------------------------------------
# 2d. Density plot: Area Mean
# --------------------------------------

sns.kdeplot(
    data=bc[bc["diagnosis"] == "M"],
    x="area_mean",
    fill=True,
    label="Malignant"
)

sns.kdeplot(
    data=bc[bc["diagnosis"] == "B"],
    x="area_mean",
    fill=True,
    label="Benign"
)

plt.title("Density Plot of Area Mean by Diagnosis")
plt.xlabel("Area Mean")
plt.ylabel("Density")
plt.legend()

plt.savefig("task2_density_area_mean.png", dpi=300, bbox_inches="tight")
plt.show()
