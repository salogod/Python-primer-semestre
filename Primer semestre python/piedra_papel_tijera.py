def piedra_papel_tijera(juan, ana):
    if(juan=="a" and ana== "t"):
        ganador="ANA GANA"
    elif(juan=="t" and ana=="a"):
        ganador="JUAN GANA"
    elif(juan=="p" and ana=="t"):
        ganador= "JUAN GANA"
    elif(juan=="t" and ana=="p"):
        ganador= "ANA GANA"
    elif(juan== "a" and ana=="p"):
        ganador = "JUAN GANA"
    elif(juan== "p" and ana=="a"):
        ganador = "ANA GANA"
    elif(juan== "a" and ana=="a"):
        ganador = "EMPATE"
    elif(juan== "p" and ana=="p"):
        ganador = "EMPATE"
    elif(juan== "t" and ana=="t"):
        ganador = "EMPATE"
    return ganador

juan=str(input("Ingresa una leta, (a es papel, t es tijera y p es piedra) "))
ana=str(input("Ingresa una leta, (a es papel, t es tijera y p es piedra") )

ganador= piedra_papel_tijera(juan, ana)
print(ganador)



    
