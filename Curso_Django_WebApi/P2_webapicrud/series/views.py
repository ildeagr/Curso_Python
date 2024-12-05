from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    api_url= "https://apiseriespersonajes.azurewebsites.net/api/Series"
    response = requests.get(api_url)

    info = response.json()

    context = {
        'datos': info
    }
    return render(request, "index.html",context)

def indexper(request):
    api_url = "https://apiseriespersonajes.azurewebsites.net/api/Series"
    response = requests.get(api_url)

    info = response.json()

    context = {
        'datos': info
    }
    return render(request, "indexper.html",context)

def indexserie(request):
    return render(request, "indexserie.html",)

def indexupdateserie(request):
    api_url = "https://apiseriespersonajes.azurewebsites.net/api/Series"
    response = requests.get(api_url)

    info = response.json()

    context = {
        'datos': info
    }
    return render(request, "updateserie.html",context)

def insertserie(request):
    per = request.POST['txtper']
    img = request.POST['txtimg']
    pun = request.POST['txtpun']
    anyo = request.POST['txtanyo']

    apiurl = "https://apiseriespersonajes.azurewebsites.net/api/Series"
    serie = {"idSerie": 0, "nombre": per, "imagen": img, "puntuacion": int(pun), "anyo": int(anyo)}

    requests.post(apiurl, json=serie)

    return render(request, "index.html")


def updateserie(request):
    numS = request.POST['series']
    per = request.POST['txtper']
    img = request.POST['txtimg']
    pun = request.POST['txtpun']
    anyo = request.POST['txtanyo']

    apiurl = "https://apiseriespersonajes.azurewebsites.net/api/Series"
    serie = {"idSerie": int(numS), "nombre": per, "imagen": img, "puntuacion": int(pun), "anyo": int(anyo)}

    response = requests.put(apiurl, json=serie)

    return render(request, "index.html")

def selectserie(request):
    num = request.POST['series']
    api_url = "https://apiseriespersonajes.azurewebsites.net/api/Series/"
    response = requests.get(api_url + num)
    info = response.json()
    context = {
        'datos': info
    }

    print(context)

    return render(request, "serie.html",context)

def selectper(request):
    num = request.POST['series']
    api_url = "https://apiseriespersonajes.azurewebsites.net/api/Series/"
    response = requests.get(api_url + num)
    info = response.json()
    print(info["nombre"])
    context = {
        'datos': info
    }

    print(context)

    return render(request, "serie.html",context)

def insertper(request):
    numS = request.POST['series']
    per = request.POST['txtper']
    img = request.POST['txtimg']
    apiurl = "https://apiseriespersonajes.azurewebsites.net/api/Personajes"
    personaje = {"idPersonaje": 0, "nombre": per, "imagen": img, "idSerie": int(numS)}

    requests.post(apiurl, json=personaje)

    return render(request, "index.html")