
# coding: utf-8

# Name: Daniel Yan
# 
# Email: daniel.yan@vanderbilt.edu
# 
# Finds the shuffled parts of the human genome within the features matrices in files 50-99 from /dors/capra_lab/users/yand1/te_ml/data/2018_07_11_pca_te_enhancers/batch_output
# and normalize them by dividing by the number of base pairs. Store the new features matrix containing only information about shuffled parts of the human genome to a /dors/capra_lab/users/yand1/te_ml/data/2018_07_12_pca_te_enhancers/shuffled_features_matrix.tsv

# In[1]:


# Libraries
import pandas as pd
import reformat_df


# In[ ]:


def combine(file_list, axis = "index"):
    """
    Combines rows of the files together on the given axis and returns combined data frame
    
    Args:
        file_list(list): List of files with same columns
        axis(string): Concatenate on index or columns
    """
    # List to store all the data frames to concatenate
    frames_list = []
    
    # Read in all files
    for file in file_list:
        frames_list.append(pd.read_table(file))
            
    # Combine data frames      
    return pd.concat(frames_list, axis = axis) 


# In[ ]:


if __name__ == "__main__":
    # List of files to combine
    file_list = []
    
    # Directory the files are in 
    directory = "/dors/capra_lab/users/yand1/te_ml/data/2018_07_11_pca_te_enhancers/batch_output/"
    
    # Generate list of files with shuffled human genome data to combine
    for i in range(50):
        file_list.append(directory + "shuffle_{}_features_matrix.tsv".format(i + 50))
        
    # Get combined data frame
    print("Combining files...")
    combined_df = combine(file_list)
    
    # Normalize counts 
    print("Normalizing counts...")
    reformat_df.normalize(combined_df, lengths_col = 4, normalize_cols = list(range(5, 4101)))
    
    # Save to new file
    combined_df.to_csv("/dors/capra_lab/users/yand1/te_ml/data/2018_07_11_pca_te_enhancers/shuffled_features_matrix.tsv",
                      header = False, Index = False, sep = '\t')

