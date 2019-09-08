class Tour:
    def __init__(self, tour_admin, tour=None):
        self.tour_admin = tour_admin
        self.tour = []
        self.distancia = 0
        if tour is not None:
            self.tour = list(tour)
        else:
            for i in range(0, self.tour_admin.numero_de_ciudades()):
                self.tour.append(None)

    def __getitem__(self, index):
        return self.tour[index]

    def generar_tour(self):
        for indice_ciudad in range(0, self.tour_admin.numero_de_ciudades()):
            self.set_city(indice_ciudad, self.tour_admin.get_city(indice_ciudad))
        #random.shuffle(self.tour)

    def get_city(self, tour_position):
        return self.tour[tour_position]

    def set_city(self, tour_position, ciudad):
        self.tour[tour_position] = ciudad
        self.distancia = 0

    def get_distancia(self):
        if self.distancia == 0:
            tour_distancia = 0
            for indice_ciudad in range(0, self.tour_tam()):
                ciudad_inicio = self.get_city(indice_ciudad)
                if indice_ciudad + 1 < self.tour_tam():
                    ciudad_lelgada = self.get_city(indice_ciudad + 1)
                else:
                    ciudad_lelgada = self.get_city(0)
                tour_distancia += ciudad_inicio.distancia(ciudad_lelgada)
            self.distancia = tour_distancia

        return self.distancia

    def tour_tam(self):
        return len(self.tour)

    def mostrar(self):
        for i in range(0, self.tour_tam()):
            print(Ciudad.get_nombre_ciudad(self.get_city(i)))
