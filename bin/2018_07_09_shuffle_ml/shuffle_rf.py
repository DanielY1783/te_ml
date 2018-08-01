
# coding: utf-8

# Tests random forest classifier for HERVs vs general parts of the genome.

# In[1]:


# Import needed libraries
import pandas as pd # For getting data
from sklearn.ensemble import RandomForestClassifier # Random forest
# Import module for testing the model
import ml_test


# In[2]:


def main():
    """Main
    """
    # Read in data file
    features_df = pd.read_table("/dors/capra_lab/users/yand1/te_ml/data/2018_07_06_genome_shuffle/all_pairs_features_matrix.tsv")
    
    # Get "x" and "y" for machine learning input.
    x_df = features_df.iloc[:,5:4100]
    y_df = features_df.iloc[:,3]
    
    # Create a random forest classifier model to test. -1 to parallelize.
    rfc = RandomForestClassifier(n_estimators = 100, n_jobs = -1)
    
    # Test the model
    ml_test.test_model(x = x_df, y = y_df, model = rfc, 
              results_directory = "/dors/capra_lab/users/yand1/te_ml/results/2018_07_09_shuffle_ml/",
              model_name = "rf")


# In[3]:


# Call main to run
main()

