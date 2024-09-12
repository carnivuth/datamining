---
id: CRISP DM METHODOLOGY
aliases: []
tags: []
index: 6
---


model for datamining process standardization, the goal is to set common names and steps to organized workloads inside the team

## PHASES

### business understending

- determining business goal, and the reasons behind them
- determined the key performance indicators (KPI)
- understand available resources, constraints, costs and risks
- create a project plan

### data understending

- what data are available
- what data sources are available
- what is the cost of raw data

in this steps we are interested in understand what data are available for the project describe them and verifying the quality

### data preparation

this is the most important phase and the most time consuming one, in this fase we want to avoid possible data leaks that can break our datamining model

in this phase data are manipulated to improve quality as follows:

- Data set description.
- Data set selection, explaining the rationale for including or excluding them.
- Data cleaning, generating a report on this step.
- Data construction, reporting which attributes have been derived or generated.
- Data integration, reporting what data has been merged.
- Data formatting, reporting what data has been reformatted.

every step of this phase should be modeled to be reproducible

### data modeling

in this phase we apply machine learning techniques to bring to light patterns hided into the data as follows

- **Modeling technique selection**: explicitly stating the modeling technique that we
chose and its related assumptions (the limits, hypothesis on the data, etc.).
- **Generating the test design**.
- **Building the model,** setting the various parameters, doing the actual modeling,
commenting and reporting on the models and the tools used.
- **Assessing the model**, performing the tests and checking for its validity, possibly
revising the parameter settings.

### evaluation step

in this step we assets the results of the data mining process, we want to evaluate the accuracy of the derived model and the impact in the decision making process as follows:

- Result evaluation, assessing the data mining results with relation to the KPIs and
typically approving the best performing model
- Process review
- Determining the list of possible future actions and decisions

### deployment

in this phase the results of the process are put into production to gain profit from the  investments as follows:

- Creating a deployment plan.
- Planning monitoring and maintenance.
- Producing a final report on the project.
- Reviewing the project and creating documentation on the experience gained.




[PREVIOUS](CONCEPTUAL_MODELING.md)
