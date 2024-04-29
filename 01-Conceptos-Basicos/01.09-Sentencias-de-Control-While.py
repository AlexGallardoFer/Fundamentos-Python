#################################################
# Sentencias de Control - While                 #
#################################################

# Declaración de variables
citricos = ["naranja", "limón", "pomelo", "lima", "mandarina"]
index = 0
valor = 0

# Uso del while
print("Inicio del WHILE")

while (valor < 5):
    valor += 1
    if (valor == 3):
        continue

    print(f"Valor actual: {valor}")

valor = 0
print("Fin del While\n")

# Utilizamos el WHILE para recorrer colecciones
print("Inicio del WHILE")

while (index < len(citricos)):
    print(f"-> {index}# {citricos[index]}")
    index += 1

index = 0
print("Fin del While\n")

# Implementar la funcionalidad que otros lenguajes ofrecen mediante 
# el uso de DO/WHILE, consiguiendo que al menos una vez se ejecute
# el bloque de sentencias

print("Inicio del WHILE")

while (True):
    valor += 1
    print(f"Valor actual: {valor}")

    if (valor > 4):
        break

valor = 0
print("Fin del While\n")