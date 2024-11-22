# Creación de clases

class Bicicleta:
    color = ""
    tamanio = ""
    Vel_max=15
    velocidad= -1

    def __init__(self):
        self.velocidad=0
    def subirmarcha(self):
        self.velocidad = self.velocidad+1
    def bajarmarcha(self):
        self.velocidad = self.velocidad-1
    def cambiarVelMax(self, maxVel):
        self.Vel_max=maxVel
    def __str__(self):
        return "Velocidad Actual:" + str(self.velocidad) + ", Velocidad Máxima:" + str

#Creamos un objeto Bicicleta
mibici=Bicicleta()
print(mibici.velocidad)
mibici.cambiarVelMax(30)
print(mibici.Vel_max)

print(mibici.__str__())