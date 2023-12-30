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
