import cx_Oracle

class connection:
    codehosp = ""
    namehosp = ""
    dire = ""
    telf = ""
    numb = ""
    rowc = None

    dataconnection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
    cursor = dataconnection.cursor()

    def __init__(self, codehosp, namehosp, dire, telf, numb):
        self.codehosp = codehosp
        self.namehosp = namehosp
        self.dire = dire
        self.telf = telf
        self.numb = numb

    def procInsert(self):
        try:
            self.cursor.callproc('INSERTHOSPITAL', (self.codehosp, self.namehosp, self.dire, self.telf, self.numb,self.rowc))

            if self.rowc.getvalue() != 0:
                return "Registro hospital insertado."

            else:
                return "Registro hospital no insertado."

        except self.dataconnection.Error as error:
            return "Error: ", error

    def procDelete(self):
        try:
            self.cursor.callproc('DELETEHOSPITAL', (self.codehosp,self.rowc))

            if self.rowc.getvalue() != 0:
                return "Registro hospital eliminado."

            else:
                return "Registro hospital no eliminado."

        except self.dataconnection.Error as error:
            return "Error: ", error


    def procUpdate(self):
        try:
            self.cursor.callproc('UPDATETELF', (self.codehosp,self.telf,self.rowc))

            if self.rowc.getvalue() != 0:
                return "Registro hospital modificado."

            else:
                return "Registro hospital no modificado."

        except self.dataconnection.Error as error:
            return "Error: ", error
