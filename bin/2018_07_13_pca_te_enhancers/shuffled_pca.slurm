#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=200G
#SBATCH --time=5:00:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_07_13_pca_te_enhancers/shuffled_pca_output.txt

module load Anaconda3
python shuffled_pca.py
