
# coding: utf-8

# kmer_counter_batch is a modified version of a similar file at
# /dors/capra_lab/users/yand1/te_ml/bin/2018_06_28_kmers_faster/accre
# This one processes data at:
# /dors/capra_lab/users/yand1/te_ml/data/2018_07_03_pca_te_enhancers/batch_input
# by taking in a command line argument and counting kmers, normalizing counts, and saving to
# /dors/capra_lab/users/yand1/te_ml/data/2018_07_03_pca_te_enhancers/batch_output

# In[1]:


# Libraries
import pandas as pd # Data manipulation 
from itertools import product # For generating all possible 6-mers
import sys # For getting name of data file as command line argument


# In[2]:


# Class constants
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/" # Root directory for project
K = 6 # Length of "k" value for k-mer
CHR = 0 # Column of chromosome of herv in data file
START = 1 # Column of start location of herv in data file
END = 2 # Column of end location of herv in data file
LABEL = 3 # Column with label of herv, enhancer, or herv_enhancer intersection
PAIRS = 4 # Column with string of actual pairs within herv
ALPHABET = "acgt" # Alphabet of base pairs in k-mers


# In[3]:


def generate_kmers():
    """Return all combinations of k-mers in alphabet to use as features.
    
    Return: 
        kmers_list(list): List that contains strings of all possible k-mers
        from the given "k" value and alphabet
    """
    # Use product to generate iterator that contains all k-mers
    kmers_iter = product(ALPHABET, repeat = K)
    # Join all the characters to form a list of strings
    kmers_list = [''.join(i) for i in kmers_iter]
    return kmers_list


# In[4]:


def count_kmers(features_df):
    """Applies counting repetitions of kmers to the entire data frame.
        
    Args:
        features_df(pd.DataFrame): Data frames containing the base pairs to be updated.
        
    Return:
        features_df(pd.DataFrame): Data frame with columns of k-mers updated to reflect 
                                counts within base pairs to use as features matrix.
    """
    features_df = features_df.apply(parse_pairs, axis = "columns")
    return features_df


# In[5]:


def parse_pairs(row):
    """Counts the repetitions of each k-mer within the row.
    
    Args:
        row(pd.Series): Single row representing a HERV to parse for the number of each k-mer.

    Return: 
        row(pd.Series): Row that is updated with count of each k-mer within the HERV.
    """
    # Get base pairs in current row
    pairs = row[PAIRS]
    # Find k-mers in base pairs using a sliding window and update count in features matrix
    for i in range(len(pairs) - K):
        kmer = pairs[i: i + K]
        # Check that the column exists
        if kmer in row:
            # Update corresponding column number in features matrix
            row.loc[kmer] += 1
    return row


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


# In[6]:


## Main
def main():
    # Get name of data file to process from command line.
    data_file = sys.argv[1]
    # File to write features matrix to. Remove ".tsv" from the original first, then add new ending.
    write_file = data_file[:-4] + "_features_matrix.tsv" 
    
    # Read in file as pandas dataframe
    hervs_df = pd.read_table(DIRECTORY + "data/2018_07_03_pca_te_enhancers/batch_input/" +
                             data_file)
    
    # Generate all possible k-mers
    kmers_list = generate_kmers()
                                          
    # Create features matrix with columns as the different kmers
    features_df = hervs_df.reindex(columns = (hervs_df.columns.tolist() + kmers_list), 
                                                      fill_value = 0)
    
    # Update the features matrix by going through all the base pair strings and counting
    # how many times each k-mer appears.
    features_df = count_kmers(features_df = features_df)
    
    # Normalize counts by dividing kmer counts in each row by the number of bases
    features_df = features_df.apply(normalize_row, axis = "columns")
    
    # Save to file
    features_df.to_csv(DIRECTORY + "data/2018_07_03_pca_te_enhancers/batch_output/" + write_file, 
                       sep = '\t', index = False)


# In[7]:


main() # Call main to run

