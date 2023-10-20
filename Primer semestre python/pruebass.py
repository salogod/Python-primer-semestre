import random

puntos_jugador1 = 0
puntos_jugador2 = 0
bonus_jugador1 = 0
bonus_jugador2 = 0

tablero = [
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"]
]

cartas = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18]
]

random.shuffle(cartas)

# Barajar los elementos dentro de cada fila
for fila in cartas:
    random.shuffle(fila)

# Imprime el tablero con las cartas
def imprimir_tablero():
    print('  0  1  2  3  4  5 \n')

    for i in range(6):
        print(i, '', end=' ')
        for j in range(6):
            print(tablero[i][j], '', end=' ')
        print('\n')

def turno():
    pares_encontrados = 0
    total_pares = 18  # Esto debe ser la mitad del número total de cartas

    jugar = True

    while pares_encontrados < total_pares and jugar==1:
        imprimir_tablero()
        print("Turno del jugador 1")
        columna1 = int(input("Ingresa la columna de la primera carta: "))
        fila1 = int(input("Ingresa la fila de la primera carta: "))
        carta1 = cartas[fila1][columna1]
        tablero[fila1][columna1] = carta1
        imprimir_tablero()
        print(f"Elegiste el número {carta1}")

        columna2 = int(input("Ingresa la columna de la segunda carta: "))
        fila2 = int(input("Ingresa la fila de la segunda carta: "))
        carta2 = cartas[fila2][columna2]
        tablero[fila2][columna2] = carta2
        imprimir_tablero()
        print(f"Elegiste el número {carta2}")

        if carta1 == carta2:
            print("¡Encontraste una pareja!")
        else:
            print("Las cartas no coinciden. Volviendo a los guiones.")
            tablero[fila1][columna1] = '-'
            tablero[fila2][columna2] = '-'

        if pares_encontrados < total_pares:
            seguir_jugando = input("¿Quieres seguir jugando? (Sí/No): ")
            if seguir_jugando.lower() == "si":
                jugar = 1

        imprimir_tablero()
        print("Turno del jugador 2")
        columna1 = int(input("Ingresa la columna de la primera carta: "))
        fila1 = int(input("Ingresa la fila de la primera carta: "))
        carta1 = cartas[fila1][columna1]
        tablero[fila1][columna1] = carta1
        imprimir_tablero()
        print(f"Elegiste el número {carta1}")

        columna2 = int(input("Ingresa la columna de la segunda carta: "))
        fila2 = int(input("Ingresa la fila de la segunda carta: "))
        carta2 = cartas[fila2][columna2]
        tablero[fila2][columna2] = carta2
        imprimir_tablero()
        print(f"Elegiste el número {carta2}")

        if carta1 == carta2:
            print("¡Encontraste una pareja!")
        else:
            print("Las cartas no coinciden. Volviendo a los guiones.")
            tablero[fila1][columna1] = '-'
            tablero[fila2][columna2] = '-'
            seguir_jugando = input("¿Quieres seguir jugando? (Sí/No): ")
            if seguir_jugando.lower() == "si":
                jugar = 1

    print("¡Juego terminado!")

turno()


