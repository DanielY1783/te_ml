
# coding: utf-8

# Counts k-mers for each herv by reading in file with base pairs for HERVs at /dors/capra_lab/users/yand1/te_ml/data/2018_06_26_kmers_hervs_chromehmm/hervs_hg19.tsv
# and creating a count for each k-mer and saving to 
# /dors/capra_lab/users/yand1/te_ml/data/2018_06_27_kmers_hervs_chromehmm/hervs_kmers_features_matrix.tsv

# In[1]:


# Libraries
import pandas as pd # Data manipulation 
from itertools import product # For generating all possible 6-mers


# In[2]:


# Class constants
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/" # Root directory for project
DATE = "2018_06_27_kmers_hervs_chromehmm/"
LOCATION = "accre/" # Local machine or accre cluster.
DATA_FILE = "hervs_hg19.tsv"
WRITE_FILE = "hervs_kmers_features_matrix.tsv" # File to save results to
K = 6 # Length of "k" value for k-mer
CHR = 0 # Column of chromosome of herv in data file
START = 1 # Column of start location of herv in data file
END = 2 # Column of end location of herv in data file
PAIRS = 3 # Column with string of actual pairs within herv
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


def count_kmers(pairs_df, kmers_list):
    """Counts the repetitions of each k-mer within each row of the dataframe
        by using a sliding window and storing results to corresponding column.
        
    Args:
        herv_df(pd.DataFrame): Data frames containing the base pairs for each HERV.
        kmers_list: List containing strings for all possible k-mers.
        
    Return:
        features_df(pd.DataFrame): New data frame with columns of k-mers updated to 
            reflect counts within base pairs to use as features matrix.
    """
    # Add all kmers from kmers_list as columns for new features matrix,
    # with values default initialized to 0. Drop pairs column.
    features_df = pairs_df.copy().reindex(columns = (pairs_df.columns.tolist() + kmers_list), 
                                                      fill_value = 0)
    features_df = features_df.drop("pairs", axis = "columns")
    
    # Counter for tracking row on features_df
    #counter = 0
    
    # Iterate over pairs_df to update features_df
    for index, row in pairs_df.iterrows():
        # Get base pairs in current row
        pairs = row["pairs"]
        
        # Find k-mers in base pairs using a sliding window and update count in features matrix
        for i in range(len(pairs) - K):
            kmer = pairs[i: i + K]
            # Get corresponding column number in features matrix
            column_number = features_df.columns.get_loc(kmer)
            # Update features matrix
            features_df.iloc[index, column_number] += 1
            
        # Increment counter
        #counter += 1
    
    return features_df


# In[5]:


## Main
def main():
    # Read in file as pandas dataframe
    hervs_df = pd.read_table(DIRECTORY + "data/" + "2018_06_26_kmers_hervs_chromehmm/" + DATA_FILE, header = None)
    
    # Rename columns
    hervs_df = hervs_df.rename(columns = {CHR: "chr", START: "start", END: "end", PAIRS: "pairs"})
    
    # Generate all possible k-mers
    kmers_list = generate_kmers()
                                          
    # Create features matrix containing count of each k-mer from the base pairs data frame
    features_matrix = count_kmers(pairs_df = hervs_df, kmers_list = kmers_list)
    
    features_matrix.to_csv(DIRECTORY + "data/" + "2018_06_27_kmers_hervs_chromehmm/" + WRITE_FILE, sep = '\t', index = False)


# In[6]:


main() # Call main to run

