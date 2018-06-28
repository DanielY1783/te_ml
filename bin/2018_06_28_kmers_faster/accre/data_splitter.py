
# coding: utf-8

# Splits the HERV data at /dors/capra_lab/users/yand1/te_ml/data/2018_06_26_kmers_hervs_chromehmm/hervs_hg19.tsv 
# into smaller files, with the number of the file appended before .tsv
# (for example, hervs_hg19_1.tsv)
# Smaller files are saved to /dors/capra_lab/users/yand1/te_ml/data/2018_06_28_kmers_faster/batch_input

# In[1]:


# Libraries
import pandas as pd # Data manipulation 


# In[2]:


# Class constants
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/" # Root directory for project
DATE = "2018_06_28_kmers_faster/"
DATA_FILE = "hervs_hg19.tsv"
SPLITS = 100 # Number of files to make


# In[3]:


def main():
    # Read in file as pandas dataframe
    hervs_df = pd.read_table(DIRECTORY + "data/" + "2018_06_26_kmers_hervs_chromehmm/" + DATA_FILE, header = None)
    
    # Store number of rows in data file.
    rows_num = hervs_df.shape[0]
    
    # Split data frame into parts.
    for i in range(SPLITS):
        start_row = i * (rows_num/SPLITS)
        end_row = (i + 1) * (rows_num/SPLITS)
        temp_df = hervs_df.loc[start_row:end_row,]
        # Save to file
        temp_df.to_csv(DIRECTORY + "data/" + DATE + "/batch_input/hervs_hg19_" + str(i) + ".tsv", 
                       sep = '\t', index = False)


# In[4]:


# Call main to run
main()

