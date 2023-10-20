
def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def encontrar_primos_en_rango(primer_numero, segundo_numero):
    numeros_primos = []
    for numero in range(primer_numero, segundo_numero + 1):
        if es_primo(numero):
            numeros_primos.append(numero)
    return numeros_primos

def obtener_primer_numero():
    return int(input("Ingrese el primer número: "))


def obtener_segundo_numero(primer_numero):
    while True:
        segundo_numero = int(input("Ingrese el segundo número (debe ser mayor que el primero): "))
        if segundo_numero > primer_numero:
            return segundo_numero
        else:
            print("El segundo número debe ser mayor que el primero. Intente de nuevo.")


def main():
    primer_numero = obtener_primer_numero()
    segundo_numero = obtener_segundo_numero(primer_numero)
    
    numeros_primos = encontrar_primos_en_rango(primer_numero, segundo_numero)
    
    print("Números primos entre {} y {}:".format(primer_numero, segundo_numero))
    for numero in numeros_primos:
        print(numero)
    
    print("Cantidad de números primos encontrados:", len(numeros_primos))

if __name__ == "__main__":
    main()
