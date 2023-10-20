def calcula_grado(grado):
    if grado >= 0.9:
        grade= "A"
    elif grado == 0.8:
        grade= "B"
    elif grado == 0.7:
        grade="C"
    elif grado == 0.6:
        grade= "D"
    elif grado <0.6:
        grade= "F"
    return grade

def main():
    grado= float(input("Ingresa una calificacion numerica de 0-1:"))
    calificacion_letra=calcula_grado(grado)
    print(f"Tu calificacion con letra es de {calificacion_letra}")


if __name__ == "__main__":
    main()

