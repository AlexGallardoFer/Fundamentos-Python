#######################################################################
# Escribe un programa que determine si una frase es un palíndromo
#
# Requerimientos:
#
#   -> Pregunta una frase al usuario
#   -> Responde: La frase SI/NO es un palíndromo
#   
# Los PALÍNDROMOS son palabras o frases que se leen igual de izquierda
# a derecha, que de derecha a izquierda. Por ejemplo:
#
#   Allí ves Sevilla
#   A mí me mima
#
#######################################################################
try:
    frase = input("Introduce una frase para comprobar si es un palíndromo o no")
    frase = frase.replace(" ", "").replace(",", "").replace(".", "").lower()
    longitud = len(frase)
    esPalindromo = True

    for i in range(longitud // 2):
        if frase[i] != frase[longitud - 1 - i]:
            esPalindromo = False

    if esPalindromo:
        print("SI es un palíndromo.")
    else:
        print("NO es un palíndromo")

except Exception as err:
    print(err)