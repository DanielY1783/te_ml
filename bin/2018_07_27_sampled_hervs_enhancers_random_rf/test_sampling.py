# Author: Daniel Yan
#
# Date: 2018-07-17
#
# Email: daniel.yan@vanderbilt.edu
#
# Description: Pytests for sampling.py module

from sampling import stratified_sample
import pandas as pd
import pytest

# Tests for the stratified_sample function in sampling.py

# Check that taking 1/4 of data works correctly
def test_stratified_sample_1():
    dict = {"col 1": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            "label": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]}
    df = pd.DataFrame(data=dict)
    sampled_df = stratified_sample(df, fraction = 0.25)
    assert len(sampled_df.loc[sampled_df.loc[:,"label"] == 0]) == 1
    assert len(sampled_df.loc[sampled_df.loc[:,"label"] == 1]) == 2

# Check that taking 1/2 of data works correctly
def test_stratified_sample_2():
    dict = {"col 1": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            "label": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]}
    df = pd.DataFrame(data=dict)
    sampled_df = stratified_sample(df, fraction = 0.5)
    assert len(sampled_df.loc[sampled_df.loc[:,"label"] == 0]) == 2
    assert len(sampled_df.loc[sampled_df.loc[:,"label"] == 1]) == 4

# Check that taking all of data works correctly
def test_stratified_sample_3():
    dict = {"col 1": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            "label": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]}
    df = pd.DataFrame(data=dict)
    sampled_df = stratified_sample(df, fraction = 1)
    assert sampled_df.shape == df.shape

# Check that taking small fraction of data results in no data in sample
def test_stratified_sample_4():
    dict = {"col 1": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            "label": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]}
    df = pd.DataFrame(data=dict)
    sampled_df = stratified_sample(df, fraction = 0.0001)
    assert len(sampled_df.loc[sampled_df.loc[:,"label"] == 0]) == 0
    assert len(sampled_df.loc[sampled_df.loc[:,"label"] == 1]) == 0

# Check that doubling data raises exception
def test_stratified_sample_5():
    dict = {"col 1": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            "label": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]}
    df = pd.DataFrame(data=dict)
    with pytest.raises(Exception):
        sampled_df = stratified_sample(df, fraction = 2)
