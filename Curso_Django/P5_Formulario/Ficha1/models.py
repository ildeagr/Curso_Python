import cx_Oracle

class Peticion:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def insert(self,datos):
        cursor = self.connection.cursor()
        try:
            consulta = ("INSERT INTO clientesAlumnos VALUES (:P1, :P2, :P3, :P4, :P5, :P6, :P7, :P8)")
            cursor.execute(consulta, datos)
            self.connection.commit()


        except self.connection.Error as error:
            print("Error: ", error)

        return "Insertado correctamente"