import math

print("MINISTERIO DE EDUCACION")
print("COLEGIO INSTITUTO DAVID")
print()
print("PROGRAMA QUE EJECUTA LAS FUNCIONES DE UNA CALCULADORA")
print()

continuacion = "SI"

# Se establece el mensaje y la lectura que se dará al inicio del programa


def inicializacion():
    print("OPERACIONES")
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACION")
    print("4. DIVISION")
    print("5. POTENCIACION")
    print("6. RADICACION")
    print("7. LOGARITMO NEPERIANO")
    print("8. LOGARITMO")
    print("9. SENO")
    print("10. COSENO")
    print("11. TANGENTE")

    operacion = int(input("Qué tipo de operación desea realizar?: "))
    return operacion

# Se definen las funciones relacionadas al efecto matemático de cada operación


def suma(x, y):
    resultado = x + y
    return resultado


def resta(x, y):
    resultado = x - y
    return resultado


def multiplicacion(x, y):
    resultado = x * y
    return resultado


def division(x, y):
    resultado = x / y
    return resultado


def potenciacion(x, y):
    resultado = x ** y
    return resultado


def radicacion(x, y):
    resultado = x ** (1/y)
    return resultado


def log(x, y):
    resultado = math.log(x, y)
    return resultado


def ln(x):
    resultado = math.log(x)
    return resultado


def seno(x):
    resultado = math.sin(x)
    return resultado


def coseno(x):
    resultado = math.cos(x)
    return resultado


def tangente(x):
    resultado = math.tan(x)
    return resultado

# Definir la función para leer


def leer(operacion):
    x = 0
    y = 0
    if operacion == 1 or operacion == 2 or operacion == 3 or operacion == 4:
        x = float(input("Introduzca el primer valor a operar: "))
        y = float(input("Introduzca el segundo valor a operar: "))

    elif operacion == 5:
        x = float(input("Introduzca la base: "))
        y = float(input("Introduzca el exponente: "))

    elif operacion == 6:
        x = float(input("Introduzca el subradical: "))
        y = float(input("Introduzca el indice: "))

    elif operacion == 7:
        x = float(input("Introduzca el argumento: "))
        y = float(input("Introduzca la base: "))

    elif operacion == 8:
        x = float(input("Introduzca el argumento: "))

    elif operacion == 9 or operacion == 10 or operacion == 11:
        x = float(input("Introduzca el ángulo: "))
    return(x, y)

# Ahora a establecer la última función que va a decidir que operación realizar

def decision_operativa(operacion):
    if operacion == 1:
        final = suma(x,y)
    elif operacion == 2:
        final = resta(x,y)
    elif operacion == 3:
        final = multiplicacion(x,y)
    elif operacion == 4:
        final = division(x,y)
    elif operacion == 5:
        final = potenciacion(x,y)
    elif operacion == 6:
        final = radicacion(x, y)
    elif operacion == 7:
        final = log(x,y)
    elif operacion == 8:
        final = ln(x)
    elif operacion == 9:
        final = seno(x)
    elif operacion == 10:
        final = coseno(x)
    elif operacion == 11:
        final = tangente(x)
    return final

while continuacion == "SI":
    operacion = inicializacion()
    valores = []
    valores = leer(operacion)
    x = valores[0]
    y = valores[1]
    valores_op = []
    valor_operado = decision_operativa(operacion)
    print(valor_operado)
    continuacion = str(input("Desea realizar otra operacion?SI/NO: "))

