data_splitter is a modified version of a similar file at /dors/capra_lab/users/yand1/te_ml/bin/2018_06_28_kmers_faster/accre
that splits data at:
/dors/capra_lab/users/yand1/te_ml/data/2018_07_03_pca_te_enhancers/combined_hg19.tsv
into 100 smaller files at:
/dors/capra_lab/users/yand1/te_ml/data/2018_07_03_pca_te_enhancers/batch_input

kmer_counter_batch is a modified version of a similar file at
/dors/capra_lab/users/yand1/te_ml/bin/2018_06_28_kmers_faster/accre
This one processes data at:
/dors/capra_lab/users/yand1/te_ml/data/2018_07_03_pca_te_enhancers/batch_input
by taking in a command line argument and counting kmers, normalizing counts, and saving to
/dors/capra_lab/users/yand1/te_ml/data/2018_07_03_pca_te_enhancers/batch_output

kmer_counter.slurm submits kmer_counter_batch.py to the accre scheduler in a job array to parallelize things
