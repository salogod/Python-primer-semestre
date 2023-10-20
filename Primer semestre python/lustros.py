def lustros(añodenacimiento, añoactual):
    edad= añoactual-añodenacimiento
    lustros= edad/5
    return lustros

añodenacimiento= float(input("¿En que año naciste?"))
añoactual= float (input("Introduce el año en el que estamos"))

lustros= lustros(añodenacimiento, añoactual)

print(lustros)