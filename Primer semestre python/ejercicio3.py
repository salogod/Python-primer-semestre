import math

def area_triangulo(a,b,c):
    s=a+b+c/2
    area= math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

a= float(input("Ingrese el valor de a"))
b= float(input("Ingrese el valor de b"))
c= float(input("Ingrese el valor de c"))

area= area_triangulo(a,b,c)

print(f"El area del triangulo es de {area:.2f}")
