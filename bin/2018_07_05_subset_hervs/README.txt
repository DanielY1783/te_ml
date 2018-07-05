herv_types_count:
	gets counts for each subset of HERV from /dors/capra_lab/users/yand1/te_ml/data/2018_07_05_subset_hervs/no_dups_hervs.tsv to find largest HERV subset

filter_mltk1:
	filters the HERVs from /dors/capra_lab/users/yand1/te_ml/data/2018_07_05_subset_hervs/no_dups_hervs.tsv 
	for only the MLT1K HERVs and save to  
	/dors/capra_lab/users/yand1/te_ml/data/2018_07_05_subset_hervs/mlt1k.tsv 
	
reformat_mlt1k_intersect_enhancers:
	New version of /dors/capra_lab/users/yand1/te_ml/bin/2018_06_29_kmers_enhancer_intersect/reformat_hervs_intersect enhancers.py
	This program takes in
	/dors/capra_lab/users/yand1/te_ml/data/2018_07_05_subset_hervs/enhancers_mlt1k_intersect.tsv
	and changes overlap to boolean value: 1 for overlap between transposable element and enhancer; 0 for no overlap.