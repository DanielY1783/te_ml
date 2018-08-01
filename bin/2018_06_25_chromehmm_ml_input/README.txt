Takes in the formatted intersection of enhancers and transposable elements (with transcription factors) at /dors/capra_lab/users/yand1/te_ml/data/2018_06_22_chromehmm/full_chromehmm.tsv and converts it to a matrix with rows as transposable elements columns as transcription factors (each transcription factor is given one column) and if enhancer overlaps with transposable element. This is stored at /dors/capra_lab/users/yand1/te_ml/data/2018_06_25_chromehmm_ml_input/ to be used as input data for machine learning models.

local version is to run a quick test trial on a much smaller set of data on a local machine, while the other version runs on the full set of data on the ACCRE cluster.

slurm file is to send job to accre scheduler.