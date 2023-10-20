import random
import sys

# Declaración de variables
x = 0
y = 0
x2 = 0
y2 = 0
p1 = 0
p2 = 0
matrix = [['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-']]
# `matrix` es el tablero de juego, inicializado con guiones ("-").

matrix2 = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]]
# `matrix2` contiene los valores que estarán en el tablero (las parejas de cartas).

guion = '-'
variable = 5

# Función para el jugador 1
def memorama():
    imprimir()
    print('Jugador 1')

    # Solicita al jugador las coordenadas de la primera carta
    x = int(input('Ingresa un valor en la horizontal: '))
    if x > 5:
        print('ERROR')
        memorama()

    y = int(input('Ingresa un valor en la vertical: '))
    if y > 5:
        print('ERROR')
        memorama()

    matrix[x][y] = matrix2[x][y]

    imprimir()

    # Solicita al jugador las coordenadas de la segunda carta
    x2 = int(input('Ingresa un valor en la horizontal: '))
    if x2 > 5:
        print('ERROR')
        matrix[x][y] = '-'
        memorama()
    else:
        y2 = int(input('Ingresa un valor en la vertical: '))
        if y2 > 5:
            print('ERROR')
            matrix[x][y] = '-'
            memorama()

    matrix[x2][y2] = matrix2[x2][y2]

    condiciones(x,y,x2,y2)

    imprimir()

# Función para el jugador 2
def memorama2():
    imprimir()
    print('Jugador 2')

    # Solicita al jugador las coordenadas de la primera carta
    x = int(input('Ingresa un valor en la horizontal: '))
    if x > 5:
        print('ERROR')
        memorama2()

    y = int(input('Ingresa un valor en la vertical: '))
    if y > 5:
        print('ERROR')
        memorama2()

    matrix[x][y] = matrix2[x][y]

    imprimir()

    # Solicita al jugador las coordenadas de la segunda carta
    x2 = int(input('Ingresa un valor en la horizontal: '))
    if x2 > 5:
        print('ERROR')
        matrix[x][y] = '-'
        memorama2()
    else:
        y2 = int(input('Ingresa un valor en la vertical: '))
        if y2 > 5:
            print('ERROR')
            matrix[x][y] = '-'
            memorama2()

    matrix[x2][y2] = matrix2[x2][y2]

    condiciones2(x,y,x2,y2)

    imprimir()

# Función para verificar si las cartas coinciden para el jugador 1
def condiciones(x,y,x2,y2):
    global p1
    if matrix[x][y] != matrix[x2][y2]:
        matrix[x2][y2] = "-"
        matrix[x][y] = "-"
        respuesta = str(input('¿Quiere seguir jugando? s/n: '))
        if respuesta == 's':
            memorama2()
        elif respuesta == 'n':
            print('El jugador tiene',p1,'pares')
            print('El jugador tiene',p2,'pares')
            if p1 > p2:
                print('El ganador fue el jugador 1')
            elif p2 > p1:
                print('El ganador fue el jugador 2')
            elif p2 == p1:
                print('Fue un empate!')
            elif p1 == p2:
                print('Fue un empate!')
            sys.exit()    
    else:
        p1 += 1 
        memorama()

# Función para verificar si las cartas coinciden para el jugador 2
def condiciones2(x,y,x2,y2):
    global p2
    if matrix[x][y] != matrix[x2][y2]:
        matrix[x2][y2] = "-"
        matrix[x][y] = "-"
        respuesta = str(input('¿Quiere seguir jugando? s/n: '))
        if respuesta == 's':
            memorama()
        elif respuesta == 'n':
            print(p1)
            print(p2)
            if p1 > p2:
                print('El jugador tiene',p1,'pares')
            elif p2 > p1:
                print('El jugador tiene',p2,'pares')
            elif p2 == p1:
                print('Fue un empate!')
            elif p1 == p2:
                print('Fue un empate!')
            sys.exit()

# Función para imprimir el tablero
def imprimir():
    contador = 0
    print('  0 1 2 3 4 5 \n')

    for i in range(6):
        print(contador, '', end = '')
        contador += 1
        for j in range(6):
            print((matrix[i][j]),'', end = '')

        print('\n')

# Función principal
def main():
    while variable == 5:
        random.shuffle(matrix2)
        for i in matrix2:
            random.shuffle(i)
        memorama()

# Inicia el juego
main()
