def calcular_costo_mensual(mensajes, megas, minutos):
    costo_por_mensaje = 0.80
    costo_por_mega = 0.80
    costo_por_minuto = 0.80
    
    costo_total = (mensajes * costo_por_mensaje) + (megas * costo_por_mega) + (minutos * costo_por_minuto)
    
    return costo_total


mensajes = int(input("Ingrese el número de mensajes: "))
megas = float(input("Ingrese el número de megas: "))
minutos = int(input("Ingrese el número de minutos: "))
        
costo_total = calcular_costo_mensual(mensajes, megas, minutos)
print(f"El costo mensual total es: ${costo_total:.2f}")

