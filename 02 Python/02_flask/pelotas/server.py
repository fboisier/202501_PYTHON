from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("pelotas.html")


@app.route("/juego")
def juego():
    return render_template("juego_x_color.html", contador=3)


@app.route("/juego/<contador>")
def juego_x(contador):
    return render_template("juego_x_color.html", contador=int(contador))


@app.route("/juego/<contador>/<color>")
def juego_x_color(contador, color):
    return render_template("juego_x_color.html", contador=int(contador), color=color)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
