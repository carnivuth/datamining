---
id: DIMENSIONALITY REDUCTION
aliases: []
tags: []
index: 6
---

# DIMENSIONALITY REDUCTION

when dimensionality is very high occupation of the space become sparse and discrimination based on distance becomes ineffective

the scope of this processing is to:

- avoid this problem called the **curse of dimensionality**
- reduce noise on data
- reduce time and memory complexity of the mining algorithms
- improve visualization

## PCA

procedure to extract important variables from the dataset and reduce dimensionality. The new dataset will contains the attributes that capture most of the data variation

the PCA algorithm uses [singular value decomposition](https://en.wikipedia.org/wiki/Singular_value_decomposition) to find the attributes that capture most of the data variation and reduce the number of dimensions in the dataset to make it more suitable for ML processes

[PREVIOUS](FEATURE_SUBSET_SELECTION.md) [NEXT](SCALING.md)
