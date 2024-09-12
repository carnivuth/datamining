---
id: RULES GENERATION
aliases: []
tags: []
index: 3
---

# RULES GENERATION

The goal of this phase is, given an item-set $L$ to find all non empty $f$ subsets that the association rule $f \rightarrow (L-f)$ have a $conf \gt threshold$ where $threshold$ is a parameter defined from the designer

It'important to understand how to generate rules with an high $conf$ from a given item-set

so from [this formula](ASSOCIATION_RULES.md#CONFIDENCE_FROM_SUPPORT) we can say that for rules generated from the same item-sets:

$$
conf(ABC \rightarrow D) \geq conf(AB \rightarrow CD) \geq conf(A \rightarrow BCD)
$$

this means that rules confidence is anti-monotone in relation of the number of elements that creates the antecedent

this characteristic can be used to prune the generation tree when there is a rule with a $conf \lt threshold$

## INTERESTING RULE GENERATION METRICS

Confidence metrics can be insufficient in the rule generation process, other interesting metrics are also used

so given a rule in the form of $A \rightarrow C$ we can compute the **contingency table** as follow

|     | C        | $\overline{C}$       |          |
| --- | -------- | -------- | -------- |
| A   | $f_{11}$ | $f_{10}$ | $f_{1+}$ |
| $\overline{A}$  | $f_{01}$ | $f_{00}$ | $f_{0+}$ |
|     | $f_{+1}$         | $f_{+0}$         |          |

from this table we can derive some interesting measures like

### LIFT

lift is defined as

$$
lift(A \rightarrow C) = \frac{conf(A \rightarrow C)}{sup(C)}
$$

it indicates the ratio between rule true cases and independence, it tend to $1$  when the item-sets are independent

### LEVERAGE

leverage is defined as

$$
leve(A \rightarrow C) = sup(A \cup C) - sup(A)sup(C)
$$

leverage indicates the number of additional cases, it tends to $0$ when the item-sets are independent

### CONVICTION

conviction is defined as

$$
conv(A \rightarrow C) = \frac{1 - sup(C)}{1 - conf(A \rightarrow C)}
$$

it's the ratio that $A$ occurs without $C$  if $A$ and $C$ where independent, higher value means that the rules is violated less often (in the assumption that the $A$ and $C$ are independent)

[PREVIOUS](ASSOCIATION_RULES_MINING.md) [NEXT](FREQUENT_ITEMSET_GENERATION.md)
