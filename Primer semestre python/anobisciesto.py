def ano_bisiesto(ano):
    if(ano%4==0 or ano%100==0 or ano%400==0):
        tipodeano= "TRUE"
    else:
        tipodeano= "FALSE"
    return tipodeano

ano=int(input("Ingresa un ano"))

bisciesto= ano_bisiesto(ano)

print(bisciesto)
