# Petición calculo letra dni a la clase

from ClaseDNI import Dni

numDni = input("Introduce número DNI:")
if len(numDni)==8:
    newDni = Dni(int(numDni))
    newDni.calculoLetra()
    print(newDni.__str__())
else:
    print("Número Dni erróneo")