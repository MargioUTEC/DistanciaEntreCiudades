import requests
import math
from Haversine import distanciall

def obtener_coordenadas(ciudad, pais):
    # Añadimos la API
    url = f'https://nominatim.openstreetmap.org/search?q={ciudad},{pais}&format=json'

    # Llamamos a la API con get
    response = requests.get(url)

    # Verificaciòn de solicitudes
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
        print("Error al consultar la API.")
        return None

def distancia_entre_ciudades(ciudad1, pais1, ciudad2, pais2):
    coordenadas1 = obtener_coordenadas(ciudad1, pais1)
    coordenadas2 = obtener_coordenadas(ciudad2, pais2)

    if coordenadas1 and coordenadas2:
            # Calcula la distancia utilizando el archivo que contiene el mètodo Haversine
            lat1, lon1 = coordenadas1
            lat2, lon2 = coordenadas2
            distancia = distanciall(lat1, lon1, lat2, lon2)
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
print(f'La distancia entre lo solicitado es {distancia:.2f} km.')