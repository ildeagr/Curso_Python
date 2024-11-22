import cx_Oracle

class connection:
    codehosp = ""
    namehosp = ""
    dire = ""
    telf = ""
    numb = ""
    rowc = 0

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
            self.rowc = self.cursor.var(cx_Oracle.NUMBER)
            self.cursor.callproc('INSERTHOSPITAL', (self.codehosp, self.namehosp, self.dire, self.telf, self.numb,self.rowc))
            return self.statusregister()

        except self.dataconnection.Error as error:
            return "Error: ", error

    def procDelete(self):
        try:
            self.rowc = self.cursor.var(cx_Oracle.NUMBER)
            self.cursor.callproc('DELETEHOSPITAL', (self.codehosp,self.rowc))
            return self.statusregister()

        except self.dataconnection.Error as error:
            return "Error: ", error


    def procUpdate(self):
        try:
            self.rowc = self.cursor.var(cx_Oracle.NUMBER)
            self.cursor.callproc('UPDATETELF', (self.codehosp,self.telf,self.rowc))
            return self.statusregister()

        except self.dataconnection.Error as error:
            return "Error: ", error

    def statusregister(self):
        if self.rowc.getvalue() != 0:
            return "Registro Ok"
        else:
            return "Registro no Ok"

    def desconnect(self):
        self.cursor.close()
        self.dataconnection.close()