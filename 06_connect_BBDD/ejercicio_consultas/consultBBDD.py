import cx_Oracle

class connection:
    numhosp = ""
    codedoctor = ""
    apellido = ""
    especialidad = ""
    salario = ""

    dataconnection= cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
    cursor = dataconnection.cursor()
    result=""

    def __init__(self,numhosp, codedoctor, apellido, especialidad, salario):
        self.numhosp=numhosp
        self.codedoctor=codedoctor
        self.apellido=apellido
        self.especialidad=especialidad
        self.salario=salario

    def sqlInsert(self):
        try:
            insertdoctor = ("INSERT INTO doctor "
                            "(hospital_cod,doctor_no,apellido,especialidad,salario) "
                            "VALUES (:P1, :P2, :P3, :P4, :P5)")

            datosdoctor = (self.numhosp,self.codedoctor,self.apellido,self.especialidad, self.salario)
            self.cursor.execute(insertdoctor, datosdoctor,)

            if self.cursor.rowcount > 0:
                self.dataconnection.commit()
                return "Registro modificado satisfactoriamente"
            else:
                return "Dato no encontrado"

        except self.dataconnection.Error as error:
            return "Error: ", error


    def sqldelete(self):
        try:
            deletedoctor = "Delete from doctor where doctor_no=:P1"
            self.cursor.execute(deletedoctor, (self.codedoctor,))

            if self.cursor.rowcount > 0:
                self.dataconnection.commit()
                return "Registro eliminado satisfactoriamente"
            else:
                return "Dato no encontrado"

        except self.dataconnection.Error as error:
            return "Error: ", error

    def sqlupdatesalario(self):
        try:
            updatesalario = "Update doctor set salario=:P1 where doctor_no=:P2"
            self.cursor.execute(updatesalario, (self.salario,self.codedoctor,))

            if self.cursor.rowcount > 0:
                self.dataconnection.commit()
                return "Registro modificado satisfactoriamente"
            else:
                return "Dato no encontrado"

        except self.dataconnection.Error as error:
            return "Error: ", error

    def sqlselectdoctor(self):

        try:
            selectdoctor = "Select apellido, especialidad from doctor where doctor_no=:P1"
            self.cursor.execute(selectdoctor, (self.codedoctor,))

            for ape, espe in self.cursor:
                self.result = self.result + (f"\nApellido: {ape} \nEspecialidad: {espe}")
                return self.result

        except self.dataconnection.Error as error:
            return "Error: ", error

    def sqlgroup(self):
        try:
            selectgroup = "select sum(salario),avg(salario),count(doctor_no) from doctor where hospital_cod=:P1"
            self.cursor.execute(selectgroup, (self.numhosp,))
            return self.cursor

        except self.dataconnection.Error as error:
            return "Error: ", error

