pca.py is a module for an incremental principal component analysis that can also be run as a standlone script on HERVs, enhancers, and HERV-enhancer overlap from the data at /dors/capra_lab/users/yand1/te_ml/data/2018_07_03_pca_te_enhancers/combined_features_matrix.tsv this version allows user to specify axis coordinates.

pca.slurm is a slurm file to submit pca.py to the accre scheduler

format_shuffled_genome.py skeleton to finds the shuffled parts of the human genome within a features matrix. This version is uses an old directory structure and is currently unusable, but provides the bases for the similar file in the 2018_07_11_pca_te_enhancers folder.