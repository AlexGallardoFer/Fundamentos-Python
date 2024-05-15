###################################################
# Consultar número de plazas libres por parking   #
###################################################
import requests, json

def InfoParking(item):
    mensaje = ""

    if item["freeParking"] == None:
        mensaje = f"{item["name"]}\nNo hay información sobre el número de plazas libres.\n"
    else:
        mensaje = f"{item["name"]}\nQuedan {item["freeParking"]} plazas libres.\n"

    return mensaje

# Obtener token de acceso a la API
urls = {
    "base": "https://openapi.emtmadrid.es/v2/",
    "login": "mobilitylabs/user/login/",
    "parking": "citymad/places/parkings/availability/"
}

token = ""

try:
    # Obtener token de acceso a la API
    endpoint1 = urls["base"] + urls["login"]
    headers1 = {
        "X-ClientId": "25d3d248-fc0c-479d-8276-78ac52c647f2",
        "passKey": "141FE2B578702B63F6EE4E03049F95AB594A28BA9B67A7CAFF0D08BDB8B045463A14B6EADF5885D589B00DA11919CB9D12FFC012A317404D1EF97656E67A86B0"
    }

    response = requests.get(endpoint1, headers=headers1)

    if response.status_code == 200:
        token = response.json()["data"][0]["accessToken"]
    else:
        print(f"Error {response.status_code}: {response.reason}")
        quit()

    endpoint2 = urls["base"] + urls["parking"]
    headers2 = {"accessToken": token}
    
    response2 = requests.get(endpoint2, headers=headers2)

    if response2.status_code == 200:
        for item in response2.json()["data"]:
            print(InfoParking(item))

    else:
        print(f"Error {response2.status_code}: {response2.reason}")
        quit()

except Exception as e:
    print(f"Error: {e}")