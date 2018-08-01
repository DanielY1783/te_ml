#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=64G
#SBATCH --time=128:30:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_06_21_svm_grid/accre/svc_grid_search_test/output.txt

module load Anaconda3
source activate imblearn
python svc_rbf.py
