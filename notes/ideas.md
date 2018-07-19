## Ideas for further analysis
1. Use frameworks like Apache Spark for distributed computing on bigger data sets, such as 7-mers or 8-mers, since an 8-mer features matrix might be around 300 GB.
2. Use multicore implementation of tsne to do tsne on all elements, rather than a small sample of 10,000.
3. Use frameworks like Apache Spark for distributed computing to run more resource intensive computations on existing features such as grid search to tune hyperparameters for machine learning models.
4. Use more complex machine learning models, such as neural network built in tensorflow.
5. Use custom distance function in TSNE instead of the default euclidean distance. A *aaaaaa* sequence is much more similar to a *aaaaat* sequence than a *tgctgc* sequence, but right now they are being treated in a similar manner.
