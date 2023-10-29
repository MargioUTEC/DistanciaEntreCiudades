from Formas_funciones import *
import requests

ciudadesValidas = []
def TestNombre(forma, pais1, ciudad1, pais2, ciudad2):
    if (forma == 1):
        ciudades_Validas()
        if(ciudad1 != ciudadesValidas or ciudad2 != ciudadesValidas):
            print("No existe la ciudad que has digitado. Test 1 funcionó!!!")
        else:
            print("Test 1 no funcionó :(")
    elif (forma == 2):
        if verificarAPI(ciudad1, ciudad2, pais1, pais2):
            print("No existe la ciudad que has digitado. Test 1 funcionó!!!")
        else:
            print("Test 1 no funcionó :(")

    elif (forma == 3):
        ciudades_Validas()
        if (ciudad1 != ciudadesValidas or ciudad2 != ciudadesValidas):
            print("No existe la ciudad que has digitado. Test 1 funcionó!!!")
        else:
            print("Test 1 no funcionó :(")

