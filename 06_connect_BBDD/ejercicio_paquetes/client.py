import sys

from consultBBDD import connection
from valid_params import validated

while True:
    print("\n*** SELECCIONA UNA OPCIÓN ***")
    print("1 -  Mostrar salario y comisión.")
    print("2 -  Modificar salario y comisión.")
    print("3 -  Salir")

    option = int(input("\nEscriba su opción:"))
    valor =""

    if option > 0 and option < 4:
        if option == 1:
            codeemp = input("\nEscriba código empleado:")

            validparam = (codeemp,)
            valido = validated()
            responsevalidate = valido.paramsnoemtpy(validparam)

            if not responsevalidate:
                consult = connection(codeemp,"","")
                response = consult.procSelect()
                valor = f"Salario: {response[0]}€ \nComisión: {response[1]}€"

            else:
                valor = f"Uno de los parámetros está vacio."


        elif option == 2:
            codeemp = input("\nEscriba código empleado:")
            sal = input("\nEscriba elnuevo salario:")
            comi = input("\nEscriba la nueva comisión:")

            validparam = (codeemp,sal,comi)
            valido = validated()
            responsevalidate = valido.paramsnoemtpy(validparam)

            if not responsevalidate:
                consult = connection(codeemp, sal, comi)
                valor = consult.procUpdate()

            else:
                valor = (f"Uno de los parámetros está vacio.")

        else:
            consult = connection("", "", "")
            consult.desconnect()
            sys.exit()

    else:
        valor = ("\nOpcion no disponible")

    print (valor)

""" Paquete creado en BBDD """
"""
create or replace package tablaempsal
as
  procedure showsal(p_emp_no emp.emp_no%type,p_salario out emp.salario%type, p_comision out emp.comision%type,p_afectados OUT number);
  procedure updatesal(p_emp_no emp.emp_no%type,p_salario emp.salario%type,p_comision emp.comision%type,p_afectados OUT number);
end;

create or replace package body tablaempsal
as
   procedure showsal(p_emp_no emp.emp_no%type,p_salario out emp.salario%type,p_comision out emp.comision%type,p_afectados OUT number)
    as
    begin
      select SALARIO,NVL(COMISION, 0) into p_salario, p_comision from emp where emp_no =p_emp_no;
      p_afectados:=SQL%ROWCOUNT;
    end;

   procedure updatesal(p_emp_no emp.emp_no%type,p_salario emp.salario%type,p_comision emp.comision%type,p_afectados OUT number)
    as
    begin
      update emp
      set SALARIO = p_salario, COMISION = p_comision
      where emp_no =p_emp_no;
      p_afectados:=SQL%ROWCOUNT;
      commit;
    end;
end;
"""