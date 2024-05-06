###################################################
# Declaración de Funciones Lambda                 #
###################################################

def Saludo(nombre):
    print(f"Hola, me llamo {nombre}.")

miNombre = "Borja"
Saludo(miNombre)

Saludo("Franciso")

# Una función Lambda equivalente a la función Saludo()
demo = lambda nombre: print(f"Hola, me llamo {nombre}.")

print(f"Tipo de demp: {type(demo)}")

miNombre = "Ana María"
demo(miNombre)

demo("Ana")

# Creamos una función Calcular() que recibe como parámetro una función Lambda
# con el calculo que tiene que realizar

def Sumar(num):
    return lambda a: a + num

def Restar(num):
    return lambda a: a - num

def Multiplicar(num):
    return lambda a: a * num

def Dividir(num):
    return lambda a: a / num

def Calcular(formula):
    for n in range(1, 11, 1):
        print(f"Número: {n} --> Resultado de la fórmila: {formula(n)}")