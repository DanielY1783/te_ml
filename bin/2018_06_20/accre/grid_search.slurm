#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=8
#SBATCH --ntasks=8
#SBATCH --mem=64G
#SBATCH --time=24:30:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_06_20/accre/svc_grid_search/output_new.txt

module load Anaconda3
source activate imblearn
python SVM_grid_search.py
