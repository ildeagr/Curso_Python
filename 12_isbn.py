#Comprobacion de ISBN
import sys

print("\n***Comprobacion de ISBN***")
num = input("Introduce el número ISBN: ")

#Aquí comprobamos que la longitud sea de 10 con la funcion len()
if len(num)!=10:
    print("ISBN debe ser de 10 dígitos")
    sys.exit()

resultado=0
for i in range(1,11):
    resultado = resultado+(int(num[i-1])*i)

if resultado%11==0:
    print("ISBN es correcto")
else:
    print("ISBN es incorrecto")