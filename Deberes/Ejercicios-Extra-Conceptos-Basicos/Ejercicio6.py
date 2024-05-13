#######################################################################
# Escribe un programa que sume los digitos de un número
#
# Requerimientos:
#
#   -> Pregunta el número al usuario
#   -> Muestra el resultado de la suma
#  
# Si el usurio indica el número 159 tenemos que calcular la suma de
# los números 1 + 5 + 9
#
#######################################################################
try:
    while True:
        numero = input("Introduce un número: ")
        if numero.isdigit():
            break
    total = 0
    for digito in numero:
        total += int(digito)
    
    print(f"La suma de los números {' + '.join(numero)} es: {total}")
    
except Exception as err:
    print(err)