#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --mem=100G
#SBATCH --time=2:00:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_07_18_tf_chromhmm/rf_naive_output.txt

module load Anaconda3
python rf_naive.py /dors/capra_lab/users/yand1/te_ml/data/2018_06_25_chromehmm_ml_input/x_chromhmm.tsv /dors/capra_lab/users/yand1/te_ml/data/2018_06_25_chromehmm_ml_input/y_chromhmm.tsv /dors/capra_lab/users/yand1/te_ml/results/2018_07_18_tf_chromhmm/


