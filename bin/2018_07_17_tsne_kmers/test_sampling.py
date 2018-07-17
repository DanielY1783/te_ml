# Author: Daniel Yan
#
# Date: 2018-07-17
#
# Email: daniel.yan@vanderbilt.edu
#
# Description: Pytests for sampling.py module

from sampling import stratified_sample
import pandas as pd

def stratified_sample_1():
    dict = {"col 1": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            "labels": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]}
    df = pd.DataFrame(data=dict)
    print(df)


stratified_sample_1()