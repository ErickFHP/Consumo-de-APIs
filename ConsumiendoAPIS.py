import requests
import json

#URL base
base_url = "https://fakerapi.it/api/v1/"
#Recursos
recursos = ["books", "credit_cards", "images"]

#Se itera por los recursos y se obtienen 2 de cada uno
for recurso in recursos:
    # URL del estilo "https://fakerapi.it/api/v1/{recurso}?_quantity=2"
    url = base_url + recurso + "?_quantity=2"

    # Hacemos una solicitud GET a la URL y guardamos la respuesta
    response = requests.get(url)
    if response.status_code == 200:
        # Si es 200, significa que la solicitud fue exitosa
        # Obtenemos el contenido de la respuesta en formato JSON y lo guardamos en una variable
        data = response.json()
        # Imprimimos el JSON con una indentación de 4 espacios para que sea más legible
        print(json.dumps(data, indent=4))
    else:
        # Si no es 200, significa que hubo algún error en la solicitud
        # Imprimimos el código de estado y el motivo del error
        print(f"Error: {response.status_code} - {response.reason}")

#Se obtienen otras peticiones
url = base_url + recursos[0] + "?_quantity=1&_seed=1234"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print(f"Error: {response.status_code} - {response.reason}")

url = base_url + recursos[1] + "?_quantity=1&_seed=1234"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print(f"Error: {response.status_code} - {response.reason}")

url = base_url + recursos[2] + "?_quantity=1&_seed=7896"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print(f"Error: {response.status_code} - {response.reason}")
