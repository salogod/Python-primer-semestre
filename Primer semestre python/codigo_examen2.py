def calcular_calificacion_final(parcial1, parcial2, examen_final):
    calificacion_final = (parcial1 * 0.4) + (parcial2 * 0.4) + (examen_final * 0.2)
    return calificacion_final

def main():
    materias = []

    while True:
        print("Ingrese la información de la materia:")
        nombre_materia = input("Nombre de la materia: ")
        calificacion_parcial1 = float(input("Calificación Parcial 1: "))
        calificacion_parcial2 = float(input("Calificación Parcial 2: "))
        examen_final = float(input("Examen Final: "))

        calificacion_final = calcular_calificacion_final(calificacion_parcial1, calificacion_parcial2, examen_final)
        materias.append((nombre_materia, calificacion_parcial1, calificacion_parcial2, examen_final, calificacion_final))

        otro = input("¿Desea agregar otra materia? (S/N): ")
        if otro.upper() != "S":
            break

    print("\n" + "=" * 80)
    print("Información de las Materias".center(80))
    print("=" * 80)
    print(f"{'Materia'.ljust(30)} {'Parcial 1'.rjust(10)} {'Parcial 2'.rjust(10)} {'Examen Final'.rjust(10)} {'Calificación Final'.rjust(20)}")
    print("=" * 80)

    for materia in materias:
        nombre, parcial1, parcial2, examen_final, calificacion_final = materia
        print(
            f"{nombre.ljust(30)} {parcial1:.2f}".rjust(10),
            f"{parcial2:.2f}".rjust(10),
            f"{examen_final:.2f}".rjust(10),
            f"{calificacion_final:.2f}".rjust(20),
        )

    promedio_final = sum(calificacion_final for _, _, _, _, calificacion_final in materias) / len(materias)
    print("-" * 80)
    print(f"{'Promedio Final:'.ljust(70)} {promedio_final:.2f}".rjust(10))
    print("=" * 80)

if __name__ == "__main__":
    main()

