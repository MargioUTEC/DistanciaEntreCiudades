import csv
from Haversine import distanciall

def obtener_latlong(ciudad):
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
latitud1, longitud1 = obtener_latlong(ciudad1)
latitud2, longitud2 = obtener_latlong(ciudad2)
distancia = distanciall(int(latitud1), int(longitud1), int(latitud2), int(longitud2))

if latitud1 is None or latitud2 is None and longitud1 is None or longitud1 is None:
    print(f'No se encontraron datos de alguna de esas ciudades')
else:
    print(f'La distancia desde {ciudad1} a {ciudad2} es de {distancia:.2f} km.')

if latitud1 is not None and longitud1 is not None and latitud2 is not None and longitud2 is not None:
    distancia = distanciall(int(latitud1), int(longitud1), int(latitud2), int(longitud2))
else:
    print("No se pudieron obtener las coordenadas para una de las ciudades.")
