#Uso de potencia con pow
print("\n***Comprobacion número narcisista***")
num = input("Introduce el número: ")
resultado = 0

for i in range(len(num)):
    resultado = resultado + (pow(int(num[i]),len(num)))

if resultado==int(num):
    print(f"El número {num} es narcisista")
else:
    print(f"El número {num} no es narcisista")