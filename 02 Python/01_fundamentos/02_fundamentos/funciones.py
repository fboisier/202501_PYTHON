def saludar(nombre="no existe nombre"):
    return f"Hola {nombre}"


print(saludar("pancho"))
print(saludar("francisco"))
print(saludar())


def contar_hasta(desde=0, hasta=10, incremento=1):
    for indice in range(desde, hasta, incremento):
        print(f"el indice actual es {indice}")


contar_hasta()
contar_hasta(hasta=2, desde=1)
contar_hasta(incremento=200, hasta=1000)


def apellidos(apellido):
    print("esto es desde apellido", apellido)


def saludar_siempre(nombre, *args, **kwargs):
    print(nombre, args, kwargs)
    if "apellido" in kwargs:
        apellidos(**kwargs)


saludar_siempre("Francisco", "Javier", "Loco", apellido="Boisier")

diccionarioBase = {
    "nombre": "Francisco",
    "apellido": "Boisier",
}

diccionario1 = {**diccionarioBase, "edad": 30}

print(diccionario1)
