#################################################
# Asignación Simultanea                         #
#################################################

# Declaración de variables
a = 5
b = 10

# Intercambiar los valores entre a y b. Intento 1.
a = b
b = a

print("Intento 1, incorrecto.")
print(f"Variable a: {a}")
print(f"Variable b: {b}\n")

# Intercambiar los valores entre a y b. Intento 2.
a = 5
b = 10

temp = a
a = b
b = temp

print("Intento 2, correcto con una variable temporal.")
print(f"Variable a: {a}")
print(f"Variable b: {b}\n")

# Intercambiar los valores entre a y b. Intento 3.
a = 5
b = 10

a,b = b,a

print("Intento 3, correcto.")
print(f"Variable a: {a}")
print(f"Variable b: {b}")