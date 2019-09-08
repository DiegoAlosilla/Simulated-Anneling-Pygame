class PointsAdmin:
    #Inicializamos el arreglo de destionos
    destinations = []
    #Funcuin para agregar destionos
    def add_coordinates(self, coordinates):
        self.destinations.append(coordinates)
    #Funcion para obtener destiono
    def get_coordinates(self, index):
        return self.destinations[index]
    #Fubncion para obtener el numero de destionos
    def get_size(self):
        return len(self.destinations)
