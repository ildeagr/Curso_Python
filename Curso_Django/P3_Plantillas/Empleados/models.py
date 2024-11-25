import cx_Oracle


class Empleados:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def devolverdato(self):
        cursor = self.connection.cursor()
        dato=''
        try:
            cursor.execute("SELECT APELLIDO, FECHA_ALT FROM EMP")
        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def devolverpeliculas(self):
        cursor = self.connection.cursor()
        dato=''
        try:
            cursor.execute("SELECT TITULO, FOTO FROM PELICULAS")
        except self.connection.Error as error:
            print("Error: ", error)

        return cursor