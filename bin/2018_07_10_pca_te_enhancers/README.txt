pca.py is a module for an incremental principal component analysis that can also be run as a standlone script on HERVs, enhancers, and HERV-enhancer overlap from the data at /dors/capra_lab/users/yand1/te_ml/data/2018_07_03_pca_te_enhancers/combined_features_matrix.tsv this version allows user to specify axis coordinates.

pca.slurm is a slurm file to submit pca.py to the accre scheduler

format_shuffled_genome.py finds the shuffled parts of the human genome within the features matrix from /dors/capra_lab/users/yand1/te_ml/data/2018_07_10_pca_te_enhancers/all_pairs_features_matrix.tsv
and normalize them by dividing by the number of base pairs. Store the new features matrix containing only information about shuffled parts of the human genome to a /dors/capra_lab/users/yand1/te_ml/data/2018_07_10_pca_te_enhancers/shuffled_features_matrix.tsv