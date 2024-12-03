import requests
import json

api_url = "https://apiseriespersonajes.azurewebsites.net/api/Series"
#capturamos la respuesta
response = requests.get(api_url)
#convertimos la respuesta a objeto diccionario
series = response.json()
print("\nListado Seies")
print("-------------------")
for i in series:
    print(i["nombre"] , i["puntuacion"])