from flask import Flask, render_template, flash, request, redirect

app = Flask(__name__)

app.secret_key = "cualquier cosa"


@app.route("/")
def home():
    return render_template("inicio.html")


@app.route("/formulario")
def formulario():
    return render_template("formulario.html")


@app.route("/procesar_algo", methods=["POST"])
def procesar_algo():

    print("FORMULARIO:", request.form)

    flash("TODO SALIO PERFECTO!", "info")
    flash("Que mal!", "error")
    return redirect("/resultados")


@app.route("/procesar_algo_mejor", methods=["POST"])
def procesar_algo_mejor():

    print("FORMULARIO:", request.form)

    flash("Que genial esto.", "warning")
    return redirect("/distinta")


@app.route("/resultados")
def resultados():
    return render_template("resultados.html")


@app.route("/distinta")
def resultados_distinta():
    return render_template("otra_cosa.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
