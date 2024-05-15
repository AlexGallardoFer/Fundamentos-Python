###################################################
# Consultar numero de bicis libres por lugar      #
###################################################
import requests, json

# Obtener token de acceso a la API
urls = {
    "base": "https://openapi.emtmadrid.es/",
    "version": "<version>/",
    "login": "mobilitylabs/user/login/",
    "stations": "transport/bicimad/stations"
}

token = ""

try:
    # Obtener token de acceso a la API
    endpoint1 = urls["base"] + urls["version"].replace("<version>", "v2") + urls["login"]
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

    endpoint2 = urls["base"] + urls["version"].replace("<version>", "v1") + urls["stations"]
    headers2 = {"accessToken": token}
    
    response2 = requests.get(endpoint2, headers=headers2)
    total = 0

    if response2.status_code == 200:
        for item in response2.json()["data"]:
            print(f"Estación: {item["name"]}")
            print(f"Bicis libres: {item["dock_bikes"]}\n")
            total += int(item["dock_bikes"])

        print(f"Total de bicis libres: {total}")

    else:
        print(f"Error {response2.status_code}: {response2.reason}")
        quit()

except Exception as e:
    print(f"Error: {e}")