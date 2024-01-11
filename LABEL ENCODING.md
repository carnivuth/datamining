# LABEL ENCODING

Transforming in a numerical quantity the features that represent categories.

there are 2 types of encoders
## ENCODERS APPLIED TO PREDICTORS

- ### ONE HOT ENCODER  
  		   
	It transforms features in a set of columns that integrate the predictor X:
	
	-  it counts all the categories within the features;
	-  it replaces the analyzed features with as many columns as there are categories;
	-  all the new columns values will be 0 or 1. For every sample (X's rows), it will be put the 1 value only if the column corresponds to the represented category.

	here a usage example:
	
	```python
	from sklearn.preprocessing import OneHotEncoder
	ohe = OneHotEncoder() # creating object
	ohe.fit(X) # fit the data
	ohe.categories_ # show categories founded
	ohe.transform(X) # apply the transformation
	```

- ### ORDINAL ENCODER  

	- it locates all the categories available;
	-  it assignes an incremental value to every category
	-  a single column with the corresponding incremental values is returned

	here a usage example:

```python
from sklearn.preprocessing import OrdinalEncoder
oe = OrdinalEncoder() # creating object
oe.fit(X) # fit the data
oe.categories_ # show categories founded
oe.transform(X) # apply the transformation
```
## ENCODERS APPLIED TO TARGET

The most famous is **LabelEncoder**.
It's similar to OrdinalEncoding, but it's applied to the targed instead of the predictor.

here a usage example:

```python
from sklearn.preprocessing import LabelEncoding
le = LabelEncoding() # creating object
le.fit(y) # fit the data
le.classes # show classes founded
le.transform(y) # apply the transformation
```