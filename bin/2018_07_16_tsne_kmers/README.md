## Libraries
### pca.py 
Module for labeling data frame.

### test_pca.py
pytests for pca.py

## Programs
### pca_n_components.py/ipynb
pca on data to reduce to "n" components for tsne visualization. 
###### Command Line Arguments
1. First command line argument: Data file to transform. Include directory and extension.
2. Second command line argument: File to store transformed coordinates. Include directory and extension.
3. Third command line argument: File to store the PCA model. Include directory and extension. Must be loaded again using Scikit-learn joblib.load on same architecture.
4. Fourth command line argument: File to store explained variance to. Include directory and extension.
5. Fifth command line argument: Integer number of components to reduce to.

Error will occur if any arguments are invalid
###### Preconditions: 
+ Data file must contain one column named "label" in the header that contains labels for the data. 
+ Columns for features must contain labels starting with *aaaaaa* and ending with *tttttt* 
+ Data file must not have indices for rows.
+ Data file should not contain missing data.
###### Postconditions:
+ Tab separated file with header and no indices will be saved at *arg2*
+ PCA model will be saved at *arg3*
+ Explained variance ratios for the *arg5* components will be saved to *arg4*

### tsne.py/ipynb
t-distributed stochastic neighbor embedding analysis on data reduced by pca_n_components.py/ipynb with scatter plot visualization. 
###### Command Line Arguments
1. First argument: Name of data file to read from. Include directory and extension.
2. Second argument: Name of file to store scatterplot to. Include directory, but leave out extension (will automatically be saved as .png).
3. Third argument: Name of file to store tsne model to. Include directory, but leave out extension (will automatically be saved as .pkl).
4. Fourth argument: Integer number of components to reduce to.

Error will result if any argument is invalid.
###### Preconditions: 
+ Data file must contain one column named "label" in the header that contains labels for the data. 
+ All other columns must contain features with numeric data. 
+ Data file must not have indices for rows.
+ Data file should not contain missing data.
###### Postconditions:
+ Scatter plot of tsne for all labels is saved at *arg1*.png
+ For each label, a scatterplot is saved at *arg1_label*.png
+ TSNE model is saved at *arg3*.pkl and must be loaded using scikit-learn joblib.load on a machine with the same architecture

## .slurm files (for accre scheduler)
### pca_10_components.slurm
accre job using pca_components.py to reduce data in */dors/capra_lab/users/yand1/te_ml/data/2018_07_13_pca_te_enhancers/hervs_enhancers_shuffled_features_matrix.tsv to 10 features for tsne using pca_n_components.py*

### pca_50_components.slurm
accre job using pca_n_components.py to reduce data in */dors/capra_lab/users/yand1/te_ml/data/2018_07_13_pca_te_enhancers/hervs_enhancers_shuffled_features_matrix.tsv to 50 features for tsne using pca_n_components.py*

### tsne_10.slurm
accre job using tsne.py to create a tsne scatterplot visualization from the top 10 components 

### tsne_50.slurm
accre job using tsne.py to create a tsne scatterplot visualization from the top 50 components