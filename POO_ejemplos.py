class Coche():
    def __init__(self):
# el def __init__ es un constructor que crea propiedades de los objetos de la clase Coche()
        self.__largo=250
        self.__ancho=120
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar(self,arrancamos):
#def en este caso es un metodo y no una funcion por eso siempre se usa un self como parameto
        self.__enmarcha=arrancamos

        if self.__enmarcha:
            chequeo=self.chequeo_interno()

        if self.__enmarcha and chequeo:
            return "El coche esta en marcha"
        elif self.__enmarcha and chequeo==False:
            return "Algo fue mal en el chequeo, no se puede arrancar"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene",self.__ruedas,"ruedas. Un ancho de",self.__ancho,
        "y un largo de",self.__largo)

    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="ok"):
            return True
        else:
            return False

miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()
print("-----------------A continuacion se crea el segundo objeto-----------------")
miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()
