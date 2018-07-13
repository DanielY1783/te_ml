summary.docx contains a summary of the results from the different machine learning models.

2018_06_14: Random forest run on smaller test subset of data

2018_06_15: Random forest run on full set of HERVs

2018_06_18: Random forest on test subset with oversampling

2018_06_19: Random forest on full HERVs with undersampling, random oversampling, SMOTE, ADASYN

2018_06_20: Linear SVC on full HERVs and SVC grid search on test HERVs.

2018_06_21_chromehmm_te: Reformatted version of intersection of transposable elements and 
		transcription factors as intermediate data set.
		
2018_06_21_svm_grid: Grid search for SVC on full set of HERVs.

2018_06_22_chromehmm: Intersection of transcription factors with transposable elements. Reformatting done on ACCRE cluster.
		
2018_06_22_svc_rbf: SVC with RBF kernel run on full set of HERVs.

2018_06_25_chromehmm_ml_input: Reformat intersection of tranposable elements with chromehmmm enhancers to form input data for machine learning model.
		
2018_06_27_kmers_hervs_chromehmm: Standard output from accre jobs at /dors/capra_lab/users/yand1/te_ml/bin/2018_06_27_kmers_hervs_chromehmm/accre
		
2018_06_28_kmers_faster: Standard output from accre jobs at /dors/capra_lab/users/yand1/te_ml/bin/2018_06_28_kmers_faster/accre
		
2018_06_29_kmers_enhancer_intersect: Histogram of kmer distribution within HERVs.

2018_07_02_kmers_pca_rf: Principal component analysis, random forest, gradient boosting with decision trees, and support vector classifier run on kmers from HERVs
		
2018_07_03_pca_te_enhancers: Principal component analysis on kmers from tranposable elements that don't overlap an enhancer, enhancers, and overlap of enhancers and tranposable elements. Enhancers are chromhmm enhancers.

2018_07_05_subset_hervs: Run enhancer classifier on largest subset of HERVs.

2018_07_06_genome_shuffle: Classify hervs vs random parts of the human genome

2018_07_09_shuffle_ml: Machine learning models on classifying hervs vs random parts of the human genome. HERVs are positives (1), random parts are negatives (0).

2018_07_09_pca_te_enhancers: Python version of principal component analysis on kmers from transposable elements only, intersection of tranposable elements and enhancers, and enhancers only. Uses chromhmm enhancers.

2018_07_10_pca_te_enhancers: Python version of principal component analysis on kmers from transposable elements only, intersection of tranposable elements and enhancers, and enhancers only. Uses chromhmm enhancers, and separate plots for different groups as well.

2018_07_11_pca_te_enhancers: Python version of principal component analysis on kmers from transposable elements only, intersection of tranposable elements and chromhmm enhancers,  enhancers only, and control group of generic parts of the human genome, with separate plots for different groups.

2018_07_12_pca_te_enhancers: Standard output from reformatting features matrix of shuffled parts of the human genome.

2018_07_13_pca_te_enhancers: Principal component analysis on shuffled parts of human genome, hervs, enhancers, and intersection of hervs and enhancers.