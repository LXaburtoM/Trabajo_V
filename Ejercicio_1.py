# Definimos las secciones y los días de clase
secciones = ["Sección A", "Sección B", "Sección C"]
dias = ["Día 1", "Día 2", "Día 3", "Día 4", "Día 5"]

# Inicializamos un diccionario para almacenar la cantidad de asistencias por sección
asistencia = {seccion: 0 for seccion in secciones}

# Iteramos sobre cada día de clase
for dia in dias:
    print(f"\nRegistro de asistencia para {dia}:")
    
    # Iteramos sobre cada sección
    for seccion in secciones:
        print(f"\n{seccion}:")
        
        # Tomamos asistencia para seis estudiantes en cada sección
        for i in range(1, 3):  
            # Pedimos al usuario que indique si el estudiante asistió
            asistencia_estudiante = input(f"¿El estudiante {i} asistió? (s/n): ")
            
            # Si el estudiante asistió, incrementamos el contador de asistencias
            if asistencia_estudiante.lower() == 's':
                asistencia[seccion] += 1

# Mostramos el total de asistencias por sección
print("\nTotal de asistencias por sección:")
for seccion, total in asistencia.items():
    print(f"{seccion}: {total} asistencias")

# Calculamos y mostramos el total general de asistencias
total_general = sum(asistencia.values())
print(f"\nTotal general de asistencias en la semana: {total_general}")
