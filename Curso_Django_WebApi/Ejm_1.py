import requests
import json

api_url = "https://apiempleadosspgs.azurewebsites.net/api/Empleados/7839"
#capturamos la respuesta
response = requests.get(api_url)
#convertimos la respuesta a objeto diccionario
empleado = response.json()
print(empleado)
print(empleado["apellido"])