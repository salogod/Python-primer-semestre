def suma_promedio(primer_numero, segundo_numero):
    if segundo_numero > primer_numero:
        suma=0
        for numero in range(primer_numero, segundo_numero +1):
            n=segundo_numero-primer_numero+1
            suma+= numero
            primedio= suma/n
        print("La suma es de " , suma)
        print("El promedio es de " , primedio)

primer_numero= int(input("Ingresa un numero"))
segundo_numero= int(input("Ingresa otro numero"))

suma_promedio(primer_numero,segundo_numero)