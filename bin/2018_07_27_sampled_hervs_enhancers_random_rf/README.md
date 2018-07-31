## Programs
**sampling.py**
Take stratified sample of rows from a labeled data frame.

**rf_faster.py** Random forest classifier on enhancers, hervs, herv-enhancer overlap, and control of random parts of human genome length matched to hervs. Leave out cross validation and limit max_depth for faster running on accre to deal with resource issues.

## Tests
**test_sampling.py**
Pytests for sampling.py

## Slurm files
**sampling_2018_07_13_kmers_feature.slurm**
accre scheduling file to take a stratified sample of 10,000 instances between hervs, chromhmm enhancers, herv-enhancer intersection, and random set length matched to hervs.

**sampling_2018_13_kmers_feature_100000.slurm**
accre scheduling file to take a stratified sample of 100,000 instances between hervs, chromhmm enhancers, herv-enhancer intersection, and random set length matched to hervs.

**rf_faster_sampled.slurm** 
accre scheduler file to run *rf_faster.py* on stratified sample of 10,000 instances between hervs, chromhmm enhancers, herv-enhancer intersection, and random set length matched to hervs.
