def positivo_negativo(num):
    res= num%2
    if res==0 and num>0:
        print(f"{num} es par positivo")
    elif res==0 and num<0:
        print(f"{num} es par negativo")
    if res!=0 and num>0:
         print(f"{num} es impar positivo")
    elif res!=0 and num<0:
        print(f"{num} es impar negativo")   


num= int(input("Ingrese en unmero entero"))

positivo_negativo(num)