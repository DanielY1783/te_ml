#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=200G
#SBATCH --time=14-0:00:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_07_16_tsne_kmers/tsne_50_output.txt

module load Anaconda3
python tsne.py /dors/capra_lab/users/yand1/te_ml/data/2018_07_16_tsne_kmers/dors/components_50.tsv /dors/capra_lab/users/yand1/te_ml/results/2018_07_16_tsne_kmers/tsne_50 /dors/capra_lab/users/yand1/te_ml/results/2018_07_16_tsne_kmers/tsne_50 2

