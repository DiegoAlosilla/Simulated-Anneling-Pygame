import random
import math
from Points import Points
class SimulatedAnnealing:
    def __init__(self, destinos, temperatura_inicial, valocidad_enfriamiento):
            self.points_admin = destinos
            self.points = Points(destinos)
            self.points.generar_points()
            self.el_mejor = self.points
            self.temperatura = temperatura_inicial
            self.valocidad_enfriamiento = valocidad_enfriamiento

    def funcion_aceptacion(self, delta_energia):
        if delta_energia < 0:
            return True
        elif random.random() <= math.exp(-(delta_energia / self.temperatura)):
            return True
        return False

    def nuevo_points(self):
        points_nuevo = Points(self.points_admin, self.points)

        pos1 = random.randrange(self.points.point_size())
        pos2 = random.randrange(self.points.point_size())
        ciudad1 = points_nuevo.get_coordinates(pos1)
        ciudad2 = points_nuevo.get_coordinates(pos2)
        points_nuevo.set_coordinates(pos2, ciudad1)
        points_nuevo.set_coordinates(pos1, ciudad2)

        actual_energia = self.points.get_distance()
        nueva_energia = points_nuevo.get_distance()
        delta = nueva_energia - actual_energia

        if self.funcion_aceptacion(delta):
            self.points = points_nuevo

        if points_nuevo.get_distance() < self.el_mejor.get_distance():
            self.el_mejor = points_nuevo
            print(points_nuevo.get_distance())

    def run(self):
        while self.temperatura > 1:
            self.nuevo_points()
            self.temperatura *= 1 - self.valocidad_enfriamiento
