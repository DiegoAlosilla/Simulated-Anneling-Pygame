class Ciudad:
    def __init__(self, lon, lat, name):
        self.lon = lon
        self.lat = lat
        self.name = name

    def distancia(self, ciudad):
        distanciaX = (ciudad.lon - self.lon) * 40000 * math.cos((self.lat + ciudad.lat) * math.pi / 360) / 360
        distanciaY = (self.lat - ciudad.lat) * 40000 / 360
        distancia = math.sqrt((distanciaX * distanciaX) + (distanciaY * distanciaY))
        return distancia

    def get_nombre_ciudad(ciudad):
        return ciudad.name
