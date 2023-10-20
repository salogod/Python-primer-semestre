def que_triangulo(x,y,z):
    if x > 0  and y > 0  and z > 0:
        if x+y>0 and x+z>y and y+z>x:
            if x==y==z:
                print("Es un triangulo Equilatero")
            elif x!=y!=z:
                print("Es un triangulo Escaleno")
            elif x==y!=z or x==z!=y or z==y!=x:
                print("Es un triangulo Isoseles")
    

x= float(input("Ingresa la longitud del primer lado del triángulo:"))
y= float(input("Ingresa la longitud del segundo lado del triángulo:"))
z= float(input("Ingresa la longitud del tercer lado del triángulo:"))

que_triangulo(x,y,z)