

- Stocastico: una propagazione forward è semre seguita da un aggiornamento dei pesi (ciò introduce rumore nella minimizzazione del gradiente). Valido per learning online.
- Batch : fatte alcune propagazioni forward si aggiornano i pesi, accumula il possibile errore sui pesi (di solito porta in maniera più rapida a una condizione di discesa costante del gradiente perché l’aggiornamento si basa sull’errore medio)