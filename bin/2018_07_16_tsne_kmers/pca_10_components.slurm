#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=200G
#SBATCH --time=2:00:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_07_16_tsne_kmers/pca_10_components_output.txt

module load Anaconda3
python pca_n_components.py /dors/capra_lab/users/yand1/te_ml/data/2018_07_13_pca_te_enhancers/hervs_enhancers_shuffled_features_matrix.tsv /dors/capra_lab/users/yand1/te_ml/data/2018_07_16_tsne_kmers/components_10.tsv /dors/capra_lab/users/yand1/te_ml/results/2018_07_16_tsne_kmers/components_10.pkl /dors/capra_lab/users/yand1/te_ml/results/2018_07_16_tsne_kmers/explained_variance_10.txt 10

