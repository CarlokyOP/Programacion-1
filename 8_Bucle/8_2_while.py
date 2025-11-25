from random import *
numero = randint(0,100)
numeroMio = 10000
while numero!=numeroMio:
    numeroMio = int(input("Ingresar número"))
    if numero == numeroMio:
        print("Ganaste")
    elif numero>numeroMio:
        print("numero es menor" )
    else:
        print("Numero es mayor" )
