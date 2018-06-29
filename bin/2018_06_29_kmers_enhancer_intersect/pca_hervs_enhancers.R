# Libaries
library("FactoMineR")
library("factoextra")

# Class constants
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/"
DATE_DIR = "2018_06_29_kmers_enhancers_intersect/"
DATA_FILE = "reformatted_hervs_kmers_intersect_enhancers.tsv"
ENHANCER = 4099 # Column showing enhancer overlap

# Read in input file as data frame.
hervs_df = read.table(paste(DIRECTORY, "/data", DATE_DIR, DATA_FILE, sep = ""))

# Save to png file
png_file_name <-
  paste(DIRECTORY, "/data", DATE_DIR, "pca.png", sep = "")
png(
  filename = png_file_name,
  width = 100,
  height = 100,
  res = 100
)

# Generate PCA, but leave out the enhancer column as classifier. Keep in 2 dimensions for graphing.
hervs_pca <- PCA(hervs_df[,-ENHANCER], graph = FALSE, ncp = 2)
print(fviz_pca_ind(hervs_pca,
             geom.ind = "point", # Show points
             col.ind = hervs_df$enhancer, # Color by presence or absence of enhancers.
             legend.title = "Enhancer Overlap"
             )
)
# Close png file
dev.off()