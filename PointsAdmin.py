class PointsAdmin:
    #Inicializamos el arreglo de destionos
    destinations = []
    #Funcuin para agregar destionos
    def add_coordinates(self, coordinates):
        self.destinations.append(coordinates)
    #Funcion para obtener coordenadas
    def get_coordinates(self, index):
        return self.destinations[index]
    #Funcion para actualizar valor del arreglo
    def set_coordinates(self, index, coordinates):
        self.destinations[index] = coordinates
    #Fubncion para obtener el numero de destionos
    def get_size(self):
        return len(self.destinations)
