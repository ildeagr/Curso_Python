from django.shortcuts import render
from Post.models import Empleado


def index(request):
     return render(request, "inicio.html")

def empleados(request):
    ofi = request.POST['txtOficio']
    emple = Empleado()
    cursor=emple.devolverdato(ofi)
    contexto = {
        'listado_empleados': cursor
    }
    return render(request, "empleados.html", contexto)