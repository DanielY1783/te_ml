# Libaries
library("FactoMineR")
library("factoextra")

# Class constants
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/"
DATE_DIR = "2018_06_29_kmers_enhancers_intersect/"
DATA_FILE = "reformatted_hervs_kmers_intersect_enhancers.tsv"

# Read in input file as data frame.
hervs_df = read.table(paste(DIRECTORY, "/data", DATE_DIR, DATA_FILE))

# Generate PCA, but leave out the enhancer column as classifier
