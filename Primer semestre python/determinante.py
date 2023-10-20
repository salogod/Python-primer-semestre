def calcular_determinante(matriz):
    # Asegurémonos de que la matriz sea de tamaño 2x2
    if len(matriz) != 2 or len(matriz[0]) != 2 or len(matriz[1]) != 2:
        raise ValueError("La matriz debe ser de tamaño 2x2")

    # Extraer los elementos de la matriz
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[1][0]
    d = matriz[1][1]

    # Calcular el determinante
    determinante = a * d - c * b

    return determinante

# Ejemplo de uso
matriz_ejemplo = [[3, 4], [1, 2]]
resultado = calcular_determinante(matriz_ejemplo)
print("El determinante de la matriz es:", resultado)
