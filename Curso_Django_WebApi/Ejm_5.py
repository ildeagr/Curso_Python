import requests
apiurl = "https://apicruddepartamentoscore.azurewebsites.net"
request = "/api/departamentos"
departamento = {"numero": 33, "nombre": "INVESTIGACION", "localidad": "MADRID"}

response = requests.put(apiurl + request, json=departamento)
#convertimos la respuesta a objeto diccionario
#print(response.json())
print("Status: " + str(response.status_code))