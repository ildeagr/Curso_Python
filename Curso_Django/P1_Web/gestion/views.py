from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Página de inicio")

def mensaje(request):
    return HttpResponse("Hola programaitors")
