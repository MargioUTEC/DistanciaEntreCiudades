import csv
import math
def calcular_distancia(latitud1, longitud1, latitud2, longitud2):
    radio_tierra_km = 6371.0  # Radio de la Tierra en kilómetros

    # Convertir latitudes y longitudes de grados a radianes
    latitud1_rad = math.radians(latitud1)
    longitud1_rad = math.radians(longitud1)
    latitud2_rad = math.radians(latitud2)
    longitud2_rad = math.radians(longitud2)

    # Calcular la diferencia entre las longitudes y latitudes
    delta_latitud = latitud2_rad - latitud1_rad
    delta_longitud = longitud2_rad - longitud1_rad

    # Aplicar la fórmula haversine
    a = math.sin(delta_latitud / 2)**2 + math.cos(latitud1_rad) * math.cos(latitud2_rad) * math.sin(delta_longitud / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = radio_tierra_km * c

    return distancia
def obtener_latitud_longitud(ciudad):
    with open('worldcities.csv', 'r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            if fila['city'] == ciudad:
                latitud = float(fila['lat'])
                longitud = float(fila['lng'])
                return latitud, longitud
    return None, None

ciudad1= input(str("Ingresa la ciudad 1: "))
ciudad2= input(str("Ingresa la ciudad 2: "))
latitud1, longitud1 = obtener_latitud_longitud(ciudad1)
latitud2, longitud2 = obtener_latitud_longitud(ciudad2)
distancia=calcular_distancia(int(latitud1), int(longitud1), int(latitud2), int(longitud2))

if latitud1 is None or latitud2 is None and longitud1 is None or longitud1 is None:
    print(f'No se encontraron datos de alguna de esas ciudades')
else:
    print(f'La distancia de la ciudad {ciudad1} a la ciudad {ciudad2} es {distancia:.2f} km.')
