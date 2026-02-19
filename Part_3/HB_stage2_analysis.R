# =========================
# LOAD LIBRARIES
# =========================
library(readxl)
library(ggplot2)
library(pheatmap)
library(igraph)
library(patchwork)
library(ggplotify)

# =========================
# READ EXCEL FILE
# =========================
data_a <- read_excel("HB_Stage_2.xlsx", sheet = "a")
data_b <- read_excel("HB_Stage_2.xlsx", sheet = "b")
data_c <- read_excel("HB_Stage_2.xlsx", sheet = "c")
data_d <- read_excel("HB_Stage_2.xlsx", sheet = "d_1")
data_e <- read_excel("HB_Stage_2.xlsx", sheet = "e")
data_f <- read_excel("HB_Stage_2.xlsx", sheet = "f")
data_g <- read_excel("HB_Stage_2.xlsx", sheet = "g")

# =========================
# TASK 1
# =========================
p1 <- ggplot(data_a, aes(x = cell_type, y = new_ratio, fill = cell_type)) +
  geom_boxplot() +
  theme_classic() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# =========================
# TASK 2
# =========================
data_b$log2_alpha <- log2(data_b$alpha)
data_b$log2_half_life <- log2(data_b$half_life)

cut_x <- median(data_b$log2_half_life, na.rm = TRUE)
cut_y <- median(data_b$log2_alpha, na.rm = TRUE)

p2 <- ggplot(data_b, aes(x = log2_half_life, y = log2_alpha)) +
  geom_point() +
  geom_vline(xintercept = cut_x, linetype = "dashed") +
  geom_hline(yintercept = cut_y, linetype = "dashed") +
  theme_classic()

# =========================
# TASK 3
# =========================
mat_c <- as.matrix(data_c[,-1])
rownames(mat_c) <- data_c[[1]]

heat_c <- pheatmap(mat_c, cluster_rows = TRUE, cluster_cols = FALSE, silent = TRUE)
p3 <- as.ggplot(heat_c)

# =========================
# TASK 4
# =========================
mat_d <- as.matrix(data_d[,-1])
rownames(mat_d) <- data_d[[1]]

heat_d <- pheatmap(mat_d, cluster_rows = FALSE, cluster_cols = FALSE,
                   color = colorRampPalette(c("blue", "white", "red"))(50),
                   silent = TRUE)

p4 <- as.ggplot(heat_d)

# =========================
# TASK 5
# =========================
p5 <- ggplot(data_e, aes(x = half_life, y = alpha, color = stage, size = count)) +
  geom_point() +
  theme_classic()

# =========================
# TASK 6
# =========================
data_f_sub <- subset(data_f, stage %in% c("s00h", "s72h"))

p6 <- ggplot(data_f_sub, aes(x = stage, y = proportion, fill = cell_type)) +
  geom_bar(stat = "identity") +
  ylim(0, 0.3) +
  theme_classic()






# =========================
# FINAL ASSEMBLY
# =========================
final_plot <- (p1 | p2 | p3) /
  (p4 | p5 | p6)

final_plot

ggsave("HB_stage2_final_plot.png",
       plot = final_plot,
       width = 12,
       height = 8,
       dpi = 300)

