class Equipo(object):
    """
    """

    def __init__(self, n, cd, camp, num_ju):# Contructor que resive 6 parametros(nombre, apellido, edad, codigo, nota1 y nota2) 
        """
        """
        self.nombre = n
        self.ciudad = cd
        self.campeonatos = int(camp)
        self.numJugadores = int(num_ju)

    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_ciudad(self, n):
        """
        """
        self.ciudad = int(cd)

    def obtener_ciudad(self):
        """
        """
        return self.ciudad

    def agregar_campeonatos(self, n):
        """
        """
        self.campeonatos = int(camp)

    def obtener_campeonatos(self):
        """
        """
        return self.campeonatos

    def obtener_numJugadores(self):
        """
        """
        return self.numJugadores
    def agregar_numJugadores(self, n):
        """
        """
        self.numJugadores = int(num_ju)

    def __str__(self):#Muestra los datos que retorna la clase 
        """
        """
        return "%s - %s - %d - %d" % (self.obtener_nombre(), self.obtener_ciudad(),\
                self.obtener_campeonatos(), self.obtener_numJugadores())