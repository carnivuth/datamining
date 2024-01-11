# REGRESSION

It's a supervised task used on numeric variables with the objective of **minimize the error of the prediction**  using the other variables for the prediction

## LINEAR REGRESSION

given a data set $X$ with $N$ rows and $D$ columns:

- $xi$ is a $D$ dimensional data element response vector $y$ with $N$ values $yi$
- $w$ is a $D$-dimensional vector of coefficients that needs to be learned

so the relation between the $yi$ element and the $xi$ elements is modeled

$$
yi = w^T*xi \space \forall i \in [1...N]
$$
so the forecast is given by

$$
y^f = X*w^T
$$


![](Pasted%20image%2020240102171514.png)

## QUALITY INDICATORS

- Mean of the observed data 

$$
y^{avg} = \frac{1}{N}*\sum_{i}{yi}
$$

- Sum of squared residuals SSres “ ř

$$
SSres = \sum_{i}({yi-yi^f})^2
$$

- Total sum of squares SStot “ ř

$$
SStot = \sum_{i}({yi-yi^{avg}})^2
$$

- Coefficient of determination 

$$
R^2 = 1 - \frac{SSres}{SStot}
$$

the Coefficient of determination compares the chosen model with that of a horizontal straight line

if the model does not follow the trend of the data the $R^2$ value can be also negative

when the number of feature is high overfitting is possible

## POLYNOMIAL REGRESSION

the target is influenced by a single feature and the relationship can't be describe by a straight line

![](Pasted%20image%2020240102175121.png)