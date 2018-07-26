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

import os
import pandas as pd  # Data manipulation
import pca  # Labeling components
# Function to generate combinations of components to plot
from shuffled_pca import generate_combinations
# Incremental PCA because of large size of data
from sklearn.decomposition import IncrementalPCA
import sys  # Command line arguments


def plot_combinations(df, results_dir, labels_list, combinations_list,
                      colors_list, ipca):
    # Plot different combinations of principal components
    for combination in combinations_list:

        component_x = combination[0]  # Component on x-axis
        component_y = combination[1]  # Component on y-axis

        print("Plotting component {} and {}".format(component_x, component_y))

        # Create directory if it does not exist
        directory = (results_dir + "/components_{}_{}/".format(component_x,
                                                               component_y))
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Get labels for x and y axis
        x_label = "Component {} accounting for {}% of "
        x_label = "Component {} accounting for {}% of "
        "variation".format(component_x,
                           100 * ipca.explained_variance_ratio_[component_x]),
        y_label = "Component {} accounting for {}% of variation".format(
            component_y, 100 * ipca.explained_variance_ratio_[component_y])

        # Plot the pca and get axis for further use
        saved_axis = pca.scatterplot_cords(df=df,
                                           file_name=directory +
                                                     "all_labels.png",
                                           labels_list=labels_list,
                                           colors_list=colors_list,
                                           title="All labels on components {} "
                                                 "and {"
                                                 "}".format(component_x,
                                                            component_y),
                                           component_x=component_x,
                                           component_y=component_y, alpha=0.5,
                                           # Label axis with how much
                                           # variation this
                                           # component accounts for
                                           x_label="Component {} accounting "
                                                   "for {}% "
                                                   "of "
                                                   "variation".format(
                                               component_x, 100 *
                                                            ipca.explained_variance_ratio_[
                                                                component_x]),
                                           y_label="Component {} accounting "
                                                   "for {}% "
                                                   "of "
                                                   "variation".format(
                                               component_y, 100 *
                                                            ipca.explained_variance_ratio_[
                                                                component_y]))

        # Plot just the random sets if there are more than 1
        randoms_list = [label for label in labels_list if "random" in label]
        random_num = len(randoms_list)
        labels_num = len(labels_list)
        print(colors_list[labels_num - random_num: labels_num])
        if random_num > 1:
            pca.scatterplot_cords(df=df,
                                  file_name=directory + "random_sets.png",
                                  labels_list=randoms_list,
                                  colors_list=colors_list[
                                              labels_num - random_num:
                                              labels_num],
                                  title="Random sets on components {} and {"
                                        "}".format(component_x, component_y),
                                  component_x=component_x,
                                  component_y=component_y, alpha=0.5,
                                  x_label="Component {} accounting for {}% of "
                                          "variation".format(component_x, 100 *
                                                             ipca.explained_variance_ratio_[
                                                                 component_x]),
                                  y_label="Component {} accounting for {}% of "
                                          "variation".format(component_y, 100 *
                                                             ipca.explained_variance_ratio_[
                                                                 component_y]),
                                  axis=saved_axis)

        # Plot each of the individual labels to prevent overlapping issues.
        count = 0
        for label in labels_list:
            pca.scatterplot_cords(df=df,
                                  file_name=directory + "{}.png".format(label),
                                  labels_list=[label],
                                  colors_list=[colors_list[count]],
                                  title="{} on components {} and {}".format(
                                      label, component_x, component_y),
                                  component_x=component_x,
                                  component_y=component_y, alpha=0.5,
                                  # Label axis with how much variation this
                                  # component accounts for
                                  x_label="Component {} accounting for {}% of "
                                          "variation".format(component_x, 100 *
                                                             ipca.explained_variance_ratio_[
                                                                 component_x]),
                                  y_label="Component {} accounting for {}% of "
                                          "variation".format(component_y, 100 *
                                                             ipca.explained_variance_ratio_[
                                                                 component_y]),
                                  axis=saved_axis)
            # Increment count for color
            count += 1


def pipeline(data_file, cords_file, results_dir, n_components):
    # Load in data file
    print("Loading data file...")
    data_frame = pd.read_table(data_file)
    # Get features used in PCA
    features_df = data_frame.loc[:, "aaaaaa":"tttttt"]
    # Get labels
    labels_df = data_frame.loc[:, "label"]
    labels_list = sorted(list(set(labels_df)))

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
    pca.save_variances(pca=ipca, file_name=results_dir + "variances.txt")

    # Create combinations of principal components to plot
    components = (1, 2, 3, 4, 5)
    combinations_list = generate_combinations(components)

    # Plot all the combinations of components. Choose colors list with colors
    #  in matplotlib.
    plot_combinations(transformed_df, results_dir=results_dir,
                      labels_list=labels_list,
                      combinations_list=combinations_list,
                      colors_list=["saddlebrown", "gold", "darkgreen", "cyan",
                                   "darkblue", "magenta"], ipca=ipca)


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
