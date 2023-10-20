
def operaciones_numeros(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    return suma, resta, multiplicacion


try:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    

    resultado_suma, resultado_resta, resultado_multiplicacion = operaciones_numeros(numero1, numero2)
    
    print(f"Suma: {numero1} + {numero2} = {resultado_suma}")
    print(f"Resta: {numero1} - {numero2} = {resultado_resta}")
    print(f"Multiplicación: {numero1} * {numero2} = {resultado_multiplicacion}")
except ValueError:
    print("Por favor, ingrese números válidos.")
