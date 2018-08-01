# Author: Daniel Yan
#
# Email: daniel.yan@vanderbilt.edu
#
# Date: 2018-07-23
#
# Description: Pytests for kmer_counter_batch module.

# Libaries
import kmer_counter_batch
import pandas as pd
import pytest


# Tests for generate_kmers function
def test_generate_kmers_1():
    kmers_list = kmer_counter_batch.generate_kmers(k=2)
    assert kmers_list == ["aa", "ac", "ag", "at", "ca", "cc", "cg", "ct", "ga",
                          "gc", "gg", "gt", "ta", "tc", "tg", "tt"]


def test_generate_kmers_2():
    kmers_list = kmer_counter_batch.generate_kmers(alphabet="1!", k=2)
    assert kmers_list == ["11", "1!", "!1", "!!"]


def test_generate_kmers_3():
    kmers_list = kmer_counter_batch.generate_kmers(alphabet="")
    assert kmers_list == []


def test_generate_kmers_4():
    kmers_list = kmer_counter_batch.generate_kmers(k=0)
    assert kmers_list == [""]


def test_generate_kmers_5():
    with pytest.raises(Exception):
        kmers_list = kmer_counter_batch.generate_kmers(k=-1)


## Tests for count_kmers function
def test_count_kmers_1():
    dict = {"chr": ["chr1", "chr2"], "start": [1235, 4325], "end": [1465, 4562],
            "label": ["random_enhancers", "random_herv_enhancer_intersect"],
            "pairs": ["atte", "tatat"], "aa": [0, 0], "at": [0, 0],
            "ta": [0, 0], "tt": [0, 0]}
    df = pd.DataFrame(data=dict)
    dict_counted = {"chr": ["chr1", "chr2"], "start": [1235, 4325],
                    "end": [1465, 4562],
                    "label": ["random_enhancers",
                              "random_herv_enhancer_intersect"],
                    "pairs": ["atte", "tatat"], "aa": [0, 0], "at": [1, 2],
                    "ta": [0, 2], "tt": [1, 0]}
    df_counted = pd.DataFrame(data=dict_counted)
    kmer_counter_batch.k = 2  # Set k to 2 for easier quick testing.
    df = kmer_counter_batch.count_kmers(df)
    kmer_counter_batch.k = 6  # Set k back to 6
    assert df.equals(df_counted)

# Test that invalid value for base pairs raises an exception.
def test_count_kmers_2():
    dict = {"chr": ["chr1", "chr2"], "start": [1235, 4325], "end": [1465, 4562],
            "label": ["random_enhancers", "random_herv_enhancer_intersect"],
            "pairs": [True, False], "aa": [0, 0], "at": [0, 0],
            "ta": [0, 0], "tt": [0, 0]}
    df = pd.DataFrame(data=dict)
    with pytest.raises(Exception):
            kmer_counter_batch.count_kmers(df)
