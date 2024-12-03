import cx_Oracle

class Peticion:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")


    def select(self,dato):
        cursor = self.connection.cursor()
        try:
            consulta = "SELECT apellido, oficio, salario FROM emp WHERE UPPER(oficio)=UPPER(:P1)"
            cursor.execute(consulta,(dato,))

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor