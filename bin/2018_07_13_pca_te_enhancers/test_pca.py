# Name: Daniel Yan
# Date: 2018-07-13
# Email: daniel.yan@vanderbilt.edu

# Tests on functions within pca.py module

import pca
import pandas as pd

def test_label_coordinates_1():
    # Create pandas dataframe for testing
    dict_1 = {"col 0": [1, 2, 3],
              "col 1": [5, 20, 15],
              "col 2": [100, 200, 300]}
    df_1 = pd.DataFrame(data = dict_1)

    df_1_labels = pd.DataFrame(["label 1", "label 2", "label 3"])

    dict_1_correct = {"col 0": [1, 2, 3],
                      "col 1": [5, 20, 15],
                      "col 2": [100, 200, 300],
                      "label": ["label 1", "label 2", "label 3"]}
    df_1_correct = pd.DataFrame(data=dict_1_correct)

    # Test that labels work correctly
    labled_1 = pca.label_coordinates(df_1, labels = df_1_labels)
    assert labled_1.equals(df_1_correct)

def test_label_coordinates_2():
    # Create pandas dataframe for testing
    dict_2 = {"col 0": [1, 2, 3],
              "col 1": [5, 20, 15],
              "col 2": [100, 200, 300]}
    df_2 = pd.DataFrame(data = dict_2)

    df_2_labels = pd.DataFrame(["label 1", "label 2"])

    # Test with missing label
    dict_2_correct = {"col 0": [1, 2, 3],
                      "col 1": [5, 20, 15],
                      "col 2": [100, 200, 300],
                      "label": ["label 1", "label 2", None]}
    df_2_correct = pd.DataFrame(data=dict_2_correct)

    # Test that labels work correctly
    labled_2 = pca.label_coordinates(df_2, labels = df_2_labels)
    assert labled_2.equals(df_2_correct)