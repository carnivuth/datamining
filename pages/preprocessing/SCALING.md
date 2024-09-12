---
id: SCALING
aliases: []
tags: []
index: 7
---

# SCALING

Task that makes data more omogeneous. It's used when there is a massive presence of outliers, which could affect too much the model during the training step.

**Scalers** allow to scale values in such a way that these values have a more omogeneous distribution. The most famous one is the MinMaxScaler:

				`from sklearn.preprocessing import MinMaxScaler

It transforms values to make them stay in a [0,1] range.

USAGE:

`#1) Initiate the scaler`
`scaler = MinMaxScaler()`

`#2)Reshaping data --> we want them in a column/row-array-like form (1-Dim)`
	`#2.1) Column`
		`X.reshape(-1,1)`
	`#2.2) Row`
		`X.reshape(1,-1)`

`#2)fitting and transforming the data`
`Xs = scaler.fit_transform(X)`

Now we have a scaled dataset!

[PREVIOUS](DIMENSIONALITY_REDUCTION.md) [NEXT](SAMPLING.md)
