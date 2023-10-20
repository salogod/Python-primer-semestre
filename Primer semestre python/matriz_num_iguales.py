def crear_matriz(n, m):
    if n < 2 or m < 2:
        return "Error"

    matriz = []
    numero = 1

    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(numero)
        matriz.append(fila)
        numero+=1;

    return matriz

try: 
    n = int(input("Ingrese el número de renglones (n): "))
    m = int(input("Ingrese el número de columnas (m): "))
    
    resultado = crear_matriz(n, m)
    
    if resultado == "Error":
        print("Error")
    else:
        for fila in resultado:
            print(fila)
except ValueError:
    print("Error")







