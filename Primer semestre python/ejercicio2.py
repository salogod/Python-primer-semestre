import math

def area_volumen(radio):
    area= math.pi*math.pow(radio, 2)
    volumen=(math.pi*4*math.pow(radio, 3)) /3
    return area, volumen

radio=float(input("Ingrese el valor del radio"))

area , volumen=  area_volumen(radio)

print(f"El rdio de la figura es de {area:.2f}")
print(f"El rdio de la figura es de {volumen:.2f}")
