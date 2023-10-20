def tres_en_tres(primer_valor , segundo_valor):
    if segundo_valor > primer_valor:
        for numero in range(primer_valor, segundo_valor + 1, 3):
            print(numero)

primer_valor= int(input("Ingresa un numero "))
segundo_valor= int(input("Ingresa otro numero "))

tres_en_tres(primer_valor,segundo_valor)
