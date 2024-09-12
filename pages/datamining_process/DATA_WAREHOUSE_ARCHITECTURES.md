---
id: DATA WAREHOUSE ARCHITECTURES
aliases: []
tags: []
index: 4
---

## REQUIREMENTS

### separation

-  analitycal and transactional processing should be take apart
### scalability

- the DWH need to be capable of handle large amounts of data
### extensibility

- the DWH should be able to host new applications without the need to redesign the hole system

### security

- the access to the DWH should be monitored
### administrability

- the DWH should be easy to manage

## SINGLE LAYER ARCHITECTURE

![](Pasted_image_20231010120852.png)

- the goal is to minimize the data collected in the DWH by reducing the separation between source layer and analysis layer
- to achieve this, a middleware software need to abstract the complexity and the divergency of the Source layer data

| PROS                              | CONS                                             |
|-----------------------------------|--------------------------------------------------|
| the space occupation is minimized | no separation between source and analysis layers |


## TWO LAYERS ARCHITECTURE

![](Pasted_image_20231010121252.png)

- in this architecture data are extracted from source layers trough ETL and are inserted in a data warehouse layer where they are stored and accessed by the analysis layer
- the source and the analysis layer are separated but there is more space occupied

| PROS                              | CONS                                             |
|-----------------------------------|--------------------------------------------------|
| source and analysis data are separated | less space optimization |


## THREE LAYERS ARCHITECTURE

![](Pasted_image_20231010122320.png)

- the reconciled layer is added to the two layers architecture that creates a consistent model of the data and separate data extraction problem and integration problem

| PROS                                                     | CONS                 |
|----------------------------------------------------------|----------------------|
| more logical separation between the problem's management | more data redundancy |


[PREVIOUS](DATA_LAKES.md) [NEXT](CONCEPTUAL_MODELING.md)
