class Coche():
    def desplazamiento(self):
        print("Uso 4 ruedas")


class Moto():
    def desplazamiento(self):
        print("Uso 2 ruedas")


class Camion():
    def desplazamiento(self):
        print("Uso 6 ruedas")


def desplazamiento_vehiculo(vehiculo):
#con esta funcion se puede convertir cualquier vehiculo
    vehiculo.desplazamiento()


miVehiculo=Camion()
desplazamiento_vehiculo(miVehiculo)
