def calcular_precio(silla, cliente, cantidad):
    precios = {'B': 700.00, 'E': 900.00, 'L': 1500.00}
    precio_unitario = precios.get(silla, 0)
    precio_total = precio_unitario * cantidad
    descuento = 0

    if cliente == 'F':
        descuento = precio_total * 0.20
    elif cliente == 'N':
        if precio_total >= 10000 and precio_total < 20000:
            descuento = precio_total * 0.10
        elif precio_total >= 20000:
            descuento = precio_total * 0.15

    total_pagar = precio_total - descuento

    return precio_total, descuento, total_pagar

def verificar(silla, cliente, cantidad):
    if (silla in ["B", "E", "L"]) and (cliente in ["F", "N"]) and cantidad > 0:
        return True
    else:
        return False

def main():
    silla = input("Tipo de silla (B - Básica, E - Estándar, L - De Lujo): ")
    cliente = input("Tipo de cliente (N - Normal, F - Frecuente): ")
    cantidad = int(input("Cantidad de sillas a comprar: "))
    
    if verificar(silla, cliente, cantidad):
        precio, descuento, total = calcular_precio(silla, cliente, cantidad)
        print(f"Precio antes del descuento: ${precio:.2f}")
        print(f"Descuento aplicado: ${descuento:.2f}")
        print(f"Total a pagar: ${total:.2f}")
    else:
        print("Valores de entrada no válidos. Asegúrese de ingresar valores correctos.")

if __name__ == "__main__":
    main()



    