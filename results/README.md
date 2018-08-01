# Directory Descriptions
Directories are organized by date and into groups with a header before each group of related directories.


## HERVs intersected with fantom enhancers using transcription factors as features.

**2018_06_14**
Random forest run on smaller test subset of data

**2018_06_15**
Random forest run on full set of hervs

**2018_06_18**
Random forest on test subset with oversampling

**2018_06_19**
Random forest on full hervs with undersampling, random oversampling, SMOTE, ADASYN

**2018_06_20**
Linear SVC on full hervs and SVC grid search on test hervs.

**2018_06_21_svm_grid**
Grid search for SVC on full set of hervs.

**2018_06_22_svc_rbf**
SVC with RBF kernel run on full set of hervs.



## Transposable Elements intersected with chromhmm enhancers using transcription factors as features. 
Use all transposable elements instead of HERVs subset, and use chromhmm definition of enhancers. Predict transposable element overlap with enhancers based on transcription factors as features. 

**2018_06_21_chromehmm_te**
Reformatted version of intersection of transposable elements and transcription factors as intermediate data set.

**2018_06_22_chromehmm**
Intersection of transcription factors with transposable elements. Reformatting done on ACCRE cluster.

**2018_06_25_chromehmm_ml_input**
Reformat intersection of tranposable elements with chromehmmm enhancers to form input data for machine learning model.

**2018_07_18_tf_chromhmm**
Metrics from random forest classifier prediction of transposable element overlap (all transposable elements) with chromhmm enhancers.

**2018_07_19_tf_chromhmm**
Metrics from random forest classifier prediction of transposable element overlap (all transposable elements) with chromhmm enhancers, with weights assigned for random forest classifier using the weights parameter as {0: 1, 1: 10000000}

**2018_07_20_tf_chromhmm**
Metrics from random forest classifier prediction of transposable element overlap (all transposable elements) with chromhmm enhancers, with weights assigned for random forest classifier using the weights parameter as "balanced"

## HERVs intersected with chromhmm enhancers using 6-mers as features. 
		
**2018_06_27_kmers_hervs_chromehmm**
Standard output from accre jobs doing data reformatting at */dors/capra_lab/users/yand1/te_ml/bin/2018_06_27_kmers_hervs_chromehmm/accre*
		
**2018_06_28_kmers_faster**
Standard output from accre jobs doing kmer counts at */dors/capra_lab/users/yand1/te_ml/bin/2018_06_28_kmers_faster/accre*
		
**2018_06_29_kmers_enhancer_intersect**
Histogram of kmer distribution within hervs.

**2018_07_02_kmers_pca_rf**
Principal component analysis, random forest, gradient boosting with decision trees, and support vector classifier on herv overlap with chromhmm enhancers using kmers as features. Support vector classifier timed out, so no results from that model.
		
**2018_07_03_pca_te_enhancers**
Principal component analysis on kmers from tranposable elements that don't overlap an enhancer, enhancers, and overlap of enhancers and tranposable elements.

**2018_07_05_subset_hervs**
Run random forest classifier on largest subset of hervs (mlt1k), with 1 representing overlap with chromhmm enhancer and 0 representing no overlap.

**2018_07_06_genome_shuffle**
accre output from converting control group of random parts of the human genome length matched to hervs.

**2018_07_09_shuffle_ml**
Random forest classifier for hervs vs random parts of the human genome. hervs are positives (1), random parts are negatives (0).

**2018_07_09_pca_te_enhancers**
Scatter plots from python version of principal component analysis on kmers from transposable elements only, intersection of tranposable elements and enhancers, and enhancers only.

**2018_07_10_pca_te_enhancers**
Continued from previous day (*2018_07_09_pca_te_enhancers*), but add separate plots for each of the different groups.

**2018_07_11_pca_te_enhancers**
Standard output from reformatting features matrix of shuffled parts of the human genome.

**2018_07_12_pca_te_enhancers**
Standard output from reformatting features matrix of shuffled parts of the human genome.

**2018_07_13_pca_te_enhancers**
Scatter plot from principal component analysis on shuffled parts of human genome, hervs, enhancers, and intersection of hervs and enhancers (added control of shuffled parts of human genome to previous plots in *2018_07_13_pca_te_enhancers*

**2018_07_16_tsne_kmers**
Saved pca models and explained variance ratios of principal components for dimensionality reduction for tsne.

**2018_07_17_tsne_kmers**
TSNE scatterplots from top 50 principal components on shuffled parts of human genome, hervs, enhancers, and intersection of hervs and enhancers.

**2018_07_18_rf_enhancers_hervs_shuffled**
Results from random forest on shuffled parts of human genome, hervs, enhancers, and intersection herv-enhancer intersection. No results obtained yet because of memory timeout on accre.

**2018_07_23_random_sets**
Standard output from formatting of new length matched random sets created by accre job at 
*/dors/capra_lab/users/yand1/te_ml/bin/2018_07_23_random_sets/kmer_counter_batch.slurm*

**2018_07_26_random_sets_pca**
Scatter plots from principal component analysis on kmer counts in hervs, chromhmm enhancers, herv-enhancer overlap, and three random sets length each matched to one of those groups. No results obtained because of memory timeout on accre.


# Individual Files
**summary.docx**
Summary of the results from the different machine learning models.

