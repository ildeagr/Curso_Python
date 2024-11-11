#Calculo de la conjetura de Collatz
print("***Calculo conjetura de Collatz***")
num = int(input("Introduce un número: "))
valor =""

while num != 1:
    if num%2==0:
        num=num/2
    else:
        num=num*3+1
    valor=valor+(str(int(num))+"\n")

print(valor)
