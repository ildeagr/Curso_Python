#Creacion de instancias Bicicleta

from claseBicicleta import Bicicleta


#Creamos un objeto Bicicleta
mibici=Bicicleta()
print(mibici.velocidad)
mibici.cambiarVelMax(30)
print(mibici.Vel_max)

print(mibici.__str__())