
edificios = ["Edificio A", "Edificio B", "Edificio C", "Edificio D"]


dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


turnos = ["Mañana", "Tarde", "Noche"]


consumo_total = {
    "Edificio A": 0,
    "Edificio B": 0,
    "Edificio C": 0,
    "Edificio D": 0
}


for edificio in edificios:
    print("\n--- Ingresando datos para", edificio, "---")
    
    
    for dia in dias:
        print("\nDía:", dia)
        
        
        for turno in turnos:
            
            consumo = float(input("Ingrese el consumo en kWh en el turno " + turno + ": "))
            
            
            consumo_total[edificio] += consumo


print("\n--- RESULTADOS FINALES ---")
for edificio in edificios:
    total = consumo_total[edificio]
    promedio = total / 7  
    print("Edificio:", edificio)
    print("  Consumo total de la semana:", total, "kWh")
    print("  Promedio diario:", promedio, "kWh")
    print()
