## Created by */dors/capra_lab/users/yand1/te_ml/bin/2018_07_19_tf_chromhmm/rf_weighted.slurm*
random forest classifier of transposable element (all, not just hervs) overlap with chromhmm enhancers based on transcription factors after train test split. 0 represents no overlap, and 1 represents overlap. This version uses the weights parameter {0: 1, 1: 10000000} to try to correct for too many 0's.

1. **rf_weighted_naive_output.txt**
Standard output.
2. **rf_weighted_confusion_matrix.tsv**
Confusion matrix.
3. **rf_weighted_cross_val_scores.tsv**
Cross validation f1_macro scores with 10 fold cross validation.
4. **rf_weighted_metrics.txt**
Machine learning metrics like precision, recall, f1 score.