#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=25G
#SBATCH --time=5:00:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_07_27_sampled_hervs_enhancers_random_rf/rf_100000/rf_faster_sampled_100000_output.txt

module load Anaconda3
python rf_faster.py /dors/capra_lab/users/yand1/te_ml/data/2018_07_27_sampled_hervs_enhancers_random_rf/sampled_100000_hervs_enhancers_shuffled_features_matrix.tsv /dors/capra_lab/users/yand1/te_ml/results/2018_07_27_sampled_hervs_enhancers_random_rf/rf_100000/ label
