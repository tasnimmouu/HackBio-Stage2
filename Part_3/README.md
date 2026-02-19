# Part 3 – Figure Reproduction and Conceptual Analysis

This section reproduces Figure 2 panels (a–g) from the provided dataset (hb_stage_2.xlsx) and includes reasoning behind each conceptual check.

---

## Task 0 – Orientation and Data Hygiene

- Downloaded and inspected the Excel file (hb_stage_2.xlsx).
- Identified Figure 2 panels (a–g) from the source paper.
- Mapped sheets to panels:
  - Sheet a → Panel 2a
  - Sheet b → Panel 2b
  - Sheet c → Panel 2c
  - Sheet d_1 → Panel 2d
  - Sheet e → Panel 2e
  - Sheet f → Panel 2f
  - Sheet g → Panel 2g
- Installed required packages:
  - readxl
  - ggplot2
  - pheatmap
  - igraph
- Checked column names and data structure before analysis.

---

## Task 1 – Panel 2a: Cell-type Ratio Distributions

- Created boxplot of `new_ratio` grouped by `cell_type`.
- Matched orientation (rotated labels).
- Preserved outliers and relative scaling.

**Concept:** Compare immune cell-type distribution differences.

---

## Task 2 – Panel 2b: Half-life vs Alpha-life Scatter

- Plotted log2(half_life) vs log2(alpha).
- Added vertical and horizontal cutoffs.
- Highlighted gene subsets.
- Labeled exemplar genes (Camp, Ccr2).

**Conceptual Checks:**
- Log2 used to stabilize variance and interpret fold changes.
- Quadrants represent different kinetic regimes.

---

## Task 3 – Panel 2c: Heatmap (Cell Type × Time)

- Converted data to matrix.
- Added column annotations (CellType, Time).
- Clustered rows only (genes).
- Did not cluster columns (time order preserved).

**Concept:** Identify temporal expression structure.

---

## Task 4 – Panel 2d: Pathway Enrichment Heatmap

- Used pathway names as row names.
- No clustering applied.
- Used diverging color scale centered at zero.

**Conceptual Checks:**
- No clustering because pathway order is meaningful.
- Diverging palette shows up vs down regulation clearly.

---

## Task 5 – Panel 2e: Bubble Plot of Kinetic Regimes

- Scatter plot:
  - x = half_life
  - y = alpha
  - color = stage
  - size = count
- Included two legends (stage and count).

**Concept:** Show count-weighted kinetic behavior.

---

## Task 6 – Panel 2f: Stacked Proportions

- Subset to s00h and s72h.
- Stacked barplot of B vs Plasma proportions.
- Fixed y-axis (0–0.3).

**Conceptual Check:**
- Stacked view emphasizes proportional change over time.

---

## Task 7 – Panel 2g: Directed Cell–Cell Interaction Network

- Converted data to adjacency matrix.
- Built directed graph.
- Removed zero-weight edges.
- Edge size proportional to weight.
- Used force-directed layout.

**Conceptual Checks:**
- Directed edges show communication direction.
- Edge weight represents interaction strength.

---

## Final Assembly

All panels arranged into a single figure with:
- Consistent color usage
- Clear labels
- No clipping
- Exported as publication-quality PNG/PDF
