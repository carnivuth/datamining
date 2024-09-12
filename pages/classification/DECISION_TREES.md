---
id: DECISION TREES
aliases: []
tags: []
index: 4
---

# DECISION TREES

Decision trees are tree shaped data structures with node and leaf
that represents operations on the datasets used to classified data

- leaf -> put data in class c (class of the leaf node)

- node -> split dataset and exec leaf node with the dataset subsets

## SPLITTING DATASET METHODS

### INFORMATION THEORY BASED METHOD

based on the concept of entropy

$$
H(X)= -\sum{p_{j}\log{2}{p_{j}}}
$$

- higher the entropy -> attribute values with the same probability

- lower the entropy -> attribute values with the same probability

the entropy of a child node is always lower of the entropy of the father node

#### INFORMATION GAIN

the difference between the dataset entropy and the subset entropy obtained from a threshold based split

the objective is to maximize information gain in order to obtain the best split

#### CHOOSING THE RIGHT ATTRIBUTE FOR THE SPLIT

the attribute with the maximum [IG](#INFORMATION_GAIN) is chosen

### BUILD DECISION TREE WITH BINARY SPLITS

```python
procedure buildTree(dataset X , node p)

	if all the class values of X are c then
		return node p as a leaf, label of p is c

	if no attribute can give a positive information gain in X then
		say that the majority of elements in X has class c
		return node p as a leaf, label of p is c

find the attribute d and threshold t giving maximum information gain in X
create two internal nodes descendant of p, say pleft and pright
let X left = selection on X with d < t
buildTree(X left , pleft )
let X right = selection on sdata with d >= t
buildTree(X right , pright )

```

### TRAINING SET ERROR

number of discordance between predictions on the training set and the actual values of the attributes

it's a lower bound for the error rate of the predictions

### TEST SET ERROR

same calculus of the  [training set error](#TRAINING_SET_ERROR)

the value is more indicative of the expected behavior

### OVERFITTING

it happens when the hypothesis is fits too well the training data

$$
error_{train}(h) \lt error_{train}(h')
$$
$$
error_{X}(h) \gt error_{X}(h')

$$

possible causes of over-fitting can be the presence of noise on the data or a bad representative training set of the $X$ dataset.

One of the possible solutions to overfitting is [decision tree pruning](DECISION_TREE_PRUNING.md)

### CHOOSING ATTRIBUTE FOR SPLIT WITH THE HIGHEST PURITY

- [INFORMATION THEORY BASED METHOD](#INFORMATION_THEORY_BASED_METHOD)
- [GINI INDEX](#GINI_INDEX)
- [MISCLASSIFICATION ERROR](#MISCLASSIFICATION_ERROR)

### GINI INDEX

based on the probability of wrong classification of a random assignment based on class frequencies

it is the sum of the frequencies of wrong classification

$$
GINI_{p}=1- \sum_{j}{f^{2}_{pj}}
$$

the split is done by minimize the gini index reduction

$$
GINI_{split}=GINI_{p} - \sum_{i=1}^{ds}{\frac{N_{p,i}}{N_{p}}*GINI(p_{i})}
$$

### MISCLASSIFICATION ERROR


it's complement to 1  of the highest label frequency called accuracy
the split is like the one of the [GINI INDEX](#GINI_INDEX)

$$
ME(p) = 1 - max_{j}(f_{pj})
$$


[PREVIOUS](PERFORMANCE_OF_A_CLASSIFIER.md) [NEXT](DECISION_TREE_PRUNING.md)
