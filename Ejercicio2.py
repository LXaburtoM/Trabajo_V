#Uso de computadoras en laboratorios
#simular el estado de uso de computadoras en dos laboratorios del campus
#cada laboratorio contiene 5 filas de 4 computadoras c/u
#registrar si cada computadora esta ocupada o libre (manual o simulado)
#mostrar el resumen de las computadoras ocupadas y libres por laboratorio
import random
labs = []
modo = input("¿Desea ingresar los valores manualmente? (s/n):").strip().lower()
for l in range(2):
    print(f"\nLaboratorio {l + 1}")
    lab = []
    for i in range(5):
        fila = []
        for j in range(4):
            if modo == "s":
                val = input(f"fila {i + 1}, columna {j + 1} (0=Libre, 1=Ocupada): ")
                while val not in ("0", "1"):
                    val = input("Este valor no es válido, por favor ingrese 0 o 1: ")
                fila.append(int(val))
            else:
                fila.append(random.randint(0, 1))
        lab.append(fila)
    labs.append(lab)
for i in range(len(labs)):
    lab = labs[i]
    ocupadas = sum(sum(fila) for fila in lab)
    total = 5 * 4
    print(f"\nResumen Laboratorio {i + 1}: Ocupadas = {ocupadas}, Libres = {total - ocupadas}")