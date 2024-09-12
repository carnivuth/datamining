---
id: CLUSTERING
aliases: []
tags: []
index: 1
---

# CLUSTERING

Clustering manage the problem of arrange data in a series of $k$ cluster such as the intra-cluster [similarity](SIMILARITY_AND_DISSIMILARITY.md#SIMILARITY) is maximized.

So given a set of $N$ object with $D$ features the result of clustering is a **clustering scheme**, a function that maps each object in a $[1....k]$ clusters or to noise

$$
\forall x_{1},x_{2} \in X clust(x_{1}) = clust(x_{2})\space if \space x_{1}\space is \space similar \space to \space x_{2}
$$

$$
\forall x_{1},x_{2} \in X clust(x_{1}) \neq clust(x_{2})\space if \space x_{1}\space is \space not \space similar \space to \space x_{2}
$$

## CENTROID

A point which is the center of gravity of the cluster, for each cluster $k$ and dimension $d$, the $d$ coordinate of the centroid is

$$
	centroid_{d}^{k}= \frac{1}{x_{i}: clust(x_{i})=k}\sum_{x_{i}: clust(x_{i})=k}{x_{id}}
$$




 [NEXT](CLUSTERING_SCHEME_EVALUATION.md)
