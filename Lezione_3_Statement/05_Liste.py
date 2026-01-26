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

for i in range(len(colori)):
    print(f"posizione {i+1} - colore {colori[i]}")

   
          
