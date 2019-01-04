import  codecs #Importamos las librerias 
import sys

# sys.path.append('./')
from Modelado.Mimodelo import *

class MiArchivo:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/informacion.csv", "r") # Abrimos el archivo y asignamos la direccion  

    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self): # Cierra el archivo 
        self.archivo.close()


class MiArchivoEscribir:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/informacion2.csv", "a") # Abrimos el archivo y asignamos la direccion 

    def agregar_informacion(self, p):
        self.archivo.write("%s-%s-%d-%d\n" % (p.nombre, p.ciudad,\
                p.campeonatos, p.numJugadores))

    def cerrar_archivo(self): # Cierra el archivo 
        self.archivo.close()
