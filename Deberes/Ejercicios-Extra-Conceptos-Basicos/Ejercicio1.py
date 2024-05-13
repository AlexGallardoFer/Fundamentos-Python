#######################################################################
# Escribe un programa que calcule la velocidad en km/h
#
# Requerimientos:
#
#   -> La información la tenemos en metros y minutos
#   -> Mostrar la velocidad en km/h y un comentario indicando si es 
#      alta, baja o moderada
#   -> Alta por encima de 75km/h; 
#      Baja por debajo de 30km/h; 
#      el resto moderada
#
#######################################################################
try:
    while True:
        metros = input("Introduzca la distancia recorrida en metros: ")
        if metros.isdigit():
            break

    while True:
        minutos = input("Introduzca el tiempo tardado en minutos: ")
        if minutos.isdigit():
            break

    km = int(metros) / 1000
    h = int(minutos) / 60
    velocidad = km/h
    vel = ""

    if velocidad <= 75 and velocidad >= 30:
        vel = "moderada"
    elif velocidad > 75:
        vel = "alta"
    else:
        vel = "baja"

    print(f"Usted ha ido a una velocidad {vel} media de: {velocidad:1.2f} km/h.")

except Exception as err:
    print(err)