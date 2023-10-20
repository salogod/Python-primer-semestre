def contar_pares_en_renglones(matriz):
    cantidades_pares = []
    for fila in matriz:
        pares = 0
        for numero in fila:
            if numero % 2 == 0:
                pares += 1
        cantidades_pares.append(pares)
    return cantidades_pares

def main():
    # Leer el número de renglones y columnas de la matriz
    num_renglones = int(input("Ingrese el número de renglones: "))
    num_columnas = int(input("Ingrese el número de columnas: "))

    # Leer los datos de la matriz
    matriz = []
    for i in range(num_renglones):
        fila = []
        for j in range(num_columnas):
            valor = int(input(f"Ingrese el valor de la casilla ({i+1}, {j+1}): "))
            fila.append(valor)
        matriz.append(fila)

    # Llamar a la función para contar pares en renglones
    cantidades_pares = contar_pares_en_renglones(matriz)

    # Mostrar la lista de cantidades de pares en cada renglón
    print("Cantidad de números pares en cada renglón:")
    for i, cantidad in enumerate(cantidades_pares):
        print(f"Renglón {i+1}: {cantidad} números pares")

if __name__ == "__main__":
    main()
