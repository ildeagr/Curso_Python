#Calculo serie Fibonacci
print("\n***Desarrollo seri de Fibonacci***")
num = input("Introduce el número: ")
numbef=0
numcurrent=1
resultado=""


while numcurrent < int(num):
    resultado= resultado + (f"{numcurrent}\n")
    temp= numcurrent
    numcurrent = numcurrent + numbef
    numbef = temp

print(resultado)