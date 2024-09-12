---
id: PERFORMANCE OF A CLASSIFIER
aliases: []
tags: []
index: 3
---

# PERFORMANCE OF A CLASSIFIER


## DEFINITIONS

in a classification problem where **class is a binary attribute** the follow schema can be produced in order to study data

|              | POS-PRED   | NEG-PRED   |
| ------------ | ---------- | ---------- |
| **POS-TRUE** | $TP$       | $FP_{a-b}$ |
| **NEG-TRUE** | $FP_{b-a}$ | $TN$       |

where:

- $TP$ true positives
- $TN$ true negatives
- $FP$ false positives
- $FN$ false negatives

these measurements can be used to calculate some interesting performance metrics such as

- ### SUCCESS RATE (ACCURACY)

accuracy of the classifier

	$$
	\frac{TP + TN}{Ntest}
	$$

- ### ERROR RATE

	$$1 - accuracy$$
- ### PRECISION

	rate of true positives among positive classifications

	$$
	\frac{TP}{TP + FP}
	$$


- ### RECALL

	rate of positives that the classifier can catch (sensitivity)

	$$
	\frac{TP}{TP + FN}
	$$

- ### SPECIFICITY

	rate of negatives that the classifier can catch

	$$
	\frac{TN}{TN + FP}
	$$

- ### F1 SCORE

	armonic mean of precision and recall

	$$
	2*\frac{precision*recall}{precision + recall}
	$$

![](Pasted_image_20231230184224.png)

**accuracy** gives an inital idea of the performance but **can be misleading when classes are unbalanced**

**f1 score** is insteresting because is higher when **precision and recall are balanced**

if the **cost of positive and negative errors are different** than **precision and recall** should be considered

## MULTI CLASS CASE

in a problem with non binary class attribute the previous table can be extended, it's called **confusion matrix**

|           | a        | b        | c        | Total   |
| --------- | -------- | -------- | -------- | ------- |
| **a**     | $TP_{a}$ | $FP_{a-b}$         | $FP_{c-a}$         | $T_{a}$ |
| **b**     | $FP_{b-a}$         | $TP_{b}$ | $FP_{c-b}$         | $T_{b}$ |
| **c**     | $FP_{c-a}$         | $FP_{b-c}$         | $TP_{c}$ | $T_{c}$ |
| **Total** | $P_{a}$         | $P_{b}$         | $P_{c}$         | N       |

- $T_{x}$ true number of $x$ labels in the dataset
- $P_{x}$ total number of predictions of class $x$
- $TP_{x}$ true positives for class $x$
- $FP_{i-j}$ false positives for class $i$ predicted as $j$

- ### ACCURACY

	$$
	\frac{\sum_{i}{TPi}}{N}
	$$
- ### PRECISION $i$

	$$
	\frac{TPi}{Pi}
	$$


- ### RECALL $i$

	$$
	\frac{TPi}{Ti}
	$$

these measures can be global:

$$
f(C)= \frac{\sum{f(ci)}}{C}
$$

these measures can be weighted:

$$
f(C)= \frac{\sum{f(ci)*Ci}}{C}
$$

[PREVIOUS](TRAINING_STRATEGIES.md) [NEXT](DECISION_TREES.md)
