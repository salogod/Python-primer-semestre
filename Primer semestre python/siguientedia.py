def es_bisiesto(año):
    if año % 4 == 0:
        if año % 100 != 0 or año % 400 == 0:
            return True
    return False

def fecha_siguiente(año, mes, día):
    días_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if es_bisiesto(año):
        días_por_mes[2] = 29

    if día < días_por_mes[mes]:
        día += 1
    else:
        día = 1
        if mes < 12:
            mes += 1
        else:
            mes = 1
            año += 1

    return año, mes, día

año = int(input("Ingrese el año: "))
mes = int(input("Ingrese el mes: "))
día = int(input("Ingrese el día: "))

año_siguiente, mes_siguiente, día_siguiente = fecha_siguiente(año, mes, día)

print("La fecha del día siguiente es:", año_siguiente, mes_siguiente, día_siguiente)
