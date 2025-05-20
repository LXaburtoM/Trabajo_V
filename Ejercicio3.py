#Cree un programa que permita llevar un registro de ventas en una feria 
# estudiantil organizada por la UAM. La feria se desarrollará durante tres
# días, con cuatro stands por día. Cada stand ofrecerá tres productos distintos.
# El sistema deberá permitir ingresar el monto de venta por producto y mostrar un 
# resumen por stand, por día, y un total general de la feria.

def registrar_ventas():
    print("Presione ENTER para comenzar")
    input()
    print("\nStand: Arte y Creatividad")
    # Ingresar precios de los productos
    try:
        precio_cuadro = float(input("Precio de cuadros: "))
        precio_llavero = float(input("Precio de llaveros: "))
        precio_pulsera = float(input("Precio de pulseras: "))
    except ValueError:
        print("Por favor, ingresa números válidos para los precios.")
        return
    total_general = 0
    for dia in range(1, 4):  # Días 1 a 3
        print(f"\nDía {dia}")
        try:
            cantidad_cuadros = int(input("¿Cuántas veces vendió cuadros? "))
            cantidad_llaveros = int(input("¿Cuántas veces vendió llaveros? "))
            cantidad_pulseras = int(input("¿Cuántas veces vendió pulseras? "))
        except ValueError:
            print("Por favor, ingresa solo números enteros para las cantidades.")
            return
        total_dia = (
            cantidad_cuadros * precio_cuadro +
            cantidad_llaveros * precio_llavero +
            cantidad_pulseras * precio_pulsera
        )
        print(f"Total del día {dia}: {total_dia:.2f} C$")
        total_general += total_dia
    print(f"\nTotal general de la feria: {total_general:.2f} C$")
if __name__ == "__main__":
    registrar_ventas()