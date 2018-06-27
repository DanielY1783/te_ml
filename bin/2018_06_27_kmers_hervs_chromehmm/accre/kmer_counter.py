
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
ALPHABET = "actg" # Alphabet of base pairs in k-mers


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


# In[ ]:


# def count_kmers():
    


# In[ ]:


## Main
def main():
    # Read in file as pandas dataframe
    hervs_df = pd.read_table(DIRECTORY + "data/" + "2018_06_26_kmers_hervs_chromehmm/" + DATA_FILE, header = None)
    
    # Rename columns
    hervs_df = hervs_df.rename(columns = {CHR: "chr", START: "start", END: "end", PAIRS: "pairs"})
    
    # Generate all possible k-mers
    kmers_list = generate_kmers()
    
    # Add all kmers from kmers_list as columns, with values default initialized to 0.
    hervs_df = hervs_df.reindex(columns = (hervs_df.columns.tolist() + kmers_list), fill_value = 0)
    hervs_df.head().to_csv("test.tsv", sep = '\t', index = False)
    
#     # Get the count of each kmer from the base pairs
#     hervs_df = count_kmers(hervs_df)


# In[ ]:


main() # Call main to run

