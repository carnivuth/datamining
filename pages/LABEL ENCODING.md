# LABEL ENCODING

Transforming in a numerical quantity the features that represent categories.


We have 3 major encoders, divided in:

- ### ENCODERS APPLIED TO PREDICTORS
- ### ENCODERS APPLIED TO THE TARGET

## ENCODERS APPLIED TO PREDICTORS

We have:

- **OneHotEncoder**: we can import it by the command  
  
				  `from sklearn.preprocessing import OneHotEncoder`
				  
	It transforms features in a set of columns that integrate the predictor X:
		1. it counts all the categories within the features;
		2. it replaces the analyzed features with as many columns as there are categories;
		3. all the new columns values will be 0 or 1. For every sample (X's rows), it will be put the 1 value only if the column corresponds to the represented category.

- **OrdinalEncoder**: we can import it by the command  

				  `from sklearn.preprocessing import OrdinalEncoder`

		1. it locates all the categories available;
		2. it assignes an incremental value to every category
		3. a single column with the corresponding incremental values is returned


## ENCODERS APPLIED TO TARGET

The most famous is LabelEncoder (`from sklearn.preprocessing import LabelEncoding`).
It's similar to OrdinalEncoding, but it's applied to the targed instead of the predictor.


## USAGE

After we have imported the encoder, we have to:
1) Create an object for the encoder
   
	   ohe = OneHotEncoder()     #OneHotEncoder
	   oe = OrdinalEncoder()         #OrdinalEncoder
	   le = LabelEncoder()              #LabelEncoder
	   
2) Fit the encoder
   
	   ohe.fit(X)
	   oe.fit(X)
	   le.fit(y)
	   
3) Show the found categories
   
	   ohe.categories_
	   oe.categories_
	   le.classes

4) Transform the found categories
   
	   ohe.transform(X)
	   oe.transform(X)
	   le.transform(y)