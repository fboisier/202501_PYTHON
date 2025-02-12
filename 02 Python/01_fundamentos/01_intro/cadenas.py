nombre = "Marcelo"
edad = 4
boleano = True

print("Me llamo", nombre, edad, boleano)

flotante = 4.0
entero = 5

print(flotante + entero)

print("Mi nombre es %s y tengo %d años de edad." % (nombre, edad))
print(
    "Mi nombre es %(name)s y tengo %(age)d años de edad."
    % {"name": "Francisco", "age": 40}
)

print(nombre.upper())
