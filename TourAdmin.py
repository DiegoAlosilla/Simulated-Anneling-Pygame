class TourAdmin:
    destino_ciudades = []

    def add_city(self, ciudad):
        self.destino_ciudades.append(ciudad)

    def get_city(self, index):
        return self.destino_ciudades[index]

    def numero_de_ciudades(self):
        return len(self.destino_ciudades)
