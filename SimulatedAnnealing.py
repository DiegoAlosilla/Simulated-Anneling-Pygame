import random
import math
from Points import Points
class SimulatedAnnealing:
    def __init__(self, destinations, temperature_inicial, cooling):
        self.points_admin = destinations
        self.points = Points(destinations)
        self.points.generar_points()
        self.better = self.points
        self.temperature = temperature_inicial
        self.cooling = cooling

    def get_points(self,index):
        return self.points[index]
    def sussces_fun(self, delta_energia):
        if delta_energia < 0:
            return True
        elif random.random() <= math.exp(-(delta_energia / self.temperature)):
            return True
        return False

    def new_points(self):
        points_new = Points(self.points_admin, self.points)

        pos1 = random.randrange(self.points.get_size())
        pos2 = random.randrange(self.points.get_size())
        coordinates1 = points_new.get_coordinates(pos1)
        coordinates2 = points_new.get_coordinates(pos2)
        points_new.set_coordinates(pos2, coordinates1)
        points_new.set_coordinates(pos1, coordinates2)

        actual_energia = self.points.get_distance()
        nueva_energia = points_new.get_distance()
        delta = nueva_energia - actual_energia

        if self.sussces_fun(delta):
            self.points = points_new

        if points_new.get_distance() < self.better.get_distance():
            self.better = points_new
            print(points_new.get_distance())

    def run(self):
        while self.temperature > 1:
            self.new_points()
            self.temperature *= 1 - self.cooling
