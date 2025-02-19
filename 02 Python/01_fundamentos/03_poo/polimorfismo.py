class Animal:

    nombre = "Animal"
    rugir_defecto = "X"

    def rugir(self):
        return print(f"({self.nombre}) RUGIENDO: {self.rugir_defecto}")


class Gato(Animal):
    nombre = "Gato"
    rugir_defecto = "miau"


class Perro(Animal):
    nombre = "Perro"
    rugir_defecto = "guau"


class Tigre(Animal):
    nombre = "Tigre"
    rugir_defecto = "Grrrrr"


animales: list[Animal] = []

animal_instancia = Animal()
animales.append(animal_instancia)

gato_instancia = Gato()
animales.append(gato_instancia)

perro_instancia = Perro()
animales.append(perro_instancia)

tigre_instancia = Tigre()
animales.append(tigre_instancia)

print(animales)
for animal in animales:
    animal.rugir()


# class Animal:

#     @staticmethod
#     def rugir():
#         return "X"


# class Gato(Animal):
#     @staticmethod
#     def rugir():
#         return "miau"


# class Perro(Animal):
#     @staticmethod
#     def rugir():
#         return "guau"


# class Tigre(Animal):
#     @staticmethod
#     def rugir():
#         return "grrrrr"


# # Instancia Animal
# animal_instancia = Animal()
# print("ANIMAL", animal_instancia.rugir())


# # Instancia Gato
# gato_instancia = Gato()
# print("GATO", gato_instancia.rugir())


# # Instancia Perro
# perro_instancia = Perro()
# print("Perro", perro_instancia.rugir())

# # Instancia Tigre
# tigre_instancia = Tigre()
# print("Tigre", tigre_instancia.rugir())
