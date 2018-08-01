# Author: Daniel Yan
#
# Email: daniel.yan@vanderbilt.edu
#
# Date: 2018-07-20


# Description: Module for splitting data stored in a file in a table format
# into smaller data files by row. If run as a standalone program, it takes a
# an input file name as the first command line argument and a directory to
# write in as the second command line argument.

# Libraries
import pandas as pd  # Data manipulation
import sys  # Command line arguments


def split_data(df, splits=100):
    """
    Splits data frame into a list of smaller data frames

    :param df: Pandas data frame to split
    :param splits: Number of data frames to split into (default = 100)
    :return: List of smaller data frames
    """
    # Create list for return
    smaller_dfs_list = []

    # Store number of rows in data file.
    rows_num = df.shape[0]

    # Split up files
    for i in range(splits):
        start_row = i * (rows_num / splits)
        end_row = (i + 1) * (rows_num / splits)
        temp_df = df.loc[start_row:end_row,]
        # Reset index to prevent errors resulting from different index.
        smaller_dfs_list.append(temp_df.copy().reset_index(drop=True))
    return smaller_dfs_list


def split_files(filename, save_directory, header=None, index=False):
    # Read in files
    df = pd.read_table(filename, header=header)

    # Split data frame into parts.
    df_list = split_data(df)

    # Save to files. Use header if input had header.
    if header is None:
        header_output = False
    else:
        header_output = True
    count = 0
    for df in df_list:
        df.to_csv(save_directory + str(count) + ".tsv", sep='\t', index=False,
                  header=header_output)
        count += 1


if __name__ == "__main__":
    filename = sys.argv[1]
    save_directory = sys.argv[2]
    split_files(filename, save_directory)
