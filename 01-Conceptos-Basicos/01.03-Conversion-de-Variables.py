#################################################
# Conversión de Variables                       #
#################################################


# Declaración de variables
a = 5.3
b = "25"
c = "25.7"
d = "a 8.4"

# Conversión de números a texto con STR
print("El valor de a es: " + str(a))
print("El valor de b es: " + b + "\n")

# Conversión de texto a números con INT y FLOAT
print(f"Valor de b: {b}")
print(type(b))
print(f"Valor de b: {int(b)}")
print(type(int(b)))

print(f"Suma: {b + c} <-- El resultado es una concatenación del texto")
print(type(b + c))
print(f"Suma: {int(b) + float(c)}")
print(type(int(b) + float(c)))

print(f"Número: {d} <-- No se puede convertir a Float por contener una a")