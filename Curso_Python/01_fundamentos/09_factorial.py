# Calculo factorial
from math import factorial

print("***Calculo del número factorial***")
num = int(input("Introduce un número: "))
numfac= 1
i=num

while i > 0:
    numfac = numfac*i
    i -=1

print(f"El factorial de {num} es: {numfac}")
