# Control de errores y excepciones
import sys


def controlErrores():
    try:
        numero =int(input("Introduce un número:"))
        print("Número:", numero)
    except ValueError:
        print("Error, introduce un número")

#controlErrores()


def controlErroresDivision():
    try:
        dividendo = int(input("Introduce dividendo:"))
        divisor = int(input("Introduce divisor:"))
        resultado = dividendo/divisor
        print("El resultado es:", resultado)
    except ValueError:
        print("Error, introduce un número")
        controlErroresDivision()
    except ZeroDivisionError:
        print("Imposible dividir por cero")
        controlErroresDivision()
    except: #Esta es para controlar cualquier tipo de error pero consume más recursos que las expecíficas porque contiene todas.
        print("Error:", sys.exc_info()) #Aqui con sys.exc_info() muestra el error producido
    finally: #Esta parte la ejecuta siempre se produzcan o no excepciones
        print("Entra Siempre")

controlErroresDivision()