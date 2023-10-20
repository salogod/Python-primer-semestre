def cien_años(edad, añonactual):
    añonacimiento= añonactual-edad
    añocien= añonacimiento + 100
    return añocien

edad= int(input("¿Que edad tienes?"))
añoactual= int(input("Introduce el año en el que estamos"))

cienaños= cien_años(edad, añoactual)

print(f"Esta persona tendra cien años en el año: {cienaños:.2f}")