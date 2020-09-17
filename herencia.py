import math
class punto():
    """Representacion de un punto en el plano, los atributos son x e y que representan los valores de las coordenadas cartesianas."""

def __init__(self,x=0,y=0):
    self.x=y
    self.y=y

def mostrar(self):
    return str(self.x)+"."+str(self.y)

def distancia(self,otro):
    """Devuelve la distancia entre ambos puntos."""
    dx = self.x - otro.x
    dy = self.y - otro.y
    return math.sqrt((dx*dx + dy*dy))

class punto3d(punto):
    def __init__(self,x=0,y=0,z=0):
        super().__init__(x,y)
        self.z=z

    @property
    def z(self):
        print("Doy z")
        return self.__z

    @z.setter
    def z(self,z):
        print("Cambio z")
        self.__z=z

    @property
    def mostrar(self):
        return super().mostrar()+":"+str(self.__z)

    def distancia(self,otro):
        dx = self.__x - otro.__x
        dy = self.__y - otro.__y
        dz = self.__z - otro.__z
        return (dx*dx + dy*dy + dz*dz)**0.5

