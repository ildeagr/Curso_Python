# Ejemplo para aplicar funciones
import sys

def conjeturaCollaz(num):
    valor = ""
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        valor = valor + (str(int(num)) + "\n")
    return valor

def narcisistaNumero(num):
    resultado = 0
    for i in range(len(num)):
        resultado = resultado + (pow(int(num[i]), len(num)))

    if resultado == int(num):
        return (f"El número {num} es narcisista")
    else:
        return (f"El número {num} no es narcisista")

def letraDNI(num):
    tablaLetra = "TRWAGMYFPDXBNJZSQVHLCKET"
    resto = num % 23
    return tablaLetra[resto]

i=1

while i!=0:
    print("*** SELECCIÓN UNA OPCIÓN ***")
    print("1 -  Comprobar número Narcisista")
    print("2 -  Mostrar Conjetura de Collazt")
    print("3 -  Calcula letra DNI")
    print("4 -  Salir")

    option = int(input("\nEscriba su opción:"))

    if(option > 0  and option < 5):
        if(option == 2):
            num = input("\nEscriba un número:")
            valor = conjeturaCollaz(int(num))
        elif( option == 1):
            num = input("\nEscriba un número:")
            valor = narcisistaNumero(num)
        elif (option == 3):
            num = input("\nEscriba un número de DNI:")
            valor = letraDNI(num)
        else:
            sys.exit()
    else:
        valor = ("\nOpcion no disponible")

    print(valor + "\n")