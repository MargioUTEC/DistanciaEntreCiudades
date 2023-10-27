from Archivos.interfaz1 import *
class withMock(Interfaz):
    def obtenerll(self, Ciudad: str, Pais: str) -> Tuple[float, float]:
        return 37.5600, 126.9900

# piden 2 valores fijos entonces como ejemplo insertamos la ciudad de Seul y su pais respectivo
# dataMock = withMock()
# print(f'Las coordenadas de Seul son (Latitud,Longitud):')
# print(dataMock.obtenerll("Seoul","South Korea"))