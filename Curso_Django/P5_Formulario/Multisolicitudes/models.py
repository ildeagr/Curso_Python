import cx_Oracle

class Peticion:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")


    def insert(self,num,nom,loc):
        cursor = self.connection.cursor()
        try:
            consulta = "INSERT INTO DEPT VALUES (:P1,UPPER(:P2), UPPER(:P3))"
            cursor.execute(consulta, (int(num),nom,loc))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)


    def update(self,num,nom,loc):
        cursor = self.connection.cursor()
        try:
            consulta = "UPDATE DEPT SET DNOMBRE = UPPER(:P1) , LOC = UPPER(:P2) WHERE DEPT_NO =:P3"
            cursor.execute(consulta,(nom, loc, int(num)))
            self.connection.commit()


        except self.connection.Error as error:
            print("Error: ", error)


    def delete(self,num):
        cursor = self.connection.cursor()
        try:
            consulta = "DELETE FROM DEPT WHERE DEPT_NO = :P1"
            cursor.execute(consulta, (num,))
            self.connection.commit()


        except self.connection.Error as error:
            print("Error: ", error)


    def select(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM DEPT")

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor