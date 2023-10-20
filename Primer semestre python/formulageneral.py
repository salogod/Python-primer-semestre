def calcular_formula_general(a, b, c):

    discriminante = b**2 - 4*a*c

    if discriminante >= 0:

        x1 = (-b + discriminante**0.5) / (2*a)
        x2 = (-b - discriminante**0.5) / (2*a)
        return x1, x2
    else:

        return None

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

soluciones = calcular_formula_general(a, b, c)

if soluciones:
    x1, x2 = soluciones
    print(f"Las soluciones son: x1 = {x1}, x2 = {x2}")
else:
    print("La ecuación no tiene soluciones reales.")
