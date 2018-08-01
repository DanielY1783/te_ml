#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=50G
#SBATCH --time=24:00:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_07_26_random_sets_pca/pca_tasks_pipeline_output.txt

module load Anaconda3
python pca_tasks_pipeline.py /dors/capra_lab/users/yand1/te_ml/data/2018_07_25_random_sets_features/hervs_enhancers_randoms_features.tsv /dors/capra_lab/users/yand1/te_ml/data/2018_07_26_random_sets_pca/components_50.tsv /dors/capra_lab/users/yand1/te_ml/results/2018_07_26_random_sets_pca 50 
