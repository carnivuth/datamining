---
id: RETI NEURALI
aliases: []
tags: []
index: 10
---



Possiamo identificare un neurone come una rete combinatoria a soglia, restituisce 1 o 0 se supera o meno la soglia.
	 I valori in input, inseriti tramite le sinapsi, sono numeri reali pesati;
	 Allo stesso modo sono pesati i dendriti, cioè le connessioni tra neuroni interne alla rete;
	 La soglia è data da una funzione matematica, solitamente un Sigmoide (squashing function)![](Pasted_image_20231230124921.png) è continua, differenziabile e non lineare(così da creare una rete robusta in presenza di rumore).
La forma della funzione influenza il processo di apprendimento che consiste nel calibrare i pesi di sinapsi e dendriti basandosi sui dati del training set.
![](Pasted_image_20231230145255.png)
Nella Feed-Forward multi-layered Network troviamo di base 3 layer:
- Input Layer (nutrito dagli Input tramite le sinapsi)
- Hidden Layer (nutrito dall'input layer tramite dentriti)
- Output Layer (nutrito dall'hidden layer)

![](Pasted_image_20231230145402.png)
g= sigmoidi (funzioni di trasferimento)
Gli archi sono orientati (rete feed-forward)
l'algoritmo di training:
![](Pasted_image_20231230145700.png)

nella rete vengono immessi tutti gli elementi del dataset e durante il processo i pesi vengono calibrati sulla base delle classi dai supervisori, ma la convergenza non è garantita.

##### Calcolo dell'errore
L'errore si calcola:
![](Pasted_image_20231230150120.png)
la modifica in retroazione fatta vuole minimizzare l'errore E(w) seguendo il gradiente della funzione che si calcola dalle derivate parziali del sigmoide: ![](Pasted_image_20231230150356.png)

![](Pasted_image_20231230150251.png)

Sottrai la derivata per il parametro costante detto Learning Rate
![](Pasted_image_20231230150551.png)


[PREVIOUS](SVM.md)
