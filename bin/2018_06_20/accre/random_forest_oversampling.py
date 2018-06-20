
# coding: utf-8

# Takes in data from /dors/capra_lab/users/yand1/te_ml/data/2018_06_12_te_enhancers_ml
# to predict if transposable elements overlap with enhancers given a set of transcription
# factors. This version uses naive random oversampling to compensate for the fact that
# most transposable elements do not overlap with enhancers.

# In[1]:


# Import needed libraries
import pandas as pd # For getting data
from sklearn import metrics # Get model metrics
from sklearn.ensemble import RandomForestClassifier # Random Forest
from sklearn.model_selection import train_test_split # For data splitting
from imblearn import over_sampling # Oversampling


# In[2]:


# Class constants
DATE = "2018_06_20/" 
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/" # Root directory
LOC = "accre/" # local or accre cluster
TYPE = "rf_oversampled/" # Type of model
DATA_FILE = "full.tsv" # Full data set or smaller test set
CHROMOSOME = 0 # Column for the chromosome number of transposable element
START = 1 # Column for the start location of transposable element
END = 2 # Column for the end location of transposable element
TF = 8 # Column for the transcription factor intersecting with transposable element
ENHANCER = 13 # Column for if enhancer is present. 1 means enhancer is present
CROSS_VAL = 10 # Number of subdivisions of data for cross validation


# In[3]:


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


# In[4]:


def create_predictions(model, x_df, y_df):
    """create_predictions splits the data into a training and testing set,
        oversamples the training set, and predicts the testing set.
        
    Args:
        model(sklearn.ensemble.RandomForestClassifier): The machine learning model to train and predict with
        x_df(pd.DataFrame): Input "x" vector 
        y_df(pd.DataFrame): Output "y" vector
    """
    # Split the data into training and testing data
    x_train_df, x_test_df, y_train_df, y_test_df = train_test_split(x_df, y_df)
    
    # Oversample the training data
    oversampling = over_sampling.RandomOverSampler()
    x_resampled, y_resampled = oversampling.fit_sample(x_train_df, y_train_df)
    
    # Train the model on the oversampled training data
    model.fit(x_resampled, y_resampled)
    
    # Use model to predict the testing set
    y_pred_df = model.predict(x_test_df)
    
    # Create a confusion matrix and write to file.
    cm_df = pd.DataFrame(metrics.confusion_matrix(y_test_df, y_pred_df), index = ["actual_negative", "actual_positive"]
                    , columns = ["predicted_negative", "predicted_positive"])
    cm_df.to_csv((DIRECTORY + "results/" + DATE + LOC + TYPE + "confusion_matrix.csv"), sep = '\t')
    
    # Create a file to store metrics.
    metrics_file = open((DIRECTORY + "results/" + DATE + LOC + TYPE + "metrics.txt"), "w+")
    metrics_file.write(metrics.classification_report(y_test_df, y_pred_df))


# In[5]:


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

# Create a random forest classifier model
rfc = RandomForestClassifier(n_estimators = 100, n_jobs = -1)

# Create predictions with random forests model
create_predictions(model = rfc, x_df = x_df, y_df = y_df)

