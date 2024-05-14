###################################################
# API de Código Postal                            #
###################################################
import requests

codigoPostal = input("Introduce un código postal: ")

endpoint = f"https://api.zippopotam.us/es/{codigoPostal}"
try:
    response = requests.get(endpoint)

    if response.status_code == 200:
        data = response.json()
        sitios = data["places"]
        for lugar in sitios:
            print(f"   Ubicación: {lugar["state"]}")
            print(f"     Latitud: {lugar["latitude"]}")
            print(f"    Longitud: {lugar["longitude"]}")
            print(f"Nombre Lugar: {lugar["place name"]}\n")
    else:
        print(f"Error {response.status_code}: {response.reason}")

except Exception as err:
    print(f"{err}")