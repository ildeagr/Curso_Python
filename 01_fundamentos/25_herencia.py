#Herencia en clases

class Bicicleta:
    color = ""
    tamanio = ""
    Vel_max=15
    velocidad= -1

    def __init__(self):
        self.velocidad=0
    def subirVelocidad(self):
        self.velocidad = self.velocidad+1
    def bajarVelocidad(self):
        self.velocidad = self.velocidad-1
    def cambiarVelMax(self, maxVel):
        self.Vel_max=maxVel
    def __str__(self):
        return "Velocidad Actual:" + str(self.velocidad) + ", Velocidad Máxima:" + str(self.Vel_max)

#La siguiente clase hereda de la anterior indicandoselo entre paréntesis
class BicicletaCarreras (Bicicleta):
    marcha = 0

    def subirMarcha(self):
        self.marcha = self.marcha + 1
    def bajarMarcha(self):
        self.marcha = self.marcha - 1
    def velocidadMaximaAutopista(self,velAutp):
        super().cambiarVelMax(velAutp)