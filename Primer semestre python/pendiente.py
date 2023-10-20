def calcular_pendiente(x1, y1, x2, y2):
    if x1 == x2:
        print("La pendiente es infinita (recta vertical)")
    else:
        pendiente = (y2 - y1) / (x2 - x1)
        print(f"La pendiente de la recta es: {pendiente}")

def main():
    try:
        x1 = float(input("Ingrese la coordenada x del primer punto: "))
        y1 = float(input("Ingrese la coordenada y del primer punto: "))
        x2 = float(input("Ingrese la coordenada x del segundo punto: "))
        y2 = float(input("Ingrese la coordenada y del segundo punto: "))

        calcular_pendiente(x1, y1, x2, y2)
    except ValueError:
        print("Error: Ingrese coordenadas válidas (números)")

if __name__ == "__main__":
    main()
