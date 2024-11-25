from django.shortcuts import render
from AccesoDatos.models import Jugador


def index(request):
    emple = Jugador()
    cursor=emple.devolverdato()
    contexto = {
        'listado_empleados': cursor
    }
    return render(request, "deportes/JugadoresPrimera.html", contexto)
