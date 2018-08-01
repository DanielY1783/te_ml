#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=64G
#SBATCH --time=300:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_06_29_kmers_enhancers_intersect/accre/reformatter_output.txt

module load Anaconda3
python reformat_hervs_intersect_enhancers.py
