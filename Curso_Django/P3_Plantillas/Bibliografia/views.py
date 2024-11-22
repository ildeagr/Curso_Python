from django.shortcuts import render

def index(request):
    return render(request, "politica/ildefonso.html")

def deportes(request):
    return render(request, "deportes/deportes.html")
