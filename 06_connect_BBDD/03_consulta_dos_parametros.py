#Consultas incluyendo dos parámetros

import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:
    valor1 = input("Introduce valor salario inferior:")
    valor2 = input("Introduce valor salario superior:")
    #consulta = ("SELECT apellido,oficio,salario FROM emp where UPPER(salario)>UPPER(:p1) AND UPPER(salario) < UPPER(:p2)")
    consulta = "SELECT apellido,oficio,salario FROM emp where salario between :p1 and :p2"

    cursor.execute(consulta, (valor1,valor2,))
     # Si en un único parámetro tenemos que poner ',' a continuación del valor de la variable

    for ape, ofi, sal in cursor:
        print("Apellido: ", ape)
        print("Oficio: ", ofi)
        print("Salario: ", str(sal))

except connection.Error as error:
    print("Error: ", error)

connection.close()