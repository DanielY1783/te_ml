#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:90:00       
#SBATCH --mem=128G
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_07_03_pca_te_enhancers/pca_output.txt

module load GCC OpenMPI R/3.4.3-X11-20160819

Rscript pca_combined.R
