from django.shortcuts import render


#Le pasamos los valores al html a través de un diccionario
def titular(reques):
    nombre = 'Real Madrid'
    dato= nombre.upper()
    lista = {
        "equipo1":dato
    }
    return render(reques,"futbol/Titular.html", lista)

def jugadores(request):
    listajugadores=[
        {
            "Nombre":"Sergio Ramos",
            "Demarcacion":"Defensa",
            "Numero":5
        },
        {
            "Nombre": "Eden Hazard",
            "Demarcacion": "Delantero",
            "Numero":7
        },
        {
            "Nombre": "Karim Benzema",
            "Demarcacion": "Delantero",
            "Numero":9
        },
        {
            "Nombre": "Toni Kroos",
            "Demarcacion": "Centrocampista",
            "Numero": 8
        },
        {
            "Nombre": "Thibaut Courtois",
            "Demarcacion": "Portero",
            "Numero": 1
        }
    ]
    contexto = {
        'listado_jugadores': listajugadores
    }
    return render(request, "futbol/Listajugadores.html", contexto)