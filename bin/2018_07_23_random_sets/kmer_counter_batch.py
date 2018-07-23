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
chr_col = 0  # Column of chromosome of herv in data file
start_col = 1  # Column of start location of herv in data file
end_col = 2  # Column of end location of herv in data file
label_col = 3  # Label for column
pairs_col = 4  # Column with string of actual pairs within herv


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
    """Counts the repetitions of each k-mer within the row.
    
    Args:
        row(pd.Series): Single row representing a HERV to parse for the
        number of each k-mer.

    Return: 
        row(pd.Series): Row that is updated with count of each k-mer within
        the HERV.
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

def count_file():
    pass


if __name__ == '__main__':
    # Get name of data file to process from command line.
    data_file = sys.argv[1]
    # Get name of file to write to from command line.
    write_file = sys.argv[2]

    # Read in file as pandas dataframe
    hervs_df = pd.read_table(
        DIRECTORY + "data/" + DATE_DIR + "batch_input/" + data_file,
        header=None)

    # Rename columns
    hervs_df = hervs_df.rename(
        columns={chr_col: "chr", start_col: "start", end_col: "end",
                 label_col: "label", pairs_col: "pairs"})

    # Generate all possible k-mers
    kmers_list = generate_kmers()

    # Create features matrix with columns as the different kmers
    features_df = hervs_df.reindex(
        columns=(hervs_df.columns.tolist() + kmers_list), fill_value=0)

    # Update the features matrix by going through all the base pair strings
    # and counting
    # how many times each k-mer appears.
    features_df = count_kmers(features_df=features_df)

    # Normalize features matrix by dividing by length of sequence.
    normalize(features_df, features_df.loc[:, "pairs"],
              features_df.loc[:, "aaaaaa":"tttttt"])

    # Save to file
    features_df.to_csv(
        DIRECTORY + "data/" + DATE_DIR + "batch_output/" + write_file, sep='\t',
        index=False)
