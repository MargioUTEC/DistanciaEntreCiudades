import requests
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
def obtener_coordenadas(ciudad, pais):
    # Construye la URL de la API
    url = f'https://nominatim.openstreetmap.org/search?q={ciudad},{pais}&format=json'

    # Realiza la solicitud GET a la API
    response = requests.get(url)

    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        datos = response.json()
        if datos:
            # Obtiene las coordenadas de la primera coincidencia
            latitud = float(datos[0]['lat'])
            longitud = float(datos[0]['lon'])
            return (latitud, longitud)
        else:
            return None
    else:
        print("Error al consultar la API de Nominatim.")
        return None

def distancia_entre_ciudades(ciudad1, pais1, ciudad2, pais2):
    coordenadas1 = obtener_coordenadas(ciudad1, pais1)
    coordenadas2 = obtener_coordenadas(ciudad2, pais2)

    if coordenadas1 and coordenadas2:
            # Calcula la distancia utilizando la fórmula de Haversine
            lat1, lon1 = coordenadas1
            lat2, lon2 = coordenadas2
            distancia = calcular_distancia(lat1, lon1, lat2, lon2)
            return distancia
    else:
            return None


pais1=input(str("Ingrese el Pais 1: "))
ciudad1=input(str("Ingrese la ciudad del Pais 1: "))
latitud1, longitud1 = obtener_coordenadas(ciudad1, pais1)

pais2=input(str("Ingrese el Pais 2: "))
ciudad2=input(str("Ingrese la ciudad del Pais 2: "))
latitud1, longitud1 = obtener_coordenadas(ciudad2, pais2)

distancia=distancia_entre_ciudades(ciudad1, pais1, ciudad2, pais2)
print(distancia)