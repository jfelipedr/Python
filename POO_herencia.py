class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenara(self):
        self.frena=True

    def estado(self):
        print("Marca:",self.marca,"\nModelo:",self.modelo,"\nEn marcha:",self.enmarcha
        ,"\nAcelerando:",self.acelera,"\nFrenando:",self.frena)


class Furgoneta(Vehiculos):

    def carga(self,cargar):
        self.cargado=cargar
        if self.cargado:
            return "La Furgoneta esta cargada"
        else:
            return "La Furgoneta no esta cargada"


class Moto(Vehiculos):
    hcaballito=""

    def caballito(self):
        self.hcaballito="Haciendo maniobra el caballito"

    def estado(self):
        print("Marca:",self.marca,"\nModelo:",self.modelo,"\nEn marcha:",self.enmarcha
        ,"\nAcelerando:",self.acelera,"\nFrenando:",self.frena,"\nManiobra:",self.hcaballito)


class VElectricos():

    def __init__(self):
        self.autonimia=100

    def cargarEnergia(self):
        self.cargando=True


miMoto=Moto("Honda","Competicion")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Renault","Industrial")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))


class BicicletaElectrica(Vehiculos,VElectricos):
#esta clase hereda los metodos de Vehiculos y VElectricos , pero el constructuor, osea el def __init__()
#lo hereda de la primera clase
    pass


miBici=BicicletaElectrica("GW","Pista")
miBici.estado()
