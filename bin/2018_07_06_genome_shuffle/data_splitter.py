
# coding: utf-8

# Modified version of similar file at /dors/capra_lab/users/yand1/te_ml/bin/2018_06_28_kmers_faster/accre

# In[1]:


# Libraries
import pandas as pd # Data manipulation 


# In[2]:


# Class constants
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/" # Root directory for project
DATE_DIR = "2018_07_06_genome_shuffle/" # Directory related to date
DATA_FILE = "all_pairs.tsv"
SPLITS = 100 # Number of files to make


# In[3]:


def main():
    # Read in file as pandas dataframe
    hervs_df = pd.read_table(DIRECTORY + "data/" + DATE_DIR + DATA_FILE, header = None)
    
    # Store number of rows in data file.
    rows_num = hervs_df.shape[0]
    
    # Split data frame into parts.
    for i in range(SPLITS):
        start_row = i * (rows_num/SPLITS)
        end_row = (i + 1) * (rows_num/SPLITS)
        temp_df = hervs_df.loc[start_row:end_row,]
        # Save to file
        temp_df.to_csv(DIRECTORY + "data/" + DATE_DIR + "/batch_input/shuffle_" + str(i) + ".tsv", 
                       sep = '\t', index = False, header = False)


# In[4]:


# Call main to run
main()

