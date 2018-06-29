
# coding: utf-8

# Reformats the features matrix at /dors/capra_lab/users/yand1/te_ml/data/2018_06_29_kmers_enhancers_intersect/hervs_kmers_features_matrix.tsv
# to remove column names.

# In[ ]:


# Libraries
import pandas as pd


# In[ ]:


# Class constants
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/" # Root directory for project


# In[ ]:


## Main
def main():
    """Main function
    """
    # Read in data frame
    features_df = pd.read_table(DIRECTORY + "data/2018_06_29_kmers_enhancers_intersect/hervs_kmers_features_matrix.tsv")
    
    # Store header names to file.
    with open(DIRECTORY + "data/2018_06_29_kmers_enhancers_intersect/header_names.txt", mode = "w+") as file:
        for i in range(len(features_df.columns)):
            file.write("Column " + str(i) + ": " + features_df.columns[i] + '\n')
        
    # Store data frame to file
    features_df.to_csv(DIRECTORY + "data/2018_06_29_kmers_enhancers_intersect/no_header_hervs_kmers_features_matrix.tsv"
                      , sep = '\t', index = False, header = False)
    


# In[ ]:


# Call main to run
main()

