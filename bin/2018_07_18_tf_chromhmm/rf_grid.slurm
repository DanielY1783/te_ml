#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=16
#SBATCH --ntasks=128
#SBATCH --mem=160G
#SBATCH --time=48:00:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_07_18_tf_chromhmm/rf_grid_output.txt

module load Anaconda3
python rf_grid.py /dors/capra_lab/users/yand1/te_ml/data/2018_06_25_chromehmm_ml_input/x_chromhmm.tsv /dors/capra_lab/users/yand1/te_ml/data/2018_06_25_chromehmm_ml_input/y_chromhmm.tsv /dors/capra_lab/users/yand1/te_ml/results/2018_07_18_tf_chromhmm/

