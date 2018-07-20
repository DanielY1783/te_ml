# Directory Descriptions
Directories are organized by date and into groups with a header before each group of related directories.



## HERVs intersected with fantom enhancers using transcription factors as features.

**2018_06_13**
Preliminary version of random forest classifier on HERVs.

**2018_06_14**
Random forest run on smaller test subset of data.

**2018_06_15**
Random forest run on full set of hervs with fantom enhancers using transcription factors as features.

**2018_06_18**
Random forest on test subset with oversampling with fantom enhancers using transcription factors as features.

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
Intersection of transcription factors with transposable elements reformatting done on ACCRE cluster.

**2018_06_25_chromehmm_ml_input**
Reformat intersection of tranposable elements with chromehmmm enhancers to form input data for machine learning model.

**2018_07_18_tf_chromhmm**
Random forest classifier of transposable element overlap (all transposable elements) with chromhmm enhancers.
	
**2018_07_19_tf_chromhmm**
Random forest classifier of transposable element overlap (all transposable elements) with chromhmm enhancers with weights assigned as {0: 1, 1: 10000000}.

**2018_07_20_tf_chromhmm**
Random forest classifier of transposable element overlap (all transposable elements) with chromhmm enhancers with weights assigned as "balanced.	


	
## HERVs intersected with chromhmm enhancers using 6-mers as features. 
		
**2018_06_25_kmer_hervs**
Reformat hervs data to drop transcription factors and duplicate hervs. 

**2018_06_26_kmer_hervs_chromehmm**
Fixed version of 2018_06_25_kmer_hervs

**2018_06_27_kmer_hervs_chromehmm**
kmer counter that creates a feature matrix of 6-mer counts from the data at */dors/capra_lab/users/yand1/te_ml/data/2018_06_26_kmers_hervs_chromehmm/hervs_hg19.tsv*
		
**2018_06_28_kmers_faster**
Faster implementation of kmer counter from *2018_06_27_kmer_hervs_chromehmm* that works better with pandas dataframes.
		
**2018_06_29_kmers_enhancer_intersect**
Reformatting scripts for features matrix of kmers for hervs. Principal component analysis and histogram analysis on features matrix after intersection with chromehmm enhancers.
		
**2018_07_02_kmers_pca_rf**
Principal component analysis, random forest classifier, gradient boosting classifier, and support vector classifier run on intersection of chromhmm enhancers and hervs	*/dors/capra_lab/users/yand1/te_ml/data/2018_06_29_kmers_enhancers_intersect/reformatted_hervs_kmers_intersect_enhancers.tsv*

**2018_07_03_pca_te_enhancers**
Principal component analysis on kmers from transposable elements only, intersection of tranposable elements and enhancers, and enhancers only. Uses chromhmm
	
**2018_07_05_subset_hervs**
Retrain machine learning model on a largest subset of hervs.
			
**2018_07_06_genome_shuffle**
Classify hervs vs random parts of the human genome

**2018_07_09_shuffle_ml**
Machine learning models on classifying hervs vs random parts of the human genome.

**2018_07_09_pca_te_enhancers**
Python version of principal component analysis on kmers from transposable elements only, intersection of tranposable elements and enhancers, and enhancers only. Uses chromhmm enhancers.

**2018_07_10_pca_te_enhancers**
Continued work from previous day (*2018_07_09_pca_te_enhancers*)

**2018_07_11_pca_te_enhancers**
Added control of generic shuffled parts of the human genome to previous day's work (*2018_07_10_pca_te_enhancers*)

**2018_07_12_pca_te_enhancers**
Same as previous day (*2018_07_10_pca_te_enhancers*), but try vectorized operations in pandas to increase efficiency.

**2018_07_13_pca_te_enhancers**
Scatterplot of top 5 components for hervs, herv-enhancer intersect, enhancers only, and control of shuffled parts of human genome.

**2018_07_16_tsne_kmers**
Principal component analysis to reduce features for tsne visualization on kmer counts for hervs, herv-enhancer intersect, enhancers only, and control of shuffled parts of the human genome. tsne on those dimensions.

**2018_07_17_tsne_kmers**
Same as previous day, but add script for stratified sampling of data to deal with memory error due to tsne consuming too much memory. Change tsne script to take in system argument for perplexity hyperparameter.

**2018_07_18_rf_enhancers_hervs_shuffled**
Random forest classifier of hervs, herv-enhancer intersect, enhancers, and shuffled parts of the human genome.

**2018_07_20_random_sets**
Add random sets length matched to herv-enhancer overlap and enhancers to the original random set that was length matched to hervs


# Travis Tested Modules
The following modules contain components with Travis tests and can be safely reused.
Individual components within the modules are listed after the modules.

**2018_07_11_pca_te_enhancers/shuffled_pca.py**
1. generate_combinations: Generate all possible combinations from iterable
2. generate_configurations: Generate all possible configurations from iterable
	
**2018_07_12_pca_te_enhancers/reformat_df.py**
1. normalize: Normalize rows by length of DNA sequence

**2018_07_17_pca_te_enhancers/pca.py**
1. label_coordinates: Labels coordinates with labels corresponding to index

**2018_07_17_pca_te_enhancers/sampling.py**
1. stratified_sample: Stratified sampling of a pandas dataframe based on a column with labels

# Reusable Modules
These modules contain the following reusable components that lack Travis tests due to
difficulty of writing unit tests (such as plots, machine learning models, etc)

**2018_07_13_pca_te_enhancers/pca.py**
1. create_ipca: Creates incremental pca and returns transformed coordinates
2. scatterplot_pca: Creates scatter plot based on transformed coordinates.

**2018_07_19_tf_chromhmm/ml_predict.py**
1. all_steps: Wrapper for generating and saving cross validation and predictions from scikit learn model.
2. cross_validation: Wrapper for generating and printing cross validation only from scikit learn model.
3. predictions: Wrapper for generating and saving prediction metrics only from scikit learn model.

**2018_07_20_random_sets**
1. split_files: Split a file containing a large data frame into smaller dataframes stored in separate files.
2. split_data: Split a pandas dataframe into smaller data frames and return as a list of the smaller data frames.