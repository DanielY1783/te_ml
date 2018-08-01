# Name: Daniel Yan
# Date: 2018-07-13
# Email: daniel.yan@vanderbilt.edu
# 
# Principal component analysis on HERVs, enhancers, HERV-enhancer intersect,
# and control population of shuffled parts of the human genome.

# Libaries
import pandas as pd
import pca # Module containing wrappers for plotting PCAs
from sklearn.decomposition import IncrementalPCA
import matplotlib
matplotlib.use("Agg") # Avoid display error
import matplotlib.pyplot as plt
import itertools # Generator
import os # Make directories as needed

# Constants
_ROOT_DIR = "/dors/capra_lab/users/yand1/te_ml/" # Root directory for project
COLORS_LIST = ["orangered", "indigo", "limegreen", "dodgerblue"]
N_COMPONENTS = 10 # Number of components in PCA


def generate_configurations(elements, n = 2):
    """Generates a list containing tuples of the elements of the original iterable in all possible
        configurations, with repeat elements allowed.
    
    Keyword Arguments:
        elements: Iterable of all elements to permute. Iterable should contain unique elements.
        
        n: Integer length of the permutations. The returned list will contain tuples of n elements.
            (default is 2)
        
    Returns:
        configurations_list: List of all possible tuples, such that each inner tuple contains one
            configuration formed from elements in the original iterable (repeats allowed).
    """
    # Use product to generate iterator that contains permutations
    permutations_iter = itertools.product(elements, repeat = n)
    return list(permutations_iter)


def generate_combinations(elements, n = 2):
    """Generates a list of of all combinations of the elements of the original iterable. 
        Combinations are each in own list and will not contain repeated elements.
    
    Keyword Arguments:
        elements: Iterable of all elements. Iterable should contain unique elements.
        
        n: Integer length of the combinations. The returned list will contain tuples of n elements.
            (default is 2)
        
    Returns:
        combinations_list: List of tuples, where each inner tuple contains one combination 
            of the original element, and the list contains all combinations.
    """
    # Use product to generate iterator that contains permutations
    combinations_iter = itertools.combinations(elements, r = n)
    return list(combinations_iter)


if __name__ == "__main__":
        # Load in data file
        df = pd.read_table(_ROOT_DIR +
                           "data/2018_07_13_pca_te_enhancers/"
                           "hervs_enhancers_shuffled_features_matrix.tsv")

        # Get features used in PCA
        features_df = df.loc[:,"aaaaaa":"tttttt"]

        # Get labels
        labels_df = df.loc[:,"label"]

        # Create the PCA
        ipca = IncrementalPCA(n_components = N_COMPONENTS)
        features_transformed = ipca.fit_transform(features_df)

        # Label the transformed coordinates
        transformed_df = pca.label_coordinates(transformed_coordinates = features_transformed, 
                                           labels = labels_df)

        # Get a list of all unique labels
        labels_list = list(set(labels_df))

        # Create combinations of principal components to plot
        components = (1, 2, 3, 4, 5)
        combinations_list = generate_combinations(components)

        # Plot different combinations of principal components
        for combination in combinations_list:

            component_x = combination[0] # Component on x-axis
            component_y = combination[1] # Component on y-axis

            print("Plotting component {} and {}".format(component_x, component_y))

            # Create directory if it does not exist
            directory = (_ROOT_DIR +
                         "results/2018_07_13_pca_te_enhancers/components_{}_{}/"
                         .format(component_x, component_y))
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            # Plot the pca
            pca.scatterplot_pca(df = transformed_df, 
                                file_name = directory + "pca.png",
                                labels_list = labels_list,
                                colors_list = COLORS_LIST,
                                title = "All labels on components {} and {}"
                                    .format(component_x, component_y),
                                component_x = component_x,
                                component_y = component_y,
                                x_label = "Component {} accounting for {}% of variation".format(
                                    component_x, 100 * ipca.explained_variance_ratio_[component_x]),
                                y_label = "Component {} accounting for {}% of variation".format(
                                    component_y, 100 * ipca.explained_variance_ratio_[component_y]))
            
            # Plot each of the individual labels to prevent overlapping issues.
            count = 0
            for label in labels_list:
                pca.scatterplot_pca(df = transformed_df, 
                                file_name = _ROOT_DIR +
                                            "results/2018_07_13_pca_te_enhancers"
                                "/components_{}_{}/{}.png"
                                    .format(component_x, component_y, label),
                                labels_list = [label],
                                colors_list = [COLORS_LIST[count]],
                                title = "{} on components {} and {}"
                                    .format(label, component_x, component_y),
                                component_x = component_x,
                                component_y = component_y,
                                x_label = "Component {} accounting for {}% of variation".format(
                                    component_x, 100 * ipca.explained_variance_ratio_[component_x]),
                                y_label = "Component {} accounting for {}% of variation".format(
                                    component_y, 100 * ipca.explained_variance_ratio_[component_y]))
                # Increment count for color
                count += 1

        # Print out the explained variance ratios to file
        with open(_ROOT_DIR +
                  "results/2018_07_13_pca_te_enhancers/variance_ratios.txt",
                  mode = "w+") as file:
            count = 1
            for i in ipca.explained_variance_ratio_:
                file.write("Explained Variance Ratio for Component {}: {}%\n".format(count, i * 100))
                count += 1

