pca.py: Module for labeling data frame.

test_pca.py: Tests for pca.

pca_n_components.py: PCA on data to reduce to "n" components for TSNE. 
First command line argument: Data file to transform. Include directory.
Second command line argument: File to store transformed coordinates. Include directory.
Third command line argument: File to store the PCA model. Include directory. Must be loaded again using Scikit-learn joblib.load on same architecture.
Fourth command line argument: File to store explained variance to. Include directory.
Fifth command line argument: Integer number of components to reduce to.