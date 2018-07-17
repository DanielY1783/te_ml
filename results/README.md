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




## HERVs intersected with chromhmm enhancers using transcription factors as features. 
This part is incomplete because project moved to using sum of 6-mers instead of transcription factors as features. Extent of progress is that file for converting data to features matrix of transcription factors was created, but not run yet

**2018_06_21_chromehmm_te**
Reformatted version of intersection of transposable elements and transcription factors as intermediate data set.

**2018_06_22_chromehmm**
Intersection of transcription factors with transposable elements. Reformatting done on ACCRE cluster.

**2018_06_25_chromehmm_ml_input**
Reformat intersection of tranposable elements with chromehmmm enhancers to form input data for machine learning model.




## HERVs intersected with chromhmm enhancers using 6-mers as features. 
		
**2018_06_27_kmers_hervs_chromehmm**
Standard output from accre jobs doing data reformatting at */dors/capra_lab/users/yand1/te_ml/bin/2018_06_27_kmers_hervs_chromehmm/accre*
		
**2018_06_28_kmers_faster**
Standard output from accre jobs doing kmer counts at */dors/capra_lab/users/yand1/te_ml/bin/2018_06_28_kmers_faster/accre*
		
**2018_06_29_kmers_enhancer_intersect**
Histogram of kmer distribution within hervs.

**2018_07_02_kmers_pca_rf**
Principal component analysis, random forest, gradient boosting with decision trees, and support vector classifier
		
**2018_07_03_pca_te_enhancers**
Principal component analysis on kmers from tranposable elements that don't overlap an enhancer, enhancers, and overlap of enhancers and tranposable elements.

**2018_07_05_subset_hervs**
Run enhancer classifier on largest subset of hervs.

**2018_07_06_genome_shuffle**
Classify hervs vs random parts of the human genome as control

**2018_07_09_shuffle_ml**
Continued from previous day (*2018_07_06_genome_shuffle*). Machine learning models on classifying hervs vs random parts of the human genome. hervs are positives (1), random parts are negatives (0).

**2018_07_09_pca_te_enhancers**
Python version of principal component analysis on kmers from transposable elements only, intersection of tranposable elements and enhancers, and enhancers only.

**2018_07_10_pca_te_enhancers**
Continued from previous day (*2018_07_09_pca_te_enhancers*), but add separate plots for different groups as well.

**2018_07_11_pca_te_enhancers**
Standard output from reformatting features matrix of shuffled parts of the human genome.

**2018_07_12_pca_te_enhancers**
Standard output from reformatting features matrix of shuffled parts of the human genome.

**2018_07_13_pca_te_enhancers**
Continued from *2018_07_11_pca_te_enhancers*. Principal component analysis on shuffled parts of human genome, hervs, enhancers, and intersection of hervs and enhancers.

**2018_07_16_tsne_kmers**
Saved pca models and explained variance ratios of principal components for dimensionality reduction for tsne.

**2018_07_17_tsne_kmers**
TSNE scatterplots from top 50 principal components on shuffled parts of human genome, hervs, enhancers, and intersection of hervs and enhancers.

# Individual Files
**summary.docx**
Summary of the results from the different machine learning models.