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

def mostrar_lista(lista):
    for i, elemento in enumerate(lista):
        print(f"lista[{i}] = {elemento}")

n = pedir_numero_positivo()

lista = leer_lista(n)

mostrar_lista(lista)


