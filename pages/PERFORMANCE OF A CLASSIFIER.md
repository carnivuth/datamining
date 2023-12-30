# PERFORMANCE OF A CLASSIFIER 


## DEFINITIONS

![](Pasted%20image%2020231230185042.png)

- $TP$ true positives
- $TN$ true negatives
- $FP$ false positives
- $FN$ false negatives

there are a bunch of meters to measure the performance of a classifier

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

![](Pasted%20image%2020231230184224.png)

**accuracy** gives an inital idea of the performance but **can be misleading when classes are unbalanced**

**f1 score** is insteresting because is higher when **precision and recall are balanced**

if the **cost of positive and negative errors are different** than **precision and recall** should be considered


## MULTI CLASS CASE

in a multi class problem the previous table is extended in what is called **confusion matrix**

![](Pasted%20image%2020231230185422.png)

- $Tx$ true number of $x$ labels in the dataset
- $Px$ total number of predicitons of class $x$
- $TPx$ true positives for class $x$
- $FPi-j$ false positives for class $i$ predicted as $j$

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
