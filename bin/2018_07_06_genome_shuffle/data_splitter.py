
# coding: utf-8

# Module version of similar file at /dors/capra_lab/users/yand1/te_ml/bin/2018_06_28_kmers_faster/accre
# Splits data frame into smaller data frames and save to files as necessary.

# In[1]:


# Libraries
import pandas as pd # Data manipulation 


# In[2]:


# Class constants
SPLITS = 100 # Number of files to make


# In[ ]:


def split_data(df, splits = SPLITS):
    """Splits dataframe and returns list of new dataframes.
    
    Keyword Arguments:
        df (pd.DataFrame): Data frame to split
    
        splits(int): Number of data frames to split into (default = SPLITS).
        
    Return:
        smaller_dfs_list (list): List of the new data frames.
        
    """
    # Create list for return
    smaller_dfs_list = []
    
    # Store number of rows in data file.
    rows_num = df.shape[0]
    
    # Split up files
    for i in range(SPLITS):
        start_row = i * (rows_num/SPLITS)
        end_row = (i + 1) * (rows_num/SPLITS)
        temp_df = hervs_df.loc[start_row:end_row,]
        smaller_dfs_list.append(temp_df.copy())
    return smaller_dfs_list


# In[3]:


if __name__ == "__main__":
    # Read in file as pandas dataframe
    hervs_df = pd.read_table("/dors/capra_lab/users/yand1/te_ml/data/2018_07_06_genome_shuffle/all_pairs.tsv", header = None)

    # Split data frame into parts.
    df_list = split_data(df = hervs_df)
    
    # Save to files
    for df in df_list:
        df.to_csv("/dors/capra_lab/users/yand1/te_ml/data/2018_07_06_genome_shuffle/batch_input/shuffle_" + str(i) + ".tsv", 
                       sep = '\t', index = False, header = False)

