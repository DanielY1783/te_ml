#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=5-00:00:00       
#SBATCH --mem=64G
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_07_02_kmers_pca_rf/accre_gb_kmers_output.txt

module load Anaconda3

python accre_gb_kmers.py
