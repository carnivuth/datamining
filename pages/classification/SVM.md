---
id: SVM
aliases: []
tags: []
index: 9
---

# SUPPORT VECTOR MACHINE (SVM)

Studiate per superare il problema dei dataset linearmente separabili-> cerca un'ipersuperficie che divida gli individui del dataset ma la superficie è più complessa di un iperpiano.
- prima idea: far cadere il requisito di linearità della supericie, ma si ottiene una classificazione molto dipendente dai dati del dataset con molto overfitting. Ma si può ottenere una soluzione valida mappando i punti da un dominio non llinearmente separabile a uno linearmente separabile con un numero di dimensioni maggiori del dominio originale: ![](Pasted_image_20231230124031.png) ![](Pasted_image_20231230130632.png)
- altrimenti: si mantiene il requisito di linearità e si adotta il Maximum Margin Hyperplane si pensa di non adottare un singolo piano, ma piani multipli dove ogni singolo piano cerca di massimizzare il margine tra i gruppi di individui. Il margine (distanza tra piano e gruppo di individui) si valua considerando il convex hull (l’inviluppo convesso più grande che riesce a contenere tutti i punti del sottoinsieme).
	![](Pasted_image_20231230124428.png)

- Oppure ancora si possono usare le Reti Neurali: composte da numerosi percettori collocati in gerarchia.



[PREVIOUS](LINEAR_PERCEPTRON.md) [NEXT](RETI_NEURALI.md)
