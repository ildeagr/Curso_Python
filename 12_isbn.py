#Comprobacion de ISBN
print("\n***Comprobacion de ISBN***")
num = input("Introduce el número ISBN: ")
resultado=0
for i in range(1,11):
    resultado = resultado+(int(num[i-1])*i)

if resultado%11==0:
    print("ISBN es correcto")
else:
    print("ISBN es incorrecto")