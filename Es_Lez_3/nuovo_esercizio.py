#Scrivi un programma per gestire una lista della spesa (inserisci in partenza almeno 6 prodotti). Tutto questo fallo in un menu dal quale l'utente seleziona i comandi

lista_spesa = ["pane","latte","uova","pasta","riso","olio"]


print("=== LISTA DELLA SPESA ===")

scelta = ""


while scelta != 4:
    scelta = input("Seleziona un'opzione (1-4): ")

    if scelta == "1":
        print("\nLista della spesa:")
        for i, prodotto in enumerate(lista_spesa, start=1):
            print(f"{i}. {prodotto}")

    elif scelta == "2":
        nuovo_prodotto = input("Inserisci il nome del prodotto da aggiungere: ")
        lista_spesa.append(nuovo_prodotto)
        print(f"{nuovo_prodotto} aggiunto alla lista.")

    elif scelta == "3":
        prodotto = input("Inserisci il nome del prodotto da rimuovere: ")
        if prodotto in lista_spesa:
            lista_spesa.remove(prodotto)
            print(f"{prodotto} rimosso dalla lista.")
        else:
            print("Prodotto non trovato.")

    elif scelta == "4":
        print("Uscita dal programma. Arrivederci!")
        break

    else:
        print("Scelta non valida. Riprova.")