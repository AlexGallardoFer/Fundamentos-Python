###################################################
# Colecciones - Listas                            #
###################################################

# Declaración de variables
# Utilizamos [] para la declaración de variables que son listas
vacia = []
frutas = ["naranja", "limón", "pomelo", "lima", "mandarina"]
#             0         1         2        3         4           

# Mostrar el contenido de una lista
print(f"Contenido de frutas: {frutas}")

# Mostrar el valor del elemento en la posición 2 (2 = pomelo)
print(f"Posición 2: {frutas[2]}")

# Mostrar el número de elementos que contiene la lista
print(f"Número de elementos: {len(frutas)}")

# Mostrar el número de veces que tenemos un valor en la lista
fruta = "naranja"
n = frutas.count(fruta)
if (n == 1):
    print(f"{fruta} se repite {n} vez")
else:
    print(f"{fruta} se repite {n} veces")

# Modificar el valor de una posición (posición 2, 'pomelo' por 'fresa')
frutas[2] = "fresa"
print(f"Posición 2: {frutas[2]}")

# Añadir nuevos valores a la lista utilizando APPEND
frutas.append("manzana")
frutas.append("melon")
print(f"Contenido de frutas: {frutas}")

# Añadir un nuevo valor en una posición utilizando INSERT(index, value)
# Añadir sandia en la posición 1
frutas.insert(1, "sandia")
print(f"Contenido de frutas: {frutas}")

# Añadir varios elementos utilizando EXTEND(list)
nuevasFrutas = ["maracuya", "kiwi", "frambuesa"]
frutas.extend(nuevasFrutas)                         # Equivalente a frutas += nuevasFrutas
print(f"Contenido de frutas: {frutas}")


frutas.extend(["platano", "pera"])
print(f"Contenido de frutas: {frutas}")             # Equivalente a frutas += ["platano", "pera"]

# Añadir un elemento si no existe
print(f"Melocotón existe en FRUTAS: {("melocoton" in frutas)}")
print(f"Melocotón no existe en FRUTAS: {("melocoton" not in frutas)}")

if("melocoton" not in frutas):
    frutas.append("melocoton")
print(f"Contenido de frutas: {frutas}")

# Eliminar un elemento indicando su posición (posición 5, mandarina)
frutas.pop(5)
print(f"Contenido de frutas: {frutas}")

frutas.append("naranja")
print(f"Contenido de frutas: {frutas}")

# Eliminar un elemento indicando el valor
# En el caso de varios elementos con el mismo valor elimina únicamente la primera coincidencia
frutas.remove("naranja")
print(f"Contenido de frutas: {frutas}")

# Para evitar errores podemos preguntar por la existencia de un valor antes de eliminarlo
if("uva" in frutas):
    frutas.remove("uva")
    print("Uva eliminada")
else:
    print("No hay 'uva' en la lista, no se borra nada.\n")

# Invertir el orden de los valores utilizando REVERSE
frutas.reverse()
print(f"Contenido de frutas: {frutas}")

# Ordenar los elementos de la lista por orden alfabético
frutas.sort()
print(f"Contenido de frutas: {frutas}")

frutas.sort(reverse=True)
print(f"Contenido de frutas: {frutas}")

# Recorremos la lista mostrando sus valores
for fruta in frutas:
    print(f"{fruta}\n")

for index in range(len(frutas)):
    print(f"{index}# {frutas[index]}\n")

for index, value in enumerate(frutas):
    print(f"{index}# {value}\n")

# Copiar una lista
vacia = frutas.copy()
print(f"Contenido de vacia: {vacia}")

# Eliminar todos los elementos de una lista
frutas.clear()
print(f"Contenido de frutas: {frutas}")