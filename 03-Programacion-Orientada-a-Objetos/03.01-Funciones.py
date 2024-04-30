###################################################
# Funciones                                       #
###################################################

from datetime import datetime

# Ejemplo de función que NO recibe datos (NO tiene parámetros) y NO retorna datos
def Func1():
    """Func1, no tiene parámetros y no retorna datos"""
    print("Hola Mundo !!!")

# Ejemplo de función que SI recibe datos (SI tiene parámetros) y NO retorna datos
def Func2(nombre, numero):
    """Func2 tiene 2 parámetros y no retorna datos"""
    print(f"Me llamo {nombre} y mi número de la suerte es {numero}")

# Ejemplo de función que SI recibe datos (SI tiene parámetros) y SI retorna datos
def Func3(frase):
    cantidad = len(frase)
    return cantidad

# Ejemplo de función que SI recibe datos (NO tiene parámetros) y SI retorna datos
def Func4():
    return datetime.now().date().strftime("%A")

Func1()
Func2("Alejandro", 7)
print(f"La longitud del texto es de {Func3("En un lugar de la mancha de cuyo nombre ...")} caracteres")
print(f"Hoy es {Func4()}\n")

#################################################################################

# Asignación de valores a los parámetros
def Resta1(a, b):                               # Todos los parámetros son obligatorios
    return a - b

print(f"1) 85 - 10 = {Resta1(85, 10)}")         # Asignación por posición
print(f"1) 85 - 10 = {Resta1(a=85, b=10)}")     # Asignación por nombre
print(f"1) 85 - 10 = {Resta1(b=10, a=85)}\n")   # Asignación por nombre


def Resta2(a, b=10):                            # Solo el parámetro 'a' es obligatorio
    return a - b

print(f"2) 85 - 10 = {Resta2(85, 10)}")         # Asignación por posición
print(f"2) 85 - 10 = {Resta2(a=85, b=10)}")     # Asignación por nombre
print(f"2) 85 - 10 = {Resta2(b=10, a=85)}")     # Asignación por nombre

print(f"2) 85 - 10 = {Resta2(85)}")             # Asignación por posición
print(f"2) 85 - 10 = {Resta2(a=85)}\n")         # Asignación por nombre


def Resta3(a=85, b=10):                         # Todos los parámetros son opcionales
    return a - b

print(f"3) 85 - 10 = {Resta3(85, 10)}")         # Asignación por posición
print(f"3) 85 - 10 = {Resta3(a=85, b=10)}")     # Asignación por nombre
print(f"3) 85 - 10 = {Resta3(b=10, a=85)}")     # Asignación por nombre

print(f"3) 85 - 10 = {Resta3(85)}")             # Asignación por posición
print(f"3) 85 - 10 = {Resta3(a=85)}")           # Asignación por nombre
print(f"3) 85 - 10 = {Resta3(b=10)}")           # Asignación por nombre

print(f"3) 85 - 10 = {Resta3()}\n")             # Sin valores para los parámetros