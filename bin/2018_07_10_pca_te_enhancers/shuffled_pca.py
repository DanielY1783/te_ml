
# coding: utf-8

# Name: Daniel Yan
#     
# Email: daniel.yan@vanderbilt.edu
# 
# Principal component analysis on HERVs, enhancers, HERV-enhancer intersect, and control population of shuffled parts of the human genome.

# In[ ]:


# Libaries
import pca
from sklearn.decomposition import IncrementalPCA


# In[ ]:


def main():
    """Main function to run everything
    """
    # Load in data file
    df = pd.read_table("/dors/capra_lab/users/yand1/te_ml/data/2018_07_10_pca_te_enhancers/test.tsv")
    
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
        
    # Plot the pca
    pca.scatterplot_pca(df = transformed_df, file_name = 
                    "/dors/capra_lab/users/yand1/te_ml/results/2018_07_10_pca_te_enhancers/pca.png",
                   labels_set = set(labels_df), colors_list = ["orangered", "indigo", "lime", "cyan"],
                   title = "PCA on HERVs, enhancers, HERV-enhancer overlap, and shuffled human genome as control using 6-mers", 
                   alpha = 0.2)
    
    # Plot just the HERVs
    pca.scatterplot_pca(df = transformed_df, file_name = 
                    "/dors/capra_lab/users/yand1/te_ml/results/2018_07_10_pca_te_enhancers/pca_hervs.png",
                   labels_set = set(["herv_only"]), colors_list = ["orangered"],
                   title = "HERVs only", 
                   alpha = 0.2)
    
    # Plot just the enhancers
    pca.scatterplot_pca(df = transformed_df, file_name = 
                    "/dors/capra_lab/users/yand1/te_ml/results/2018_07_10_pca_te_enhancers/pca_enhancers.png",
                   labels_set = set(["enhancer_only"]), colors_list = ["indigo"],
                   title = "Enhancers only", 
                   alpha = 0.2)
    
    # Plot just HERV-enhancer intersection
    pca.scatterplot_pca(df = transformed_df, file_name = 
                    "/dors/capra_lab/users/yand1/te_ml/results/2018_07_10_pca_te_enhancers/pca_intersect.png",
                   labels_set = set(["herv_enhancer_intersect"]), colors_list = ["lime"],
                   title = "HERV-enhancer intersect", 
                   alpha = 0.2)    
    
    # Plot just the control of shuffled elements in the human genome
    pca.scatterplot_pca(df = transformed_df, file_name = 
                    "/dors/capra_lab/users/yand1/te_ml/results/2018_07_10_pca_te_enhancers/pca_control.png",
                   labels_set = set(["shuffled_genome"]), colors_list = ["cyan"],
                   title = "Control", 
                   alpha = 0.2)
    
    # Print out the explained variance ratios to file
    with open("/dors/capra_lab/users/yand1/te_ml/results/2018_07_10_pca_te_enhancers/variance_ratios.txt",
             w+) as file:
        int count = 1
        for i in ipca.explained_variance_ratio_:
            file.write("Explained Variance Ratio for Component {}: {}".format(count, i))


# In[ ]:


# Call main to run
main()

