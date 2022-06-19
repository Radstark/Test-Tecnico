# Test Tecnico

Per avviare il test è sufficiente avviare il file main.py con il comando seguente:

```
<python/python3> main.py
```

La versione di Python usata è la 3.10. I package necessari sono indicati nel file requirements.txt.

## Configurazione

Il file config.py funge da file di configurazione, con tutte le costanti necessarie. È diviso per regioni. Contiene anche i parametri relativi al server, che si trovano in fondo al file: nome del database e della collection, la tripletta host, username e password, e la stringa di connessione.

## Database

Il file database.py contiene la funzione di creazione della variabile relativa al database e le classi per la ricezione dei dati.

## Test

Il file test.py contiene le REST API che ho usato per testare il codice. La funzione post randomizza l'input secondo le direttive date.

## Main

Il file main.py contiene le funzioni ingest e retrieve, chiamare rispettivamente via post e get.

### Ingestion

La funzione di ingestion randomizza innanzitutto il codice di errore e il tempo di risposta; una volta ottenuto quest'ultimo si ferma per un tempo uguale al tempo di risposta da rispettare meno il tempo già impiegato per le operazioni precedentemente dette.

Dopo di che inserisce i dati ottenuti nella collezione di MongoDB. Oltre ai dati menzionati nelle direttive inserisce anche la data di inizio arrotondata e un intero che definisce se c'è stato un errore che funziona alla stregua di un booleano (1 per un errore, 0 altrimenti). Lo scopo di queste due variabili è velocizzare l'operazione di retrieval.

### Retrieval

La funzione di retrieval converte le date fornite da stringa a datetime, poi effettua un'aggregazione per ottenere le informazioni necessarie. Qui entrano in gioco la data arrotondata (utilizzata per non dover effettuare conversioni successivamente sulla lista ottenuta, che risulterebbero più lente) e lo "pseudo-booleano" (usato per ottenere il totale di errori tramite sum).

A questo punto viene creata una lista che viene riempita con dizionari contenenti i dati recuperati sopra e poi ordinata in modo da rendere il formato di output identico a quello di esempio. (Non sono sicuro se quest'ultimo passaggio fosse necessario.) Questa lista costituisce il valore di ritorno insieme al codice della risposta.
