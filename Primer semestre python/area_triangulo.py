def area_triangulo(base, altura):
    area = (base * altura) /2
    return area

base = float(input("Ingrese la medida de la base del triangulo"))
altura = float(input("Ingrese el valor de la altura del triangulo"))

area= area_triangulo(base, altura)

print(f"El area del triangulo es: {area:.2f}")