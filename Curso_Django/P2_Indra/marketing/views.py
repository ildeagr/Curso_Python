from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1 style='color:green;'>Ildefonso</h1>")


def datos(request):
    return HttpResponse("<h1>Albares Garcia</h1>")