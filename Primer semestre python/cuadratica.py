import math

def calcular_ecuacion_cuadratica(a, b, c):
    if a == 0 and b == 0:
        return "No tiene solución"
    elif a == 0:
        x = -c / b
        return x
    elif a != 0 and b != 0:
        discriminante = b ** 2 - 4 * a * c
        if discriminante < 0:
            return "Raices complejas"
        elif discriminante > 0:
            x1 = (-b + math.sqrt(discriminante)) / (2 * a)
            x2 = (-b - math.sqrt(discriminante)) / (2 * a)
            return x1, x2
        else:
            x = -b / (2 * a)
            return x

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

resultados = calcular_ecuacion_cuadratica(a, b, c)

if isinstance(resultados, tuple):
    for x in resultados:
        print(x)
else:
    print(resultados)
