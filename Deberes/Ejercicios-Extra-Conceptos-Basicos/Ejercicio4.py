#######################################################################
# Escribe un programa que cuente vocales
#
# Requerimientos:
#
#   -> Pregunta una frase al usuario
#   -> Cuenta el número de cada vocal tanto en mayúsculas como en
#      minúsculas
#
#######################################################################
try:
    vocalesMayus = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
    vocalesMinus = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    frase = input("Introduzca una frase: ")

    for letra in frase:
        if letra in vocalesMayus:
            vocalesMayus[letra] += 1
        elif letra in vocalesMinus:
            vocalesMinus[letra] += 1
    
    for vocal in vocalesMinus:
        print(f"La vocal {vocal} aparece {vocalesMinus[vocal]} veces en la frase")

    print("")
    
    for vocal in vocalesMayus:
        print(f"La vocal {vocal} aparece {vocalesMayus[vocal]} veces en la frase")

except Exception as err:
    print(err)