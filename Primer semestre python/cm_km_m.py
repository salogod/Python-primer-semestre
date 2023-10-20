def convertir_distancia(distancia_cm):
    km = distancia_cm // 100000
    distancia_cm %= 100000
    m = distancia_cm // 100
    cm = distancia_cm % 100

    resultados = []
    if km > 0:
        resultados.append(f"{km} km")
    if m > 0:
        resultados.append(f"{m} m")
    if cm > 0:
        resultados.append(f"{cm} cm")

    return resultados

distancia_cm = int(input("Ingrese una distancia en centímetros: "))

resultados = convertir_distancia(distancia_cm)

for resultado in resultados:
    print(resultado)
