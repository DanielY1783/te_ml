#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=32G
#SBATCH --time=0:30:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_06_27_kmers_hervs_chromehmm/accre/test_output.txt

module load Anaconda3
python test_kmer_counter.py
