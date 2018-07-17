# Author: Daniel Yan
# 
# Date: 2018-07-17
# 
# Email: daniel.yan@vanderbilt.edu
# 
# Description: t-distributed stochastic neighbor embedding analysis on
#               data with scatter plot visualization.
# 
# Preconditions:
# Data file must contain one column named "label" in the header
#  that contains labels for the data.
# All other columns must contain features.
# Data file must not have indices for rows.
# Note: tsne is memory intensive and memory error may result on large
#  files. Fix this by passing a smaller file.
# 
# Command Line Arguments:
# First argument: Name of data file to read from. Include directory and extension.
# Second argument: Name of file to store scatterplot to. Include directory, but leave out extension 
#     (will automatically be saved as .png).
# Third argument: Name of file to store tsne model to. Include directory, but leave out extension (will 
#     automatically be saved as .pkl).
# Fourth argument: Integer number of components to reduce to.
# Fifth argument: Integer perplexity for tsne hyperparameter between 5 and 50.
# Error will result if any argument is invalid.


# Libraries
import pandas as pd # Data
from pca import scatterplot_cords, label_coordinates # For creating scatterplot from labeled coordinates
from sklearn.externals import joblib # Save tsne model
from sklearn.manifold import TSNE
import sys # Command line arguments

# Constants
COLORS_LIST = ["orangered", "indigo", "limegreen", "dodgerblue"]


if __name__ == "__main__":
    # Get data file to process.
    data_file = sys.argv[1]
    # Get name of file to save scatterplot to.
    scatterplot_file = sys.argv[2]
    # Get name of file to save model to.
    model_file = sys.argv[3]
    # Get number of components to reduce to.
    n_components = int(sys.argv[4])
    # Get perplexity for tsne
    perplexity = int(sys.argv[5])
    
    # Load in data file with header on top row.
    print("Loading data file...")
    data_frame = pd.read_table(data_file, header = 0)
    
    # Get labels.
    labels_df = data_frame.loc[:,"label"]

    # Get features.
    features_df = data_frame.drop(labels = ["label"], axis = "columns")
    features_df = features_df.apply(pd.to_numeric)
    
    # Create tsne and transform coordinates. Use random seed of 0 for reproducibility.
    print("Calculating tsne...")
    tsne = TSNE(n_components = n_components, random_state = 0,
                perplexity = perplexity, verbose=2)
    features_transformed = tsne.fit_transform(features_df)
    
    # Label the transformed coordinates.
    transformed_df = label_coordinates(transformed_coordinates = features_transformed, 
                                       labels = labels_df)
    
    # Get the list of unique labels.
    labels_list = list(set(labels_df))
    
    # Plot the transformed coordinates.
    print("Creating scatterplot...")
    axis = scatterplot_cords(df = transformed_df, 
                             file_name = scatterplot_file + ".png", 
                             labels_list = labels_list,
                             colors_list = COLORS_LIST,
                             title = "TSNE on hervs, enhancers, herv-enhancer overlap, and control",
                             alpha = 0.3)
    
    # Plot the different groups individually in case of overlap.
    count = 0
    for label in labels_list:
        scatterplot_cords(df = transformed_df, 
                          file_name = scatterplot_file + "_" + label + ".png",
                          labels_list = [label],
                          colors_list = [COLORS_LIST[count]],
                          title = label,
                          alpha = 0.5, 
                          axis = axis)
        # Increment counter for color
        count += 1
    
    # Save the tsne model.
    print("Saving tsne...")
    joblib.dump(tsne, model_file + ".pkl")

