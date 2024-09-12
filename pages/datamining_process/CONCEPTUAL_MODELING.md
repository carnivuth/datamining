---
id: CONCEPTUAL MODELING
aliases: []
tags: []
index: 5
---

# CONCEPTUAL MODELING

- DWH modeling approaches are as follow

| REQUIREMENT DRIVEN APPROACH | the model is based of user interaction requirements, no knowledge about data sources |
|-----------------------------|--------------------------------------------------------------------------------------|
| DATA DRIVEN APPROACH        | the model is based on the data sources available                                     |
| MIXED APPROACH              | the requirement analysis refine the model derived by the data sources available      |

## DIMENSIONAL FACT MODEL

### objectives

- create effective documentation
- support for conceptual design
- user friendly environment for queries
- favor communication between the designer and the user

### dictionary

| CONCEPT               | DESCRIPTION                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------|
| fact                  | something relevant to the decision making process                                                    |
| measure               | numerical property of a fact                                                                         |
| dimension             | it's a fact property with a finite domain                                                            |
| dimensional attribute | dimensions with possible attributes                                                                  |
| hierarchy             | directed tree with dimensional attributes as nodes, it includes a dimension at the root of the tree  |

| CONCEPT         | DESCRIPTION                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------|
| PRIMARY EVENT   | particular occurrence of a fact identified by a n-ple for each dimension                         |
| SECONDARY EVENT | identified by a set of n-ple dimensional attribute values, it aggregates a set of primary events |


![](Pasted_image_20231010165953.png)


[PREVIOUS](DATA_WAREHOUSE_ARCHITECTURES.md) [NEXT](CRISP_DM_METHODOLOGY.md)
