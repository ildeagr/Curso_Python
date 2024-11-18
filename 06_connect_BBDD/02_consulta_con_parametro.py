#Consultas incluyendo parámetros

import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:
    miOficio = input("Introduce Oficio Empleado:")
    #Si ponemos UPPER o LOWER tanto en oficio como en el parámetro p1, el resultado es el mismo donde igual mayuscula que minuscula
    consulta = ("SELECT apellido,oficio,salario FROM emp where UPPER(oficio)=UPPER(:p1)")
    cursor.execute(consulta, (miOficio,))
     # Si en un único parámetro tenemos que poner ',' a continuación del valor de la variable

    for ape, ofi, sal in cursor:
        print("Apellido: ", ape)
        print("Oficio: ", ofi)
        print("Salario: ", str(sal))

except connection.Error as error:
    print("Error: ", error)

connection.close()