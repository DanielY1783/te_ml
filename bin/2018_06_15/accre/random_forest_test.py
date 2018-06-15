
# coding: utf-8

# In[1]:


# Import needed libraries
import pandas as pd
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, cross_val_predict, train_test_split


# In[2]:


# Class constants
DATE = "2018_06_15/" 
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/" # Root directory
LOC = "accre/" # local or accre cluster
DATA_FILE = "test.tsv" # Name of data file to process
CHROMOSOME = 0 # Column for the chromosome number of transposable element
START = 1 # Column for the start location of transposable element
END = 2 # Column for the end location of transposable element
TF = 8 # Column for the transcription factor intersecting with transposable element
ENHANCER = 13 # Column for if enhancer is present. 1 means enhancer is present


# In[3]:


def remove_dups (old_df, col_names):
    """Function that takes in an old dataframe and creates a new dataframe with duplicates removed
    
    Args:
        old_df(pd.DataFrame): Data frame to remove duplicates from
        col_names(list): List of column names to in string format
    
    Returns:
        New pd.DataFrame that has duplicates removed with reindexing, and renamed columns.
    """
    new_df = pd.DataFrame(old_df)
    new_df = new_df.drop_duplicates()
    new_df.index = range(len(new_df.iloc[:,0])) # Reindex
    # Rename columns
    new_df.columns = ["chr", "start", "end"]
    return new_df


# In[4]:


def col_labels (df, col_list):
    """col_labels creates new columns corresponding to transcription factors and enhancer presence
    
    Args:
        df(pd.DataFrame): Data frame to add columns to
        col_list(list): List of transcription factors
    """
    for tf in col_list:
        df[tf] = 0
    # Create a column for if enhancer overlaps transposable element
    df["enhancer_actual"] = 0


# In[5]:


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


def test_model(model, df):
    """test_model checks how well the model performs and writes output to /results directory
    
    Args:
        model(sklearn.ensemble.RandomForestClassifier): The machine learning model to test
        df(pd.DataFrame): The original data; used to compare results with labels.
    """
    # Get index number for the "y" vector for machine learning model.
    end_index = len(df.columns) - 1
    # Set the machine learning input vector as all columns of transcription factors.
    x_df = df.copy().iloc[:,3:end_index]
    # Set the machine learning prediction vector as the last column, which tells if enhancer is present.
    y_actual = df.copy().iloc[:,end_index]
    
    # Perform 5-fold cross validation on the random forest model.
    cvs = cross_val_score(model, x_df, y_actual, cv = 5)
    # Print the cross validation scores to a file.
    cvs_df = pd.DataFrame(data = cvs, index = ["cvs 1", "cvs 2", "cvs 3", "cvs 4", "cvs 5"], columns = ["score"])
    cvs_df.to_csv((DIRECTORY + "results/" + DATE + LOC + "cross_val_scores.csv"), sep = '\t', index = False)
    
    # Create predictions using 5-fold cross validation to view incorrect predictions.
    y_pred = cross_val_predict(model, x_df, y_actual, cv = 5)
    # Convert the prediction results to a dataframe.
    predictions_df = pd.DataFrame(data = y_pred, columns = ["enhancer_predicted"])
    # Create a dataframe to combine predictions with actual data.
    output_df = pd.DataFrame(df.copy()[["chr", "start", "end", "enhancer_actual"]])
    # Copy over predictions and print to csv file.
    output_df["enhancer_predicted"] = predictions_df
    output_df.to_csv((DIRECTORY + "results/" + DATE +  LOC + "predictions.csv"), sep = '\t')
    
    # Create a confusion matrix and write to file.
    cm_df = pd.DataFrame(metrics.confusion_matrix(y_actual, y_pred), index = ["actual_negative", "actual_positive"]
                    , columns = ["predicted_negative", "predicted_positive"])
    cm_df.to_csv((DIRECTORY + "results/" + DATE + LOC + "confusion_matrix.csv"), sep = '\t')
    
    # Create a file to store metrics.
    metrics_file = open((DIRECTORY + "results/" + DATE + LOC + "metrics.txt"), "w+")
    metrics_file.write(metrics.classification_report(y_actual, y_pred))


# In[ ]:


## Main

# Open the transposable elements data as a dataframe.
te_df = pd.read_table((DIRECTORY + "data/2018_06_12_te_enhancers_ml/" + DATA_FILE), header = None)

# Create new data frame for machine learning model by setting columns as the different transcription
# factors from the original data frame. Each row will now have the location of the transposable 
# element, the number of intersections with each transcription factor, and if there is an overlap
# with an enhancer.
te_new_df = transform_df(te_df)

# Create a random forest classifier model
rfc = RandomForestClassifier(n_estimators = 1000, n_jobs = -1)

# Test the random forest classifer model
test_model(model = rfc, df = te_new_df)

