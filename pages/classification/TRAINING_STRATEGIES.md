---
id: TRAINING STRATEGIES
aliases: []
tags: []
index: 2
---

# TRAINING STRATEGIES

there are 2 main strategies for test

- ### [HOLDOUT](#HOLDOUT)

	splitting data into training set and test set

- ### [CROSS VALIDATION](#CROSS_VALIDATION)

	repeted tests with different splits

## HOLDOUT

this strategy splits the data in static groups, training and test with a test ratio parameter (typical value $2/1$ )

 the split should be random and the proportion of classes between the data should be the same
### PROS

- train validation loop is faster than the cross validation
- the hyperparameters tuning is done with a different set of data

### CONS

- test is done with a portion of the samples



## CROSS VALIDATION

the training set is partitioned in $k$ subsets, than the **model is trained with 1 of the subsets for test and the other for training**, this **process is done $k$ times**. the final results are then combined together

![](Pasted_image_20231230181830.png)

### PROS

- more reliability thanks to the multiple runs
- all the data are used once for testing
- the final model is obtained using all data

### CONS

- train test loop repeated $k$ times


[PREVIOUS](CLASSIFICATION.md) [NEXT](PERFORMANCE_OF_A_CLASSIFIER.md)
