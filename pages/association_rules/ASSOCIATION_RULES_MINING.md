---
id: ASSOCIATION RULES MINING
aliases: []
tags: []
index: 2
---

# ASSOCIATION RULES MINING

The goal of this procedure it's, given a list of $N$ item-set, finding association rules that have  $conf$ and $sup$ grater than some thresholds

## BRUTE-FORCE APPROACH

generate all possible combination and compute $conf$ and $sup$, this approach is always possible but is too much computational expensive

## TWO STEP APPROACH

this approach is based on the fact that rules that are generated from the same item-set have the same $sup$

- **[frequent itemset generation](FREQUENT_ITEMSET_GENERATION.md)** -> in the first step all item-set that have $sup \gt threshold$ are generated (**this step is still computational expensive**)
- **RULE GENERATION** -> in the second step rules with high confidence are generated from the previous generated item-sets

[PREVIOUS](ASSOCIATION_RULES.md) [NEXT](RULES_GENERATION.md)
