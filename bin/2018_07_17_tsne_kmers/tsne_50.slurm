#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=240G
#SBATCH --time=10:00:00
#SBATCH --array=5,10,15,20,25,30,35,40,45,50
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_07_17_tsne_kmers/tsne_50_perplexity_%a_output.txt

module load Anaconda3
python tsne.py /dors/capra_lab/users/yand1/te_ml/data/2018_07_17_tsne_kmers/sampled_components_50.tsv /dors/capra_lab/users/yand1/te_ml/results/2018_07_17_tsne_kmers/tsne_50_perplexity_${SLURM_ARRAY_TASK_ID} /dors/capra_lab/users/yand1/te_ml/results/2018_07_16_tsne_kmers/tsne_50_perplexity_${SLURM_ARRAY_TASK_ID} ${SLURM_ARRAY_TASK_ID}
