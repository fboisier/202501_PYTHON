from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hola_mundo():
    return "¡Hola Mundo!"


@app.route("/pancho")
def hola_pancho():
    return "¡Hola Pancho NUEVAMENTE!"


@app.route("/saludar/<nombre>")
def saludar(nombre):
    return f"¡Hola {nombre}!"


@app.route("/sumar/<numero1>/<numero2>")
def sumar(numero1, numero2):
    return str(int(numero1) + int(numero2))


@app.route("/html")
def html():
    return """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hola</title>
</head>
<body>
    <h1>HOLA MUNDO DESDE MI HTML</h1>
</body>
</html>

    """


@app.route("/html_template")
def html_template():
    return render_template("hola_mundo.html")


@app.route("/mision")
def mision():

    return render_template(
        "mision.html", nombre_mision="Esto es desde el contexto", repite=10
    )


@app.route("/listado")
def listado():

    lista_cosas = ["perro", "gato", "tigre"]
    lista_cosas.append("LEON")

    return render_template("listado.html", lista_cosas=lista_cosas)


if __name__ == "__main__":

    app.run(debug=True, port=5001)
