#Verificacion de código EAN

from codigo_ean import Ean

num = input("Introduzca el código EAN (8 0 13 caracteres:")
print(num)


if(len(num)==8 or len(num)==13):
    numean = Ean(num)
    numean.validarcodigo()
    print(numean.__str__())

else:
    print("Longitud del código incorrecta. Debe ser de 8 o 13")
