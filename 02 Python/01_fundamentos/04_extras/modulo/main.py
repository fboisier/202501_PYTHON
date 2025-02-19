from clases import Animal, Perro, Gato, Tigre
from otra_cosa import Oso

animales: list[Animal] = []

animal_instancia = Animal()
animales.append(animal_instancia)

gato_instancia = Gato()
animales.append(gato_instancia)

perro_instancia = Perro()
animales.append(perro_instancia)

tigre_instancia = Tigre()
animales.append(tigre_instancia)

oso_instancia = Oso()
animales.append(oso_instancia)

print(animales)
for animal in animales:
    animal.rugir()
