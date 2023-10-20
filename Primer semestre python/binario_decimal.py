def binario_a_decimal(numero_binario):

    resultado_decimal = 0

    for i in range(len(numero_binario) - 1, -1, -1):

        if numero_binario[i] not in ('0', '1'):

            return -1

        if numero_binario[i] == '1':

            resultado_decimal += 2 ** (len(numero_binario) - 1 - i)

    return resultado_decimal

def main():

    numero_binario = input("Ingresa un número binario: ")

    resultado_decimal = binario_a_decimal(numero_binario)

    if resultado_decimal == -1:
        print("Entrada inválida. El número binario debe contener solo '0' y '1'.")
    else:
 
        print("El número decimal equivalente es:", resultado_decimal)

if __name__ == "__main__":
    main()
