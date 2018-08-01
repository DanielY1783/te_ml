# Author: Daniel Yan
#
# Email: daniel.yan@vanderbilt.edu
#
# Date: 2018-07-19
#
# Description: Random forest classifier of enhancers overlap
# with transposable elements based on transcription factors as features. 0
# represents no overlap; 1 represents overlap in labels. Add custom weights
# to try to prevent classifier from predicting too many negatives.
#
# Command Line Arguments:
# 1. Name of data file with features, including directory and extension.
# 2. Name of data file with labels to predict
# 3. Directory to store output files to. End with backslash.
#
# Preconditions:
# 1. Features data file must include header names in first row and no indices
# 2. Labels data file must not include a header.
#
# Postconditions:
# Files containing predictions from the random forest classifier
# are written to the directory passed as third parameter.


# Libraries
import ml_predict  # Wrappers for scikit learn machine learning models
import numpy as np  # For ravel
import pandas as pd  # Data manipulation
from sklearn.ensemble import RandomForestClassifier  # Random forest
from sklearn.model_selection import GridSearchCV  # Grid search
from sklearn.model_selection import train_test_split  # For data splitting
import sys  # Command line arguments

# Constants
CV = 10  # Cross validation folds
WEIGHTS ={0: 1, 1: 10000000} # Class weights for penalization

if __name__ == '__main__':
    # Read in name of features file
    features_file = sys.argv[1]
    # Read in name of data file with things to predict.
    predictors_file = sys.argv[2]
    # Read in name of directory to write results to
    output_directory = sys.argv[3]

    # Read in features file with headers in row 0
    print("Reading in data files")
    x_df = pd.read_table(features_file, header=0)
    # Get labels to predict
    y_df = pd.read_table(predictors_file, header=None)
    y_df = y_df.values.ravel()

    # Train test split
    x_train, x_test, y_train, y_test = train_test_split(x_df, y_df)

    # Create random forest classifier
    print("Creating random forest classifier")
    model = RandomForestClassifier(random_state=0, class_weight=WEIGHTS)

    # Predict results using model
    print("Generating predictions")
    ml_predict.all_steps(x_train=x_train, x_test=x_test, y_train=y_train,
                         y_test=y_test, model=model,
                         results_directory=output_directory,
                         model_name="rf_weighted", cv=CV)
