[![Build Status](https://travis-ci.org/DanielY1783/te_ml.svg?branch=master)](https://travis-ci.org/DanielY1783/te_ml)

# Machine Learning on Transposable Elements
Machine learning models on transposable elements and their intersection with enhancers.

Includes random forest classifier and support vector classifier to predict HERV overlap with fantom enhancers based on transcription 
factors, random forest classifier and gradient boosted decision trees to predict HERV overlap with chromhmm enhancers based
on 6-mers, random forest classifer for HERVs vs generic parts of the human genome as baseline, and principal component analysis on HERVs,
enhancers, and HERV-enhancer overlap based on 6-mers.

Data files are too large to store on Github and are on the Vanderbilt ACCRE cluster at: /dors/capra_lab/users/yand1/te_ml/data

results folder added on 2018-07-13 for easier synchronizing between local machine and Vanderbilt accre cluster. results/2018_06_21_chromehmmte folder is ignored because file within it is too large on Github and can be found on the Vanderbilt accre cluster at /dors/capra_lab/users/yand1/te_ml/results/2018_06_21_chromehmm_te


test_requirements.txt: Provides dependencies for travis testing.
