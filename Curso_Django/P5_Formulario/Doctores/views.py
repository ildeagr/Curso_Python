from django.shortcuts import render

from Doctores.models import Peticion


def formulario(request):
    return render(request, "Doctores.html")

def select(request):
    hospital = request.POST.getlist('chkhosp')
    hospitales = ",".join(hospital)

    consulta = Peticion()
    response = consulta.select(hospitales)

    context = {
        'lista_doctores': response
    }

    return render(request, "respuesta.html", context)