kmer_counter_batch counts the number of each 6-mer within each HERV at
/dors/capra_lab/users/yand1/te_ml/data/2018_06_26_kmers_hervs_chromehmm/hervs_hg19.tsv
and is designed for use with slurm batch arrays for faster parallel processing.

data_splitter splits the HERV data at /dors/capra_lab/users/yand1/te_ml/data/2018_06_26_kmers_hervs_chromehmm/hervs_hg19.tsv 
into smaller files, with the number of the file appended before .tsv
(for example, hervs_hg19_1.tsv)
Smaller files are saved to /dors/capra_lab/users/yand1/te_ml/data/2018_06_28_kmers_faster/batch_input