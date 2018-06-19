#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=4
#SBATCH --ntasks=4
#SBATCH --mem=64G
#SBATCH --time=0:20:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_06_15/accre/output.txt

module load Anaconda3
python random_forest_test.py
