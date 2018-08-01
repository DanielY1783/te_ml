# Name: Daniel Yan
# Email: daniel.yan@vanderbilt.edu

# Libaries
import reformat_df
import pandas as pd
import pytest

# Check that all columns can be normalized
def test_normalize_1():
    # Create pandas dataframe for testing
    dict_1 = {"col 0": [1, 2, None],
              "col 1": [5, 20, 15],
              "col 2": ["a", "tg", "ctatg"],
              "col 3": [100, 200, 300]}
    df_1 = pd.DataFrame(data = dict_1)

    dict_1_norm = {"col 0": [1.0, 1.0, None],
                   "col 1": [5.0, 10.0, 3.0],
                   "col 2": ["a", "tg", "ctatg"],
                   "col 3": [100.0, 100.0, 60.0]}
    df_1_normalized = pd.DataFrame(data = dict_1_norm)

    # Test normalize function
    reformat_df.normalize(df_1, 2, [0, 1, 3])
    assert df_1.equals(df_1_normalized)

# Check that exception is thrown for invalid column
def test_normalize_2():
    # Create pandas dataframe for testing
    dict_2 = {"col 0": [1, 2, None],
              "col 1": [5, 20, 15],
              "col 2": ["", "tg", "ctatg"],
              "col 3": [100, 200, 300]}
    df_2 = pd.DataFrame(data=dict_2)

    with pytest.raises(Exception):
        reformat_df.normalize(df_2, 4, [0, 1, 3])

# Check that one column can be normalized while others are not
def test_normalize_3():
    # Create pandas dataframe for testing
    dict_3 = {"col 0": [1, 2, 3],
              "col 1": [5, 20, 15],
              "col 2": ["a", "tg", "ctatg"],
              "col 3": [100, 200, 300]}
    df_3 = pd.DataFrame(data = dict_3)

    dict_3_norm = {"col 0": [1, 2, 3],
                   "col 1": [5.0, 10.0, 3.0],
                   "col 2": ["a", "tg", "ctatg"],
                   "col 3": [100, 200, 300]}
    df_3_normalized = pd.DataFrame(data = dict_3_norm)

    # Test normalize function
    reformat_df.normalize(df_3, 2, [1])
    assert df_3.equals(df_3_normalized)


# Check that exception is thrown for invalid column
def test_normalize_4():
    # Create pandas dataframe for testing
    dict_4 = {"col 0": [1, 2, None],
              "col 1": [5, 20, 15],
              "col 2": ["", "tg", "ctatg"],
              "col 3": [100, 200, 300]}
    df_4 = pd.DataFrame(data=dict_4)

    with pytest.raises(Exception):
        reformat_df.normalize(df_4, 4, [0, 1, 3])
