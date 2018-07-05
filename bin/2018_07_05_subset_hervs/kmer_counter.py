
# coding: utf-8

# New version of 
# /dors/capra_lab/users/yand1/te_ml/bin/2018_06_28_kmers_faster/accre/kmer_counter_batch
# for use with data file of mlt1k and enhancer intersect at
# /dors/capra_lab/users/yand1/te_ml/data/2018_07_05_subset_hervs/pairs_mlt1k_enhancers.tsv

# In[1]:


# Libraries
import pandas as pd # Data manipulation 
from itertools import product # For generating all possible 6-mers


# In[2]:


# Class constants
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/" # Root directory for project
DATE_DIR = "2018_07_05_subset_hervs/" # Directory corresponding to date
DATA_FILE = "pairs_mlt1k_enhancers.tsv"
WRITE_FILE = "mlt1k_kmers_features_matrix.tsv" # File to save results to
K = 6 # Length of "k" value for k-mer
CHR = 0 # Column of chromosome of herv in data file
START = 1 # Column of start location of herv in data file
END = 2 # Column of end location of herv in data file
ENHANCER = 3 # Column with enhancer presence
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


# In[ ]:


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


# In[5]:


## Main
def main():
    # Read in file as pandas dataframe
    hervs_df = pd.read_table(DIRECTORY + "data/" + DATE_DIR + DATA_FILE, header = None)
    
    # Rename columns
    hervs_df = hervs_df.rename(columns = {CHR: "chr", START: "start", END: "end", 
                                          ENHANCER: "enhancer", PAIRS: "pairs"})
    
    # Generate all possible k-mers
    kmers_list = generate_kmers()
                                          
    # Create features matrix with columns as the different kmers
    features_df = hervs_df.reindex(columns = (hervs_df.columns.tolist() + kmers_list), 
                                                      fill_value = 0)
                                          
    # Create features matrix containing count of each k-mer from the base pairs data frame
    features_matrix = count_kmers(features_df = features_df)
    
    features_matrix.to_csv(DIRECTORY + "data/" + DATE_DIR + WRITE_FILE, sep = '\t', index = False)


# In[6]:


main() # Call main to run

