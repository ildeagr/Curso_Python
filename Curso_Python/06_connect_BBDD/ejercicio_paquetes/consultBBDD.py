import cx_Oracle

class connection:
    codeemp = ""
    sal = ""
    comi = ""
    rowc = 0

    dataconnection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
    cursor = dataconnection.cursor()

    def __init__(self, codeemp, sal, comi):
        self.codeemp = codeemp
        self.comi = comi
        self.sal = sal

    def procSelect(self):
        try:
            self.sal = self.cursor.var(cx_Oracle.NUMBER)
            self.comi = self.cursor.var(cx_Oracle.NUMBER)
            self.rowc = self.cursor.var(cx_Oracle.NUMBER)
            self.cursor.callproc('tablaempsal.showsal', (self.codeemp, self.sal, self.comi,self.rowc))
            return self.sal.getvalue(),self.comi.getvalue(),self.statusregister()

        except self.dataconnection.Error as error:
            return "Error: ", error

    def procUpdate(self):
        try:
            self.rowc = self.cursor.var(cx_Oracle.NUMBER)
            self.cursor.callproc('tablaempsal.updatesal', (self.codeemp,self.sal, self.comi,self.rowc))
            return self.statusregister()

        except self.dataconnection.Error as error:
            return "Error: ", error


    def statusregister(self):
        if self.rowc != 0:
            return "Registro Ok"
        else:
            return "Registro no Ok"

    def desconnect(self):
        self.cursor.close()
        self.dataconnection.close()