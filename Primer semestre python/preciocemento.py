def calcular_precio_cemento(cantidad_bultos, precio_por_bulto):
    precio_antes_impuestos = cantidad_bultos * precio_por_bulto
    impuestos = precio_antes_impuestos * 0.16
    total_a_pagar = precio_antes_impuestos + impuestos
    
    return precio_antes_impuestos, impuestos, total_a_pagar


cantidad_bultos = int(input("Ingrese la cantidad de bultos de cemento: "))
precio_por_bulto = float(input("Ingrese el precio por bulto de cemento: "))
        
precio_antes_impuestos, impuestos, total_a_pagar = calcular_precio_cemento(cantidad_bultos, precio_por_bulto)
        
print(f"Precio antes de impuestos: ${precio_antes_impuestos:.2f}")
print(f"Impuestos: ${impuestos:.2f}")
print(f"Total a pagar: ${total_a_pagar:.2f}")
    

