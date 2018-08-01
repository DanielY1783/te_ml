
# coding: utf-8

# Name: Daniel Yan
# 
# Email: daniel.yan@vanderbilt.edu
# 
# Finds the shuffled parts of the human genome within the features matrices in files 50-99 from /dors/capra_lab/users/yand1/te_ml/data/2018_07_10_pca_te_enhancers/batch_output
# and normalize them by dividing by the number of base pairs. Store the new features matrix containing only information about shuffled parts of the human genome to a /dors/capra_lab/users/yand1/te_ml/data/2018_07_10_pca_te_enhancers/shuffled_features_matrix.tsv

# In[ ]:


# Libraries
import pandas as pd


# In[ ]:


# Constants
PAIRS = 4 # Column with base pairs


# In[ ]:


def normalize_counts(df):
    """Normalize all kmer counts by dividing by the total number of bases
    """
    # Normalize counts by dividing kmer counts in each row by the number of bases
    df = df.apply(normalize_row, axis = "columns")
    return df


# In[ ]:


def normalize_row(row):
    """Divides the count of kmers by the number of pairs to get normalized value for PCA
    
    Args:
        row(pd.Series): Single row representing a HERV with counts of k-mers
        
    Return:
        row(pd.Series): Row that has k-mer counts divided by number of base pairs
    """
    # Get number of pairs in current row
    pairs_length = len(row[PAIRS])
    
    # Update k-kmer counts
    for i in range(PAIRS + 1, len(row)):
        row.iloc[i] = (row.iloc[i])/pairs_length
    
    return row


# In[ ]:


def combine(file_list, axis = "index"):
    """Combines rows of the files together on the given axis and returns combined data frame
    
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


def main():
    """Main
    """
    # List of files to combine
    file_list = []
    
    # Directory the files are in 
    directory = "/dors/capra_lab/users/yand1/te_ml/data/2018_07_10_pca_te_enhancers/batch_output/"
    
    # Generate list of files with shuffled human genome data to combine
    for i in range(50):
        file_list.append(directory + "shuffle_{}_features_matrix.tsv".format(i))
        
    # Get combined data frame
    combined_df = combine(file_list)
    
    # Normalize counts 
    combined_df = normalize_counts(combined_df)
    
    # Save to new file
    combined_df.to_csv("/dors/capra_lab/users/yand1/te_ml/data/2018_07_10_pca_te_enhancers/shuffled_features_matrix.tsv",
                      header = False, Index = False, sep = '\t')


# In[ ]:


# Call main to run
main()

