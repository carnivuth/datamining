

Genera una probabilità per ogni possibile classe (simile al classificatore Crisp).
Possiamo settare un Threashold di probabilità oltre il quale si restituisce il valore Binario.

- Lift Chart: individui un campione di N individui ed effettui il test e ripeti usando un classificatore casuale. Disegnando il grafico maggiore è l'area tra le due curve migliore è la classificazione.
	![](Pasted%20image%2020231230150751.png)
- ROC Curve : simula il tradeoff tra Veri Positivi e Falsi Positivi in una trasmissione con canale affetto da rumore. 
	![](Pasted%20image%2020231230150901.png)Calcola e traccia il grafico ponendo nell'asse X la Pr dei falsi positivi (specificity) e nell'asse delle Y la Pr dei veri positivi (sensitività) al variare della soglia di threshold, maggiore è la distanza tra le due curve migliore è il classificatore->migliore il threshold usato.
	![](Pasted%20image%2020231230151003.png)![](Pasted%20image%2020231230151021.png)
	