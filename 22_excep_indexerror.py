# Excepción de índice (IndexError)
premios = [166116.06,133948.48,32353.38,1528.22,123.12,66.37,44.89,15.91]

def comprobarPremio():
    try:
        num = int(input("Introduce el número del premio a mostrar:"))
        print(f"Premio obtenido:"
              f"{premios[num]}")
    except IndexError:
        print("Erro: El índice del premio no se encuentra en la lista")
        comprobarPremio()

comprobarPremio()