pca.py: Module for labeling data frame.

test_pca.py: Tests for pca.

pca_n_components.py: pca on data to reduce to "n" components for tsne visualization. 
First command line argument: Data file to transform. Include directory.
Second command line argument: File to store transformed coordinates. Include directory.
Third command line argument: File to store the PCA model. Include directory. Must be loaded again using Scikit-learn joblib.load on same architecture.
Fourth command line argument: File to store explained variance to. Include directory.
Fifth command line argument: Integer number of components to reduce to.

pca_10_components.slurm: accre job to reduce data in /dors/capra_lab/users/yand1/te_ml/data/2018_07_13_pca_te_enhancers/hervs_enhancers_shuffled_features_matrix.tsv to 10 features for tsne.

pca_50_components.slurm: accre job to reduce data in /dors/capra_lab/users/yand1/te_ml/data/2018_07_13_pca_te_enhancers/hervs_enhancers_shuffled_features_matrix.tsv to 50 features for tsne.