from django.shortcuts import render


#Le pasamos los valores al html a través de un diccionario
def infocv(reques):
    lista = {
        "nombre": "Ildefonso",
        "edad": "36",
        "apellidos": "Albares García"
    }
    return render(reques,"Infocv/cv.html", lista)