# Creacion de excepciones propias

class MiExcepcionPropia (Exception):
    def __init__(self,mensaje):
        super().__init__(mensaje)


#Para lanzar una excepcion personalizada se hace con "raise"

try:
    raise MiExcepcionPropia("Algo inesperado ha sucedido al conectar un Arduino")
except MiExcepcionPropia as e:
    print("Se ha producido una excepcion personalizada:",e)