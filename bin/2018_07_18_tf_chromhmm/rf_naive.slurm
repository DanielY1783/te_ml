#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --mem=100G
#SBATCH --time=48:00:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_07_18_rf_enhancers_hervs_shuffled/rf_grid_output.txt

module load Anaconda3
python rf_grid.py /dors/capra_lab/users/yand1/te_ml/data/2018_07_13_pca_te_enhancers/hervs_enhancers_shuffled_features_matrix.tsv /dors/capra_lab/users/yand1/te_ml/results/2018_07_18_rf_enhancers_hervs_shuffled label
