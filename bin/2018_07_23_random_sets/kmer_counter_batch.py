# Author: Daniel Yan
#
# Email: daniel.yan@vanderbilt.edu
#
# Date: 2018-07-23
#
# Description: Reusable module for counting k-mers from a table and storing
# results in table form.


# Libraries
import pandas as pd  # Data manipulation
from reformat_df import normalize
from itertools import product  # For generating all possible 6-mers
import sys  # For getting name of data file as command line argument

# Class constants
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/"  # Root directory for project
DATE_DIR = "2018_07_06_genome_shuffle/"  # Directory corresponding to date
K = 6  # Length of "k" value for k-mer
CHR = 0  # Column of chromosome of herv in data file
START = 1  # Column of start location of herv in data file
END = 2  # Column of end location of herv in data file
LABEL = 3  # Label for column
PAIRS = 4  # Column with string of actual pairs within herv
ALPHABET = "acgt"  # Alphabet of base pairs in k-mers


def generate_kmers(alphabet="acgt", k=6):
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
    """Applies counting repetitions of kmers to the entire data frame.
        
    Args:
        features_df(pd.DataFrame): Data frames containing the base pairs to
        be updated.
        
    Return:
        features_df(pd.DataFrame): Data frame with columns of k-mers updated
        to reflect
                                counts within base pairs to use as features
                                matrix.
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
    pairs = row[PAIRS].lower()
    # Find k-mers in base pairs using a sliding window and update count in
    # features matrix
    for i in range(len(pairs) - K):
        kmer = pairs[i: i + K]
        # Check that the column exists
        if kmer in row:
            # Update corresponding column number in features matrix
            row.loc[kmer] += 1
    return row


if __name__ == '__main__':
    # Get name of data file to process from command line.
    data_file = sys.argv[1]
    # File to write features matrix to. Remove ".tsv" from the original
    # first, then add new ending.
    write_file = data_file[:-4] + "_features_matrix.tsv"

    # Read in file as pandas dataframe
    hervs_df = pd.read_table(
        DIRECTORY + "data/" + DATE_DIR + "batch_input/" + data_file,
        header=None)

    # Rename columns
    hervs_df = hervs_df.rename(
        columns={CHR: "chr", START: "start", END: "end", LABEL: "label",
                 PAIRS: "pairs"})

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
