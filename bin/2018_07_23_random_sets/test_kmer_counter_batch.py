# Author: Daniel Yan
#
# Email: daniel.yan@vanderbilt.edu
#
# Date: 2018-07-23
#
# Description: Pytests for kmer_counter_batch module.

# Libaries
import kmer_counter_batch
import pytest

# Tests for generate_kmers function
def test_generate_kmers_1():
    kmers_list = kmer_counter_batch.generate_kmers(k=2)
    assert kmers_list == ["aa", "ac", "ag", "at", "ca", "cc", "cg", "ct",
                          "ga", "gc", "gg", "gt", "ta", "tc", "tg", "tt"]

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

