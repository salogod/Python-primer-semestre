def mayor_tres(num1, num2, num3):
    mayor = num1
    if num2 > mayor:
     mayor = num2
    if num3 > mayor:
     mayor = num3
    return mayor

num1= int(input("Dame un numero"))
num2= int(input("Dame un numero"))
num3= int(input("Dame un numero"))

mayor=mayor_tres(num1, num2, num3)
print(mayor)