
# coding: utf-8

# Filters the HERVs from /dors/capra_lab/users/yand1/te_ml/data/2018_07_05_subset_hervs/no_dups_hervs.tsv 
# for only the MLT1K HERVs and save to  
# /dors/capra_lab/users/yand1/te_ml/data/2018_07_05_subset_hervs/mlt1k.tsv 

# In[ ]:


# Libraries
import pandas as pd


# In[ ]:


def main():
    """Main
    """
    hervs_df = pd.read_table("/dors/capra_lab/users/yand1/te_ml/data/2018_07_05_subset_hervs/no_dups_hervs.tsv", header = None)
    hervs_df.loc[hervs_df.iloc[:,3] == "MLT1K"].to_csv("/dors/capra_lab/users/yand1/te_ml/data/2018_07_05_subset_hervs/mlt1k.tsv",
                                          index = False, header = False)


# In[ ]:


# Call main to run
main()

