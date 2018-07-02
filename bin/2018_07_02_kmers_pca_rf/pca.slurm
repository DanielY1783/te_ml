#!/bin/bash
#SBATCH --mail-user=daniel.yan@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=10:00:00       
#SBATCH --mem=64G
#SBATCH --output=/dors/capra_lab/users/yand1/te_ml/results/2018_07_02_kmers_pca_rf/pca_output.txt

module load GCC OpenMPI R/3.4.3-X11-20160819

Rscript pca_hervs_enhancers.R
