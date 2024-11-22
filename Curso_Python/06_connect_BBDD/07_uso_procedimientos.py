#Uso de procedimientos almacenados desde Python

import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
cursor = connection.cursor()

try:
    dp = input("Número de departamento:")
    nombre = input("Nombre departamento:")
    localidad = input("localidad:")
    cursor.callproc("InsertarDEPT", (dp, nombre, localidad))

    if cursor.rowcount > 0:
        print("Registro insertado satisfactoriamente")
    else:
        print("Dato no encontrado")

except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()

"""Procedimiento creado en Oracle"""

"""
CREATE OR REPLACE PROCEDURE INSERTARDEPT
(DP DEPT.Dept_No%TYPE,NOMBRE DEPT.DNOMBRE%TYPE,LOCA DEPT.LOC%TYPE)
AS
BEGIN
    INSERT INTO DEPT VALUES(DP,NOMBRE,LOCA);
    COMMIT;
END;
"""