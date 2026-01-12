email = "dario.mennillo@email.it"

#validazione: deve essere presente il carattere @; deve esserci un dominio (.com, .it, .org); deve essere maggiore di 8 caratteri

if "@" in email:
    if email.endswith((".com", ".it", ".org")):
        if not email.startswith("@"):
            if len(email) >= 8:
                print("Email valida")
            else:
                print("Email troppo corta")
        else:
            print("La mail non può cominciare con una @")
    else:
        print("Dominio non valido")
else:
    print("Manca la @, email non valida")