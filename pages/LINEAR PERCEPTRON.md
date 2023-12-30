

Combinazione lineare di input pesati->rete combinatoria che in maniera ricorsiva modifica i pesi dati a ogni parametro dell'iperpiano fino a convergere al quello ottimo o ammissibile![](Pasted%20image%2020231230121407.png)

Quindi dato un dataset con attributi numerici X e Y per classificarli in 2 classi li tracciamo come punti nel piano e cerchiamo di tracciare l'iperpiano che li divide
![](Pasted%20image%2020231230121721.png)

d1,d2....d*d* sono gli attributi w0,w1...wd sono i pesi da calibrare, il primo elemento ha sempre valore input=1, detto Bias serve ad ammettere iperpiano che non passano dall'origine. 
L'iperpiano è descritto da un set di pesi in una equazione lineare sugli attributi x0...xd ![](Pasted%20image%2020231230122322.png)

l'algoritmo di apprendimento:
![](Pasted%20image%2020231230122400.png)

Ogni modifica dei pesi sposta il piano verso individui mal classificati, se l'algoritmo è classificato male e dovrebbe essere positivo aggiungo ai pesi del percettrone il valore dei suoi attributi se è negativo sottraggo.
L'algoritmo termina solo de il dataset  è linearmente Separabile quindi è bene impostare un limite temporale ammettendo errori.