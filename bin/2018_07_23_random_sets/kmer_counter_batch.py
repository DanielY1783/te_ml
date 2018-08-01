# Author: Daniel Yan
#
# Email: daniel.yan@vanderbilt.edu
#
# Date: 2018-07-23
#
# Description: Reusable module for counting k-mers from a table and storing
# results in table form.
#
# Command Line Arguments when run as standalone script:
# Argument 1: Name of file containing data file including directory and
# extension.
# Argument 2: Name of file to store new table with counted kmers, including
# directory and extension.


# Libraries
import pandas as pd  # Data manipulation
from reformat_df import normalize
from itertools import product  # For generating all possible 6-mers
import sys  # For getting name of data file as command line argument

# Class values
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/"  # Root directory for project
DATE_DIR = "2018_07_06_genome_shuffle/"  # Directory corresponding to date
k = 6  # Length of "k" value for k-mer
chr_col = 0  # Column with chromosome location
start_col = 1  # Column  start location
end_col = 2  # Column of end location
label_col = 3  # Column with labels
pairs_col = 4  # Column with string of base pairs


def generate_kmers(alphabet="acgt", k=k):
    """
    Generate and return all k-mer from an alphabet.
    :param alphabet: String containing alphabet to generate kmers from.
    Should not contain repeats.
    :param n: Integer length of the kmer
    :return: List containing all kmers.
    """
    # Use product to generate iterator that contains all k-mers
    kmers_iter = product(alphabet, repeat=k)
    # Join all the characters to form a list of strings
    kmers_list = [''.join(i) for i in kmers_iter]
    return kmers_list


def count_kmers(features_df):
    """
    Counts kmers for each row of a data frame and stores counts in columns.
    :param features_df: Data frame containing the base pairs to count. All
    k-mers from the base pairs should contain a corresponding column whose
    name matches the base pair, or the kmer will not be counted. Base pairs
    should be in column PAIRS (4), or error will result.
    :return: Data frame with columns updated to reflect kmer counts.
    """
    features_df = features_df.apply(parse_pairs, axis="columns")
    return features_df


def parse_pairs(row):
    """
    Count the sequence in the row for kmers and update counts of kmers
    :param row: Row to count. Must contain columns of 0's for all kmers. Any
    kmers that do not have a corresponding column name will not be counted.
    :return: Row with kmer counts updated in corresponding columns.
    """
    # Get base pairs in current row
    pairs = row[pairs_col].lower()
    # Find k-mers in base pairs using a sliding window and update count in
    # features matrix
    for i in range(len(pairs) - k + 1):
        # Get the current kmer
        kmer = pairs[i: i + k]
        # Check that the column exists
        if kmer in row:
            # Update corresponding column number in features matrix
            row.loc[kmer] += 1
    return row


def count_file(input_file, output_file, input_header=None,
               output_header=False, sep = '\t'):
    """
    Wrapper for counting all kmers in a table of base pairs stored in a file.
    :param input_file: File containing data table. Columns in file should
    correspond to the variables chr_col, start_col, end_col, labels_col,
    pairs_col in this module.
    :param output_file: File to write table with updated kmer counts.
    :param input_header: Row of header in input_file (default=None)
    :param output_header: Whether to write header in output_file(default=False)
    :param sep: Separator for table in output_file(default='\t)
    :return: None
    """
    # Read in file as pandas dataframe
    input_df = pd.read_table(input_file, header=input_header)

    # Rename columns
    input_df = input_df.rename(
        columns={chr_col: "chr", start_col: "start", end_col: "end",
                 label_col: "label", pairs_col: "pairs"})

    # Generate all possible k-mers
    kmers_list = generate_kmers()

    # Create features matrix with columns as the different kmers
    features_df = input_df.reindex(
        columns=(input_df.columns.tolist() + kmers_list), fill_value=0)

    # Update the features data frame.
    features_df = count_kmers(features_df=features_df)

    # Get list of integer column numbers to normalize
    kmer_cols_list = []
    for kmer in kmers_list:
        kmer_cols_list.append(features_df.columns.get_loc(kmer))
    # Normalize the features data frame by the length of sequences of base
    # pairs.
    normalize(features_df, lengths_col=pairs_col, normalize_cols=kmer_cols_list)

    # Save to output file
    features_df.to_csv(output_file, header=output_header, sep=sep, index=False)

if __name__ == '__main__':
    # Get name of data file to process from command line.
    data_file = sys.argv[1]
    # Get name of file to write to from command line.
    write_file = sys.argv[2]

    # Count kmers in input file and store to output file
    count_file(input_file=data_file, output_file=write_file)
