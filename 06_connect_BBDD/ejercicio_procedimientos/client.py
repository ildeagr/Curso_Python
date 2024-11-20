import sys

from consultBBDD import connection
from valid_params import validated

i=1
while i!=0:
    print("\n*** SELECCIONA UNA OPCIÓN ***")
    print("1 -  Alta hospital")
    print("2 -  Baja hospital")
    print("3 -  Modificar teléfono")
    print("4 -  Salir")

    option = int(input("\nEscriba su opción:"))
    valor =""

    if (option > 0 and option < 5):
        if (option == 1):
            codehosp = input("\nEscriba código del hospital:")
            namehosp = input("Escriba el nombre del hospital:")
            dir = input("Escriba la direccion:")
            telf = input("Escriba el teléfono:")
            numb = input("Escriba el número de camas:")

            validparam = (codehosp, namehosp, dir, telf, numb)
            valido = validated()
            responsevalidate = valido.paramsnoemtpy(validparam)

            if not responsevalidate:
                consult = connection(codehosp, namehosp, dir, telf, numb)
                response = consult.procInsert()

                if response.getvalue() != 0:
                    valor = ("Registro hospital insertado.")

            else:
                valor = (f"Uno de los parámetros está vacio.")


        elif (option == 2):
            codehosp = input("\nEscriba código del hospital:")

            validparam = (codehosp,)
            valido = validated()
            responsevalidate = valido.paramsnoemtpy(validparam)

            if not responsevalidate:
                consult = connection(codehosp, "", "", "", "")
                valor = consult.procDelete()

            else:
                valor = (f"Uno de los parámetros está vacio.")

        elif (option == 3):
            codehosp = input("\nEscriba código del hospital:")
            telf = input("Escriba el teléfono:")

            validparam = (codehosp,)
            valido = validated()
            responsevalidate = valido.paramsnoemtpy(validparam)

            if not responsevalidate:
                consult = connection(codehosp, "", "", telf, "")
                valor = consult.procUpdate()

            else:
                valor = (f"Uno de los parámetros está vacio.")
        else:
            consult = connection("", "", "", "", "")
            consult.desconnect()
            sys.exit()

    else:
        valor = ("\nOpcion no disponible")

    print (valor)


"""Procedimientos implementados en Oracle"""

"""CREATE OR REPLACE PROCEDURE INSERTHOSPITAL
(CODEH HOSPITAL.HOSPITAL_COD%TYPE, NAMEH HOSPITAL.NOMBRE%TYPE, DIR HOSPITAL.DIRECCION%TYPE, TELF HOSPITAL.TELEFONO%TYPE, NUMB HOSPITAL.NUM_CAMA%TYPE)
AS
BEGIN
  INSERT INTO HOSPITAL VALUES(CODEH, NAMEH, DIR, TELF, NUMB );
  COMMIT;
END;

CREATE OR REPLACE PROCEDURE DELETEHOSPITAL
(CODEH HOSPITAL.HOSPITAL_COD%TYPE, ROWC OUT NUMBER)
AS
BEGIN
  DELETE FROM HOSPITAL WHERE HOSPITAL_COD = CODEH;
  ROWC:=SQL%ROWCOUNT;
  COMMIT;
END;

CREATE OR REPLACE PROCEDURE UPDATETELF
(CODEH HOSPITAL.HOSPITAL_COD%TYPE, TELF HOSPITAL.TELEFONO%TYPE, ROWC OUT NUMBER)
AS
BEGIN
  UPDATE HOSPITAL
  SET TELEFONO = TELF
  WHERE HOSPITAL_COD = CODEH;
  ROWC:=SQL%ROWCOUNT;
  COMMIT;
END;
"""
