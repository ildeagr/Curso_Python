import requests
apiurl = "https://apicruddepartamentoscore.azurewebsites.net"
request = "/api/departamentos"
departamento = {"numero": 102, "nombre": "PRODUCCION", "localidad": "SEVILLA"}

response = requests.post(apiurl + request, json=departamento)
#convertimos la respuesta a objeto diccionario
#print(response.json())
print("Status: " + str(response.status_code))