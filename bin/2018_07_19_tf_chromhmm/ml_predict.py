# Author: Daniel Yan
#
# Email: daniel.yan@vanderbilt.edu
#
# Date: 2018-07-19
#
# Description: Module version containing wrappers for easy train/test split,
# cross validation, and predictions with a scikit learn machine learning model.


# Import needed libraries
import pandas as pd  # For writing results
from sklearn import metrics  # Get model metrics
from sklearn.metrics import average_precision_score
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import cross_val_score  # Cross validation

# Class constants
CROSS_VAL = 10  # Number of subdivisions of data for cross validation


def all_steps(x_train, x_test, y_train, y_test, model, results_directory="",
              model_name="ml", cv=10):
    """
    Wrapper for cross validation and predictions with scikit-learn model

    Performs cross validation on the training set with macro f1 score and
    prints results to directory. Trains using training set and then generates
    predictions using the testing set for more metrics, which are also stored
    to the directory.
    :param x_train: Input matrix for machine learning training set
    :param x_test: Input matrix for machine learning testing set
    :param y_train: Prediction vector for machine learning training set
    :param y_test: Actual values for machine learning testing set
    :param model: Scikit-learn machine learning model to use
    :param results_directory: String containing name of directory to write
    results to (default working directory)
    :param model_name: String containing name of model to use for
    choosing file names (default ml)
    :param cv: Number of cross validation folds to use.
    :return: None
    """
    cross_validate(model=model, x=x_train, y=y_train,
                   results_directory=results_directory, model_name=model_name)

    predictions(model=model, x_train=x_train, y_train=y_train, x_test=x_test,
                y_test=y_test, results_directory=results_directory,
                model_name=model_name)


def cross_validate(model, x, y, results_directory="", model_name="ml",
                   cross_val=CROSS_VAL):
    """
    Performs k-fold cross validation on the model and prints results to file.

    :param model: Scikit-learn machine Learning model to test
    :param x: Features matrix for model.
    :param y: Prediction vector for model.
    :param results_directory: String containing directory to write cross
    validation scores to (default working directory)
    :param model_name: String containing name of the model used in choosing
    filename to write to (default ml)
    :param cross_val: Integer k value to use for cross validation
    (default is CROSS_VAL)
    :return: None
    """
    # Test random forest model using cross validation.
    cvs = cross_val_score(model, x, y, scoring="f1_macro", cv=CROSS_VAL)

    # Print the cross validation scores to a file.
    cvs_df = pd.DataFrame(data=cvs, columns=["f1 score"])
    cvs_df.to_csv((results_directory + model_name + "_cross_val_scores.tsv"),
                  sep='\t', index=False)


def predictions(model, x_train, y_train, x_test, y_test, results_directory="",
                model_name="ml"):
    """
    Trains and generates predictions from the given model and prints out
    metrics.

    :param model: Scikit-learn machine Learning model to test
    :param x_train: Features matrix used in training
    :param y_train: Feature to predict used in training
    :param x_test: Features matrix used in prediction
    :param y_test: Actual values in testing set to compare to predictions
    :param results_directory: String containing name of directory to write to
    (default working directory)
    :param model_name: String containing name of the model used in choosing
    filename to write to (default ml)
    :return: None
    """
    # Train the model on training data.
    model.fit(x_train, y_train)

    # Use the model to predict the test set.
    y_pred = model.predict(x_test)
    # Predict probabilities to calculate area under curve metrics
    y_proba = model.predict_proba(x_test)
    # Get scores as probability of positive
    y_scores = y_proba[:, 1]

    # Generate confusion matrix indices
    labels_list = sorted(list(set(y_train)))
    index_list = ["actual_" + str(label) for label in labels_list]
    columns_list = ["predicted_" + str(label) for label in labels_list]

    # Save confusion matrix to file
    cm_df = pd.DataFrame(metrics.confusion_matrix(y_test, y_pred),
                         index=index_list, columns=columns_list)
    cm_df.to_csv(results_directory + model_name + "_confusion_matrix.tsv",
                 sep='\t')

    # Create a file to store metrics.
    with open((results_directory + model_name + "_metrics.txt"), mode="w+") \
            as metrics_file:
        # Write precision, recall, and f1 score
        metrics_file.write(metrics.classification_report(y_test, y_pred))
        # Write area under precision-recall curve
        metrics_file.write("\nPrecision-Recall AUC: {}".format(
            average_precision_score(y_test, y_scores)))
        # Write area under ROC curve
        metrics_file.write("\nROC AUC: {}".format(
            roc_auc_score(y_test, y_scores)))
