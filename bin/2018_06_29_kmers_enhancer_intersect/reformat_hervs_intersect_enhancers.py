
# coding: utf-8

# Changes columns of /dors/capra_lab/users/yand1/te_ml/data/2018_06_29_kmers_enhancers_intersect/hervs_kmers_intersect_enhancers.tsv 
# so that overlap of enhancers and hervs is a single boolean value in the last column; 1 for overlap, 0 for no overlap. Result is stored to:
# /dors/capra_lab/users/yand1/te_ml/data/2018_06_29_kmers_enhancers_intersect/reformatted_hervs_kmers_intersect_enhancers.tsv 

# In[ ]:


# Libraries
import pandas as pd


# In[ ]:


# Class constants
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/"
DATE_INFO = "2018_06_29_kmers_enhancers_intersect/"
DATA_FILE = "hervs_kmers_intersect_enhancers.tsv"
REFORMATTED_DATA_FILE = "reformatted_hervs_kmers_intersect_enhancers.tsv" # New data file to write to
COLUMN_NAMES_FILE = "header_names.txt" # File with column names
CHR_INTERSECT= 4099 # Column of chromosome of intersection
START_INTERSECT = 4100 # Column of start location of intersection
END_INTERSECT = 4101 # Column of end location of intersection
ENHANCER_INFO = 4102 # Column with intersection of enhancer


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
    features_df.drop([START_INTERSECT, END_INTERSECT, ENHANCER_INFO], axis ="columns", inplace = True)
    
    # Get count of number of overlaps and save to file.
    overlaps = features_df.iloc[:,CHR_INTERSECT].sum()
    with open(DIRECTORY + "results/" + DATE_INFO + "count_overlaps.txt", mode = "w+") as file:
        file.write("Overlaps: " + str(overlaps) + '\n')
        file.write("No overlaps: " + str(features_df.shape[0] - overlaps) + '\n')
    
    # Rename columns using file with column names.
    with open(DIRECTORY + "data/" + DATE_INFO + COLUMN_NAMES_FILE, mode = "r") as file:
        # Read in file
        lines_list = file.readlines()
        # List to store column names
        column_names = []
        
        # Get the column name using split
        for line in lines_list:
            column_names.append(line.split(': ')[1].strip())
            
        # Add in enhancer overlap as column name
        column_names.append("enhancer")
        # Rename columns
        features_df.columns = column_names
    
    # Save data frame.
    features_df.to_csv(DIRECTORY + "data/" + DATE_INFO + REFORMATTED_DATA_FILE, 
                       index = False, sep = '\t')


# In[ ]:


main()

