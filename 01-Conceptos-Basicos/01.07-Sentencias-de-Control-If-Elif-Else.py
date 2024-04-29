#################################################
# Sentencias de Control - If / Elif / Else      #
#################################################

# Declaración de variables
a = 200
b = 33

# Ejemplo 1, IF/ELIF/ELSE
print("Inicio del programa ==========")

if (b > a):
    print("'b' es mayor que 'a'")
    print(f"El valor de 'b' es igual a {b}")
elif(a > b):
    print("a es mayor que b")
    print(f"El valor de 'a' es igual a {a}")
else:
    print("'a' es igual a 'b'")

print("Fin del programa  ============")

# Ejemplo 2, IF/ELIF
print("Inicio del programa ==========")

if (b > a):
    print("'b' es mayor que 'a'")
    print(f"El valor de 'b' es igual a {b}")
elif(a > b):
    print("a es mayor que b")
    print(f"El valor de 'a' es igual a {a}")
elif(a == b):
    print("'a' es igual a 'b'")

print("Fin del programa  ============")

# Ejemplo 3, IF/ELSE/IF/ELSE
print("Inicio del programa ==========")

if (b > a):
    print("'b' es mayor que 'a'")
    print(f"El valor de 'b' es igual a {b}")
else:
    if (a > b):
        print("a es mayor que b")
        print(f"El valor de 'a' es igual a {a}")
    else:
        print("'a' es igual a 'b'")

print("Fin del programa  ============")