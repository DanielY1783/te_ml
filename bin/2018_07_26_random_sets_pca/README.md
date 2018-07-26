## Modules
**pca.py**
Wrappers for plotting PCA.

**shuffled_pca.py**
Function for generating combinations of principal components to plot.

## Tests
**test_pca.py**
Unit tests for some functions pca.py (some are difficult to test)

**test_shuffled_pca.py**
Unit tests for some functions shuffled_pca.py (some are difficult to test)

## Program
**pca_tasks_pipeline.py** 
Pipeline for running PCA, saving transformed coordinates, and generating scatterplots. Standalone script is principal component analysis on kmer counts in hervs, chromhmm enhancers, herv-enhancer overlap, and three random sets length each matched to one of those groups.

## Slurm
**pca_tasks_pipeline.slurm**
accre scheduler file to run pca_tasks_pipeline.py

