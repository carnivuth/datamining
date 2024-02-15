## Which is different from the others:

- Expectation Maximisation
- Apriori
- K-means
- **Decision Tree** 

## What is the cross validation:

- **A technique to obtain a good estimation of the performance of a classifier when it will be used with data different from the training set**
- A technique to obtain a good estimation of the performance of a classifier with the training set
- A technique to improve the quality of a classifier
- A technique to improve the speed of a classifier

## What is the single linkage?

- A method to compute the distance between two objects, it can be used in hierarchical clustering
- **A method to compute the distance between two sets of items, it can be used in hierarchical clustering**
- A method to compute the distance between two classes, it can be used in decision trees
- A method to compute the separation of the objects inside a cluster

## Which of the following characteristic of data can reduce the effectiveness of DBSCAN?

- Clusters have concavities
- All the variables are the same range of values
- Presence of outliers
- **Presence of clusters with different densities**

## Which of the following types of data allows the use of the euclidean distance?

- **Points in a vector space**
- Ordered data
- Transactional data
- Document representations

## How does pruning work when generating frequent itemsets?

- **If an itemset is not frequent, then none of its supersets can be frequent, therefore the frequencies of the supersets are not evaluated**
- If an itemset is frequent, then none of its supersets can be frequent, therefore the frequencies of the supersets are not evaluated
- If an itemset is not frequent, then none of its subsets can be frequent, therefore the frequencies of the subsets are not evaluated
- If an itemset is frequent, then none of its subsets can be frequent, therefore the frequencies of the subsets are not evaluated

## In a decision tree, the number of objects in a node...

- **... is smaller than the number of objects in its ancestor**
- ... is not related to the number of objects in its ancestor
- ... is smaller than or equal to the number of objects in its ancestor
- ... is bigger than the number of objects in its ancestor

## What does K-means try to minimise?

- The distortion, that is the sum of the squared distances of each point with respect to the points of the other clusters
- **The distortion, that is the sum of the squared distances of each point with respect to its centroid**
- The separation, that is the sum of the squared distances of each point with respect to its centroid
- The separation, that is the sum of the squared distances of each cluster centroid with respect to the global centroid of the dataset

## Given the following definitions: TP = True Positives; TN = True Negatives; FP = False Positives; FN = False Negatives. Which of the formulas below computes the precision of a binary classifier?

- **$TP / (TP + FP)$**
- $(TP + TN) / (TP + FP + TN + FN)$
- $TN / (TN + FP)$
- $TP / (TP + FN)$

## Given the two binary vectors below, which is their similarity according to the Jaccard Coefficient?

```
1000101101
1011101010
```

- 0.1
- 0.2
- 0.5
- **0.375**

## Consider the transactional dataset below: Which is the support of the rule A,C->B

| ID Items |
| ---- |
| A,B,C |
| A,B,D |
| B,D,E |
| C,D |
| A,C,D,E |

- 100%
- **20%**
- 40%
- 50%

## Which of the following statements is true?

- **The noise can generate outliers**
- The noise always generate outliers
- The data which are similar to the majority are never noise
- **Outliers can be due to noise**

## Which of the following clustering methods is not based on distances

- between objects?
- Hierarchical Agglomerative
- DBSCAN
- K-Means
- **Expectation Maximization**

## In a decision tree, an attribute which is used only in nodes near the leaves...

- ... is irrelevant with respect to the target
- ... guarantees high increment of purity
- **... gives little insight with respect to the target**
- ... has a high correlation with respect to the target

## Which of the statements below is true? (Only one)

- **Sometimes k-means stops to a configuration which does not give the minimum distortion for the chosen value of the number of clusters**
- K-means always stop to a configuration which gives the minimum distortion for the chosen value of the number of clusters
- K-means works well also with datasets having a very large number of attributes
- K-means finds the number of clusters which give the minimum distortion

## Which of the statements below is true? (One or more)

- **Increasing the radius of the neighourhood can decrease the number of noise points**
- DBSCAN always stops to a configuration which gives the optimal number of clusters
- **Sometimes DBSCAN stops to a configuration which does not include any cluster**
- **DBScan can give good performance when clusters have concavities**

## In data preparation which is the effect of normalisation?
- **Map all the numeric attributes to the same range, without altering the distribution, in order to avoid that attributes with large ranges have more influence**
- Map all the numeric attributes subtracting the respective mean and dividing by variance
- Map all the numeric attributes to the same range and to have a Gaussian (or normal distribution, in order to avoid that attributes with large ranges have more influence
- Map all the numeric attributes in order to have a Gaussian (or 𝘯𝘰𝘳𝘮𝘢𝘭## 𝘥𝘪𝘴𝘵𝘳𝘪𝘣𝘶𝘵𝘪𝘰𝘯, in order to avoid that attributes with large ranges have more influence

## Consider the transactional dataset below: Which is the confidence of the rule A,C->B

| ID Items |
| ---- |
| A,B,C |
| A,B,D |
| B,D,E |
| C,D |
| A,C,D,E |

- **50%**
- 40%
- 20%
- 100%

## Which of the statements below about Hierarchical Agglomerative Clustering is true?

- Requires the definition of Inertia of clusters
- **Requires the definition of distance between sets of objects**
- Is very efficient also with large datasets
- Is based on a well founded statistical model

## When training a neural network, what is the learning rate?

- The speed of convergence to a stable solution during the learning process
- The ratio between the size of the hidden layer and the input layer of the network
- The slope of the activation function in a specific node
- **A multiplying factor of the correction to be applied to the connection weights**

## What are the hyperparameters of a Neural Network? (Possibly non exhaustive)

- Hidden layers structure, Output layer structure, Activation function, Number of epochs
- Network structure, Learning rate, Backpropagation algorithm, Number of epochs
- Input layers structure, Learning rate, Activation function, Number of epochs
- **Hidden layers structure, Learning rate, Activation function, Number of epochs**

## Which of the following preprocessing activities is useful to build a Naive Bayes classifier if the independence hypothesis is violated:

- Discretisation
- Normalisation
- Standardisation
- **Feature selection**

## Which is different from the others?

- **Silhouette Index**
- Misclassification Error
- Entropy
- Gini Index

## Why do we prune a decision tree?

- **To eliminate parts of the tree where the decisions could be influenced by random effects**
- To eliminate rows of the dataset which could be influenced by random effects
- To eliminate parts of the tree where the decision could generate underfitting
- To eliminate attributes which could be influenced by random effects

## In a dataset with D attributes, how many subsets of attributes should be considered for feature selection according tp an exhaustive search?

- **$\mathcal{o}(2^{d})$**
- $\mathcal{o}(D!)$ 
- $\mathcal{o}(D)$
- $\mathcal{o}(D^{2})$
## In which mining activity the Information Gain can be useful?

- Discovery of association rules
- **Classification**
- Clustering
- Discretization
## Given the two binary vectors below, which is their similarity according to the Simple Matching Coefficient?

```
1000101101
1011101010
```

- 0.1
- 0.3
- **0.5**
- 0.2
## Which is the main reason for the standardization of numeric attributes?

- Change the distribution of the numeric attributes, in order to obtain gaussian distributions
- **Map all the numeric attributes to a new range such that the mean is zero and the variance is one**
- Map all the nominal attributes to the same range, in order to prevent the values with higher frequency from having prevailing influence
- Remove non-standard values
## Which of the following measure can be used as an alternative to the Information Gain?

- Sihlouette Index
- **Gini Index**
- Rand Index
- Jaccard Index
## Which of the following is not an objective of feature selection

- **Select the features with higher range, which have more influence on the computation**
- Reduce time and memory complexity of the mining algorithms
- Reduce the effect of noise
- Avoid the curse of dimensionality
## After fitting DBSCAN with the default parameter values the results are: 0 clusters, 100% of noise points. Which will be your next trial?

- **Reduce the minimum number of objects in the neighborhood**
- Reduce the minimum number of objects in the neighborhood and the radius of the neighborhood
- **Increase the radius of the neighborhood**
- Decrease the radius of the neighborhood
## What is the meaning of the statement "the support is anti-monotone"?

- **The support of an itemset never exceeds the support if its subsets**
- The support of an itemset is always smaller than the support of its supersets
- The support of an itemsets never exceeds the support if its supersets
- The support of an itemset is always smaller than the support of its subsets
## In feature selection, what is the Principal Component Analysis?

- A mathematical technique used to transform non numeric attributes into numeric attributes
- **A mathematical technique used to transform a set of numeric attributes into a smaller set of numeric attributes which capture most of the variability in data**
- A heuristic technique used to find a subset of the attributes which produces the same classifier
- A mathematical technique used to find the principal attributes which determine the classification process
## A Decision Tree is...

- A tree-structured plan of tests on single attributes to forecast the cluster
- **A tree-structured plan of tests on single attributes to forecast the target**
- A tree-structured plan of tests on single attributes to obtain the maximum purity of a node
- A tree-structured plan of tests on multiple attributes to forecast the target
## In data preprocessing, which of the following are the objectives of the aggregation of attributes?

- Obtain a more detailed description of data
- **Obtain a less detailed scale**
- **Reduce the variability of data**
- **Reduce the number of attributes or distinct values**
## In order to reduce the dimensionality of a dataset, which is the advantage of Multi Dimensional Scaling (MDS), with respect to Principal Component Analysis (PCA)

- MDS requires less computational power
- **MDS can be used also with categorical data, provided that the matrix of the distance is available, while PCA is limited to vector spaces**
- MDS can be used with categorical data after a transformation in a vector space
- MDS can work on any kind of data, while PCA is limited to categorical data

## What is the main purpose of smoothing in Bayesian classification?

- **Classifying an object containing attribute values which are missing from some classes in the training set**
- Dealing with missing values
- Reduce the variability of the data
- Classifying an object containing attribute values which are missing from some classes in the test set

## Consider the transactional dataset below: Which is the confidence of the rule B -> E ?
 
| ID Items |
| -------- |
| A,B,C         |
| A,B,D         |
| B,D,E         |
| C,D         |
| A,C,D,E         |

- 100%
- 50%
- **33%**
- 20%
## In a Decision Tree for classification, what is a lead node?

- **A node which assigns a class value to the objects passing the tests on the path from the root to the node itself**
- A node where all the objects belong to the same class
- A node which allows classification without errors
- A node which assigns a class value only by majority of examples

## Match the rule evaluation formulas with their names:

- 1. $sup(A ∪ C) − sup(A)sup(C)$
- 2. $\frac{conf(A ⇒ C)}{sup(C)}$
- 3. $\frac{sup(A ⇒ C)}{sup(A)}$
- 4. $\frac{1 − sup(C)}{1 − conf(A ⇒ C)}$
​
Options:

- Confidence → 3
- Lift → 2
- Leverage → 1
- Conviction → 4

## Which of the statements below best describes the strategy of Apriori in finding the frequent itemsets?

- Evaluation of the support of the itemsets in an order such that uninteresting parts of the search space are considered only at the end of the execution
- Evaluation of the confidence of the itemsets in an order such that uninteresting parts of the search space are pruned as soon as possible
- **Evaluation of the support of the itemsets in an order such that uninteresting parts of the search space are pruned as soon as possible**
- Evaluation of the support of the itemsets in an order such that the interesting parts of the search space are pruned as soon as possible

## What is the Gini index?

- A measure of the entropy of a dataset
- An accuracy measure of a dataset alternative to the Information Gain and to the Misclassification Index
- **An impurity measure of a dataset alternative to the Information Gain and to the Misclassification Index**
- An impurity measure of a dataset alternative to overfitting and underfitting

## What measure is maximised by the Expectation Maximisation algorithm for clustering?

- **The likelihood of a class label, given the attributes of the example**
- The likelihood of an attribute, given the class label
- The likelihood of an example
- The support of a class

## Given the following definitions: TP = True Positives; TN = True Negatives; FP = False Positives; FN = False Negatives. Which of the formulas below computes the accuracy of a binary classifier?

- $\frac{TN}{TN + FP}$
- $\frac{TP + TN}{TP + FP + TN + FN}$
- $\frac{TP}{TP + FN}$
- $\frac{TP}{TP + FP}$

answer: 2

## In data preprocessing, which of the following is not an objective of the aggregation of attributes

- Reduce the variability of data
- Obtain a less detailed scale
- Reduce the number of attributes or objects
- **Obtain a more detailed description of data**

## Which of the following is a strength of the clustering algorithm DBSCAN?

- Requires to set the number of clusters as a parameter
- **Ability to find cluster with concavities**
- **Ability to separate outliers from regular data**
- Very fast by computation

## Which of the following statements regarding the discovery of association rules is true? (One or more)

- **The confidence of a rule can be computed starting from the supports of the itemsets**
- **The support of an itemset is anti-monotonic with respect to the composition of the itemset**
- The support of a rule can be computed given the confidence of the rule
- The confidence of an itemset is anti-monotonic with respect to the composition of the itemset
## For each type of data choose the best suited distance function

- Vector space with real values -> euclidean distance
- Vectors of terms representing documents -> cosine distance
- High dimensional spaces -> Manhattan distance
- Boolean data -> jaccard coefficient

## Which of the following is not a strength point of Dbscan with respect to K-means

- The robustness with respect to outliers
- The effectiveness, even in presence of noise
- The effectiveness even if there are clusters with non-convex shape
- **The efficiency even in large datasets**

## Which is the effect of the curse of dimensionality

- When the number of dimensions increases the results tend to be prone to overfitting
- **When the number of dimensions increases the euclidean distance becomes less effective to discriminate between points in the space**
- When the number of dimensions increases the computing power necessary to compute the distances becomes too high
- When the number of dimensions increases the classifiers cannot be correctly tuned
## Which is different from the others?

- Expectation Maximisation
- **Decision Tree**
- K-means
- Dbscan

## In a Neural Network, what is the backpropagation?

- The technique used to adjust the node weights according to the difference between the desired output and the output generated by the network
- The technique used to adjust the weights limiting the probability of overfitting
- The technique used to adjust the output according to the difference between the desired weights and the actual weights
- **The technique used to adjust the connection weights according to the difference between the desired output and the output generated by the network**

## Which is different from the others?

- **Dbscan**
- SVM
- Neural Network
- Decision Tree

## Which of the following is not a property of a metric distance function

- Symmetry
- Positive definiteness
- Triangle inequality
- **Boundedness**

## Which of the statements below is true? (One or more)

- K-mean always stops to a configuration which gives the minimum distortion for the chosen value of the number of clusters
- **K-means is very sensitive to the initial assignment of the centers**
- **K-means is quite efficient even for large datasets**
- **Sometimes k-means stops to a configuration which does not give the minimum distortion for the chosen value of the number of clusters**

## Which of the following characteristic of data can reduce the effectiveness of K-Means?

- Presence of values with high frequency
- **Presence of outliers**
- All the variables have the same distribution of values
- All the variables have the same range of values

## Which is the purpose of discretisation?

- Increase the number of distinct values in an attribute, in order to put in evidence possible patterns and regularities
- Reduce the number of distinct values in an attribute, in order to increase the efficiency of the computations
- **Reduce the number of distinct values in an attribute, in order to put in evidence possible patterns and regularities**
- Reduce the range of values of a numeric attribute, to make all the attributes more comparable

## Given the following definitions: TP = True Positives; TN = True Negatives; FP = False Positives; FN = False Negatives. Which of the formulas below computes the recall of a binary classifier?

- $\frac{TP}{TP + FN}$
- $\frac{TN}{TN + FP}$
- $\frac{TP}{TP + FP}$
- $\frac{TP + TN}{TP + FP + TN + FN}$

answer: 1
## The Information Gain is used to

- **select the attribute which maximises, for a given training set, the ability to predict the class value**
- select the attribute which maximises, for a given test set, the ability to predict the class value
- select the attribute which maximises, for a given training set, the ability to predict all the other attribute values
- select the class with maximum probability

## Which is the main reason for the MinMax scaling (also known as "rescaling") of attributes?

- Change the distribution of the numeric attributes, in order to obtain gaussian distributions
- Map all the nominal attributes to the same range in order to prevent the values with higher frequency from having prevailing influence
- Remove abnormal values
- **Map all the numeric attributes to the same range, in order to prevent attributes with higher range from having prevalent influence**

## Which of the following is a base hypothesis for a bayesian classifier?

- **The attributes must be statistically independent inside each class**
- The attributes must have negative correlation
- The attributes must be statistically independent
- The attributes must have zero correlation

## When developing a classifier, which of the following is a symptom of overfitting?

- The error rate in the test set is much smaller than the error rate in the training set
- The precision is much greater than the recall
- The error rate in the test set is more than 30%
- **The error rate in the test set is much greater than the error rate in the training set**

## With reference to the total sum of squared errors and separation of a clustering scheme, which of the statements below is true?

- They are two ways to measure the same thing
- They are strictly correlated, if, changing the clustering scheme, one increases, then the other does the same
- It is possible to optimise them (i.e. minimise SSE and maximise SSB) separately
- **They are strictly correlated, if, changing the clustering scheme, one increases, then the other decreases**
