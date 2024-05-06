###################################################
# Declaración de Funciones Lambda                 #
###################################################

from functools import reduce

numeros = [1, 85, 200, 15, 152, 450, 5, 3061, 63, 77, 8]

# Escribe una función que retorne una lista con los números mayores de 100
def MayordeCien(lista):
    resultado = []

    for numero in lista:
        if numero > 100:
            resultado.append(numero)

    return resultado

print(f"Función Estándar: {MayordeCien(numeros)}")


# Escribe una función que returne TRU cuando un número es mayor de 100, si 
# no, retorn FALSE

def NumMayorCien(numero):
    if numero > 100:
        return True
    else:
        return False

# Utilizando Filter con una función estándar 
print(f"FILTER + función estándar: {list(filter(NumMayorCien, numeros))}")


# Extraer números mayores de 100 utilizando FILTER y LAMBDA
print(f"Números mayores de 100: {list(filter(lambda numero: numero > 100, numeros))}")

# Extraer números menores de 50 utilizando FILTER y LAMBDA
print(f"Números menores de 50: {list(filter(lambda x: x < 50, numeros))}")

# Extraer números pares utilizando FILTER y LAMBDA
print(f"Numeros pares: {list(filter(lambda x: x % 2 == 0, numeros))}")


# Utilizamos MAP y LAMBDA
print(f"Datos: {numeros}")
print(f"Resultado de sumar 10 y dividir entre 2: {list(map(lambda x: (x + 10) / 2, numeros))}")

# Ejemplo de REDUCE con una suma
print(f"Resultado SUM: {sum(numeros)}")
print(f"Resultado: {reduce(lambda x, y: x + y, numeros)}")

print(f"Datos: {numeros}")
print(f"Pares: {list(map(lambda x: x % 2 == 0, numeros))}")

print(f"Algun número par? {any(map(lambda x: x % 2 == 0, numeros))}")
print(f"Todos son pares? {all(map(lambda x: x % 2 == 0, numeros))}")