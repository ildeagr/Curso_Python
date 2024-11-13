class Ean:
    codigo = "0000000000000"
    numcontrol = 0
    digcontrol = 0
    validacion = "válido"

    def __init__(self, num):
        self.codigo = num[0:len(num)-1]
        self.numcontrol = int(num[len(num)-1])


    def validarcodigo(self):
        pares = 0
        impares = 0

        for i in range (0,len(self.codigo),2):
            impares = impares + int(self.codigo[i])
            if i+1 < len(self.codigo):
                pares = pares + int(self.codigo[i+1])

        if len(self.codigo) == 12:
            pares = pares*3
        else:
            impares = impares*3

        self.digcontrol= 10 - (int((pares+impares)%10))

        if self.digcontrol == 10:
            self.digcontrol = 0

        if self.numcontrol != self.digcontrol:
            self.validacion = "inválido"


    def __str__(self):
        return "Número control: " + str(self.numcontrol) + "\nDigito control: " + str(self.digcontrol) + "\nEl código " + str(self.codigo) + " es " + str(self.validacion)
