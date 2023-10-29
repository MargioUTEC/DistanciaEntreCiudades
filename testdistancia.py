from Formas_funciones import *
def TestDistancia (forma, pais1, ciudad1, pais2,ciudad2):
    if (forma==1):
        latitud1, longitud1 = obtener_latitud_longitud(ciudad1)
        latitud2, longitud2 = obtener_latitud_longitud(ciudad2)
        distancia = calcular_distancia(int(latitud1), int(longitud1), int(latitud2), int(longitud2))
    elif(forma == 2):
        latitud1, longitud1 = obtener_coordenadas(ciudad2, pais2)
        distancia=distancia_entre_ciudades(ciudad1, pais1, ciudad2, pais2)
    elif(forma == 3):
        distancia=distancia_heversine(ciudad1, pais1, ciudad2, pais2)

    if (distancia == 0.00):
        return("Buen trabajo. Test 2 aprobado!!!")
    else:
        return("El Test 2 ha fallado")
    