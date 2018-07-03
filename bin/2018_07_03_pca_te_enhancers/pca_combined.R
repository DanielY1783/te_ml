# Libaries
.libPaths("~/R/rlib-3.4.3") # Pick up installed libraries on ACCRE
library("FactoMineR")
library("factoextra")

# Class constants
DIRECTORY <- "/dors/capra_lab/users/yand1/te_ml/"
DATA_FILE <- "combined_features_matrix.tsv"
CHROMOSOME <- 0 # Column of chromosome of HERV
START <- 1 # Column of start location of HERV
END <- 2 # Column of end location of HERV
LABEL <- 3 # Column labeling as HERV, enhancer, or HERV_enhancer overlap
PAIRS <- 4 # Column with base pairs

# Read in input file as data frame.
hervs_df <- read.table(paste(DIRECTORY, "data/2018_07_03_pca_te_enhancers/", DATA_FILE, sep = "")
                       ,header = TRUE)


# Save to png file
png_file_name <-
  paste(DIRECTORY, "results/2018_07_03_pca_te_enhancers/", "pca.png", sep = "")
# Use type as cairo to avoid X11 display error
png(
  filename = png_file_name, type = "cairo"
)

# Generate PCA, but leave out the enhancer column as classifier. Keep in 2 dimensions for graphing.
pca_hervs_enhancers <- PCA(hervs_df[-c (CHROMOSOME, START, END, LABEL, PAIRS)], graph = FALSE, ncp = 2)
pca_graph <-fviz_pca_ind(pca_hervs_enhancers,
                         geom.ind = "point", # Show points
                         col.ind = hervs_df$enhancer, # Color by presence or absence of enhancers.
                         legend.title = "Enhancer Overlap")
# Change color palette.
print(ggpubr::ggpar(pca_graph, palette = "rainbow")
      )
# Close png file
dev.off()
