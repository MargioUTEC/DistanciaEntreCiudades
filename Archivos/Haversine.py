from math import radians, sin, cos, sqrt, atan2

def distanciall(latitud1, longitud1, latitud2, longitud2):
    radio_tierra_km = 6371.0

    # Primero convertimos las latitudes y longitudes de grados a radianes pq al aplicar el mètodo de Haversine debemos obtener senos y cosenos y la medida para ello es en radianes:)
    latitud1_rad = radians(latitud1)
    longitud1_rad =radians(longitud1)
    latitud2_rad = radians(latitud2)
    longitud2_rad = radians(longitud2)

    # Hallamos la resta entre las longitudes y latitudes
    dlatitud = latitud2_rad - latitud1_rad
    dlongitud = longitud2_rad - longitud1_rad

    # Aplicando la Fórmula Haversine
    a = sin(dlatitud / 2)**2 + cos(latitud1_rad) * cos(latitud2_rad) * sin(dlongitud / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distancia = radio_tierra_km * c

    return distancia