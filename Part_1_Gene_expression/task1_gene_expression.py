# ======================================
# IMPORT LIBRARIES
# ======================================
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

sns.set(style="whitegrid")

# ======================================
# TASK 1a: HEATMAP (HBR vs UHR)
# ======================================

expr = pd.read_csv("Untitled spreadsheet - Sheet1 (2).csv", index_col=0)

scaler = StandardScaler()
scaled_expr = pd.DataFrame(
    scaler.fit_transform(expr),
    index=expr.index,
    columns=expr.columns
)

sns.clustermap(
    scaled_expr,
    cmap="Blues",
    figsize=(8, 6),
    linewidths=0.5
)

plt.suptitle(
    "Clustered Heatmap of Differentially Expressed Genes (HBR vs UHR)",
    y=1.05
)

plt.savefig("task1a_heatmap_HBR_UHR.png", dpi=300, bbox_inches="tight")
plt.show()


# ======================================
# TASK 1b: VOLCANO PLOT
# ======================================

deg = pd.read_csv("Untitled spreadsheet - Sheet1 (1).csv")

color_map = {"up": "green", "down": "orange", "ns": "grey"}
colors = deg["significance"].map(color_map)

plt.figure(figsize=(8, 6))
plt.scatter(
    deg["log2FoldChange"],
    deg["-log10PAdj"],
    c=colors,
    alpha=0.7
)

plt.axvline(1, linestyle="--", color="black")
plt.axvline(-1, linestyle="--", color="black")

plt.xlabel("log2FoldChange")
plt.ylabel("-log10(PAdj)")
plt.title("Volcano Plot of Differential Gene Expression")

plt.savefig("task1b_volcano_plot.png", dpi=300, bbox_inches="tight")
plt.show()
