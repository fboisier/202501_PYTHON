from flask import Flask, render_template, flash, request, redirect, session

app = Flask(__name__)

app.secret_key = "cualquier cosa"


@app.route("/")
def home():

    if 'usuario' not in session:
        return redirect("/login")

    return render_template("inicio.html")

@app.route("/login")
def login():
    if 'usuario' in session:
        flash("No seas loco. Ya estás logeado.", "info")
        return redirect("/")

    return render_template("login.html")

@app.route("/login_usuario", methods=["POST"])
def login_usuario():
    print(request.form)
    session['usuario'] = request.form['email']
    flash("Logeado correctamente", "success")
    return redirect("/")

@app.route("/salir")
def salir():

    if 'usuario' in session:
        del session['usuario'] #opcion 1
        session.clear() #opcion 2
        flash("Saliste sin problemas.", "info")

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
