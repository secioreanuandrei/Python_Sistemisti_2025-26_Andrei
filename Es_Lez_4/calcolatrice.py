def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b == 0:
        return "Errore: divisione per zero"
    return a / b


def menu():
    print("\nCALCOLATRICE BASE")
    print("1 - Somma")
    print("2 - Sottrazione")
    print("3 - Moltiplicazione")
    print("4 - Divisione")
    print("0 - Esci")


while True:
    menu()
    scelta = input("Scegli un'operazione: ")

    if scelta == "0":
        print("Uscita dal programma")
        break

    if scelta in ["1", "2", "3", "4"]:
        num1 = float(input("Inserisci il primo numero: "))
        num2 = float(input("Inserisci il secondo numero: "))

        if scelta == "1":
            print("Risultato:", somma(num1, num2))
        elif scelta == "2":
            print("Risultato:", sottrazione(num1, num2))
        elif scelta == "3":
            print("Risultato:", moltiplicazione(num1, num2))
        elif scelta == "4":
            print("Risultato:", divisione(num1, num2))
    else:
        print("Scelta non valida")
1