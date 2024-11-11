# Manejo de Listas

print("*** Creacion de Listas ***")

edades = [20,45,85,44,12,36]
print(edades[5])

nombres = ["Marcos", "Juan", "Marian", "Alvaro", "Miguel", "Ana"]
print(nombres[3])

print("\n*** Añadir elementos ***")
print(nombres)
nombres.append("Alberto")
print(nombres) #Muestra la lista completa

print("\n*** Insertar un elemento nuevo en la posicion deseada ***")
nombres.insert(3, "Teresa")
print(nombres)

print("\n*** Conocer la longitud de la lista ***")
print(f"El número de elementos es: {len(nombres)}")

print("\n*** Ver si un elemento existe ***")
print("Juan" in nombres)
if("Juan" in nombres):
    print("Juan está en la lista")
else:
    print("Juan no está en la lista")

print("\n*** Ordenacion de las listas ***")
nombres.sort() #Ordena de menor a mayor
print(nombres)
nombres.sort(reverse=True)
print(nombres)

print("\n*** Eliminar elementos de la lista por el argumento***")
nombres.remove("Miguel")
print(nombres)

print("\n*** Eliminar un elemento por su indice ***")
del nombres[1] #Elimina el elemento indicado
print(nombres)
del nombres[2:3] #Elimina ese rango indicado
print(nombres)
del nombres[1:] #Elimina todos los elementos empezando desde el indicado
print(nombres)
del nombres[:] #Elimina la lista completa
print(nombres)

