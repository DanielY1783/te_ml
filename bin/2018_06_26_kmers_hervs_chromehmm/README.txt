Reformats data in /dors/capra_lab/users/yand1/te_ml/data/2018_06_25_kmer_hervs 
and stores to /dors/capra_lab/users/yand1/te_ml/data/2018_06_26_kmers_hervs_chromehmm/

drop_dups_herv.py takes /dors/capra_lab/users/yand1/te_ml/data/2018_06_25_kmers_hervs/full_hervs.tsv
and drops all duplicate hervs by looking at chromosome, start location, end location, and
herv name and stores the resulting 4 columns to 
/dors/capra_lab/users/yand1/te_ml/data/2018_06_26_kmers_hervs_chromehmm/no_dups_hervs.tsv

drop_dups_herv_no_names.py takes /dors/capra_lab/users/yand1/te_ml/data/2018_06_25_kmers_hervs/full_hervs.tsv
and drops all duplicate hervs by looking at chromosome, start location, end location and stores the resulting 3 columns to 
/dors/capra_lab/users/yand1/te_ml/data/2018_06_26_kmers_hervs_chromehmm/no_dups_hervs_no_names.tsv

local directory for files to test run on local system.