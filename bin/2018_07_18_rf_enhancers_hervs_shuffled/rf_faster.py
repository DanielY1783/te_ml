# Author: Daniel Yan
#
# Email: daniel.yan@vanderbilt.edu
#
# Date: 2018-07-19
#
# Description: Faster random forest classifier of hervs,
# herv-enhancer overlap, enhancers, and generic shuffled parts of human
# genome (as control) by leaving out cross validation and limiting max_depth.
#
# Command Line Arguments:
# 1. Name of data file, including directory and extension.
# 2. Directory to store output files to. End with backslash.
# 3. Name of column to predict
#
# Preconditions:
# 1. Data file must include header names in first row and no indices
# 2. Data file must contain 6-mer counts as features, with first features
# column named "aaaaaa" and last features column named "tttttt"
# 3. Data file must contain a string column name for the column to predict
# 4. Data file must contain different instances in rows and features in
# columns, with no missing or invalid values.
#
# Postconditions:
# Files containing predictions from the random forest classifier are written
# to the directory passed as second parameter.


# Libraries
import ml_predict  # Wrappers for scikit learn machine learning models
import pandas as pd  # Data manipulation
from sklearn.ensemble import RandomForestClassifier  # Random forest
from sklearn.model_selection import GridSearchCV  # Grid search
from sklearn.model_selection import train_test_split  # For data splitting
import sys  # Command line arguments

# Constants
CV = 10  # Cross validation folds
FIRST_FEATURE = "aaaaaa"  # Name of column with first feature
LAST_FEATURE = "tttttt"  # Name of column with last feature

if __name__ == '__main__':
    # Read in name of data file
    data_file = sys.argv[1]
    # Read in name of directory to write results to
    output_directory = sys.argv[2]
    # Read in name of the column to predict
    predict_col = sys.argv[3]

    # Read in data file with headers in row 0
    print("Reading in data file")
    data_frame = pd.read_table(data_file, header=0)
    # Get the features.
    x_df = data_frame.loc[:, FIRST_FEATURE:LAST_FEATURE]
    # Get labels to predict
    y_df = data_frame.loc[:, predict_col]

    # Train test split
    x_train, x_test, y_train, y_test = train_test_split(x_df, y_df)

    # Create random forest model with set random state for reproducibility.
    print("Creating random forest model")
    model = RandomForestClassifier(random_state=0, max_depth=25)

    # Predict results using best model
    print("Generating predictions")
    ml_predict.predictions(x_train=x_train, x_test=x_test, y_train=y_train,
                             y_test=y_test, model=model,
                             results_directory=output_directory,
                             model_name="rf_faster")
