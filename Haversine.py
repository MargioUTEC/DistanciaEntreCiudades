import math

def distanciall(latitud1, longitud1, latitud2, longitud2):
    radio_tierra_km = 6371.0

    # Primero convertimos las latitudes y longitudes de grados a radianes pq al aplicar el mètodo de Haversine debemos obtener senos y cosenos y la medida para ello es en radianes:)
    latitud1_rad = math.radians(latitud1)
    longitud1_rad = math.radians(longitud1)
    latitud2_rad = math.radians(latitud2)
    longitud2_rad = math.radians(longitud2)

    # Hallamos la resta entre las longitudes y latitudes
    dlatitud = latitud2_rad - latitud1_rad
    dlongitud = longitud2_rad - longitud1_rad

    # Aplicando la Fórmula Haversine
    a = math.sin(dlatitud / 2)**2 + math.cos(latitud1_rad) * math.cos(latitud2_rad) * math.sin(dlongitud / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = radio_tierra_km * c

    return distancia