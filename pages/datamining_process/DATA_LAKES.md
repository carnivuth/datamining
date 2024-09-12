---
id: DATA LAKES
aliases: []
tags: []
index: 3
---


- it's a repository of data stored in raw format
- no schema on write requirements for the input sources to make easy the injection process
- to access data we follow a  schema on read approach for more versatility

## BENEFITS

- higher scalability (no need to scale large computing architectures)
- data are stored only in one place
- support for unstructured data
- support for machine learning workloads

## USE CASES VS TECH SOLUTIONS

| USE CASES                                                   | TECH SOLUTIONS     | FEATURES TRENDS                                                                                                                              |
|-------------------------------------------------------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Mission critical, low latency, insight apps                 | Data Warehouse/Hot | - More expensive HW/SW - Use case-specific data - Less latency - More governance - Higher data quality - Used by end-users and data analysts |
| Agile insight apps                                          | Data Hub/Warm      |                                                                                                                                              |
| Staging area, data mining, searching, profiling, cataloging | Data lake/Cold     | - Less expensive HW/SW - All enterprise data - More latency - Less governance - Lower data quality - Used by data scientists                 |


## INSIGHT DRIVEN DATA SYSTEMS VS TRADITIONAL DATA SYSTEM

| USE CASES                      | TRADITIONAL DATA SYSTEM                                                                      | INSIGHT DRIVEN DATA SYSTEM                                                                                                                                                                               |
|--------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DATA SOURCES                   | Structured, relational data from transaction systems, relational and operational data stores | Traditional sources + semi and unstructured sources: logs, web sites, social media, alternative data providers                                                                                           |
| Data Movement (Ingestion)      | limited Amount of data that can be moved                                                     | Unlimited volume of data that can be moved inside the system                                                                                                                                             |
| Storage                        | Limited volume of data                                                                       | Virtually unlimited volume of data                                                                                                                                                                       |
| Data Structure                 | schema is designed upfront before data are inserted into the system                          | no schema is defined for data, data can be stored in various formats                                                                                                                                     |
| Data Trasformation             | data need to be formatted cleaned and adjusted to fit into the model schema                  | data transformation are added to match data analysis requirements                                                                                                                                        |
| Analytics                      | sql queries BI tools full text                                                               | + self-service BI, big data analytics, realtime analytics, machine learning, data exploration/visualization. Allow users to securely explore and query raw data. Easily introduce new types of analytics |
| Price/Performance              | Highest cost storage/fastest query results                                                   | low-cost storage + performance scale/speed/cost tradeoffs                                                                                                                                                |
| Users                          | Business                                                                                     | data scientist data analysis                                                                                                                                                                             |
| Data Quality                   | High                                                                                         | use case dependent must be clear from design                                                                                                                                                             |
| Data sharing and collaboration | Very limited                                                                                 | Rich. Raw and transformed data sets, analytical models, dashboards can be easily and securely shared                                                                                                     |


- this new systems are cheaper to design, can handle multiple data inputs, enabling users to perform powerful operations in a large amount of data of various forms

## DATA LAKES STRUCTURES

![](Pasted_image_20231017155132.png)


## DATA LAKE ARCHITECTURES

### lambda lake

- designed for multiple workloads
- data are inserted in 2 pipelines one for time consuming operation (cold path) and one real-time workflows where data need to be sent to the clients faster

![](Pasted_image_20231017165627.png)

### kappa lake

-  simplified version of lambda lake, it removes the cold path stage and replace it with a long term data storage

![](Pasted_image_20231017165903.png)

### delta lake

advanced features like:

- ACID properties (it is able to deal with consistency requirements).
- Scalable metadata handling.
- Data versioning (also called time travel, it allows the analysis of different snapshots).
- Unified batch and streaming source and sink.
- Schema enforcement and evolution.
- DBMS-like operations: updates, deletes, inserts, upserts (insert, on conflict update).

[PREVIOUS](OLAP.md) [NEXT](DATA_WAREHOUSE_ARCHITECTURES.md)
