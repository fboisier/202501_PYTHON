from Vehiculo import Vehiculo


class Auto(Vehiculo):

    def __init__(self, marca, modelo, color, puertas):
        super().__init__(marca, modelo, color)
        self.puertas = puertas
        self.tiene_techo = True

    def retrocede(self):
        pass


class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, soporte):
        super().__init__(marca, modelo, color)
        self.soporte = soporte


auto1 = Auto("Mazda", "2", "Azul", 5)
print(auto1)

moto1 = Moto("Kawazaky", "ZZ1", "AZUL", 1)
print(moto1)
