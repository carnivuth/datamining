---
id: SAMPLING
aliases: []
tags: []
index: 8
---

# SAMPLING

the process of reducing the dataset dimensions making samples, the goals are:

- reduce dimension of datasets for computing necessities
- impossibility to obtain the full dataset

a sample of a dataset **can be usefull if it is representative**

## TYPES

- ### SIMPLE RANDOM

	random choice of a object with given probability distribution

- ### WITH REPLACEMENT

	repetition of independent extractions of type symple random

- ### WITHOUT REPLACEMENT

	repetition of extractions, extracted element is removed from the population, in a small population a small subject could be underestimated

- ### STRATIFIED

	split data into several partitions according to some criteria, then draw the random samples from each partition

## SAMPLE SIZE

select the sample size is a tradeoff between data reduction and precision, there are techniques to get the optimal sample size and a sample that has meaning



## MISSING CLASSES

the probability of sampling at least an element for each class is independent from the size of the dataset (**if using replacement**)

![](Pasted_image_20240104121302.png)

this is important when using a small dataset for cross-validation or train test splits cause there could be not enough data for the partition

[PREVIOUS](SCALING.md) [NEXT](FEATURE_CREATION.md)
