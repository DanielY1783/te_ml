
# coding: utf-8

# New version of /dors/capra_lab/users/yand1/te_ml/bin/2018_06_29_kmers_enhancer_intersect/reformat_hervs_intersect enhancers.py
# This program takes in
# /dors/capra_lab/users/yand1/te_ml/data/2018_07_05_subset_hervs/enhancers_mlt1k_intersect.tsv
# and changes overlap to boolean value: 1 for overlap between transposable element and enhancer; 0 for no overlap.

# In[ ]:


# Libraries
import pandas as pd


# In[ ]:


# Class constants
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/"
DATE_INFO = "2018_07_05_subset_hervs/" # Directory associated with date
DATA_FILE = "enhancers_mlt1k_intersect.tsv"
REFORMATTED_DATA_FILE = "reformatted_enhancers_mlt1k_intersect.tsv" # New data file to write to
HERV_TYPE = 3 # Column with type of HERV
CHR_INTERSECT= 4 # Column of chromosome of intersection
START_INTERSECT = 5 # Column of start location of intersection
END_INTERSECT = 6 # Column of end location of intersection
ENHANCER_INFO = 7 # Column with intersection of enhancer


# In[ ]:


def main():
    """Main function
    """
    # Read in data frame
    features_df = pd.read_table(DIRECTORY + "data/" + DATE_INFO + DATA_FILE, header = None)
    
    # Change 1 for overlap, -1 for no overlap
    features_df.iloc[:,CHR_INTERSECT] = (features_df.iloc[:,CHR_INTERSECT].apply
                                         (lambda x: 0 if x == "." else 1))
    
    # Drop unneeded columns
    features_df.drop([HERV_TYPE, START_INTERSECT, END_INTERSECT, ENHANCER_INFO],
                     axis ="columns", inplace = True)
    
    # Rename columns
    features_df.columns = ["chr", "start", "end", "enhancer"]
    
    # Get count of number of overlaps and save to file.
    overlaps = features_df.loc["enhancer"].sum()
    with open(DIRECTORY + "results/" + DATE_INFO + "count_overlaps.txt", mode = "w+") as file:
        file.write("Overlaps: " + str(overlaps) + '\n')
        file.write("No overlaps: " + str(features_df.shape[0] - overlaps) + '\n')
    

    # Rename columns
    features_df.columns = ["chr", "start", "end", "enhancer"]
    
    # Save to file.
    features_df.to_csv(DIRECTORY + "data/" + DATE_INFO + REFORMATTED_DATA_FILE, 
                       index = False, sep = '\t')


# In[ ]:


main()

