#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=4
#SBATCH --ntasks=4
#SBATCH --time=10:00       
#SBATCH --mem=64G
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_07_05_subset_hervs/rf_kmers_output.txt

module load Anaconda3

python rf_kmers.py
