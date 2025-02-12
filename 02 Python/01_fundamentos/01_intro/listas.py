cajonera = ["pantalones", "camisetas", "calcetines"]
#                0             1             2

print(cajonera[0])  # Accedemos al cajón con índice 0. Imprime: "pantalones"

print(cajonera[1])  # Accedemos al cajón con índice 1. Imprime: "camisetas"

print(cajonera[2])  # Accedemos al cajón con índice 2. Imprime: "calcetines"

cajonera[1] = "sueters"  # Cambiamos el valor del cajón con índice 1

print(cajonera)  # Imprime: ['pantalones', 'sueters', 'calcetines']


lista_grande = [2, 4, 6, 8, 10, 12, 14, 16]

print(lista_grande[3:])  # Imprime:[8, 10, 12, 14, 16]

print(lista_grande[:6])  # Imprime:[2, 4, 6, 8, 10, 12]

print(lista_grande[3:6])  # Imprime:[8, 10, 12]
