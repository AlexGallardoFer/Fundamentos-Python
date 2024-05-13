#######################################################################
# Escribe un programa que adivine un número
#
# Requerimientos:
#
#   -> Se calcula un número de forma aleatoria entre 1 y 100
#   -> Pregunta el número hasta que el usuario lo adivine
#   -> Cuando el usuario no acierta hay que mostrar un mensaje
#      de más o menos y cuando este a menos de 10 números hay que
#      mostrar el mensaje 'caliente caliente'
#
#######################################################################
import random

try:
    # Generar un número aleatorio entre 1 y 100
    numero_aleatorio = random.randint(1, 100)
    numero = 0
    acertado = False
    while acertado == False:
        while True:
            numero = input("Dime un número del 1 al 100")
            if numero.isdigit() and int(numero) <= 100 and int(numero) >= 1:
                break
        
        diferencia = numero_aleatorio-int(numero)

        if diferencia == 0:
            print(f"Has acertado!! El número era: {numero_aleatorio}")
            acertado = True    
        else:
            if abs(diferencia) < 10:
                print("Caliente caliente...")
            if int(numero) > numero_aleatorio:
                print(f"El número que estoy pensando es menor que {numero}")
            else:
                print(f"El número que estoy pensando es mayor que {numero}")

except Exception as err:
    print(err)