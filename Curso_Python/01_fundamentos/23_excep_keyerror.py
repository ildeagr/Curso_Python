# Excepción de clave (Keyerror)

colors = dict()

colores = {
    "Blanco": "White",
    "Negro": "Black",
    "Amarillo": "Yellow",
    "Azul": "Blue",
    "Rojo": "Red"
}


def mostrarTraduccion():

    try:
        color = input("Introduce el color a traducir:")
        print(f"El color {color} es {colores[color]}")
    except KeyError:
        print("Lo siento, el color introducido no se encuentra.")


mostrarTraduccion()