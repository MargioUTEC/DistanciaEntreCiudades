import requests
from Forma3 import withMock
from Haversine import distanciall
from interfaz1 import *

class withAPI(Interfaz):
    def obtenerll(self, Ciudad: str, Pais: str) -> Tuple[float, float]:
        # Añadimos la API
        url = f'https://nominatim.openstreetmap.org/search?q={Ciudad},{Pais}&format=json'
        # Llamamos a la API con get
        response = requests.get(url)

        # Verificaciòn de solicitudes
        if response.status_code == 200:
            datos = response.json()
            if datos:
                latitud = float(datos[0]['lat'])
                longitud = float(datos[0]['lon'])
                return (latitud, longitud)
        print("Error al consultar la API.")
        return None

def distancia_entre_ciudades(ciudad1, pais1, ciudad2, pais2):
    datapi = withAPI()
    coordenadas1 = datapi.obtenerll(ciudad1, pais1)
    coordenadas2 = datapi.obtenerll(ciudad2, pais2)

    if coordenadas1 and coordenadas2:
            # Calcula la distancia utilizando el archivo .py que contiene el mètodo Haversine
            lat1, lon1 = coordenadas1
            lat2, lon2 = coordenadas2
            distancia = distanciall(lat1, lon1, lat2, lon2)
            return distancia
    else:
            return None