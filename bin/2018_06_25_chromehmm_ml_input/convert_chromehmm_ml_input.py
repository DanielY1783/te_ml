
# coding: utf-8

# Takes in the formatted intersection of enhancers and transposable elements (with transcription factors) at /dors/capra_lab/users/yand1/te_ml/data/2018_06_22_chromehmm/full_chromehmm.tsv and converts it to a matrix with rows as transposable elements columns as transcription factors (each transcription factor is given one column) and if enhancer overlaps with transposable element. This is stored at /dors/capra_lab/users/yand1/te_ml/data/2018_06_25_chromehmm_ml_input/ to be used as input data for machine learning models.

# In[1]:


# Import needed libraries
import pandas as pd # For getting data formatting


# In[2]:


# Class constants
DATE = "2018_06_25_chromehmm_ml_input/" 
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/" # Root directory
LOC = "local/" # local or accre cluster
DATA_FILE = "full_chromehmm.tsv" # Name of data file to process
X_FILE = "x_chromehmm.tsv" # Name of file to save "x" input machine learning vector to
Y_FILE = "y_chromehmm.tsv" # Name of file to save "y" prediction machine learning vector to
CHROMOSOME = 4 # Column for the chromosome number of transposable element
START = 5 # Column for the start location of transposable element
END = 6 # Column for the end location of transposable element
TF = 3 # Column for the name of the transcription factor intersecting with transposable element
ENHANCER = 9 # Column for if enhancer is present. -1 means enhancer is not present


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
    new_df = te_df.groupby([TF, CHROMOSOME, START, END, ENHANCER], sort = False).size().unstack(TF, fill_value = 0).reset_index()

    # Reformat enhancer column to have 1 or 0 value.
    new_df[ENHANCER] = new_df[ENHANCER].apply(lambda x: 0 if str(x) == "-1" else 1)

    # Rename the columns
    new_df.rename(columns = {CHROMOSOME: "chr", START: "start", END: "end", ENHANCER: "enhancer"}, inplace = True)

    # Sum any repeated rows (in case any rows were identical other than enhancer presence)
    new_df.groupby(new_df.index).sum()

    # Move row with enhancer to the end.
    enhancer_df = new_df.copy()["enhancer"]
    new_df.drop(labels = ["enhancer"], axis = 1, inplace = True)
    new_df.insert(len(new_df.columns), "enhancer_actual", enhancer_df)
    
    new_df.head()
    
    return new_df


# In[ ]:


## Main

# Open the transposable elements data as a dataframe.
te_df = pd.read_table((DIRECTORY + "data/2018_06_22_chromehmm/" + DATA_FILE), header = None)

# Create new data frame for machine learning model by setting columns as the different transcription
# factors from the original data frame. Each row will now have the location of the transposable 
# element, the number of intersections with each transcription factor, and if there is an overlap
# with an enhancer.
te_new_df = transform_df(te_df)

# Get index number for the "y" vector for machine learning model.
end_index = len(te_new_df.columns) - 1
# Set the "x" machine learning input vector as all columns of transcription factors.
x_df = te_new_df.iloc[:,3:end_index]
# Set the "y" machine learning prediction vector as the last column, which tells if enhancer is present.
y_df = te_new_df.iloc[:,end_index]

# Save the "x" input vector to a file
x_df.to_csv(DIRECTORY + "data/" + DATE + X_FILE, sep = '\t', index = False)
# Save the "y" prediction vector to a file
y_df.to_csv(DIRECTORY + "data/" + DATE + Y_FILE, sep = '\t', index = False)

