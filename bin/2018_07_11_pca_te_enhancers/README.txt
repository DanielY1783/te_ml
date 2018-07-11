pca.py is a module used for incremental principal component analysis.

format_shuffled_genome.py finds the shuffled parts of the human genome within the features matrix from /dors/capra_lab/users/yand1/te_ml/data/2018_07_11_pca_te_enhancers/all_pairs_features_matrix.tsv
and normalize them by dividing by the number of base pairs. Store the new features matrix containing only information about shuffled parts of the human genome to a /dors/capra_lab/users/yand1/te_ml/data/2018_07_11_pca_te_enhancers/shuffled_features_matrix.tsv

shuffled_pca.py: Principal component analysis on HERVs, enhancers, intersection of HERVs and enhancers, and a control of random parts of the human genome using the pca.py module.