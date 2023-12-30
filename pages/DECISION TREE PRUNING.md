# DECISION TREE PRUNING

In order to avoid over fitting  pruning can be done

## C4.5 STRATEGY

based on the error, it prunes the leaves if the maximum error of the root of a subtree is lower than the weighted sum of the errors of the leaves

$$eroot <= ei$$

where:

$$
ei = \sum_{leaf}{e}
$$
## BEFORE PRUNING 

![](Pasted%20image%2020231230175754.png)

## AFTER PRUNING

![](Pasted%20image%2020231230175803.png)

