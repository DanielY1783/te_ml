2018_06_13: Preliminary version of random forest classifier.

2018_06_25_kmer_hervs: Reformat transposable elements to remove duplicates and information
		about transcription factors since we are looking at 6-mers now.

2018_06_14: Random forest run on smaller test subset of data

2018_06_15: Random forest run on full set of HERVs

2018_06_18: Random forest on test subset with oversampling

2018_06_19: Random forest on full HERVs with undersampling, random oversampling, SMOTE, ADASYN

2018_06_20: Linear SVC on full HERVs and SVC grid search on test HERVs.

2018_06_21_chromehmm_te: Reformatted version of intersection of transposable elements and 
		transcription factors as intermediate data set.
		
2018_06_21_svm_grid: Grid search for SVC on full set of HERVs.

2018_06_22_chromehmm: Intersection of transcription factors with transposable elements reformatting
		done on ACCRE cluster.
		
2018_06_22_svc_rbf: SVC with RBF kernel run on full set of HERVs.

2018_06_25_chromehmm_ml_input: Reformat intersection of tranposable elements with chromehmmm
		enhancers to form input data for machine learning model.
		
2018_06_25_kmer_hervs: Reformat hervs data to drop transcription factors and duplicate hervs. 

2018_06_26_kmer_hervs_chromehmm: Fixed version of 2018_06_25_kmer_hervs

2018_06_27_kmer_hervs_chromehmm: kmer counter that creates a feature matrix of 6-mer counts from
		the data at /dors/capra_lab/users/yand1/te_ml/data/2018_06_26_kmers_hervs_chromehmm/hervs_hg19.tsv
		
2018_06_28_kmers_faster: Faster implementation of kmer counter from 2018_06_27_kmer_hervs_chromehmm
		that works better with pandas dataframes.
		
2018_06_29_kmers_enhancer_intersect: Reformatting scripts for features matrix of kmers for hervs.
		PCA and histogram analysis on features matrix after intersection with chromehmm enhancers.
		
2018_07_02_kmers_pca_rf: Principal component analysis and random forest classifier run 