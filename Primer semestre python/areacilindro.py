def calcular_area_cilindro(radio, altura):
    area_lateral = 2 * 3.14159 * radio * altura
    area_base = 3.14159 * radio ** 2
    area_total = 2 * area_base + area_lateral
    return area_lateral, area_total

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

area_lateral, area_total = calcular_area_cilindro(radio, altura)

print(f"El área de la superficie lateral del cilindro es: {area_lateral:.2f}")
print(f"El área total del cilindro es: {area_total:.2f}")