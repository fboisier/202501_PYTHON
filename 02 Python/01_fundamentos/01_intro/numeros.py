import random

variable = "5"

print(type(variable))

numero = int(variable)

print(type(numero))

flotante = float(variable)
print(type(flotante), flotante)

print(str(int(flotante)))


al_azar = random.randint(5, 10)
print(al_azar)

import random

al_azar = 0
contador = 1
while al_azar != 10:
    contador += 1
    al_azar = random.randint(1, 20)
    print(al_azar)

print(f"Tuvimos que ejecutar {contador} veces el while para encontrar el 10.")
