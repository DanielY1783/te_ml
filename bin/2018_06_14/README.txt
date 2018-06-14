Takes data from D:\Daniel\Documents\2018 Summer\te_ml\data\2018_06_12_te_enhancers_ml 
and transforms it into a matrix for machine learning. The rows contain each unique transposable
element and start and end location (same transposable element in different locations get separate
rows), and the columns are the different transcription factors(E_CTCF, E_JUND, E_MYC, etc). The
"y" vector to predict is the last column from the original data. A 1 in the "y" vector represents 
overlap between a transcription factor and binding site; otherwise, 0.