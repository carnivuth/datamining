---
id: MODEL SELECTION
aliases: []
tags: []
---

# MODEL SELECTION

In order to select the best model for a given problem the follow parameters need to be identified:

- best classification model
- best classification algorithm
- best parameter configuration

## EVALUATION

the process for detecting the best classification model, this process is **independent from the algorithm used to create the model**

### DATASET IN EVALUATION

supervised data are usually scarse so the dataset must be split

- train
- evaluation
- test

### TEST SET ERROR AND RUN TIME RELATIONS

the bond between training dataset and the real data $X$ is subject to probabilistic variability so the  **prevision of the run time error error is the test set error ratio + confidence interval**

#### CONFIDENCE INTERVAL

the empirical frequency of error $f = \frac{S}{N}$ with $S$ the test error and $N$ the test set dimension is related with the true error frequency through **noise** that is represented with a normal distribution (for $N >= 30$ )

the confidence interval is the probability that the true frequency of success is below the pessimistic frequency

$$
P(z_{\alpha/2} \leq \frac{f-p}{\sqrt{p(1-p)/N}}\leq z_{(1-\alpha)/2}) = 1- \alpha
$$

boundaries on the curve $z$ depends on the desired confidence level $\alpha$

![](Pasted_image_20231230173630.png)



 [NEXT](CLASSIFICATION.md)
