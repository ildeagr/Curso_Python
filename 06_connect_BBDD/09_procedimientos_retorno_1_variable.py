#Procedimiento con retorno de variables
import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:
    dp = input("Número de departamento:")
    loc = cursor.var(cx_Oracle.STRING) #Indicamos que es un dato de retorno con .var y ademas el tipo de dato

    cursor.callproc('RETURNLOC', (loc, dp))
    print(loc.getvalue())

except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()