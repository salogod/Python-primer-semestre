def peso(pesofinal, pesoinicial, tiempo):
    kilosabajar= pesofinal-pesoinicial
    kilospormes= kilosabajar/tiempo
    return kilospormes

pesoinicial= float(input("Introduce tu peso inicial"))
pesofinal= float(input("Introduce el peso al que quieres llegar"))
tiempo= float(input("Introduce el tiempo en meses en el cual quieres llegar a ese peso"))

kilosmes= peso(pesofinal,pesoinicial,tiempo)

print(f"Necesitas bajar {kilosmes:.2f} por mes")