class Coordinates:
    def __init__(self, x, y):
        #Longitud
        self.x = x
        #Latitud
        self.y = y
    #Calcular la distancia entre dos puntos(Coordenadas)
    def distance(self, coordinates):
        distanceX = (coordinates.x - self.x) * 40000 * math.cos((self.y + ciudad.y) * math.pi / 360) / 360
        distanceY = (self.y - ciudad.y) * 40000 / 360
        distance = math.sqrt((distanceX * distanceX) + (distanceY * distanceY))
        return distance
