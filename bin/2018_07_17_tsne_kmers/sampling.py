# Author: Daniel Yan
#
# Date: 2018-07-17
#
# Email: daniel.yan@vanderbilt.edu
#
# Description: Stratified sampling on labeled data in a table format. Each
#  label is given the same number of occurrences within the sample
#
# Preconditions:
# Data file must contain one column named "label" in the header
#  that contains labels for the data.
# All other columns must contain features.
# Data file must not have indices for rows.
#
# Postconditions:
# Stratified sample of data file is written to a new data file with no
# indices. New file has tabs as separator.
#
# Reusable Components:
# statified_sample(df, fraction = 0.1, label_col = "label"): Return a
#  stratified sample from a pandas dataframe.
#
# Command Line Arguments:
# First argument: Name of data file to read from. Include directory and extension.
# Second argument: Name of file to save sampled data to. Include directory
#  and extension.
# Third argument: Number of elements to sample down to.
# Error will result if any argument is invalid.

# Libraries
import pandas as pd # Data
import sys # Command line arguments

def stratified_sample(df, fraction = 0.1, label_col = "label"):
    """
    Return a stratified sample of the pandas dataframe using a column of
    labels to form groups.
    :param df: Pandas data frame to stratify subsample.
    :param fraction: Fraction size of sampled dataframe relative to df
    between 0 and 1(default = 0.1). Value larger than 1 raises exception.
    :param label_col: Name of the column with the labels (default = "label")
    :return: Pandas dataframe with a stratified sample of the original data.
    """
    return df.groupby(label_col).apply(pd.DataFrame.sample,
                                 frac=fraction).reset_index(drop=True)


if __name__ == "__main__":
    # Get name of data file to read from
    data_file = sys.argv[1]
    # Get name of file to save subsampled data to
    write_file = sys.argv[2]
    # Get number of elements to sample
    n_elements = int(sys.argv[3])

    # Read in data file
    print("Reading in data file...")
    data_frame = pd.read_table(data_file)

    # Get fraction of data to retain
    fraction_retain = n_elements / data_frame.shape[0]

    # Get stratified sample
    print("Getting stratified sample...")
    sample_df = stratified_sample(data_frame, fraction=fraction_retain)

    # Save the sample to file
    sample_df.to_csv(write_file, sep = '\t', index=False)