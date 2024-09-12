---
id: CLASSIFICATION
aliases: []
tags: []
index: 1
---

# CLASSIFICATION

a procedure which computes an unknown parameter for a given element

## CLASSIFICATION MODEL

An algorithm which, given an individual for which the class is not known, computes the class. The algorithm make use of parameters for tuning

the core of a classification model is the decision function.

- ### DECISION FUNCTION (the model)

	function that makes a prediction on the class element as

	$$
	M(x,\theta) = y(x)pred
	$$

where $\theta$ is a **set of values for the parameters** of the decision function

![](Pasted_image_20231227172912.png)

## VAPNIK-CHERVONENKIS DIMENSION

if a [classification model](#CLASSIFICATION_MODEL) is able to shatter all possible problems with N elements it's  Vapnik-Chervonenkis dimension is equal to $N$

## CLASSIFICATION WORKFLOW

- use the training dataset for tuning parameters

- use the training set against the classification model obtained at the previous step to calculate the accuracy

![](Pasted_image_20231227174100.png)


## CLASSIFICATION TYPES

- ### CRISP

	the classifier assigns to each individual one label

- ### PROBABILISTIC

	the classifier assigns a probability for each of the possible labels



 [NEXT](TRAINING_STRATEGIES.md)
