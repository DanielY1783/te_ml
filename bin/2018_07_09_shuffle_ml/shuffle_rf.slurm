#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=8
#SBATCH --ntasks=8
#SBATCH --mem=128G
#SBATCH --time=1:00:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_07_09_shuffle_ml/shuffle_rf_output.txt

module load Anaconda3
python shuffle_rf.py
