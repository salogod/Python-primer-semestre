
def pedir_numero_positivo():
    while True:
        n = int(input("Ingrese el número de elementos para la lista: "))
        if n > 0:
            return n
        else:
            print("El número de elementos debe ser mayor que 0.")

def leer_lista(n):
    lista = []
    for i in range(n):
        elemento = int(input(f"Ingrese el elemento {i + 1}: "))
        lista.append(elemento)
    return lista

def calcular_promedio(lista):
    if len(lista) == 0:
        return 0
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

n = pedir_numero_positivo()

lista = leer_lista(n)

promedio = calcular_promedio(lista)

print("Lista:", lista)

print("Promedio:", promedio)
