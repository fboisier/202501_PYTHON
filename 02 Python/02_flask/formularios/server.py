from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Prueba 2"


@app.route("/")
def home():
    return render_template("formularios.html")


@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    print("DATOS INGRESADOS", request.form)
    return redirect("/")


@app.route("/frutas")
def frutas():
    return render_template("frutas.html")


@app.route("/procesar_frutas", methods=["POST"])
def procesar_frutas():

    contexto = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"],
        "fresas": request.form["fresas"],
        "frambuesas": request.form["frambuesas"],
        "manzanas": request.form["manzanas"],
    }

    session.update(contexto)

    suma = (
        int(request.form["fresas"])
        + int(request.form["frambuesas"])
        + int(request.form["manzanas"])
    )

    print("LA SUMA DE LAS CANTIDADES DE FRUTAS ES: ", suma)

    return redirect("/resultado_orden")


@app.route("/resultado_orden")
def resultado_frutas():

    return render_template(
        "checkout.html",
        nombre=session.get("nombre", "No existe"),
        apellido=session.get("apellido", "No Existe"),
        email=session.get("email", "No Existe"),
        fresas=session.get("fresas", "No Existe"),
        frambuesas=session.get("frambuesas", "No Existe"),
        manzanas=session.get("manzanas", "No Existe"),
    )


@app.route("/limpiar_sesion")
def limpiar_sesion():
    session.clear()
    return redirect("/frutas")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
