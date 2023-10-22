import csv
from Haversine import distanciall
from Forma3 import withMock
from interfaz1 import *

class withcsv(Interfaz):
    def obtenerll(self, Ciudad: str, Pais: str) -> Tuple[float, float]:
        with open('worldcities.csv', 'r', encoding='utf-8') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            for fila in lector_csv:
                if fila['city'] == Ciudad:
                    latitud = float(fila['lat'])
                    longitud = float(fila['lng'])
                    return latitud, longitud
        return None, None
