#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --mem=64G
#SBATCH --time=0:20:00
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_06_20/accre/svc_grid_search/output.txt

module load Anaconda3
source activate imblearn
python test.py
