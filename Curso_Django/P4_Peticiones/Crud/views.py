from django.shortcuts import render

from Crud.models import Peticion


def index(request):
     return render(request, "index.html")

def peticion(request):
     name = request.POST.get('submit')

     if name == 'Alta':
          return render(request, "alta.html")

     elif name == 'Baja':
          return render(request, "borrar.html")

     elif name == 'Modificacion':
          return render(request, "modificar.html")

     elif name == 'Consultar':
          consulta = Peticion()
          cursor = consulta.select()
          context = {
               'listado_doctor': cursor
          }

          return render(request, "consultar.html",context)

def insert(request):
     hosp = request.POST['txthosp']
     doc =request.POST['txtdoc']
     ape = request.POST['txtape']
     espe = request.POST['txtespe']
     sal = request.POST['txtsal']

     datos = (int(hosp), int(doc), ape, espe, int(sal))
     print(datos)

     consulta = Peticion()
     response = consulta.insert(datos)

     context = {
          'dato': response
     }

     return render(request, "respuesta.html", context)

def delete(request):
     doc =request.POST['txtdoc']
     consulta = Peticion()
     response = consulta.delete(doc)

     context = {
          'dato': response
     }

     return render(request, "respuesta.html", context)

def update(request):
     doc =request.POST['txtdoc']
     espe = request.POST['txtespe']
     datos = (espe,int(doc))

     consulta = Peticion()
     response = consulta.update(datos)

     context = {
          'dato': response
     }

     return render(request, "respuesta.html", context)