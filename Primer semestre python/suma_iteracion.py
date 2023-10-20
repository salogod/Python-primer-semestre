def suma_iteraciones(num_iteraciones):
    suma = 0  
    for i in range(num_iteraciones):
        num = float(input("Ingresa un número: "))  
        suma += num 
    
    return suma  

num_iteraciones = int(input("Ingrese la cantidad de iteraciones que desea: "))

resultado = suma_iteraciones(num_iteraciones)
print("La suma de los números ingresados es:", resultado)
