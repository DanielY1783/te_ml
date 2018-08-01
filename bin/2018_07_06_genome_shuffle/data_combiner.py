
# coding: utf-8

# Combines files containing rows with the same column together either on the rows or columns. Output file has no index.
# 
# Combine can be used a module or standalone script.

# In[ ]:


"""
Combines files containing rows with the same column together either on the rows or columns.

Functions:
    combine(file_list, header, output_file, axis, sep ='\t', index = False): Combines files.
"""


# In[ ]:


# Libraries
import pandas as pd


# In[ ]:


def combine(file_list, header, output_file, axis, sep ='\t', index = False):
    """Combines rows of the files together on the given axis and saves to output_file.
    Output file has header if input had header. No index in output file.
    
    Args:
        file_list(list): List of files with same columns
        header(boolean): True if the files have a header, false otherwise
        output_file(string): Name of file to save to
        axis(string): Concatenate on rows or columns
        sep(string): Seperator for columns in output file
        index(boolean): True if output file needs index, false otherwise 
    """
    # List to store all the data frames to concatenate
    frames_list = []
    
    # Open files and save files differently depending on if there is a header
    if header:
        # Read in all files
        for file in file_list:
            frames_list.append(pd.read_table(file))
    else:
        # Read in all files
        for file in file_list:
            frames_list.append(pd.read_table(file, header = None))
            
    # Combine and save
    pd.concat(frames_list, axis = axis).to_csv(output_file, sep = sep,
                                                index = index, header = header)
        


# In[ ]:


if __name__ == "__main__":
    file_list = []
    for i in range(100):
        file_list.append("/dors/capra_lab/users/yand1/te_ml/data/2018_07_06_genome_shuffle/batch_output/shuffle_{}_features_matrix.tsv".format(i))
    combine(file_list = file_list, header = True, 
            output_file = "/dors/capra_lab/users/yand1/te_ml/data/2018_07_06_genome_shuffle/all_pairs_features_matrix.tsv",
            axis = "index")

