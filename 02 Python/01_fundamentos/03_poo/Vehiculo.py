class Vehiculo:
    def __init__(self, marca, modelo, color):

        self.modelo = modelo
        self.marca = marca
        self.combustible = "DIESEL"
        self.carroseria = ""
        self.color = color
        self.patente = "XXYYZZ"
        self.duenio = "Ninguno"
        self.traccion = "4x4"
        self.kilometraje = 0

    def encender_motor(self):
        pass

    def apagar_motor(self):
        pass

    def accelerar(self):
        self.kilometraje += 10
        pass

    def virar(self):
        pass

    def cambiarCambio(self):
        pass

    def frenar(self):
        pass

    def __str__(self):
        return f"{self.marca} - {self.modelo} de color {self.color} || {self.combustible}({self.traccion})"


if __name__ == "__main__":
    auto1 = Vehiculo("Suzuki", "Jimny", "Negro")
    auto1.traccion = "4x2"
    auto2 = Vehiculo("Toyota", "Yaris", "Rojo")
    print(auto1)
    print(auto2)

    auto1.accelerar()
    auto1.accelerar()
    auto1.accelerar()
    auto1.accelerar()
    print(auto1.kilometraje)
