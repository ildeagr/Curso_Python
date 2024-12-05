import requests
apiurl = "https://apicruddepartamentoscore.azurewebsites.net"
request = "/api/departamentos/122234"
#departamento = {"numero": 10, "nombre": "CONTABILIDAD", "localidad": "ELCHE"}
response = requests.delete(apiurl + request)
#response = requests.put(apiurl + request, json=departamento)
#convertimos la respuesta a objeto diccionario
#print(response.json())
print("Status: " + str(response.status_code))