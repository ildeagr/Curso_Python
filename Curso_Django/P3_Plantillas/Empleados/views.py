from django.shortcuts import render
from Empleados.models import Empleados


def index(request):
    emple = Empleados()
    cursor=emple.devolverdato()
    contexto = {
        'listado_empleados': cursor
    }
    return render(request, "empleados/empleados.html", contexto)

def index2(request):
    emple = Empleados()
    cursor=emple.devolverpeliculas()
    contexto = {
        'listado_pelis': cursor
    }
    return render(request, "peliculas/peliculas.html", contexto)

def formulario(request):

    return render(request, "formulario/formulario.html")

