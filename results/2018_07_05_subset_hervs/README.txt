herv_subset_counts.txt contains the number of each subset of hervs created by running /dors/capra_lab/users/yand1/te_ml/bin/2018_07_05_subset_hervs/herv_types_count.ipynb

count_overlaps.txt was created by running 
/dors/capra_lab/users/yand1/te_ml/bin/2018_07_05_subset_hervs/reformat_mlt1k_intersect_enhancers.py
on accre and contains the number of mlt1k hervs that overlap an enhancer and the number that do not

rf_kmers_output.txt is the standard output from the accre job from the slurm script:
/dors/capra_lab/users/yand1/te_ml/bin/2018_07_05_subset_hervs/rf_kmers.slurm

rf_confusion_matrix, rf_metrics, and rf_cross_val_scores are metrics from a random forest machine learning model at that runs a random forest on the mlt1k HERVs. /dors/capra_lab/users/yand1/te_ml/bin/2018_07_05_subset_hervs/rf_kmers.py