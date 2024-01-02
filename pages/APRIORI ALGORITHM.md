### APRIORI PRINCIPLE
If an itemset is frequent, then all of its subsets must also be frequent and viceversa.
We can see this principle as follows: 


![](Pasted%20image%2020231230172030.png)

"The itemset support is less equal then its subsets support."

### HOW THE ALGORITHM WORKS

1) It scans the data and generates every itemset X with |X|=1;
2) calculates the *$sup_i$ for each X and drops those itemsets with $sup_i < minSup$  (***pruning***);
3) generates the itemsets with greater cardinality, according to the remaining items (***self-join***);
4) repeats the steps untill it can't generate more itemsets.

### COMPLEXITY
The Apriori Algorithm complexity is influenced by:
- **$minsup$ value** --> The less is this value the greater is the number of frequent itemsets, with the reduction of the pruning effectiveness.
- **size of the inventory**, that is reflected in the need for space to store the counting of each item and increasing the number of frequent items.
- **database dimension** --> number of transations.
- **average size of a transaction**, which results in an increase of the average length of frequent itemset and therefore in the number of frequent subsets

Even if we filter the dataset according to the value of $sup$, the frequent itemsets number can still be high. --> we need to identify a small number of frequent and representatives itemsets:
- **MAXIMAL FREQUENT ITEMSET** --> the smallest itemsets set from which it's possible to derive the entire frequent itemsets. A MFI doesn't have an immediate frequent itemset and it's located near the border between frequent itemsets and non frequent itemsets. There are some algorithms that allow us to find MFIs without counting the relative subsets.
- **CLOSED ITEMSETS** --> the minimum representation of the itemset without losing information about the value of $sup$. An itemset is **closed** if none of its over-sets have the same support value.

# IMPORTANT
**MFIs are subsets of Closed Frequent Itemsets.  CFIs are subsets of frequent itemsets.**