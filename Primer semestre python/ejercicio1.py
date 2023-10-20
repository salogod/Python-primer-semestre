import math

def cateto_opuesto(hipotenusa):
    angulo= math.radians(30)
    catetoopuesto= math.sin(angulo)*hipotenusa
    return catetoopuesto

hipotenusa= float(input("Ingrese el valor de la hipotenusa: "))

catetoopuesto = cateto_opuesto(hipotenusa)

print(f"El valor del cateto opuesto es de {catetoopuesto:.2f}")

