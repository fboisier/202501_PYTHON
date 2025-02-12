tupla = "a", "b"

tupla_un_valor = (
    "mucho texto en una sola linea alg mucho texto en una sola linea algoo",
    " y necesito que quede en dos al mucho texto en una sola linea algogo",
)
print(tupla_un_valor)
print(type(tupla_un_valor))


def suma_multiplicacion(x, y):

    suma = x + y

    multiplicacion = x * y

    return suma, multiplicacion


c = suma_multiplicacion(2, 3)

print(f"el valor de {c[0]} y de")
