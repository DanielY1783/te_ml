
# coding: utf-8

# Name: Daniel Yan
#     
# Email: daniel.yan@vanderbilt.edu
# 
# Principal component analysis on HERVs, enhancers, HERV-enhancer intersect, and control population of shuffled parts of the human genome.

# In[1]:


# Libaries
import pandas as pd
import pca # Module containing wrappers for plotting PCAs
from sklearn.decomposition import IncrementalPCA
import matplotlib
matplotlib.use("Agg") # Avoid display error
import matplotlib.pyplot as plt
import itertools # Generator


# In[2]:


# Constants
ROOT_DIR = "../../" # Root directory for project
COLORS_LIST = ["orangered", "indigo", "limegreen", "dodgerblue"]


# In[ ]:


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


# In[ ]:


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


# In[3]:


if __name__ == "__main__":
        """Main function to run everything
        """
        # Load in data file
        df = pd.read_table(ROOT_DIR + "data/2018_07_11_pca_te_enhancers/test.tsv")

        # Get features used in PCA
        features_df = df.loc[:,"aaaaaa":"tttttt"]

        # Get labels
        labels_df = df.loc[:,"label"]

        # Create the PCA
        ipca = IncrementalPCA(n_components = 10)
        features_transformed = ipca.fit_transform(features_df)

        # Label the transformed coordinates
        transformed_df = pca.label_coordinates(transformed_coordinates = features_transformed, 
                                           labels = labels_df)

        # Get a list of all unique labels
        labels_list = list(set(labels_df))

        # Create combinations of principal components to plot
        components = (1, 2, 3, 4, 5)
        combinations_list = generate_permutations(components)

        # Plot all possible combinations
        for combination in combinations_list:
            
            # Plot the pca
            pca.scatterplot_pca(df = transformed_df, 
                                file_name = ROOT_DIR + "results/2018_07_11_pca_te_enhancers/pca_all_{}_{}"
                                    .format(combination[0], combination[1]),
                                labels_list = labels_list,
                                colors_list = COLORS_LIST,
                                title = "All labels on components {} and {}"
                                    .format(combination[0], combination[1]),
                                component_x = combination[0])

#         # Plot just the HERVs
#         pca.scatterplot_pca(df = transformed_df, file_name = 
#                         "/dors/capra_lab/users/yand1/te_ml/results/2018_07_10_pca_te_enhancers/pca_hervs.png",
#                        labels_set = set(["herv_only"]), colors_list = ["orangered"],
#                        title = "HERVs only", 
#                        alpha = 0.2)

#         # Plot just the enhancers
#         pca.scatterplot_pca(df = transformed_df, file_name = 
#                         "/dors/capra_lab/users/yand1/te_ml/results/2018_07_10_pca_te_enhancers/pca_enhancers.png",
#                        labels_set = set(["enhancer_only"]), colors_list = ["indigo"],
#                        title = "Enhancers only", 
#                        alpha = 0.2)

#         # Plot just HERV-enhancer intersection
#         pca.scatterplot_pca(df = transformed_df, file_name = 
#                         "/dors/capra_lab/users/yand1/te_ml/results/2018_07_10_pca_te_enhancers/pca_intersect.png",
#                        labels_set = set(["herv_enhancer_intersect"]), colors_list = ["lime"],
#                        title = "HERV-enhancer intersect", 
#                        alpha = 0.2)    

#         # Plot just the control of shuffled elements in the human genome
#         pca.scatterplot_pca(df = transformed_df, file_name = 
#                         "/dors/capra_lab/users/yand1/te_ml/results/2018_07_10_pca_te_enhancers/pca_control.png",
#                        labels_set = set(["shuffled_genome"]), colors_list = ["cyan"],
#                        title = "Control", 
#                        alpha = 0.2)

        # Print out the explained variance ratios to file
        with open(ROOT_DIR + "results/2018_07_11_pca_te_enhancers/test_variance_ratios.txt", 
                  mode = "w+") as file:
            count = 1
            for i in ipca.explained_variance_ratio_:
                file.write("Explained Variance Ratio for Component {}: {}\n".format(count, i))
                count += 1

