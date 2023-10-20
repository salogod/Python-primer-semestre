def ordenar_ascendente(x, y, z):
    if x > y:
        x, y = y, x
    if y > z:
        y, z = z, y
    if x > y:
        x, y = y, x
    return x, y, z

x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))
z = int(input("Ingrese el tercer número: "))

ordenados = ordenar_ascendente(x, y, z)

for num in ordenados:
    print(num)
