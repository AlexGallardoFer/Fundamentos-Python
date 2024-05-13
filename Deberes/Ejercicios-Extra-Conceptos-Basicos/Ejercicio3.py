#######################################################################
# Escribe un programa que sume los números pares
#
# Requerimientos:
#
#   -> Pregunta un número al usuario, puede ser positivo o negativo
#   -> El número introducido por el usuario no puede ser cero
#   -> Muestra la suma de los número pares desde cero al número
#      introducido por el usuario
#
#######################################################################
try:
    while True:
        numero = input("Introduce un número positivo o negativo que no sea el 0: ")
        if numero.lstrip("-").isdigit() and int(numero) != 0:
            break
    
    total = 0
    if int(numero) > 0:
        for index in range(1, int(numero)+1):
            if index % 2 == 0:
                total += index
        
    else:
        for index in range(int(numero), 0):
            if index % 2 == 0:
                total += index
    
    print(f"La suma de todos los números pares entre 0 y {numero} es de {total}.")

except Exception as err:
    print(err)