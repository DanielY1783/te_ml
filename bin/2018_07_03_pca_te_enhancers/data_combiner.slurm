#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=128G
#SBATCH --time=28:00:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_07_03_pca_te_enhancers/data_combiner_output.txt

module load Anaconda3
python data_combiner.py

