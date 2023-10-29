import csv
import math
import requests
from haversine import haversine
def calcular_distancia(latitud1, longitud1, latitud2, longitud2):#se usa en la forma 1 y 2
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
def obtener_latitud_longitud(ciudad):#se usa en la forma 1
    with open('worldcities.csv', 'r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            if fila['city'] == ciudad:
                latitud = float(fila['lat'])
                longitud = float(fila['lng'])
                return latitud, longitud
    return None, None
def obtener_coordenadas(ciudad, pais):#se usa en la forma 2
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
def distancia_heversine(ciudad1, pais1, ciudad2, pais2):
    coordenadas1 = obtener_coordenadas(ciudad1, pais1)
    coordenadas2 = obtener_coordenadas(ciudad2, pais2)
    distancia=(haversine(coordenadas1, coordenadas2))
    return distancia

# FUNCIONES PARA EL TEST1.PY
ciudadesValidas = []
def ciudades_Validas():
    with open('worldcities.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ciudadesValidas.append(row['city'])

def verificarAPI (ciudad1, ciudad2, pais1, pais2):
    url1 = f"https://nominatim.openstreetmap.org/search?q={ciudad1},{pais1}&format=json"
    url2 = f"https://nominatim.openstreetmap.org/search?q={ciudad2},{pais2}&format=json"
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    if response1.status_code == 200 and response2.status_code == 200:
        data1 = response1.json()
        data2 = response2.json()
        if not data1 and not data2:
            return False
        else:
            return True
    else:
        print(f"Error al hacer la solicitud a la API")
        return False
    pass

def menu():
    print("Que forma va a solicitar?:")
    print("1: Forma con csv")
    print("2: Forma con API")
    print("3: Forma con mock")
    forma=int(input("Del 1 al 3 elija una forma: "))
    if (forma==1):
        pais1 = input(str("Ingrese el Pais 1: "))
        ciudad1 = input(str("Ingresa la ciudad 1: "))
        pais2 = input(str("Ingrese el Pais 2: "))
        ciudad2 = input(str("Ingrese la ciudad 2: "))
        latitud1, longitud1 = obtener_latitud_longitud(ciudad1)
        latitud2, longitud2 = obtener_latitud_longitud(ciudad2)
        distancia=calcular_distancia(int(latitud1), int(longitud1), int(latitud2), int(longitud2))
        if latitud1 is None or latitud2 is None and longitud1 is None or longitud1 is None:
            print(f'No se encontraron datos de alguna de esas ciudades')
        else:
            print(f"La distancia desde {ciudad1} - {pais1} hasta {ciudad2} - {pais2} es de {distancia:.2f} km.")
    elif(forma==2):
        pais1 = input(str("Ingrese el Pais 1: "))
        ciudad1 = input(str("Ingresa la ciudad 1: "))
        latitud1, longitud1 = obtener_coordenadas(ciudad1, pais1)
        pais2 = input(str("Ingrese el Pais 2: "))
        ciudad2 = input(str("Ingrese la ciudad 2: "))
        latitud1, longitud1 = obtener_coordenadas(ciudad2, pais2)
        distancia=distancia_entre_ciudades(ciudad1, pais1, ciudad2, pais2)
        print(f"La distancia desde {ciudad1} - {pais1} hasta {ciudad2} - {pais2} es de {distancia:.2f} km.")
    elif(forma==3):
        pais1 = input(str("Ingrese el Pais 1: "))
        ciudad1 = input(str("Ingresa la ciudad 1: "))
        pais2 = input(str("Ingrese el Pais 2: "))
        ciudad2 = input(str("Ingrese la ciudad 2: "))
        distancia=distancia_heversine(ciudad1, pais1, ciudad2, pais2)
        print(f"La distancia desde {ciudad1} - {pais1} hasta {ciudad2} - {pais2} es de {distancia:.2f} km.")
    else:
        print("Opción no válida!")
    return ("")
