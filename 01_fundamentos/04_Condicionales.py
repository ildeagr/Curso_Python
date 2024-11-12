#Sentencias condicionales

"""**** Condicional If ****"""
#El final de la condicion se indica con dos puntos
#Lo que debe ejecutar el "if" o el "else" debe estar tabulado dado que no tenemos llaves
edad = 20
if edad < 18:
    print("Eres menor de edad") #Dentro del if
elif edad > 18:
    print("Eres mayor de edad")
else:
    print("Tienes justo 18") #Dentro del else

print("Enhorabuena") #Fuera del condicional

# *** Comprobación de un número par e impar ***
num1 =int(input("Introduce el número a comprobar: "))

if num1%2 == 0:
    print("El número es par")
else:
    print("El número es impar")
