def calcular_total_compra(juegos_nuevos, juegos_usados):
    precio_juego_nuevo = 60
    precio_juego_usado = 30
    
    total_compra = (juegos_nuevos * precio_juego_nuevo) + (juegos_usados * precio_juego_usado)
    return total_compra

juegos_nuevos = int(input("Ingrese la cantidad de juegos nuevos: "))
juegos_usados = int(input("Ingrese la cantidad de juegos usados: "))
        
total_compra = calcular_total_compra(juegos_nuevos, juegos_usados)
print(f"Total de la compra: ${total_compra:.2f}")



