---
id: NAIVE BAYES CLASSIFIER
aliases: []
tags: []
index: 7
---



Basato (su metodi statistici) particolarmente sul teorema di Bayes.
![](Pasted_image_20231230105024.png)

con il training valuti Pr(H) creando il modello di classificazione mentre a runtime vedi Pr(E|H)

una prima versione considera tutti gli attributi assumendo siano indipendenti gli uni dagli altri ->poco applicabile ma di facile comprensione.
Un altro problema è che se un valore v di un attributo d non abbare negli elementi della classe C allora P(d=v|c)=0 la probabilità della classe conoscendo l'attrabuto crolla a zero

modi per evitare il problema:
1. Laplace smoothing
![](Pasted_image_20231230105901.png)
con alfa=0 otteniamo la formula standard non smussata, più è alto alfa maggiore importanza si da ai valori nel dataset .

Nel caso di valori mancanti non è necessario cancellare le istanze:
	-Se è un valore del Training set ometto il valore dell'attributo (ottengo una Pr maggiore che si compenserà con la normalizzazione).
	-Se è un valore del Test set lo trascuro.

2. Nel caso di valori numerici non si può usare il metodo basato sulle frequenze.
	Assumiamo che i valori si trovino su una distribuzione Gaussiana, descriviamo la distribuzione del valore degli attributi sulla base del valor medio e della varianza degli attributi all'interno di ogni classe.
	La distribuzione di valore per un atributo di una classe è :

	![](Pasted_image_20231230111308.png)

Quindi si imposta una soglia per un valore di interesse (ad esempio impostare di poter giocare a tennis se la Temperatura è superiore ai 20 gradi) e si calcola quella che viene detta Densità di Probabilità:
![](Pasted_image_20231230111910.png)

Che rappresenta la Pr(E|H) del teorema di Bayes.
Probabilità e Densità si differenziano :
	- Su domini continui la probabilità che una variabile assuma esattamente un valore è 0
	- La densità si può assumere come la probabilità che la variabile assuma un valore nell'intorno della soglia (diverso da 0)
	- Se un valore è mancante la deviazione standard è basata solo sui valori presenti

[PREVIOUS](REGRESSION.md) [NEXT](LINEAR_PERCEPTRON.md)
