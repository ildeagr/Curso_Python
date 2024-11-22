#Uso de paquetes en python

import cx_Oracle

connection = cx_Oracle.connect("system", "javaoracle", "localhost/XE")
cursor = connection.cursor()
try:
    numEmple = input("NÚMERO DE EMPLEADO:")
    cursor.callproc('tablaemp.borrar', (numEmple,))
    print("DATO ELIMINADO")

except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()