
# coding: utf-8

# Drops duplicate hervs from the file /dors/capra_lab/users/yand1/te_ml/data/2018_06_25_kmers_hervs/full_hervs.tsv
# by looking at chromosome, start, end, and herv name. Stores the new
# data frame with these four columns to 
# /dors/capra_lab/users/yand1/te_ml/data/2018_06_25_kmers_hervs/no_dups_hervs.tsv

# In[ ]:


# Libraries
import pandas as pd


# In[ ]:


# Class constants
DATE = "2018_06_26_kmers_hervs_chromehmm/" 
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/" # Root directory
DATA_FILE = "full_hervs.tsv" # Name of data file to process
WRITE_FILE = "no_dups_hervs.tsv" # Name of file to write to
CHROMOSOME = 0 # Column for the chromosome number of transposable element
START = 1 # Column for the start location of transposable element
END = 2 # Column for the end location of transposable element
HERV = 3 # Column for the transposable element of class HERV/ERV


# In[ ]:


## Main
def main:
    herv_df = pd.read_table((DIRECTORY + "data/" + "2018_06_25_kmers_hervs/"  + DATA_FILE), header = None) # Old data frame
    new_herv_df = pd.DataFrame(columns = ["chr", "start", "end", "herv"])
    new_herv_df["chr"] = herv_df.iloc[:,CHROMOSOME]
    new_herv_df["start"] = herv_df.iloc[:,START]
    new_herv_df["end"] = herv_df.iloc[:,END]
    new_herv_df["herv"] = herv_df.iloc[:,HERV]

    # Delete repeats from the data frame.
    no_dups_df = new_herv_df.drop_duplicates()

    # Save to file
    no_dups_df.to_csv(DIRECTORY + "data/" + DATE + WRITE_FILE, sep = '\t', index = False)


# In[ ]:


main()

