# WordChecker
Versione python del progetto da fare in C, da utilizzare come modello.

**Feature non implementate:**
- `stampa_filtrate`
- stampare in output il numero di parole ammissibili ancora compatibili con i vincoli appresi 

## Conversione di tipi
- `Dict[str, int]` -> array di interi di 77 elementi inizializzato a 0, 
   funzione per determinare l'indice in cui aggiungere 1: `int(letter) - 45`
- `Dict[int, Dict[str, int]]` -> Lista di dizionari come sopra definiti