from django.shortcuts import render

from Ficha1.models import Peticion
# Create your views here.


def formulario(request):
    return render(request, "formulario.html")

def insert(request):
    sistemas = ""
    nombre = request.POST['txtnombre']
    apellido1 = request.POST['txtape1']
    apellido2 = request.POST['txtape2']
    direccion = request.POST['txdirec']
    sexo = request.POST['rdbsexo']
    ciudad = request.POST['cmbCiudad']
    sistema = request.POST.getlist('chksys')
    observa = request.POST['txtobservaciones']

    for i in sistema:
        sistemas = sistemas + i + ", "

    sistemas = sistemas[:len(sistemas)-1]

    datos = (nombre, apellido1, apellido2, direccion, ciudad ,sexo,sistemas,observa)

    consulta = Peticion()
    response = consulta.insert(datos)

    context = {
        'dato': response
    }

    return render(request, "respuesta.html", context)