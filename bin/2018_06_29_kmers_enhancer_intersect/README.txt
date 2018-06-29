remove_header_features_matrix.py removes the header containing column names from
/dors/capra_lab/users/yand1/te_ml/data/2018_06_29_kmers_enhancers_intersect/hervs_kmers_features_matrix.tsv
and stores to
/dors/capra_lab/users/yand1/te_ml/data/2018_06_29_kmers_enhancers_intersect/no_header_hervs_kmers_features_matrix.tsv

kmers_hervs_distribution_histogram.py uses the feature matrix at 
/dors/capra_lab/users/yand1/te_ml/data/2018_06_29_kmers_enhancers_intersect/hervs_kmers_features_matrix.tsv
to plot a histogram of a distribution of kmer counts within HERVs to
/dors/capra_lab/users/yand1/te_ml/results/2018_06_29_kmers_enhancers_intersect/kmers_distribution.png

reformat_hervs_intersect_enhancers.py changes columns of /dors/capra_lab/users/yand1/te_ml/data/2018_06_29_kmers_enhancers_intersect/hervs_kmers_intersect_enhancers.tsv 
so that overlap of enhancers and hervs is a single boolean value in the last column; 1 for overlap, 0 for no overlap. Result is stored to:
/dors/capra_lab/users/yand1/te_ml/data/2018_06_29_kmers_enhancers_intersect/reformatted_hervs_kmers_intersect_enhancers.tsv 

pca_hervs_enhancers.R does principal component analysis on:
/dors/capra_lab/users/yand1/te_ml/data/2018_06_29_kmers_enhancers_intersect/reformatted_hervs_kmers_intersect_enhancers.tsv 
and stores the image to
/dors/capra_lab/users/yand1/te_ml/results/2018_06_29_kmers_enhancers_intersect/pca.png