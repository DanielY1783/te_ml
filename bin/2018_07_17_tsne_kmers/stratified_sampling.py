# Author: Daniel Yan
#
# Date: 2018-07-17
#
# Email: daniel.yan@vanderbilt.edu
#
# Description: Stratified sampling on labeled data in a table format.
#
# Preconditions:
# Data file must contain one column named "label" in the header
#  that contains labels for the data.
# All other columns must contain features.
# Data file must not have indices for rows.
#
# Command Line Arguments:
# First argument: Name of data file to read from. Include directory and extension.
# Second argument: Name of file to save sampled data to. Include directory
#  and extension.
# Third argument: Name of file to save count of each label in subsampled data
# Fourth argument: Number of elements to sample down to.
# Error will result if any argument is invalid.

# Libraries
import pandas as pd # Data
import sys # Command line arguments

if __name__ == "__main__":
    # Get name of data file to read from
    data_file = sys.argv[1]
    # Get name of file to save subsampled data to
    write_file = sys.argv[2]
    # Get name of file to save count of each label in subsampled data
    counts_file = sys.argv[3]
    # Get number of elements to sample
    n_elements = int(sys.argv[4])

    # Read in data file
    print("Reading in data file...")
    data_frame = pd.read_table(data_file)

    # Get set of labels in table
    print("Getting set of labels...")
    labels_col = data_frame.loc[:,"label"]
    labels_list = list(set(labels_col))

    # Get total labels for each label
    
