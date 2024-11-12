class Dni:
    numDni = 00000000
    letraDni = ""

    def __init__(self, numDni):
        self.numDni = numDni

    def calculoLetra(self):
        tablaLetra = "TRWAGMYFPDXBNJZSQVHLCKET"
        resto = self.numDni % 23
        self.letraDni = tablaLetra[resto]

    def __str__(self):
        return "Número Dni:" + str(self.numDni) + "\nLetra:" + str(self.letraDni)