## Modules
**ml_predict.py** Wrappers for quick predictions with scikit learn machine learning models.

## Programs
**rf_grid.py** Use grid search to try different random forest hyperparameters for best random forest classifier on chromhmm enhancers using transcription factors. This version ultimately was not run successfully due to lack of resources on accre.

**rf_naive.py** Random forest without hyperparameter tuning to classify herv overlap with chromhmm enhancers using transcription factors as features to reduce resource usage on accre.

## Slurm files 
**rf_grid.slurm** accre scheduler file to run *rf_grid.py*. This was unsuccessful due to lack of resources on accre cluster.

**rf_naive.slurm** accre scheduler file to run *rf_naive.py*.