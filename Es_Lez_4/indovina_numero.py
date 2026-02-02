import random


def easy_mode():
    numero_segreto = random.randint(1, 50)
    tentativi = 0

    print("\nEASY MODE (1 - 50) | Tentativi illimitati")

    while True:
        tentativi += 1
        scelta = int(input("Inserisci un numero: "))

        if scelta < numero_segreto:
            print("Troppo basso")
        elif scelta > numero_segreto:
            print("Troppo alto")
        else:
            print(f"Hai indovinato in {tentativi} tentativi!")
            break


def hard_mode():
    numero_segreto = random.randint(1, 100)
    tentativi_max = 10
    tentativi = 0

    print("\nHARD MODE (1 - 100) | 10 tentativi max")

    while tentativi < tentativi_max:
        tentativi += 1
        scelta = int(input(f"Tentativo {tentativi}/{tentativi_max}: "))

        if scelta < numero_segreto:
            print("Troppo basso")
        elif scelta > numero_segreto:
            print("Troppo alto")
        else:
            print(f"Hai indovinato in {tentativi} tentativi!")
            return

    print("Tentativi esauriti! Il numero era:", numero_segreto)


def menu():
    print("\nINDOVINA IL NUMERO")
    print("1 - Easy Mode (1 - 50)")
    print("2 - Hard Mode (1 - 100)")
    print("0 - Esci")


while True:
    menu()
    scelta = input("Scegli la modalità: ")

    if scelta == "0":
        print("Uscita dal gioco")
        break

    elif scelta == "1":
        easy_mode()

    elif scelta == "2":
        hard_mode()

    else:
        print("Scelta non valida")
1