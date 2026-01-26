#Il ciclo for serve a ripetere un'istruzione o un blocco di istruzioni un numero definito di volte

# i sta per indice
for i in range(5):
    print("Ciao",i)

for i in range(0,46, 4):
    print(i)

#Stampa tutti i numeri da 1 a 100. Quando stampi un multiplo di 3 stampa Zoom, quando stampa un multipli di 5 stampa Boom, quando stampi un multiplo di 3 e di 5 stampa Bangherang


print("========  Giochino ZOOM BOOM Bangherang =========")

quantZOOM = 0
quantBOOM = 0
quantBANGHERANG = 0

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0: 
        print(i, "bangherang")
        quantBANGHERANG += 1
    elif i % 3 == 0:
        print(i, "zoom")
        quantZOOM += 1 
    elif i % 5 == 0:
        print(i, "BOOM")
        quantBOOM += 1
    else:
        print(i)

               
print ( f"Il numero totale di ZOOM è {quantZOOM} multipli di 3 "  )
print ( f"Il numero totale di BOOM è {quantBOOM} multipli di 5 "  ) 
print ( f"Il numero totale di BANGHERANG è {quantBANGHERANG} multipli di 15 "  )


