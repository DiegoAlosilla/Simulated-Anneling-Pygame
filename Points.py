class Points:
    #Inicializamos variables
    def __init__(self, points_admin, points=None):
        self.points_admin = points_admin
        self.points = []
        self.distance = 0
        if points is not None:
            self.points = list(points)
        else:
            for i in range(0, self.points_admin.get_size()):
                self.points.append(None)

    #Obtenemos valores de un pointss
    def __getitem__(self, index):
        return self.points[index]


    def generar_points(self):
        for indice_coordinates in range(0, self.points_admin.get_size()):
            self.set_coordinates(indice_coordinates, self.points_admin.get_coordinates(indice_coordinates))
        #random.shuffle(self.points)

    #Obtenemos coordenadas
    def get_coordinates(self, points_position):
        return self.points[points_position]

    def set_coordinates(self, points_position, coordinates):
        self.points[points_position] = coordinates
        self.distance = 0

    def get_distance(self):
        if self.distance == 0:
            points_distance = 0
            for indice_point in range(0, self.point_size()):
                point_inicio = self.get_coordinates(indice_point)
                if indice_point + 1 < self.point_size():
                    point_lelgada = self.get_coordinates(indice_point + 1)
                else:
                    point_lelgada = self.get_coordinates(0)
                points_distance += point_inicio.distance(point_lelgada)
            self.distance = points_distance

        return self.distance

    def point_size(self):
        return len(self.points)
