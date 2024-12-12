# Manejo de diccionarios (clave : Valor)

#Las claves deben ser únicas
provincias = dict()

provincias = {
    924: "Badajoz",
    958: "Cadiz",
    959: "Huelva",
    91: "Madrid",
    95: "Sevila",
    922: "Sat. Cruz",
    975: "Soria"

}

print("*** Mostrar el valor de una clave con .get ***")
print("La provincia intrducida es:",provincias.get(91))

print("\n*** Mostrar clave valor con .items ***")
for clave, valor in provincias.items():
    print("Prefijo:", clave, "Provincia:", valor)

print("\n*** Mostrar solamente claves o valores (.keys y .values) ***")
for clave in provincias.keys():
    print("Prefijo:", clave)

for valor in provincias.values():
    print("Provincia:", valor)

print("\n*** Mostrar número con len ***")
print("El número de provincias es:", len(provincias))

# Modificamos el un elemento
mi_diccionario[91] = "Almeria"

print("\n*** Insertar nuevos valores .setdefault ***")
#Si la clave existiera no la inserta
provincias.setdefault(925,"Toledo")
print(provincias.get(925))

print("\n*** Eliminar el elemento indicado con la clave del diccionario con .pop ***")
provincias.pop(91)
print(provincias)

print("\n*** Eliminar todo el diccionario con .clear ***")
provincias.clear()
print(provincias)
