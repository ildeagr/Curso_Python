from django.shortcuts import render

from Get.models import Peticion
# Create your views here.


def index(request):
    return render(request, "oficios.html")

def empleados(request):
    dato = request.GET['oficio']

    print(dato)

    consulta = Peticion()
    response = consulta.select(dato)

    context = {
        'lista': response
    }

    return render(request, "resultado.html", context)