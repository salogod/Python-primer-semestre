def determinar_cuadrante(grados):
    if grados < 0 or grados > 360:
        return "excede"
    elif grados == 0 or grados == 180 or grados == 360:
        return "eje"
    elif grados > 0 and grados < 90:
        return "Cuadrante 1"
    elif grados == 90:
        return "eje"
    elif grados > 90 and grados < 180:
        return "Cuadrante 2"
    elif grados > 180 and grados < 270:
        return "Cuadrante 3"
    else:
        return "Cuadrante 4"


grados = int(input("Ingrese el número de grados (entre 0 y 360): "))

resultado = determinar_cuadrante(grados)

print(resultado)
