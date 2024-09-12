---
id: HIERARCHICAL CLUSTERING
aliases: []
tags: []
index: 4
---

# HIERARCHICAL CLUSTERING

Type of clustering that revolves around creating a nested structure of clustering, there are 2 types of hierarchical clustering:

- ## Agglomerative (bottom up approach)

```mermaid
flowchart TD
	A[each data point is considered a cluster];
	B[the two less separated cluster are merged together];
	A-->B
	B-->|repeat until the best \n clustering scheme|A
```

- ## Divisive (top down approach)


```mermaid
flowchart TD
	A[the entire dataset is the only cluster];
	B[the cluster with the lowest cohesion is split];
	A-->B
	B-->|repeat until the best \n clustering scheme|A
```

## COMPLEXITY

the complexity of hierarchical clustering is $\mathcal{O}(N^2)$ for the computation and storage of the distance matrix

for the single step iteration the complexity is $\mathcal{O}((N-1)^2)$

so in conclusion the time complexity is $\mathcal{O}(N^3)$

## CONS

 - poor scaling due to high complexity
 - no global objective function


[PREVIOUS](K-MEANS.md) [NEXT](MODEL_BASED_CLUSTERING.md)
