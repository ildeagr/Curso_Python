import sys

from consultBBDD import connection
from validar_parametros import validated

while True:
    print("\n*** SELECCIONA UNA OPCIÓN ***")
    print("1 -  Alta doctor")
    print("2 -  Modificar salario doctor")
    print("3 -  Eliminar doctor")
    print("4 -  Mostrar apellido y saladio doctor")
    print("5 -  Visualizar datos de grupo del hospital")
    print("6 -  Salir")

    option = int(input("\nEscriba su opción:"))
    valor =""

    if(option > 0  and option < 7):
        if(option == 1):
            numhosp = input("\nEscriba un número de hospital:")
            doctor_no= input("Escriba un número de doctor:")
            apellido = input("Escriba el apellido del doctor:")
            especialidad = input("Escriba el especialidad del doctor:")
            salario = input("Escriba el salario del doctor:")

            validparam = (numhosp, doctor_no, apellido, especialidad,salario)
            valido = validated()
            responsevalidate = valido.paramsnoemtpy(validparam)

            if not responsevalidate:
                consult = connection(numhosp,doctor_no,apellido,especialidad,salario)
                valor = consult.sqlInsert()

            else:
                valor = (f"Uno de los parámetros está vacio.")

        elif( option == 2):
            cod_doctor = input("\nEscriba el código doctor:")
            newsala = input("Escriba el nuevo salario:")

            validparam = (cod_doctor,newsala)
            valido = validated()
            responsevalidate = valido.paramsnoemtpy(validparam)

            if not responsevalidate:
                consult = connection("", cod_doctor, "", "", newsala)
                valor = consult.sqlupdatesalario()

            else:
                valor = (f"Uno de los parámetros está vacio.")

        elif (option == 3):
            cod_doctor = input("\nEscriba el código doctor para eliminar:")

            validparam = (cod_doctor)
            valido = validated()
            responsevalidate = valido.paramsnoemtpy(validparam)

            if not responsevalidate:
                consult = connection("", cod_doctor,"", "", "")
                valor = consult.sqldelete()
            else:
                valor = (f"Uno de los parámetros está vacio.")

        elif (option == 4):
            cod_doctor = input("\nEscriba el código doctor a consultar:")

            validparam = cod_doctor
            valido = validated()
            responsevalidate = valido.paramsnoemtpy(validparam)

            if not responsevalidate:
                consult = connection("", cod_doctor, "", "", "")
                valor = consult.sqlselectdoctor()

            else:
                valor = (f"Uno de los parámetros está vacio.")

        elif (option == 5):
            grouphosp = input("\nIntroduce código hospital para agrupar:")

            validparam = (grouphosp)
            valido = validated()
            responsevalidate = valido.paramsnoemtpy(validparam)

            if not responsevalidate:
                consult = connection(grouphosp, "", "", "", "")
                response = consult.sqlgroup()

                for sumsal, avgsal,docto in response:
                    valor = valor + (f"Sumasalarial: {sumsal} \nMedia salarial: {avgsal} \nNúmero de doctores: {docto} \n")

                print("\nDatos de grupo: \n__________________________")

            else:
                valor = (f"Uno de los parámetros está vacio.")

        else:
            sys.exit()
    else:
        valor = ("\nOpcion no disponible")

    print (valor)