from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    api_url= "https://swapi.dev/api/people/"
    response = requests.get(api_url)

    info = response.json()

    context = {
        'datos': info['results']
    }

    return render(request, "index.html",context)