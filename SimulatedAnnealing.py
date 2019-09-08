class SimulatedAnnealing:
    def __init__(self, destinos, temperatura_inicial, valocidad_enfriamiento):
        self.tour_admin = destinos
        self.tour = Tour(destinos)
        self.tour.generar_tour()
        self.el_mejor = self.tour
        self.temperatura = temperatura_inicial
        self.valocidad_enfriamiento = valocidad_enfriamiento

    def funcion_aceptacion(self, delta_energia):
        if delta_energia < 0:
            return True
        elif random.random() <= math.exp(-(delta_energia / self.temperatura)):
            return True
        return False

    def nuevo_tour(self):
        tour_nuevo = Tour(self.tour_admin, self.tour)

        pos1 = random.randrange(self.tour.tour_tam())
        pos2 = random.randrange(self.tour.tour_tam())
        ciudad1 = tour_nuevo.get_city(pos1)
        ciudad2 = tour_nuevo.get_city(pos2)
        tour_nuevo.set_city(pos2, ciudad1)
        tour_nuevo.set_city(pos1, ciudad2)

        actual_energia = self.tour.get_distancia()
        nueva_energia = tour_nuevo.get_distancia()
        delta = nueva_energia - actual_energia

        if self.funcion_aceptacion(delta):
            self.tour = tour_nuevo

        if tour_nuevo.get_distancia() < self.el_mejor.get_distancia():
            self.el_mejor = tour_nuevo
            print(tour_nuevo.get_distancia())

    def run(self):
        while self.temperatura > 1:
            self.nuevo_tour()
            self.temperatura *= 1 - self.valocidad_enfriamiento
