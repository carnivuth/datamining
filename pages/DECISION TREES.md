# DECISION TREES

Decision trees are tree shaped data structures with node and leaf
that represents operations on the datasets used to classified data

- leaf -> put data in class c (class of the leaf node)

- node -> split dataset and exec leaf node with the dataset subsets 

## SPLITTING DATASET METHODS

### INFORMATION THEORY BASED METHOD

based on the concept of entropy

$$
H(X)= -\sum{pj\log{2}{pj}}
$$

- higher the entropy -> attribute values with the same probability

- lower the entropy -> attribute values with the same probability

the entropy of a child node is always lower of the entropy of the father node

#### INFORMATION GAIN 

the difference between the dataset entropy and the subset entropy obtained from a threshold based split   

the objective is to maximize information gain in order to obtain the best split

#### CHOOSING THE RIGHT ATTRIBUTE FOR THE SPLIT

the attribute with the maximum [IG](#INFORMATION%20GAIN) is chosen

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

same calculus of the  [training set error](#TRAINING%20SET%20ERROR) 

the value is more indicative of the expected behavior 

### OVERFITTING

it happens when the hypothesis is fits too well the training data

![](Pasted%20image%2020231114164008.png)

#### CAUSES

- presence of noise 
	individuals with bad attribute values
- lack of representative instances
	some real world patterns can be underrepresented in the training data

solution to overfitting is pruning the decision tree


### CHOOSING ATTRIBUTE FOR SPLIT WITH THE HIGHEST PURITY

- [INFORMATION THEORY BASED METHOD](#INFORMATION%20THEORY%20BASED%20METHOD)
- [GINI INDEX](#GINI%20INDEX)
- [MISCLASSIFICATION ERROR](#MISCLASSIFICATION%20ERROR)

### GINI INDEX

based on the probability of wrong classification of a random assignment based on class frequencies

it is the sum of the frequencies of wrong classification

![](Pasted%20image%2020231114165002.png)

the split is done by minimize the gini index reduction

![](Pasted%20image%2020231114165235.png)

### MISCLASSIFICATION ERROR


it's complement to 1  of the highest label frequency called accuracy

the split is like the one of the [GINI INDEX](#GINI%20INDEX)

![](Pasted%20image%2020231114165507.png)



