#Cree un programa que permita llevar un registro de ventas en una feria 
# estudiantil organizada por la UAM. La feria se desarrollará durante tres
# días, con cuatro stands por día. Cada stand ofrecerá tres productos distintos.
# El sistema deberá permitir ingresar el monto de venta por producto y mostrar un 
# resumen por stand, por día, y un total general de la feria.

print("="*60)
print("Inventario de ventas - Feria estudiantil UAM")
input("Presione ENTER para comenzar")

# Datos de los 4 stands
stands = [
    ("Arte y Creatividad", ["cuadros", "llaveros", "pulseras"]),
    ("Eco-UAM", ["bolsas", "velas", "macetas"]),
    ("Sabores Callejeros", ["elotes", "jamaica", "papas fritas"]),
    ("Dulce de Feria", ["algodón", "globos", "manzanas"])
]

totales = []

for stand in stands:
    nombre, productos = stand
    print(f"\nStand: {nombre}")
    precios = []
    for producto in productos:
        precio = float(input(f"Precio de {producto}: "))
        precios.append(precio)

    total_stand = 0
    for dia in range(1, 4):
        print(f"Día {dia}")
        total_dia = 0
        for i in range(3):
            cantidad = int(input(f"¿Cuántas veces vendió {productos[i]}? "))
            total_dia += cantidad * precios[i]
        total_stand += total_dia
        print(f"Total del día {dia}: {total_dia:.2f} C$")
    
    totales.append(total_stand)

# Mostrar resumen
print("\n" + "="*50)
print("Resumen total por stand:")
for i in range(4):
    print(f"{stands[i][0]}: {totales[i]:.2f} C$")
print("="*50)
print(f"TOTAL GENERAL DE LA FERIA: {sum(totales):.2f} C$")

