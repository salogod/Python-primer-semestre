def calcular_factorial(num):
    factorial = 1

    if num < 0:
        return "El factorial no está definido para números negativos"
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            factorial *= i
        return factorial

try:
    num= int(input("Ingrese un número entero para calcular su factorial: "))
    resultado = calcular_factorial(num)
    print(f"El factorial de {num} es {resultado}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
