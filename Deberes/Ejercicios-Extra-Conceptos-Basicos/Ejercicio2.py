#######################################################################
# Escribe un programa que sume los números pares
#
# Requerimientos:
#
#   -> Pregunta 10 veces un número al usuario
#   -> Al finalizar muestra la suma de los números pares
#
#######################################################################
try:
    total = 0
    for index in range(1,11):
        while True:
            numero = input(f"Introduzca el número {index}/10: ")
            if numero.isdigit():
                break
        if int(numero) % 2 == 0:
            total += int(numero)

    print(f"La suma de todos los números pares es de {total}.")
    
except Exception as err:
    print(err)