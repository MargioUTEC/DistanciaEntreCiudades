from Archivos.interfaz1 import *
from Archivos.Haversine import *
from FactoryMethod import FactoryMethod
from Archivos.formasolicitadas import *


def main() -> None:
    factoryM: FactoryMethod = FactoryMethod()
    forma = str = ' '    
    while True:        
        formas()
        
        forma: str = input("Del 1 al 3 elija una forma: ")
        if forma in ['1', '2', '3']:
            break
        else:
            print("Opción no válida!")

    service: Interfaz = factoryM.escoger_forma(forma)

    ciudad1 = input("Ingresa la ciudad 1: ")
    pais1 = input("Ingresa el pais de esa ciudad: ")
    (latitud1, longitud1) = service.obtenerll(ciudad1, pais1)

    ciudad2 = input("Ingrese la ciudad 2: ")
    pais2 = input("Ingrese el pais de esa ciudad: ")
    (latitud2, longitud2) = service.obtenerll(ciudad2, pais2)

    distance = distanciall(latitud1, longitud1, latitud2, longitud2)

    print(f"La distancia desde {ciudad1} - {pais1} hasta {ciudad2} - {pais2} es de {distance:.2f} km.")

main()