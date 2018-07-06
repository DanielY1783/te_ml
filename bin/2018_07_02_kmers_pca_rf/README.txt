pca_hervs_enhancers.R creates a graph from a principal component analysis of the kmers within HERVs at:
/dors/capra_lab/users/yand1/te_ml/data/2018_06_29_kmers_enhancers_intersect/reformatted_hervs_kmers_intersect_enhancers.tsv

pca.slurm submits that file to the accre scheduler

local_rf_kmers.ipynb is a local version of a random forest model run on the a test subset of the 
HERVS kmers feature matrix at:
/dors/capra_lab/users/yand1/te_ml/data/2018_06_29_kmers_enhancers_intersect/test.tsv

accre_rf_kmers.ipynb is an accre version of a random forest model run on the full HERVS kmers feature matrix at:
/dors/capra_lab/users/yand1/te_ml/data/2018_06_29_kmers_enhancers_intersect/reformatted_hervs_kmers_intersect_enhancers.tsv
accre_rf_kmers.py is converted to a .py file to make it easier to run on accre.

accre_rf_kmers.slurm submits accre_rf_kmers.py to the accre scheduler

accre_gb_kmers files are the same as accre_rf_kmers files, but run a gradient boosting classifier
instead of a random forrest classifier.

accre_svc_kmers files are the same as accre_rf_kmers files, but run a support classifier
instead of a random forrest classifier.
