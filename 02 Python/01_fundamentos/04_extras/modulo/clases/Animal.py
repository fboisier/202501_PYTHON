class Animal:

    nombre = "Animal"
    rugir_defecto = "X"

    def rugir(self):
        return print(f"({self.nombre}) RUGIENDO: {self.rugir_defecto}")
