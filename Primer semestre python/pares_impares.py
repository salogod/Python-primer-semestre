
def contar_pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

lista = []

while True:
    numero = int(input("Ingrese un número entero (negativo para terminar): "))
    if numero < 0:
        break
    lista.append(numero)

pares, impares = contar_pares_impares(lista)

print(f"PARES={pares}")
print(f"IMPARES={impares}")
