#Procedimiento con retorno de varias variables
import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:
    nss = input("Indique el número de seguridad social:")
    npat = cursor.var(cx_Oracle.STRING) #Indicamos que es un dato de retorno con .var y ademas el tipo de dato
    sxpat = cursor.var(cx_Oracle.STRING)

    cursor.callproc('RETURNPATIENT', (npat, sxpat, nss))
    print(f"Nombre completo: {npat.getvalue()} \nSexo: {sxpat.getvalue()}")

except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()