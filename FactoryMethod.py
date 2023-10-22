from Forma1 import *
from Forma2 import *
from Forma3 import *
from interfaz1 import *

class FactoryMethod:
    def escoger_forma(self,form: str) -> Interfaz:
        if form == '1':
            return withcsv()
        if form == '2':
            return withAPI()
        if form == '3':
            return withMock()
