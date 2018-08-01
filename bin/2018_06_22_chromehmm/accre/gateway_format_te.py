
# coding: utf-8

# Converts old file (/dors/capra_lab/users/yand1/te_ml/data/2018_06_21_chromehmm_te/all_TE_fimo_out.txt) with overlap between transposable elements and transcription factors to
# a new file (/dors/capra_lab/users/yand1/te_ml/data/2018_06_22_chromehmm/te_tf_intersect_formatted.tsv) with different column order and some columns removed/reformatted.

# In[1]:


# Import needed libaries
import re # For string splitting


# In[2]:


# Class constants
DATE = "2018_06_22_chromehmm/" 
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/" # Root directory
DATA_FILE = "all_TE_fimo_out.txt" # Name of data file to process
TF_NAME_OLD = 0 # Column of transcription factor name in the old file
TE_NAME_OLD = 1 # Column of transposable element in the old file
TE_LOCATION_OLD = 2 # Column location string of the transposable element in the old file
TF_START_OLD = 3 # Column with transcription factor start location offset in the old file
TF_END_OLD = 4 # Column with transcription factor end location offset in the old file


# In[3]:


## Main

# Open the file to process
data_file = open(DIRECTORY + "data/" + "2018_06_21_chromehmm_te/" + DATA_FILE, "r")

# Open the file to write to
write_file = open(DIRECTORY + "data/" + DATE + "te_formatted.tsv", "w+")

count = 0;

# Go through all lines in the file
for line in data_file:
    # Get a list of values for each columns split by whitespace.
    values_list = line.split()
    
    # Get the string with the location of transposable element
    te_location_str = values_list[TE_LOCATION_OLD]
    # Get chromsome, start, and end of transposable element
    te_location_list = re.split(":|-", te_location_str)
    # Store the string for the chromosome, start, and end of transposable element
    chromosome_str = te_location_list[0]
    te_start_int = int(te_location_list[1])
    te_end_int = int(te_location_list[2])
    
    # Truncate chromosome string if needed
    if (len(chromosome_str) > 5):
        chromosome_str = chromosome_str[0:5]
    
    # Get the start location of transcription factor by adding offset and then subtracting 1
    # because of 1 based indexing
    tf_start_int = te_start_int + int(values_list[TF_START_OLD]) - 1
    # Get the end location of transcription factor by adding offset. No need to subtract
    # 1 for 1 based indexing because original index is inclusive, and new index is exclusive
    tf_end_int = te_start_int + int(values_list[TF_END_OLD])
    
    # Print chromosome of transcription factor to column 0 of new file
    write_file.write(chromosome_str + '\t')
    # Print start location of transcription factor to column 1 of new file
    write_file.write(str(tf_start_int) + '\t')
    # Print end location of transcription factor to column 2 of new file
    write_file.write(str(tf_end_int) + '\t')
    # Print the transcription factor name to column 3 of new file
    write_file.write(values_list[TF_NAME_OLD] + '\t')
    # Print the chromosome of the transposable element to column 4 of new file
    write_file.write(chromosome_str + '\t')
    # Print the start location of transposable element to column 5 of new file
    write_file.write(str(te_start_int) + '\t')
    # Print the end location of transposable element to column 6 of new file
    write_file.write(str(te_end_int) + '\t')
    # Print the name of the transposable element to column 7 of new file (last column)
    write_file.write(values_list[TE_NAME_OLD] + '\n')
    
# Close the files
data_file.close()
write_file.close()

