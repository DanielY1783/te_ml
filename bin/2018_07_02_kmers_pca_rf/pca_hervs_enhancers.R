# Libaries
library("FactoMineR")
library("factoextra")

# Class constants
DIRECTORY <- "/dors/capra_lab/users/yand1/te_ml/"
DATA_FILE <- "test.tsv"
ENHANCER <- 4099 # Column showing enhancer overlap
CHROMOSOME <- 0 # Column of chromosome of HERV
START <- 1 # Column of start location of HERV
END <- 2 # Column of end location of HERV

# Read in input file as data frame.
hervs_df <- read.table(paste(DIRECTORY, "data/2018_06_29_kmers_enhancers_intersect/", DATA_FILE, sep = "")
                       ,header = TRUE)


# Save to png file
png_file_name <-
  paste(DIRECTORY, "results/2018_07_02_kmers_pca_rf/", "pca.png", sep = "")
png(
  filename = png_file_name
)

# Generate PCA, but leave out the enhancer column as classifier. Keep in 2 dimensions for graphing.
hervs_pca <- PCA(hervs_df[-c (ENHANCER, CHROMOSOME, START, END)], graph = FALSE, ncp = 2)
pca_graph <-fviz_pca_ind(hervs_pca,
                         geom.ind = "point", # Show points
                         col.ind = hervs_df$enhancer, # Color by presence or absence of enhancers.
                         legend.title = "Enhancer Overlap")
# Change color palette.
print(ggpubr::ggpar(pca_graph, palette = "rainbow")
      )
# Close png file
dev.off()