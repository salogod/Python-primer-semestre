def convertir_decimal(cadena):
    codigos_ascii = [ord(caracter) for caracter in cadena]
    print(codigos_ascii)

def obtener_cadena_desde_codigos_ascii(lista_codigos):
    cadena = ""
    for codigo in lista_codigos:
        caracter = chr(int(codigo))
        cadena += caracter
    return cadena

opcion = input("Ingrese '1' para convertir cadena a códigos ASCII o '2' para convertir códigos a cadena: ")

if opcion == '1':
    cadena = input("Ingrese una palabra y te mostraré sus códigos ASCII separados por comas: ")
    convertir_decimal(cadena)
elif opcion == '2':
    lista_codigos = input("Ingrese los códigos ASCII separados por comas: ").split(',')
    cadena = obtener_cadena_desde_codigos_ascii(lista_codigos)
    print(cadena)
else:
    print("Opción no válida.")
