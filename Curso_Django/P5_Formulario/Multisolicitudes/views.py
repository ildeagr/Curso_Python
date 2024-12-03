from django.shortcuts import render

from Multisolicitudes.models import Peticion

def index(request):
    return render(request, "crud.html")

def peticion(request):
    dato = request.POST['operacion']
    num =request.POST['numero']
    nom = request.POST['nombre']
    loc = request.POST['localidad']

    if dato=='Insertar':
        consulta = Peticion()
        consulta.insert(num,nom,loc)
        response = consulta.select()


    elif dato=='Modificar':
        consulta = Peticion()
        consulta.update(num,nom,loc)
        response = consulta.select()

    else:
        consulta = Peticion()
        consulta.delete(num)
        response = consulta.select()

    lista = {
        "operacion": dato,
        "resultado": 'satisfactoria',
        "respuesta": response
    }

    return render(request, "crud.html", lista)