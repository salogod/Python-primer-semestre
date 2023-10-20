import random

def generar_matriz_aleatoria(filas, columnas):
    matriz = []
    for _ in range(filas):
        fila = [random.randint(0, 9) for _ in range(columnas)]  
        matriz.append(fila)
    return matriz

def imprimir_matriz_tabular(matriz):
    for fila in matriz:
        print(' '.join(map(str, fila)))

def imprimir_matriz_transpuesta(matriz):
    for columna in range(len(matriz[0])):
        fila_transpuesta = [matriz[fila][columna] for fila in range(len(matriz))]
        print(' '.join(map(str, fila_transpuesta)))

matriz_aleatoria = generar_matriz_aleatoria(5, 5)

print("Matriz Original:")
imprimir_matriz_tabular(matriz_aleatoria)


print("\nMatriz Transpuesta:")
imprimir_matriz_transpuesta(matriz_aleatoria)
