-  Online analitical processing allow users to interactively navigate on the DWH 

- navigation is done trough chains of operators

## OLAP OPERATORS

### roll-up
	
- adds aggregation to the data collection

	- ![](Pasted%20image%2020231005143104.png)

### drill-down

- removes aggregation from the data collection

 ![](Pasted%20image%2020231005143041.png)
 
### slice-and-dice

- set a dimension to a specific value reducing the data collection dimensions

![](Pasted%20image%2020231005143020.png) 

### pivot
	
 - change in layouts of the collection of the data

 ![](Pasted%20image%2020231005143426.png)

### drill-across
	
 - create a liink between data co compare them

 ![](Pasted%20image%2020231005143524.png)

### drill-through
	
 - switches from the multidimensional data model into a operational data 
 ![](Pasted%20image%2020231005143844.png)

## EXTRACTION TRANSFORMATION AND LOADING (ETL)

- ETL process aims to feeding the DWH with data from external sourcess

### EXTRACTION

-  in this fase data are extracted from the external sources

| types of data                                        | types of extraction                             |
|------------------------------------------------------|-------------------------------------------------|
| structured data (from databases or formatted files ) | static (for the first DWH population operation) |
| unstructured data (from social media)                | incremental (for the update operations on the DWH)| 

### CLEANSING

- data are processed to improve the quality, data are standardized and mistakes are corrected

#### SOLUTION FOR DATA INCONSISTENCIES

**Dictionary based techniques** 

- they make use of dictionaries and lookup tables to fix typing errors 

![](Pasted%20image%2020231008181755.png)

**Aproximate merging**

- needed when merging data from different sources and there is no common key 

![](Pasted%20image%2020231008181831.png)
### TRANSFORMATION

- data are altered to match the information schema on the DWH

#### DENORMALIZATION
	
 - for relational database data are rearranged to reduce the number of queries to do on manipulation fase
 
![](Pasted%20image%2020231005150109.png)

### LOADING

#### REFRESH 

- the DWH is completely rewritten with new data
#### UPDATE

- only changes on source are applied to the DWH existent data are not canceled or modified 