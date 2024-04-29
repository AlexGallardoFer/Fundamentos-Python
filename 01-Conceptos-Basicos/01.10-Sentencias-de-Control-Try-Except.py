###################################################
# Sentencias de Control - Try/Except/Else/Finally #
###################################################

# Importación de Módulos
import sys

# Declaración de variables
numero1 = 0
numero2 = 100

try:
    print("Nivel 1")
    print("Inicio Nivel 2")

    try:
        print("Nivel 2")
        print(100/0)

    except Exception as err:
        raise
        print(f"Nivel 2: {err}")

    finally:
        print("Fin Nivel 2")

except Exception as err:
    print(f"Nivel 1: {err}")


# Ejemplo 1
print("Inicio del programa.\n")
try:
    numero3 = numero2 / numero1
    print(f"Valor del número 3: {numero3}")
except ZeroDivisionError:
    print("Error, no se puede dividir entre cero.")
except:
    print("Upss Error !!!")
else:
    print("El bloque ELSE se ejecuta cuando el TRY finaliza correctamente.")
finally:
    print("El bloque FINALLY se ejecuta cuando el TRY o EXCEPT finalizan.")

print("\nFin del programa.\n")


# Ejemplo 2
print("============================================")
numero1 = 5

try:
    numero3 = numero2 / numero1
    print(f"Valor del número 3: {numero3}")
    f = open("miFichero.txt")

except ZeroDivisionError as err:
    print(f"-> {err}")
    print(f"-> {type(err)}")

except FileNotFoundError as err:
    print(f"-> {err}")
    print(f"-> {type(err)}")

except Exception as err:
    print(f"{err}")
    print(f"{type(err)}")

finally:
    print("F I N\n")


#Ejemplo 3
print("============================================")
numero = "32"

try:
    if(type(numero) is not int):
        raise Exception("La variable NUMERO no es un INT")
except Exception as e:
    print(f"-> {e}")
    print(f"-> {type(e)}")
