
# coding: utf-8

# Takes in data from /dors/capra_lab/users/yand1/te_ml/data/2018_06_12_te_enhancers_ml
# to predict if transposable elements overlap with enhancers given a set of transcription
# factors. This version uses a grid search to find the best hyperparameters.

# In[ ]:


# Import needed libraries
import pandas as pd # For getting data
from sklearn import metrics # Get model metrics
from sklearn.svm import SVC # Support vector classifier.
from sklearn.model_selection import GridSearchCV, train_test_split # Cross validation grid search


# In[ ]:


# Class constants
DATE = "2018_06_21_svm_grid/" 
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/" # Root directory
LOC = "accre/" # local or accre cluster
TYPE = "svc_grid_search/" # Type of model
DATA_FILE = "full.tsv" # Name of data file to process
CHROMOSOME = 0 # Column for the chromosome number of transposable element
START = 1 # Column for the start location of transposable element
END = 2 # Column for the end location of transposable element
TF = 8 # Column for the transcription factor intersecting with transposable element
ENHANCER = 13 # Column for if enhancer is present. 1 means enhancer is present
CROSS_VAL = 5 # Number of subdivisions of data for cross validation
RAM = 1000 # MB for each SVC model.


# In[ ]:


def transform_df (old_df):
    """transform_tf updates the columns of transcription factors in new_df by cross referencing old_df
    
    Each row in the old data frame is matched to the corresponding location in the new
    data frame.The column of the the transcription factor in the new data frame that corresponds
    to the old data frame is incremented by 1. The enhancer column in the new data frame is
    set to 1 if that column in the old data frame is 1.
    
    Args:
        old_df(pd.DataFrame): Data frame that contains the information about transcription factors.
        
    Return:
        new_df(pd.DataFrame): New data frame that has columns with the number of times
            each transposable element in different locations intersects with each
            transcription factor, as well as if an enhancer site is present.
    """
    # Create groups based on chromosome, start location, end location, transcription factor, and if
    # transcription factor is present. Get the size of each of those groups, and use unstack to 
    # change the transcription factors to column indices to create matrix for machine learning input.
    # Use reset_index to bring all other labels to top level.
    new_df = te_df.groupby([CHROMOSOME, START, END, TF, ENHANCER], sort = False).size().unstack(TF, fill_value = 0).reset_index()

    # Reformat enhancer column to have 1 or 0 value.
    new_df[ENHANCER] = new_df[ENHANCER].apply(lambda x: 1 if x == "1" else 0)

    # Rename the columns
    new_df.rename(columns = {CHROMOSOME: "chr", START: "start", END: "end", ENHANCER: "enhancer"}, inplace = True)

    # Sum any repeated rows (in case any rows were identical other than enhancer presence)
    new_df.groupby(new_df.index).sum()

    # Move row with enhancer to the end.
    enhancer_df = new_df.copy()["enhancer"]
    new_df.drop(labels = ["enhancer"], axis = 1, inplace = True)
    new_df.insert(len(new_df.columns), "enhancer_actual", enhancer_df)
    
    return new_df


# In[ ]:


def create_predictions(model, x_df, y_df):
    """create_predictions splits the data into a training and testing set,
        oversamples the training set, performs cross validation and predicts the testing set.
        
    Args:
        model(sklearn.ensemble.RandomForestClassifier): The machine learning model to train and predict with
        x_df(pd.DataFrame): Input "x" vector to test
        y_df(pd.DataFrame): Output "y" vector with real y values
    """  
    # Use model to predict the testing set
    y_pred = model.predict(x_df)
    
    # Create a confusion matrix and write to file.
    cm_df = pd.DataFrame(metrics.confusion_matrix(y_df, y_pred), index = ["actual_negative", "actual_positive"]
                    , columns = ["predicted_negative", "predicted_positive"])
    cm_df.to_csv((DIRECTORY + "results/" + DATE + LOC + TYPE + "confusion_matrix.csv"), sep = '\t', mode = "w+")
    
    # Create a file to store metrics.
    metrics_file = open((DIRECTORY + "results/" + DATE + LOC + TYPE + "metrics.txt"), "w+")
    metrics_file.write(metrics.classification_report(y_df, y_pred))


# In[ ]:


## Main

# Open the transposable elements data as a dataframe.
te_df = pd.read_table((DIRECTORY + "data/2018_06_12_te_enhancers_ml/" + DATA_FILE), header = None)

# Create new data frame for machine learning model by setting columns as the different transcription
# factors from the original data frame. Each row will now have the location of the transposable 
# element, the number of intersections with each transcription factor, and if there is an overlap
# with an enhancer.
te_new_df = transform_df(te_df)

# Get index number for the "y" vector for machine learning model.
end_index = len(te_new_df.columns) - 1
# Set the machine learning input vector as all columns of transcription factors.
x_df = te_new_df.iloc[:,3:end_index]
# Set the machine learning prediction vector as the last column, which tells if enhancer is present.
y_df = te_new_df.iloc[:,end_index]

# Split the data into training and testing data.
x_train, x_test, y_train, y_test = train_test_split(x_df, y_df)

# Perform a grid search to find the best parameters
parameters = {"kernel": ["poly", "rbf", "sigmoid"], "C": [0.01, 0.1, 1, 10, 100, 1000]}
model = GridSearchCV(SVC(cache_size = RAM), param_grid = parameters, n_jobs = -1, scoring = "f1_macro", cv = CROSS_VAL)
model.fit(x_train, y_train)

# Print out the best parameters from the grid search.
print("Best params: " + str(model.best_params_))
print("Best score: " + str(model.best_score_))

# Create predictions with SVM model and get metrics.
create_predictions(model = model, x_df = x_test, y_df = y_test)

