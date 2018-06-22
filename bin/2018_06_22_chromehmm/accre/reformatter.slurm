#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=32G
#SBATCH --time=90:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_06_22_chromehmm/output.txt

module load Anaconda3
python format_te.py

