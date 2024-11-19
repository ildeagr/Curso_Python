#Uso de procedimientos almacenados desde Python

import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
cursor = connection.cursor()

try:
    dp = input("Inserte número de empleado a borrar:")

    cursor.callproc("DELETEEMP", (dp,))

    print("Registros borrados satisfactoriamente", cursor.rowcount)


except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()