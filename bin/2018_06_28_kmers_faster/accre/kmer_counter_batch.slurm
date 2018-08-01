#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=32G
#SBATCH --time=90:00
#SBATCH --array=0-99
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_06_28_kmers_faster/accre/output_%a.txt

module load Anaconda3
python kmer_counter_batch.py hervs_hg19_${SLURM_ARRAY_TASK_ID}.tsv
