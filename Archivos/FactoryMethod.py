from Archivos.Forma1 import *
from Archivos.Forma2 import *
from Archivos.Forma3 import *
from Archivos.interfaz1 import *

class FactoryMethod:
    def escoger_forma(self,form: str) -> Interfaz:
        if form == '1':
            return withcsv()
        if form == '2':
            return withAPI()
        if form == '3':
            return withMock()
