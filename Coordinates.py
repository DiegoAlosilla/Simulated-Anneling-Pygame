import math
class Coordinates:
    def __init__(self, x, y):
        #Longitud
        self.x = x
        #Latitud
        self.y = y
    #Calcular la distancia entre dos puntos(Coordenadas)
    def distance(self, coordinates):
        return ((coordinates.x - self.x)**2 + (coordinates.x - self.x)**2)**(0.5)

    #Obtenemos las caoordenadas
    def get_x(coordinates):
        return coordinates.x
    def get_y(coordinates):
        return coordinates.y
    def get_coordinates(coordinates):
        return (coordinates.x,coordinates.y)
