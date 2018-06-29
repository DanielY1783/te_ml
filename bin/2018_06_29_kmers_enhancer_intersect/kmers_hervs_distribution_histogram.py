
# coding: utf-8

# Create a histogram from:
# /dors/capra_lab/users/yand1/te_ml/data/2018_06_29_kmers_enhancers_intersect/hervs_kmers_features_matrix.tsv
# by summing up each column (sum of repetitions of each kmer) and plotting those numbers on the x-axis,
# and the counts on the y-axis.

# In[1]:


# Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


# Class constants
DIRECTORY = "/dors/capra_lab/users/yand1/te_ml/"
DATE = "2018_06_29_kmers_enhancers_intersect/"
DATA_FILE = "hervs_kmers_features_matrix.tsv" # File with input
WRITE_FILE = "kmers_distribution.png" # File to store histogram


# In[ ]:


def plot_histogram(dist):
    """Plot a histogram from the given distribution of kmers and saves to WRITE_FILE 
    
    Args:
        dist(pd.Series): Distribution of kmer counts to plot
    """
    plt.figure() # Create plot
    plt.hist(dist) # Send distribution of kmers to histogram
    plt.xlabel("Repetitions 6-mers within HERVs")
    plt.ylabel("Number of 6-mers")
    plt.title("6-mer counts within HERVs")
    plt.savefig(DIRECTORY + "results/" + DATE + WRITE_FILE)


# In[ ]:


## Main
def main():
    """Main function
    """
    # Read in features matrix as dataframe 
    features_df = pd.read_table(DIRECTORY + "data/" + "2018_06_29_kmers_enhancers_intersect/" +
                               DATA_FILE)
    
    # Remove the chromsome, start, and end locations to only get kmer counts
    features_df.drop(["chr", "start", "end"], axis = "columns", inplace = True)
    
    # Get the sum of each column of kmers
    kmers_sum = features_df.sum(axis = "columns").values
    
    # Plot the histogram
    plot_histogram(kmers_sum)


# In[ ]:


# Call main to run 
main()

