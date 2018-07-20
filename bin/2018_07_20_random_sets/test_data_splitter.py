# Author: Daniel Yan
#
# Email: daniel.yan@vanderbilt.edu
#
# Date: 2018-07-20
#
# Description: pytests for the split_data(df, splits=100) function in
# data_splitter.py

import data_splitter
import pandas as pd


def test_split_data_1():
    dict = {"col 0": [1, 2, 3], "col 1": [5, 20, 15], "col 2": [100, 200, 300],
            "label": ["label 1", "label 2", "label 3"]}
    df = pd.DataFrame(data=dict)
    df_split = data_splitter.split_data(df, splits=1)
    assert df_split[0].equals(df)


def test_split_data_2():
    dict = {"col 0": [1, 2, 3], "col 1": [5, 20, 15], "col 2": [100, 200, 300],
            "label": ["label 1", "label 2", "label 3"]}
    df = pd.DataFrame(data=dict)
    df_split = data_splitter.split_data(df, splits=2)
    dict0 = {"col 0": [1, 2], "col 1": [5, 20], "col 2": [100, 200],
             "label": ["label 1", "label 2"]}
    df0 = pd.DataFrame(data=dict0)
    dict1 = {"col 0": [3], "col 1": [15], "col 2": [300], "label": ["label 3"]}
    df1 = pd.DataFrame(data=dict1)
    assert df_split[0].equals(df0)
    assert df_split[1].equals(df1)


def test_split_data_3():
    dict = {"col 0": [1, 2, 3], "col 1": [5, 20, 15], "col 2": [100, 200, 300],
            "label": ["label 1", "label 2", "label 3"]}
    df = pd.DataFrame(data=dict)
    df_split = data_splitter.split_data(df, splits=0)
    assert df_split == []