def obtener_licencia(edad, identificacion):
    if edad >= 21 and identificacion == 's':
        return 'Si'
    else:
        return 'No'


edad = int(input("Ingresa la edad de la persona: "))
identificacion = input("Ingresa 's' si tiene identificación oficial, 'n' si no tiene: ")


identificacion = identificacion.lower()

resultado = obtener_licencia(edad, identificacion)


print(resultado.capitalize())
