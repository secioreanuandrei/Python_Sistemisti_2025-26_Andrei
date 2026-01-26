#Scrivi un programma per gestire una lista della spesa
#1.Crea una lista della spesa con almeno 6 prodotti.
#2.Mostra i prodotti della lista uno alla volta.
#3.Cercare se esiste un prodotto nella lista (darea anche la possibilità all'utente di inserire a mano il prodotto tramite input)
#4.Contare quanti sono i prodotti presenti.
#5.Mostrare solo i prodotti con più di 5 lettere.
#6.Creare una nuova lista di prodotti ma in maisucolo.

listaSpesa = ["acqua", "pane", "uova", "sale", "pepe", "peperoni"]

for list in listaSpesa:
    print(list)

lista = "acqua pane uova sale pepe peperoni"    
prodotto = input("Quale prodotto stai cercando ? ")

if prodotto.lower() in lista.lower():
    print("il prodotto", prodotto, "è nella lista")
else:
    print("il prodotto", prodotto, "non è nella lista")

for i in range(len(listaSpesa)):
    print(f" {i+1} {listaSpesa[i]}")

for i in range(len(listaSpesa)):
    if len(listaSpesa[i]) > 4:
        print(listaSpesa[i])
        
        
for i in range(len(listaSpesa)):
    listaSpesa[i] = listaSpesa[i].upper()
    print(listaSpesa[i])      
   


     
        

