def calcular_conversion(unidad, valor):
    if unidad == 'Y':
        nuevo_valor = yardas_centimetros(valor)
    elif unidad == 'P':
        nuevo_valor = pulgadas_centimetros(valor)
    elif unidad == "F":
        nuevo_valor = pies_centimetros(valor)

    return nuevo_valor, 'cm'

def pulgadas_centimetros(valor):
    nuevo_valor = valor * 2.54
    return nuevo_valor

def pies_centimetros(valor):
    nuevo_valor = valor * 30.48
    return nuevo_valor

def yardas_centimetros(valor):
    nuevo_valor = valor * 91.44
    return nuevo_valor

def verificar(valor, unidad):
    if (unidad in ["Y", "P", "F"]) and valor > 0:
        return True
    else:
        return False

def main():
    unidad = input("Tipo de unidad introducida (Y - yardas, P - pulgadas, F - pies): ")
    valor = float(input("Valor a convertir a cm: "))
    
    if verificar(valor, unidad):
        nuevo_valor, nueva_unidad = calcular_conversion(unidad, valor)
        print(f"La conversión es igual a: {nuevo_valor:.2f} {nueva_unidad}")
    else:
        print("Valores de entrada no válidos. Asegúrese de ingresar valores correctos.")

if __name__ == "__main__":
    main()
