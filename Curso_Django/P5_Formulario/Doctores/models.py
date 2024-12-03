import cx_Oracle

class Peticion:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def select(self,datos):
        cursor = self.connection.cursor()
        try:
            consulta = "SELECT apellido, especialidad, salario FROM doctor WHERE hospital_cod IN(:P1)"
            cursor.execute(consulta,(datos,))

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor