def comparar_fechas(dia1, mes1, dia2, mes2):
    if mes1 < mes2:
        return "La fecha 1 ocurre primero"
    elif mes1 > mes2:
        return "La fecha 2 ocurre primero"
    else:
        if dia1 < dia2:
            return "La fecha 1 ocurre primero"
        elif dia1 > dia2:
            return "La fecha 2 ocurre primero"
        else:
            return "Las fechas son iguales"

dia1 = int(input("Ingrese el día de la fecha 1: "))
mes1 = int(input("Ingrese el mes de la fecha 1: "))
dia2 = int(input("Ingrese el día de la fecha 2: "))
mes2 = int(input("Ingrese el mes de la fecha 2: "))

resultado = comparar_fechas(dia1, mes1, dia2, mes2)

print(resultado)
