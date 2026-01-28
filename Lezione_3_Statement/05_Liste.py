#Le liste ( anche chiamate array ) sono dei contenitori di elemnti simili tra loro, cioè elemnti dello stesso tipo.
#Queste liste sono 0-based, cioè la conta parte da 0.
#Sono indicizzati e l'indice iniziale è 0.

mia_lista = []

numeri = [4,2,8,3,6,1]

parole = ["ciao" , "dario" , "arrivederci" , "oggi"]
#               0           1       2       3           4
studenti = ["Cristina", "Marco", "Ioas", "Franco", "Andrei"]

#lista mista : non ha molto senso logico pur essendo fattibile
mista = [2,"Parola", True, "Ciao", 23, "23"]


#L'indice mi serve per poter richiamare il valore dell'array (lista) in quell'esatta posizione
print(studenti[0])

#Proprietà len : mi dice quanti sono gli elementi in una lista

numStud = len(studenti)
print(f"in classe ci sono {numStud} studenti")


primoStud = studenti[0]
ultimoStud = studenti[len(studenti) -1]

print(f"L'ultimo studente dell'elenco è {ultimoStud} ma non per importanza")
print("L'ultimo studente nella lista è ",ultimoStud, "ma non per importanza")

#Per poter stampare tutti gli elementi uno alla volta
#''stud'' è una variabile creata al momento nel costrutto
for stud in studenti:
    print(stud)
    


#Scorrere con un indice
colori = ["rosso", "giallo", "blu", "nero", "bianco"]



#Modificare un elemento della lista
#Trasformare in VIOLA il colore BLU
colori[2] = "viola"

#aggiungo un colore alla lista(al fondo)
colori.append("arancione")

#aggiungo un elemento in una posizione
colori.insert(2, "blu")

colori.insert(0, "azzurro")

#rimuovo un colore 

colori.pop() #senza numeri rimuove sempre l'ultimo elemento
colori.pop(1)#rimuove il colore nella posizione che li stiamo inserendo
colori.remove("giallo")#rimuove il valore nella stringa

#metodi vari
colori.reverse()#inverte la lista 
colori.sort()#mette in ordine alfabetico crescente



for i in range(len(colori)):
    print(f"posizione {i+1} - colore {colori[i]}")


#altri metodi con liste di numeri
numeri = [4,5,8,2,43,21,1]

print(max(numeri))
print(min(numeri))  
print(len(numeri))
print(sum(numeri))

totale = 0
i = 0

for num in numeri:
    i += 1
    totale += num
    print("parziale:", i, " =", totale)

print(totale)

          
