import math

def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def determinar_posicion(radio, x1, y1, x2, y2):
    distancia = calcular_distancia(x1, y1, x2, y2)

    if distancia == radio:
        return "SOBRE"
    elif distancia < radio:
        return "DENTRO"
    else:
        return "FUERA"

radio = float(input("Ingrese el radio de la circunferencia: "))
x1 = float(input("Ingrese la coordenada x del centro de la circunferencia: "))
y1 = float(input("Ingrese la coordenada y del centro de la circunferencia: "))
x2 = float(input("Ingrese la coordenada x del punto: "))
y2 = float(input("Ingrese la coordenada y del punto: "))

posicion = determinar_posicion(radio, x1, y1, x2, y2)

print("El punto está", posicion, "de la circunferencia.")
