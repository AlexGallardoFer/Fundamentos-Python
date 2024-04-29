###################################################
# Colecciones - Diccionarios                      #
###################################################

# Declaración de variables
# Declaración de variables
# Utilizamos {} para la declaración de variables que son diccionarios
vacia = {}
frutas = {"NA":"naranja", "LI":"limón", "PO":"pomelo", "LM":"lima", "MA":"mandarina"}

# Mostrar el contenido de un diccionario
print(f"Contenido de frutas: {frutas}")

# Mostrar el valor de un elemento por su clave ("PO" = pomelo)
print(f"Fruta con clave 'PO': {frutas["PO"]}")
# print(f"Fruta con clave 'ML': {frutas["ML"]}")       # Da error

# Mostrar el valor de un elemento con la función GET
print(f"Clave 'PO': {frutas.get("PO")}")
print(f"Clave 'ML': {frutas.get("ML")}")

# Mostrar las claves del diccionario
print(f"Claves: {list(frutas.keys())}")

# Modificar los valores del diccionario
frutas["NA"] = "sandia"
print(f"Contenido de frutas: {frutas}")

frutas.update({"NA":"ciruela"})
print(f"Contenido de frutas: {frutas}")

# Añadir nuevos valores al diccionario
frutas["ML"] = "melon"
print(f"Contenido de frutas: {frutas}")

frutas.update({"MZ":"manzana"})
print(f"Contenido de frutas: {frutas}")

# Eliminar valores del diccionario
frutas.pop("NA")
del frutas["MZ"]
print(f"Contenido de frutas: {frutas}")

# Recorremos el diccionario mostrando los diferentes valores
for key in frutas:
    print(f"{key} -> {frutas[key]}")

# Copiar un diccionario
vacio = frutas.copy()
print(f"Contenido de vacio: {vacio}")

# Eliminar todos los elementos de una lista
frutas.clear()
print(f"Contenido de frutas: {frutas}")