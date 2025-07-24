import math

class Punto:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distancia_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distancia_punto(self, Punto):
        return self.distancia_xy(Punto.getx(), Punto.gety())


class Triangulo:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimetro(self):
        per = 0
        for i in range(3):
            per += self.__vertices[i].distancia_punto(self.__vertices[(i + 1) % 3])#1 2 0
        return per


triangulo = Triangulo(Punto(0, 0), Punto(1, 0), Punto(0, 1))
print(triangulo.perimetro())
    