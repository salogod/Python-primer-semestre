def calcular_distancia_recorrida(minutos):
    velocidad_caracol = 5.7  # mm/s
    minutos_a_segundos = minutos * 60
    distancia_cm = (velocidad_caracol * minutos_a_segundos) / 10  # Convertir mm a cm
    
    return distancia_cm


minutos = float(input("Ingrese la cantidad de minutos: "))
        
distancia_recorrida = calcular_distancia_recorrida(minutos)
print(f"Distancia recorrida: {distancia_recorrida:.2f} centímetros")

