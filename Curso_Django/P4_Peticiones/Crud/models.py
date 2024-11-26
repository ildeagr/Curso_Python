import cx_Oracle


class Peticion:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def insert(self,datos):
        cursor = self.connection.cursor()
        try:
            consulta = ("INSERT INTO doctor VALUES (:P1, :P2, :P3, :P4, :P5)")
            cursor.execute(consulta, datos)
            self.connection.commit()


        except self.connection.Error as error:
            print("Error: ", error)

        return "Insertado correctamente"

    def delete(self,datos):
        cursor = self.connection.cursor()
        try:
            consulta = ("DELETE FROM doctor WHERE DOCTOR_NO =:P1")
            cursor.execute(consulta, (datos,))
            self.connection.commit()


        except self.connection.Error as error:
            print("Error: ", error)

        return "Borrado correctamente"

    def update(self,datos):
        cursor = self.connection.cursor()
        try:
            consulta = ("UPDATE doctor SET especialidad =:P1 WHERE DOCTOR_NO =:P2")
            cursor.execute(consulta, datos)
            self.connection.commit()


        except self.connection.Error as error:
            print("Error: ", error)

        return "Modificado correctamente"

    def select(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM doctor")

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor