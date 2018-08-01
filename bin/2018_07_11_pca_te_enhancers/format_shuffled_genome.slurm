#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=128G
#SBATCH --time=75:00:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_07_11_pca_te_enhancers/format_shuffled_genome_output.txt

module load Anaconda3
python format_shuffled_genome.py

