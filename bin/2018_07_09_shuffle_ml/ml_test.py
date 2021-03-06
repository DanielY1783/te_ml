
# coding: utf-8

# Module version of train/test split, cross validation, and predictions with a scikit learn machine learning model.
# 
# This version can also be used as as standalone script on the features matrix at:
# /dors/capra_lab/users/yand1/te_ml/data/2018_07_06_genome_shuffle/all_pairs_feature_matrix.tsv

# In[1]:


"""Provides a test_model function that performs train/test split, cross validation, and prediction metrics.

Functions:
    test_model(x, y, model, results_directory = "", model_name = "ml"): Performs train/test split.
        Calls cross_validate to perform cross validation and predictions to generate predictions
        on the testing set and store metrics.
        
    cross_validate(model, x, y, results_directory = "", model_name = "ml", cross_val = CROSS_VAL):
        Performs cross validation and store results to file.
    
    predictions(model, x_train, y_train, x_test, y_test, results_directory = "", model_name = "ml"):
        Trains model on training set, generates predictions using test set, and saves 
        metrics to file.
"""


# In[2]:


# Import needed libraries
import pandas as pd # For writing results
from sklearn import metrics # Get model metrics
from sklearn.model_selection import train_test_split # For data splitting
from sklearn.model_selection import cross_val_score # Cross validation


# In[3]:


# Class constants 
CROSS_VAL = 10 # Number of subdivisions of data for cross validation


# In[4]:


def test_model(x, y, model, results_directory = "", model_name = "ml"):
    """Creates and tests a random forest model
    
    Performs a train/test split on the input(x) and predictor(y). Performs cross validation
    on the training set with macro f1 score and prints results to directory. Trains using 
    training set and then generates predictions using the testing set for more metrics,
    which are also stored to the directory.
    
    Keyword Arguments:
        x: Input matrix for machine learning
        y: Prediction vector for machine learning
        model: Scikit-learn machine learning model to use
        results_directory: String containing name of directory to write results to (default working directory)
        model_name: String containing name of model to use for choosing file names (default ml)
    """
    x_train, x_test, y_train, y_test = train_test_split(x, y)
    
    cross_validate(model = model, x = x_train, y = y_train, results_directory = results_directory,
                  model_name = model_name)
    
    predictions(model = model, x_train = x_train, y_train = y_train, x_test = x_test, y_test = y_test
               , results_directory = results_directory, model_name = model_name)


# In[5]:


def cross_validate(model, x, y, results_directory = "", model_name = "ml", cross_val = CROSS_VAL):
    """Performs k-fold cross validation on the model and prints results to file.
    
    Args:
        model: Scikit-learn machine Learning model to test
        x: Features matrix for model.
        y: Prediction vector for model.
        results_directory: String containing directory to write cross validation scores to (default working directory)
        model_name: String containing name of the model used in choosing filename to write to (default ml)
        cross_val: Integer k value to use for cross validation (default is CROSS_VAL)
    """
    # Test random forest model using cross validation.
    cvs = cross_val_score(model, x, y, scoring = "f1_macro", cv = CROSS_VAL)
    
    # Print the cross validation scores to a file.
    cvs_df = pd.DataFrame(data = cvs, columns = ["f1 score"])
    cvs_df.to_csv((results_directory + model_name + "_cross_val_scores.tsv"), 
                  sep = '\t', index = False)


# In[6]:


def predictions(model, x_train, y_train, x_test, y_test, results_directory = "", model_name = "ml"):
    """Trains and generates predictions from the given model and prints out metrics.
    
    Args:
        model: Scikit-learn machine Learning model to test
        x_train: Features matrix used in training
        y_train: Feature to predict used in training
        x_test: Features matrix used in prediction
        y_test: Actual values in testing set to compare to predictions
        results_directory: String containing name of directory to write to (default working directory)
        model_name: String containing name of the model used in choosing filename to write to (default ml)
    """
    # Train the model on training data.
    model.fit(x_train, y_train)
    
    # Use the model to predict the test set.
    y_pred = model.predict(x_test)
    
    # Create a confusion matrix and write to file.
    cm_df = pd.DataFrame(metrics.confusion_matrix(y_test, y_pred), 
                         index = ["actual_negative", "actual_positive"], 
                         columns = ["predicted_negative", "predicted_positive"])
    cm_df.to_csv(results_directory + model_name + "_confusion_matrix.tsv", sep = '\t')
    
    # Create a file to store metrics.
    with open((results_directory + model_name + "_metrics.txt"), "w+") as metrics_file:
        metrics_file.write(metrics.classification_report(y_test, y_pred))


# In[7]:


if __name__ == "__main__":
    """Main function
    """
    from sklearn.ensemble import RandomForestClassifier # Try random forest
    
    # Read in data file
    features_df = pd.read_table("/dors/capra_lab/users/yand1/te_ml/data/2018_07_06_genome_shuffle/all_pairs_features_matrix.tsv")
    
    # Get "x" and "y" for machine learning input.
    x_df = features_df.iloc[:,5:4100]
    y_df = features_df.iloc[:,3]
    
    # Create a random forest classifier model to test. -1 to parallelize.
    rfc = RandomForestClassifier(n_estimators = 100, n_jobs = -1)
    
    # Test the model
    test_model(x = x_df, y = y_df, model = rfc, 
              results_directory = "/dors/capra_lab/users/yand1/te_ml/results/2018_07_09_shuffle_ml/",
              model_name = "rf")

