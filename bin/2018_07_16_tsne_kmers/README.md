# Modules
**pca.py**
Module for labeling data frame and creating scatter plots

**test_pca.py**
pytests for pca.py

# Programs
**pca_n_components.py**
pca on data to reduce to "n" components for tsne visualization. 


**tsne.py**
t-distributed stochastic neighbor embedding analysis on data reduced by pca_n_components.py/ipynb with scatter plot visualization. 


# .slurm files (for accre scheduler)
**pca_10_components.slurm**
accre job using pca_components.py to reduce data in

*/dors/capra_lab/users/yand1/te_ml/data/2018_07_13_pca_te_enhancers/hervs_enhancers_shuffled_features_matrix.tsv to 10 features for tsne using pca_n_components.py*

**pca_50_components.slurm**
accre job using pca_n_components.py to reduce data in 

*/dors/capra_lab/users/yand1/te_ml/data/2018_07_13_pca_te_enhancers/hervs_enhancers_shuffled_features_matrix.tsv to 50 features for tsne using pca_n_components.py*

**tsne_10.slurm**
accre job using tsne.py to create a tsne scatterplot visualization from the top 10 components 

**tsne_50.slurm**
accre job using tsne.py to create a tsne scatterplot visualization from the top 50 components
