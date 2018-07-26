# Author: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Date: 2018-07-26
#
# Description: Principal component analysis on data file. Store transformed
# coordinates and create scatter plots. Standalone script (main portion) is
# intended for feature matrix with kmer counts in hervs, chromhmm enhancers,
# herv-enhancer overlap, and three random sets each length matched to one of
# those groups.
#
# Command Line Arguments for standalone script:
# Argument 1: Name of file containing data to perform PCA on, including
# directory and extension. Must contain table with header. Features should be
# in columns "aaaaaa" to "tttttt". Each row should have a label in column
# "label"
# Argument 2: Name of file to store transformed coordinates to, including
# directory and extension.
# Argument 3: Name of directory to store scatter plots of PCA to. Include
# final backslash.
# Argument 4: Number of components to reduce to.

import pandas as pd  # Data manipulation
import pca  # Labeling components
import sys  # Command line arguments
from sklearn.decomposition import IncrementalPCA

def pipeline(data_file, cords_file, results_dir, n_components):
    # Load in data file
    print("Loading data file...")
    data_frame = pd.read_table(data_file)
    # Get features used in PCA
    features_df = data_frame.loc[:, "aaaaaa":"tttttt"]
    # Get labels
    labels_df = data_frame.loc[:, "label"]

    # Create the PCA
    print("Creating PCA...")
    ipca = IncrementalPCA(n_components=n_components)
    features_transformed = ipca.fit_transform(features_df)

    # Label the transformed coordinates
    transformed_df = pca.label_coordinates(
        transformed_coordinates=features_transformed, labels=labels_df)

    # Save the transformed coordinates
    print("Saving transformed coordinates...")
    transformed_df.to_csv(cords_file, sep='\t', index=False)

    # Save the explained variances
    print("Saving explained variances...")
    pca.save_variances(pca = ipca, file_name=results_dir + "variances.txt")

if __name__ == '__main__':
    # Get command line arguments.
    print("Reading in command line arguments")
    data_file = sys.argv[1]
    cords_file = sys.argv[2]
    results_dir = sys.argv[3]
    n_components = int(sys.argv[4])

    # Send files into PCA pipeline to create PCA, store transformed
    # coordinates, and make plots.
    pipeline(data_file=data_file, cords_file=cords_file,
             results_dir=results_dir, n_components=n_components)
