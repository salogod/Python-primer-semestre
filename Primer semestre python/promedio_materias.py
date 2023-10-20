def promedio_materias(materia1, materia2, materia3, materia4):
    suma=materia1+materia2+materia3+materia4
    promedio= suma/4
    return promedio

materia1= float(input("Ingrese la primera calificacion "))
materia2= float(input("Ingrese la segunda calificacion "))
materia3= float(input("Ingrese la tercera calificacion "))
materia4= float(input("Ingrese la cuarta calificacion "))

prom= promedio_materias(materia1, materia2, materia3, materia4)

print(f"El promedio para estas materias es de: {prom:.2f}")


