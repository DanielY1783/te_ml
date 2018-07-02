
# coding: utf-8

# accre version of a random forest model run on the full HERVS kmers feature matrix at:
# /dors/capra_lab/users/yand1/te_ml/data/2018_06_29_kmers_enhancers_intersect/reformatted_hervs_kmers_intersect_enhancers.tsv

# In[1]:


# Import needed libraries
import pandas as pd # For getting data
from sklearn import metrics # Get model metrics
from sklearn.ensemble import RandomForestClassifier # Random Forest
from sklearn.model_selection import train_test_split # For data splitting
from sklearn.model_selection import cross_val_score # Cross validation


# In[2]:


# Class constants
DATE_DIR = "2018_07_02_kmers_pca_rf/" # Directory associated with current date 
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/" # Root directory for project
DATA_FILE = "reformatted_hervs_kmers_intersect_enhancers.tsv" # Data file with feature matrix
CROSS_VAL = 10 # Number of subdivisions of data for cross validation
FIRST_KMER = "aaaaaa" # Label for first column of kmer counts
LAST_KMER = "tttttt" # Label for last column of kmer counts
ENHANCER_OVERLAP = "enhancer" # Label for column with 1 or 0 value for if HERV overlaps with enhancer.


# In[3]:


def cross_validate(model, x, y):
    """Performs k-fold cross validation on the model and prints results to file.
    
    Args:
        model(sklearn.RandomForestClassifier): Machine Learning model to test
        x(pd.DataFrame): Features for model (kmer counts within HERVs).
        y(pd.DataFrame): Prediction vector for model (HERV overlap with enhancer).
    """
    # Test random forest model using cross validation.
    cvs = cross_val_score(model, x, y, scoring = "f1_macro", cv = CROSS_VAL)
    
    # Print the cross validation scores to a file.
    cvs_df = pd.DataFrame(data = cvs, columns = ["f1 score"])
    cvs_df.to_csv((DIRECTORY + "results/" + DATE_DIR + "rf_cross_val_scores.csv"), 
                  sep = '\t', index = False)


# In[4]:


def predictions(model, x, y):
    """Trains and generates predictions from the given model and prints out metrics.
    
    Args:
        model(sklearn.RandomForestClassifier): Machine Learning model to test
        x(pd.DataFrame): Features. In this case, it is kmer counts within HERVs.
        y(pd.DataFrame): What to predict. In this case, it is HERV overlap with enhancer.
    """
    # Split into training and testing set.
    x_train, x_test, y_train, y_test = train_test_split(x, y)
    
    # Train the model on training data.
    model.fit(x_train, y_train)
    
    # Use the model to predict the test set.
    y_pred = model.predict(x_test)
    
    # Create a confusion matrix and write to file.
    cm_df = pd.DataFrame(metrics.confusion_matrix(y_test, y_pred), index = ["actual_negative", "actual_positive"]
                    , columns = ["predicted_negative", "predicted_positive"])
    cm_df.to_csv((DIRECTORY + "results/" + DATE_DIR + "rf_confusion_matrix.tsv"), sep = '\t')
    
    # Create a file to store metrics.
    with open((DIRECTORY + "results/" + DATE_DIR + "rf_metrics.txt"), "w+") as metrics_file:
        metrics_file.write(metrics.classification_report(y_test, y_pred))


# In[5]:


def main():
    """Main function
    """
    features_df = pd.read_table(DIRECTORY + "data/2018_06_29_kmers_enhancers_intersect/" + DATA_FILE)
    
    # Get "x" and "y" for machine learning input.
    x_df = features_df.loc[:,FIRST_KMER:LAST_KMER]
    y_df = features_df.loc[:,ENHANCER_OVERLAP]
    
    # Create a random forest classifier model. -1 to parallelize.
    rfc = RandomForestClassifier(n_estimators = 100, n_jobs = -1)
    
    # Test random forest model using cross validation.
    cross_validate(model = rfc, x = x_df, y = y_df)
    
    # Generate predictions and get metrics.
    predictions(model = rfc, x = x_df, y = y_df)


# In[6]:


# Call main to run
main()

