# Name: Daniel Yan
# Date: 2018-07-13
# Email: daniel.yan@vanderbilt.edu
# 
# Module for an incremental principal component analysis on larger data sets.


# Libaries
from sklearn.decomposition import PCA, IncrementalPCA
import numpy as np
import matplotlib
matplotlib.use("Agg") # Avoid display error
import matplotlib.pyplot as plt
import pandas as pd


# Class Defaults
N_COMPONENTS = 2 # Number of principal components to keep
BATCH_SIZE = None # Size of incremental pca batch to control for memory usage. Can be int or None.



def create_ipca(features_df, n_components = N_COMPONENTS, batch_size =
BATCH_SIZE):
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


def label_coordinates(transformed_coordinates, labels, labels_col_name = "label"):
    """Labels the transformed coordinates with the correct group.
    
    Keyword Arguments:
        transformed_coordinates: Numpy array (or similar) containing the
        coordinates in the principal components
        
        labels: Array-like object containing labels for the coordinates. The labels should be in
            the same order as the rows in transformed_coordinates
            
        labels_col_name: String for the name of the column containing the labels within the dataframe
            (default = "label")
        
    Return: Pandas dataframe with labels inserted as the last column of transformed_coordinates
    """
    # Convert transformed coordinates to pandas dataframe
    transformed_df = pd.DataFrame(transformed_coordinates)
    
    # Label the transformed data
    transformed_df[labels_col_name] = labels
    
    return transformed_df


def scatterplot_pca(df, file_name, labels_list, colors_list, labels_col_name = "label",
                    figsize = (20, 20), fontsize = 30, title = "", alpha = 0.2, 
                    component_x = 1, component_y = 2, x_label = "", y_label = ""):
    """Create a scatter plot for the PCA with different groups labeled by color and saves to file
    
    Keyword Arguments:
        df: Pandas data frame containing coordinates of principal component 1 on column 0, coordinates
            of principal component 2 on column 1, and labels in column 2. 
            
        file_name: String name of the directory and file to save to
        
        labels_list: List of labels used to label the data
        
        colors_list: List of colors used for the different labels.
        
        labels_col_name: String for the name of the column containing the labels within the dataframe
            (default = "label"). Must be same as labels_col_name parameter in 
            label_coordinates function.
        
        figsize: Tuple containing height and width of the figure in inches (default (20, 20))
        
        fontsize: Integer size of the font for title and legend (default = 30)
        
        title: String title for the plot (default is empty string)
        
        alpha: Alpha level for points on scatter plot (default = 0.2)
        
        component_x: Principal component to plot on x-axis (default is 1, which is principal
            component accounting for most variation)
            
        component_y: Principal component to plot on y-axis (default is 2, which is principal
            component accounting for second most variation)
            
        x_label: String to label x-axis (default is empty string)
        
        y_label: String to label y-axis (default is empty string)
    """
    # Plot the pca
    plt.figure(figsize=figsize)
    
    # Create tuples matching labels to colors, and plot points corresponding to each label
    # one label at a time on the scatter plot
    for label, color in zip(labels_list, colors_list):
        
        # Select rows that correspond to the current label
        rows = df.loc[df.loc[:,labels_col_name] == label]
        # Plot on the points corresponding to the current label on the plot with 
        # unique color
        plt.scatter(rows.iloc[:,(component_x - 1)], rows.iloc[:,(component_y - 1)], 
                    color = color, label = label, alpha = alpha)
    
    plt.title(title, fontsize = fontsize)
    plt.legend(fontsize = fontsize)
    plt.xlabel(x_label, fontsize = fontsize)
    plt.ylabel(y_label, fontsize = fontsize)
    plt.savefig(file_name)
    plt.close()

