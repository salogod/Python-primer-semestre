def indice_de_masa(peso, altura):
    indice= peso/ altura**2
    if(indice<20):
        estatus= "PESO BAJO"
    elif(20 <= indice < 25):
        estatus= "PESO NORMAL"
    elif(25 <= indice < 30):
        estatus= "SOBREPESO"
    elif(30 <= indice < 40 ):
        estatus= "OBESIDAD"
    elif(40 >= indice):
        estatus= "OBESIDAD MORBIDA"
    return estatus

peso=float(input("Dame tu peso"))
altura=float(input("Dame tu altura"))

indice=indice_de_masa(peso, altura)
print(indice)
