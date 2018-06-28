kmer_counter_batch counts k-mers for each herv by reading command line argument with file name, with directory at:
/dors/capra_lab/users/yand1/te_ml/data/2018_06_28_kmers_faster/batch_input
After reading in the file, it creates a count of the number of each kmer within each HERV and stores
this feature matrix at
/dors/capra_lab/users/yand1/te_ml/data/2018_06_28_kmers_faster/batch_output
This version is a local version for testing of a full version on accre for batch array processing of data to create a feature matrix.

data_splitter splits the HERV data at: 
/dors/capra_lab/users/yand1/te_ml/data/2018_06_26_kmers_hervs_chromehmm/hervs_hg19.tsv 
into smaller files, with the number of the file appended before .tsv
(for example, hervs_hg19_1.tsv)
New data files are saved to:
/dors/capra_lab/users/yand1/te_ml/data/2018_06_28_kmers_faster/batch_input

test_kmer_counter_batch.slurm submits a test job to the accre cluster.

kmer_counter_batch.slurm uses a job array to submit the 100 separate jobs on creating feature matrices from split data
to the accre cluster.
