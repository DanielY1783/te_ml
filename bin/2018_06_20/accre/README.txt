.slurm files are for ACCRE scheduler to run task. 

oversampling.slurm is to test a old random forest model with oversampling to get accre working.

grid_search.slurm is for the SVC grid search with cross validation to find the best hyperparameters for a SVM and predict using those hyperparameters.

test.slurm is same as grid_search.slurm but run on a smaller sample of the data to gauge needed resources (uses the test.py file, which is same as SVM_grid_search.py except it uses the test data file instead of the full one)

output is written to /dors/capra_lab/users/yand1/te_ml/results/2018_06_20/accre/svc_grid_search/output.txt