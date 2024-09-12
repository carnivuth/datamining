---
id: OLAP
aliases: []
tags: []
index: 2
---

-  Online analitical processing allow users to interactively navigate on the DWH

- navigation is done trough chains of operators

## OLAP OPERATORS

### roll-up

- adds aggregation to the data collection

	- ![](Pasted_image_20231005143104.png)

### drill-down

- removes aggregation from the data collection

 ![](Pasted_image_20231005143041.png)

### slice-and-dice

- set a dimension to a specific value reducing the data collection dimensions

![](Pasted_image_20231005143020.png)

### pivot

 - change in layouts of the collection of the data

 ![](Pasted_image_20231005143426.png)

### drill-across

 - create a liink between data co compare them

 ![](Pasted_image_20231005143524.png)

### drill-through

 - switches from the multidimensional data model into a operational data
 ![](Pasted_image_20231005143844.png)

## EXTRACTION TRANSFORMATION AND LOADING (ETL)

The **ETL** process aims to get data from sources, improve general data quality, transform data according to the schema and loads it in the DWH


```mermaid
---
title: ETL
---
flowchart TD
A[EXTRACTION\nextract data from sources]
B[CLEANSING\nimprovements to the quality\nremoving duplicates]
C[TRASFORMATION\ndata processing according to the schema]
D[LOADING\nload data in the DWH]
A --> B
B --> C
C --> D
```

### EXTRACTION

The extraction phase aims to get data from the datasources, there are 2 possible approaches: **STATIC**  or **INCREMENTAL**


```mermaid
---
title: EXTRACTION
---
flowchart TD
A[APPROACHES]
B[STATIC\nDWH is populated for the first time]
C[INCREMENTAL\nthe DWH is updated with new data regularly]
A --> B & C
```

Each approach is more suitable for certain types of data:

| types of data                                        | types of extraction                             |
|------------------------------------------------------|-------------------------------------------------|
| structured data (from databases or formatted files ) | static (for the first DWH population operation) |
| unstructured data (from social media)                | incremental (for the update operations on the DWH)|

### CLEANSING

- data are processed to improve the quality, data are standardized and mistakes are corrected

#### SOLUTION FOR DATA INCONSISTENCIES

**Dictionary based techniques**

- they make use of dictionaries and lookup tables to fix typing errors

![](Pasted_image_20231008181755.png)

**Aproximate merging**

- needed when merging data from different sources and there is no common key

![](Pasted_image_20231008181831.png)
### TRANSFORMATION

- data are altered to match the information schema on the DWH

#### DENORMALIZATION

 - for relational database data are rearranged to reduce the number of queries to do on manipulation fase

![](Pasted_image_20231005150109.png)

### LOADING

#### REFRESH

- the DWH is completely rewritten with new data
#### UPDATE

- only changes on source are applied to the DWH existent data are not canceled or modified

[PREVIOUS](BUSINESS_INTELLIGENCE_AND_DATA_WAREHOUSE.md) [NEXT](DATA_LAKES.md)
