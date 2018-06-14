local folder contains a version of the program that operates on a smaller test data set on the local machine at D:\Daniel\Documents\2018 Summer\te_ml\data\2018_06_12_te_enhancers_ml\test.tsv
and transforms it into a matrix for machine learning. 
The rows contain each unique transposable
element and start and end location (same transposable element in different locations get separate
rows), and the columns are the different transcription factors(E_CTCF, E_JUND, E_MYC, etc). 
The "y" vector to predict is the last column from the original data. A 1 in the "y" vector represents 
overlap between a transcription factor and binding site; otherwise, 0.
Cross validation scores and predicted results are printed to the results/2018_06_14/local folder.

accre folder contains version of the program that operates on the full set of data on the ACCRE cluster
at: /dors/capra_lab/users/yand1/te_ml/data/2018_06_12_te_enhancers_ml/full.tsv
results are contained at /dors/capra_lab/users/yand1/te_ml/results/2018_06_14/accre