---
id: CLUSTERING SCHEME EVALUATION
aliases: []
tags: []
index: 2
---

# CLUSTERING SCHEME EVALUATION

Clustering scheme evaluation is important in order to comprehend the quality of a clustering scheme, it's also used to compere clustering scheme

## MEASUREMENT CRITERIA

### COHESION [(SSE)](K-MEANS.md#DISTORTION_(*SUM_OF_SQUARE_ERRORS_SSE*))

the sum of the proximities between the element of the clusters and the geometric center (**prototype**), the prototype could be a [centroid](CLUSTERING.md#CENTROID) or a medoid in context where mean is not defined

### SEPARATION (SSB)

The distance between 2 clusters (proximity between prototypes)

$$
\sum_{i=1}^{K}{N_{i}Dist(c_{i},c)}^2
$$

### TOTAL SUM OF SQUARES (TSS)

Sum of square distances between the points and the global center

the **TSS** is the sum between SSE and SSB, this is a global property of the dataset

$$
TTS=SSE+SSB
$$

### SILHOUETTE

Is a measure of how much a point contributes to separation between clusters and increasing cohesion following formulas considers  silhouette value for a point $x_{i}$

$$
\frac{b_{i}-a_{i}}{max(b_{i},a_{i})}\in [-1,1] \space with
$$

$$
a_{i}= average_{j,y(x_{j})=y(x_{i})}(dist(x_{i},x_{j}))
$$
$$
b_{i}= min_{k \in \gamma, k \ne y(x_{i})}(average_{j,y(x_{j})=k}(dist(x_{i},x_{j})))
$$

$a_{i}$ is the average between the distances of all points in the same cluster and $b_{i}$ is the distance between the point and the points of all other clusters.
A lower then $0$ value means that there is a dominance of object in other clusters that are more closer than the points of the cluster

the global scores of silhouette are given by the average of the scores of all the single points

silhouette is a lot expensive to compute due to it's nature


## SEARCHING FOR THE BEST $k$ VALUE (the elbow method)

[silhouette](#SILHOUETTE) and [sse](K-MEANS.md#DISTORTION_(*SUM_OF_SQUARE_ERRORS_SSE*)) can be used in order to find the best value parameter, the best points to look are the minimums of the relation between sse and $k$ and the maximums in the relation between silhouette and $k$

![](Pasted_image_20240116140806.png)


## COMPARING CLUSTERING SCHEMES

The concept is similar to the ones used to test [classification](CLASSIFICATION.md#CLASSIFICATION_WORKFLOW), there is a known partition of the dataset similar to the data to be clustered called **gold standard** and a labeling scheme $y_{g}(.)$

$y_{g}(.)$ acts as a test set but for clustering so we can compare a clustering scheme to it and gain information about the quality of the clustering


[PREVIOUS](CLUSTERING.md) [NEXT](K-MEANS.md)
