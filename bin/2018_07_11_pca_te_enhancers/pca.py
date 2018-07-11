
# coding: utf-8

# Name: Daniel Yan
# 
# Email: daniel.yan@vanderbilt.edu
# 
# Module for an incremental principal component analysis. This version allows for user to specify axis.
# 
# Can be run as a standalone script that performs a principal component analysis on the data at:
# /dors/capra_lab/users/yand1/te_ml/data/2018_07_03_pca_te_enhancers/combined_features_matrix.tsv
# in two components and plots the results.

# In[ ]:


"""Module for an incremental principal component analysis with scikit-learn. Results can be plotted."""


# In[ ]:


# Libaries
from sklearn.decomposition import PCA, IncrementalPCA
import numpy as np
import matplotlib
matplotlib.use("Agg") # Avoid display error
import matplotlib.pyplot as plt
import pandas as pd


# In[ ]:


# Class Constants
N_COMPONENTS = 2 # Number of principal components to keep
BATCH_SIZE = None # Size of incremental pca batch to control for memory usage. Can be int or None.


# In[ ]:


def create_ipca(features, n_components = N_COMPONENTS, batch_size = BATCH_SIZE):
    """Create an incremental pca based on a features matrix and return the transformed coordinates
    
    Keyword Arguments:
        features: Array-like object containing the features to do a PCA on.
        
        n_components: Number of dimensions to reduce down to (default N_COMPONENTS).
        
        batch_size: Size to use for incremental PCA. Can be integer or None (default BATCH_SIZE)
        
    Return:
        Numpy array with coordinates of principal components in columns. Column 0 contains component
        accounting for most variation, column 1 contains component accounting for second-most,
        and so on.
    """
    # Create the incremental PCA
    ipca = IncrementalPCA(n_components = N_COMPONENTS, batch_size = BATCH_SIZE)
    return ipca.fit_transform(features_df)


# In[ ]:


def label_coordinates(transformed_coordinates, labels):
    """Labels the transformed coordinates with the correct group.
    
    Keyword Arguments:
        transformed_coordinates: Numpy array containing the coordinates in the principal components
        
        labels: Array-like object containing labels for the coordinates. The labels should be in
            the same order as the rows in transformed_coordinates
        
    Return: Pandas dataframe with labels inserted as the last column of transformed_coordinates
    """
    # Convert transformed coordinates to pandas dataframe
    transformed_df = pd.DataFrame(transformed_coordinates)
    
    # Label the transformed data
    transformed_df["label"] = labels
    
    return transformed_df


# In[ ]:


def scatterplot_pca(df, file_name, labels_set, colors_list, figsize = (20, 20), 
                    fontsize = 30, title = "", alpha = 0.6, axis = "auto"):
    """Create a scatter plot for the PCA with different groups labeled by color
    
    Keyword Arguments:
        df: Pandas data frame containing coordinates of principal component 1 on column 0, coordinates
            of principal component 2 on column 1, and labels in column 2. 
            
        file_name: String name of the directory and file to save to
        
        labels_set: Set of labels used to label the data
        
        colors_list: List of colors used for the different labels.
        
        figsize: Tuple containing height and width of the figure in inches (default (20, 20))
        
        fontsize: Integer size of the font for title and legend (default = 30)
        
        title: String title for the plot (default is empty string)
        
        alpha: Alpha level for points on scatter plot (0 is transparent, 1 is opaque)
    """
    # Plot the pca
    plt.figure(figsize=figsize)
    
    # Create tuples matching labels to colors, and plot points corresponding to each label
    # one label at a time on the scatter plot
    for label, color in zip(labels_set, colors_list):
        # Select rows that correspond to the current label
        rows = df.loc[df.iloc[:,2] == label]
        # Plot on the points corresponding to the current label on the plot with 
        # unique color
        plt.scatter(rows.iloc[:,0], rows.iloc[:,1], 
                    color = color, label = label, alpha = alpha)
    
    plt.title(title, fontsize = fontsize)
    plt.legend(fontsize = fontsize)
    plt.axis(axis)
    plt.savefig(file_name)


# In[ ]:


if __name__ == "__main__":
    # Load in data file
    df = pd.read_table("/dors/capra_lab/users/yand1/te_ml/data/2018_07_03_pca_te_enhancers/combined_features_matrix.tsv")
    
    # Get features used in PCA
    features_df = df.loc[:,"aaaaaa":"tttttt"]
    
    # Get labels
    labels_df = df.loc[:,"label"]
    
    # Create the incremental pca
    features_transformed = create_ipca(features_df)
    
    # Label the transformed coordiantes
    transformed_df = label_coordinates(transformed_coordinates = features_transformed, 
                                       labels = labels_df)
    
    # Plot the pca
    scatterplot_pca(df = transformed_df, file_name = 
                    "/dors/capra_lab/users/yand1/te_ml/results/2018_07_10_pca_te_enhancers/pca.png",
                   labels_set = set(labels_df), colors_list = ["teal", "red", "navy"],
                   title = "PCA on HERVs, enhancers, and HERV-enhancer overlap using 6-mers", 
                   axis = [-0.05, 0.35, -0.4, 0.3], alpha = 0.2)
    
    # Plot just the HERVs
    scatterplot_pca(df = transformed_df, file_name = 
                    "/dors/capra_lab/users/yand1/te_ml/results/2018_07_10_pca_te_enhancers/pca_hervs.png",
                   labels_set = set(["herv_only"]), colors_list = ["teal"],
                   title = "HERVs only", 
                   axis = [-0.05, 0.35, -0.4, 0.3], alpha = 0.2)
    
    # Plot just the enhancers
    scatterplot_pca(df = transformed_df, file_name = 
                    "/dors/capra_lab/users/yand1/te_ml/results/2018_07_10_pca_te_enhancers/pca_enhancers.png",
                   labels_set = set(["enhancer_only"]), colors_list = ["red"],
                   title = "Enhancers only", 
                   axis = [-0.05, 0.35, -0.4, 0.3], alpha = 0.2)
    
    # Plot just HERV-enhancer intersection
    scatterplot_pca(df = transformed_df, file_name = 
                    "/dors/capra_lab/users/yand1/te_ml/results/2018_07_10_pca_te_enhancers/pca_intersect.png",
                   labels_set = set(["herv_enhancer_intersect"]), colors_list = ["navy"],
                   title = "HERV-enhancer intersect", 
                   axis = [-0.05, 0.35, -0.4, 0.3], alpha = 0.2)    

