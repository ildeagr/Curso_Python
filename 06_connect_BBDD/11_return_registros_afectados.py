#Retorno de los registros afectados por el procedimiento
#El valor de retorno se obtiene dentro del propio procedimiento con SQL%ROWCOUNT

import cx_Oracle

connection = cx_Oracle.connect("system", "javaoracle", "localhost/XE")
cursor = connection.cursor()

try:
    apeDoctor = input("Apellido Doctor:")
    resultado = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('DELETE_DOCTOR', (apeDoctor,resultado))

    print(f"Doctores borrados:{int(resultado.getvalue())}")

except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()

"""Procedimiento creado en Oracle"""

"""
CREATE OR REPLACE PROCEDURE DELETE_DOCTOR(p_doc doctor.apellido%type,
p_afectados OUT number)
AS
BEGIN 
   DELETE FROM DOCTOR
   WHERE UPPER(APELLIDO)=UPPER(p_doc); 
   p_afectados:=SQL%ROWCOUNT;
   
   commit;
END;
"""