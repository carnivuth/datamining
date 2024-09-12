---
id: DISTANCES
aliases: []
tags: []
index: 4
---

# DISTANCES

## PROPERTIES OF DISTANCES

- **symmetry** $Dist(p,q) = Dist(q, p)$
- **positive definiteness** $Dist(p,q) >= 0 \forall\space{p,q}$
- **Triangle inequality** $Dist(p,q) <= Dist(p,r) + Dist(r,q) \forall\space{p,q,r}$

## EUCLIDEAN DISTANCE

$$
\sqrt{\sum_{d=1}^{D}{(p_{d}-q_{d})^2}}
$$

Where $D$ is the number of dimensions (attributes) and $p_{d}$ and $q_{d}$ are, respectively, the d-th attributes (components) of data objects p and q.
Standardization/Rescaling is necessary if scales differ

## MINKOWSKI DISTANCE $L_{r}$

generalization of euclidean distance

$$
(\sum_{d=1}^{D}{|p_{d}-q_{d}|^r})^{\frac{1}{r}}
$$

Where $D$ is the number of dimensions (attributes) and $p_{d}$ and $q_{d}$ are, respectively, the d-th attributes (components) of data objects p and q.
Standardization/Rescaling is necessary if scales differ.
$r$ is a parameter which is chosen depending on the data set and the application

### cases

- $r=1$ Manhattan distance
	best at discriminate between 0 distance and near 0 distance

- $r=2$ Euclidean distance

- $r=\infty$ Chebyshev, supremum, $L_{max}$ norm, $L_{\infty}$ norm
	considers only the feature with the maximum difference
	$$
	\max_{d}{|p_{d}-q_{d}|}
	$$

## MAHALANOBIS DISTANCE

The Mahlanobis distance between two points p and q decreases if, keeping the same euclidean distance, the **segment connecting the points is stretched along a direction of greater variation of data**. The distribution is described by the covariance matrix of the data set

$$
\sqrt{(p-q)\sum^{-1}{(p-q)^T}}
$$


[PREVIOUS](SIMILARITY_AND_DISSIMILARITY.md) [NEXT](FEATURE_SUBSET_SELECTION.md)
