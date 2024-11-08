# Bucle for
#Automaticamente "i" inicia en 0 e incrementa hasta el número del rango menos 1
for i in range(10):
    print(f"El valor de i es: {i}")

#Para iniciar en otro valor debemos indicarlo dentro del parentersis de range
for i in range(1,11):
    print(f"El valor de i es: {i}")

#El tercer valor si se indica, es el valor del incremento
for i in range(1,11,2):
    print(f"El valor de i es: {i}")

#Ejemplo con tabla de multiplicar

print("\n***Tabla de multiplicar***")
num = int(input("Introduce un número: "))
resultado = ""
for i in range(1,11):
    resultado =resultado+(f"5 * {i} = {num*i}\n")

print(resultado)