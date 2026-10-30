def calcular_disponibilidad(tiempo_total, tiempo_caida):
    if tiempo_total <= 0: 
        return 0.0
    
    # Validación opcional para evitar porcentajes negativos
    if tiempo_caida > tiempo_total:
        return 0.0
        
    return ((tiempo_total - tiempo_caida) / tiempo_total) * 100
