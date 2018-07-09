
# coding: utf-8

# Performs a principal component analysis on two components and graphs the results. Data is at:
# /dors/capra_lab/users/yand1/te_ml/data/2018_07_03_pca_te_enhancers/combined_features_matrix.tsv

# In[1]:


# Libaries
from sklearn.decomposition import PCA, IncrementalPCA
import numpy as np
import matplotlib
matplotlib.use("Agg") # Avoid display error
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


# Class Constants
N_COMPONENTS = 2 # Number of principal components to keep
BATCH_SIZE = None # Size of incremental pca batch to control for memory usage. Can be int or None.
FIRST_KMER = "aaaaaa" # kmer in lowest column value
LAST_KMER = "tttttt" # kmer in highest column value
COLORS = ['navy', 'turquoise', 'red'] # Colors for scatter plot


# In[3]:


if __name__ == "__main__":
    # Load in data file
    #df = pd.read_table("/dors/capra_lab/users/yand1/te_ml/data/2018_07_03_pca_te_enhancers/combined_features_matrix.tsv")
    df = pd.read_table("../../data/2018_07_03_pca_te_enhancers/test.tsv")
    
    # Get features used in PCA
    features_df = df.loc[:,FIRST_KMER:LAST_KMER]
    
    # Get labels
    labels_df = df.loc[:,"label"]
    
    # Create the incremental PCA
    ipca = IncrementalPCA(n_components = N_COMPONENTS, batch_size = BATCH_SIZE)
    features_transformed = ipca.fit_transform(features_df)
    
    # Convert transformed coordinates to pandas dataframe
    transformed_df = pd.DataFrame(features_transformed)
    transformed_df.columns = ["component_1", "component_2"]
    
    # Label the transformed data
    transformed_df["label"] = labels_df
    
    # Plot the pca
    plt.figure(figsize=(20, 20))
    for label, color in zip(set(labels_df), COLORS):
        # Select rows that correspond to the current label
        rows = transformed_df.loc[transformed_df["label"] == label]
        # Plot on the points corresponding to the current label on the plot with 
        # unique color
        plt.scatter(rows.loc[:,"component_1"], rows.loc[:, "component_2"], 
                    color = color, label = label, alpha = 0.6)
    plt.title("PCA of HERVs, enhancers, and overlap of HERVs and enhancers", fontsize = 30)
    plt.legend(fontsize = 30)
    plt.savefig("../../results/2018_07_09_pca_te_enhancers/test_pca.png")

