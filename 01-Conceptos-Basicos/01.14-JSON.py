###################################################
# JSON (JavaScript Object Notation)               #
###################################################

# Importación de módulos
import json

# Declaración de variables
frutas = ["naranja", "limón", "pomelo", "lima", "mandarina"]

# Conversión de objetos en JSON
frutasJSON = json.dumps(frutas)

# Comprobaciones
print(f"Lista: {frutas}")
print(f"Posición 2: {frutas[2]}")
print(f"{type(frutas)}\n")

print(f"Lista: {frutasJSON}")
print(f"Posición 2: {frutasJSON[2]}")
print(f"{type(frutasJSON)}\n")

# Conversión de objetos JSON en objetos
frutas2 = json.loads(frutasJSON)

print(f"Lista: {frutas2}")
print(f"Posición 2: {frutas2[2]}")
print(f"{type(frutas2)}")