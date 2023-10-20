def encontrar_mayor(numero1, numero2, numero3):
    mayor = numero1
    
    if numero2 > mayor:
        mayor = numero2
    
    if numero3 > mayor:
        mayor = numero3
    
    return mayor

try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))

    resultado = encontrar_mayor(num1, num2, num3)
    
    print(f"El número mayor entre {num1}, {num2} y {num3} es {resultado}")
except ValueError:
    print("Por favor, ingrese números válidos.")
