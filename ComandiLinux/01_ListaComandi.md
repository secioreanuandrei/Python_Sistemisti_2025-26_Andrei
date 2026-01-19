# Lista Comandi Github

## cd - Change Directory
Da utilizzare con percorsi assoluti o relativi
- `~` rappresenta la mia home directory
- `/` root directory
Tutte le volte che uso questi due simboli sto navigando con un percorso assoluto.

Spiegazione dei simboli o opzioni per i comandi:
- `.` directory corrente
- `..` directory genitore
- `~` home directory 
- `/` root directory
- `-` directory precedente

### Tipi di File 
Quando lancio il comando `ls -l` ottengo vari risultati
- drwxrwxrwx 1 root ....

Primo Carattere
- `d` = directory
- `-` = file generici
- `l` = link, puntano ad un altro file
- `s` = socket 
- `p` = pipe
- `b` = block file
- `c` = character file

Permessi `rwxrwxrwx`. Si dividono in 3 parti da 3 caratteri
- i primi 3 per lo user
- i secondi 3 per il gruppo
- i terzi per gli special 

Nomenclature
- `r` readable
- `w` writable
- `x` executable

Quando incontro un `-` vuol dire che quel particolare permesso non è disponibile per quella categoria.

Esempio: `rwxrw-r--` --> l'utente può fare tutto, il gruppo solo leggere/scrivere e non eseguire, gli special solo leggere


## Comando Copia `cp`

```linux
cp source destinazione
```

ATT: anche cp può essere un comando distruttivo poiché posso mandarlo in sovrascrittura

Per chiedere la sovrascrittura lanciare `cp -i src dest`
Per evitarla completamente lanciare `cp -n src dest`

Copiare una cartella
`cp -r srcFolder destFolder`


## Comando Rimuovi `rm`
```linux
rm source
```
ATT: il comando rm è un comando distruttivo, attento ad utilizzarlo

Come rimuovere una cartella
```linux
rm -r srcFolder
```


## Comando Sposta, Muovi `mv`
`mv src dest`
Può essere utilizzato anche per rinominare un file `mv src dest/nuovoNome`.
Anche in questo caso `-i` ,  `-v` , `-n` funzionano
Il `-r` non serve col il move per spostare una cartella

Esempio:
```linux
mv ./Downloads/Videos/ ./
```
## Creare un file `touch dest/nomeFile`
## Creare una cartella `mkdir dest/nomeDir`


# Lettura file di testo 
- `less nomefile.txt`
- `more nomefile.txt`
- `head` per leggere la parte iniziale di un testo
- `tail` per leggere la parte finale di un testo

Per poter scorrere facilmente il testo utilizza:
- `spazio` per scendere giù di una pagina
- `B` per salire
- `Enter` scende giù di 1 riga
- `q` chiude, quit


# Scrittura file di testo
- opzione 1: utilizzo degli stdInput stdOutput stdError
```linux
ls ./ > mioFile.txt (scrive tutto l'output che va a buon fine)
ls ./prova 2> mioFile.txt (scrive solo l'output di errore)
ls ./ &> mioFile.txt (scrive tutto)
cat > mioFile.txt (scrive tutto ciò che io digito come input: ctrl+c per terminare)
``` 

