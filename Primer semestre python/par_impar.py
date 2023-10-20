def es_par_impar(num):
    if num % 2 == 0:
        return "par"
    else:
        return "impar"

try:
    num = int(input("Ingrese un número: "))

    resultado = es_par_impar(num)
    
    print(f"El número {num} es {resultado}.")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
