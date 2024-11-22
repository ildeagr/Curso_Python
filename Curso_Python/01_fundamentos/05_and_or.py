# Uso de and y or

letra =input("Introduce la letra a comprobar: ").lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Es una vocal")
else:
    print("Es una consonante")


print("Comprobación de nombre completo")

nombre =input("Introduce nombre: ").lower()
apellido =input("Introduce apellido: ").lower()

if nombre == "alberto" and apellido == "fernandez":
    print("Su nombre completo es:",nombre,apellido)
else:
    print("Nombre incorreto")

# .lower() convierte a minúsculas
# .upper() convierte a mayúsculas
