#################################################
# Trabajando y formateando cadenas de texto     #
#################################################


# Declaración de variables
texto = "   hola mundo !!!   "
#        01234567890123456789
print(texto)

# Mostrar determinados caracteres de la cadena
# indicando su posición o un rango

print(f"Posición 3: {texto[3]}")
print(f"Desde la posición 3 incluida: {texto[3:]}")
print(f"Hasta la posición 6 no incluida: {texto[:6]}")
print(f"Desde la posición 2 incluida hasta la 6 no incluida: {texto[2:6]}")
print(f"Los 4 primeros caractéres empezando por la derecha: {texto[-5]}")


# Funciones que podemos utilizar con cadenas de texto

print(f"Número de caracteres: {len(texto)}")
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title())
print(texto.strip())
print(texto.strip().capitalize())
print(texto.count("o"))
print(f"Es un dígito: {texto.isdigit()}")
print(f"Es un dígito: {"57".isdigit()}\n")


# Formatear texto y números

mensaje = "Mundo"

print("Hola " + mensaje + " !!!")
print("Hola {} !!!".format(mensaje))
print("Hola {s} !!!".format(s=mensaje))
print(f"Hola {mensaje} !!!")

resultado = 10/3
print("Resultado: " + str(resultado))
print("Resultado:", str(resultado))
print("Resultado:", resultado)

print(f"Resultado: {resultado}")
print(f"Resultado: {resultado:1.2f}")

print("Resultado: {r}".format(r=resultado))
print("Resultado: {r:1.2f}".format(r=resultado))