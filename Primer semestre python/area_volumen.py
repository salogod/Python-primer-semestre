import math

def calcular_area(radio, altura):
    area_lateral = 2 * math.pi * radio * altura
    area_base = math.pi * radio**2
    area_total = 2 * area_base + area_lateral
    return area_total

def calcular_volumen(radio, altura):
    volumen = math.pi * radio**2 * altura
    return volumen

def main():
    radio = float(input("Ingrese el valor del radio: "))
    altura = float(input("Ingrese el valor de la altura: "))

    area_cilindro = calcular_area(radio, altura)
    volumen_cilindro = calcular_volumen(radio, altura)

    print(f"El área del cilindro es de {area_cilindro:.2f}")
    print(f"El volumen del cilindro es de {volumen_cilindro:.2f}")

if __name__ == "__main__":
    main()
