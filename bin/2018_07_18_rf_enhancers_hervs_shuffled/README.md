## Modules
**ml_predict.py** Wrappers for quick predictions with scikit learn machine learning models.

## Programs
**rf_search.py** Use grid search to try different random forest hyperparameters for best random forest classifier on enhancers, hervs, herv-enhancer overlap, and control of generic shuffled parts of the human genome. This one was not run successfully because of memory timeout issues on accre.

**rf_naive.py** Random forest classifier on enhancers, hervs, herv-enhancer overlap, and control of generic shuffled parts of the human genome without hyperparameter tuning. Less resource intensive than rf_search.py

**rf_faster.py** Random forest classifier on enhancers, hervs, herv-enhancer overlap, and control of random parts of human genome length matched to hervs. Leave out cross validation and limit max_depth for faster running on accre.

## Slurm files
**rf_search.slurm** accre scheduler file to run *rf_search.py*. This did not run successfully due to memory timeout on accre.

**rf_faster.slurm** accre scheduler file to run *rf_faster.py* on full set of data. Did not run successfully due to memory timeout on accre.

