paises = {}  # Diccionario vacío

paises["MEX"] = "México"  # Agregando valores

paises["COL"] = "Colombia"

paises["CHL"] = "Chile"


for item in paises:
    print(item)

for item in paises.values():
    print(item)

for key, value in paises.items():
    print(key, value)


print(paises)


for item in paises.copy():
    actual = paises.pop(item)
    print(actual)

print(paises)


personaA = {
    "nombre": "Francisco",
    "edad": 40,
}

personaB = {"nombre": "Francisco", "edad": 50, "ciudad": "Coyhaique"}

personaA.update(personaB)
print(personaA)


for i in range(4):

    print(i)

for i in range(3, 4, 3):
    print(i)
