
# coding: utf-8

# Author: Daniel Yan
# 
# Date: 2018-07-16
# 
# Email: daniel.yan@vanderbilt.edu
# 
# Description:
# PCA on data to reduce to "n" components for TSNE. 
# 
# Command Line Arguments:
# First command line argument: Data file to transform. Include directory.
# Second command line argument: File to store transformed coordinates. Include directory.
# Third command line argument: File to store the PCA model. Include directory. Must be loaded again
#     using Scikit-learn joblib.load on same architecture.
# Fourth command line argument: File to store explained variance to. Include directory.
# Fifth command line argument: Integer number of components to reduce to.
# 
# Exception will be thrown if any arguments are missing or invalid.
# 
# 
# Data file format:
# The features to be transformed should be 6-mer counts in columns named "aaaaaa" to "tttttt". Each row should have a label in a column named "label"
# 
# Output file format:
# The transformed coordinates will be in columns 0 to "n-1" of the output file, and the labels will be in column "n" of the output file.

# In[ ]:


# Libaries
import pandas as pd # Data manipulation 
import sys # Command line arguments
import pca # Labeling components
from sklearn.decomposition import IncrementalPCA # Incremental PCA on large data set
from sklearn.externals import joblib # Save PCA model


# In[ ]:


if __name__ == "__main__"
    # Get data file to process
    data_file = sys.argv[1]
    # Get file to store transformed coordinates
    cords_file = sys.argv[2]
    # Get file to store PCA model to
    model_file = sys.argv[3]
    # Get file to store explained variances to
    variances_file = sys.argv[4]
    # Get number of components to reduce to using PCA
    n_components = sys.argb[5]
    
    # Load in data file
    print("Loading data file...")
    data_file = pd.read_table(data_file)

    # Get features used in PCA
    features_df = data_file.loc[:,"aaaaaa":"tttttt"]

    # Get labels
    labels_df = data_file.loc[:,"label"]
    
    # Create the PCA
    print("Creating PCA...")
    ipca = IncrementalPCA(n_components = n_components)
    features_transformed = ipca.fit_transform(features_df)

    # Label the transformed coordinates
    transformed_df = pca.label_coordinates(transformed_coordinates = features_transformed, 
                                           labels = labels_df)
    
    # Save the transformed coordinates
    print("Saving new coordinates...")
    transformed_df.to_csv(cords_file, sep = '\t', index = False)
    
    # Save the PCA model
    print("Saving PCA...")
    joblib.dump(ipca, model_file)
    
    # Save the explained variances
    print("Saving explained variance...")
    with open(variances_file) as file:
        count = 1
        sum = 0
        # Save the explained variance for each individual component
        for i in ipca.explained_variance_ratio_:
            file.write("Explained Variance Ratio for Component {}: {}%\n".format(count, i * 100))
            count += 1
            sum += i * 100
        # Save the combined explained variance from all components
        file.write("Total explained ratio: {}%\n".format(sum))

