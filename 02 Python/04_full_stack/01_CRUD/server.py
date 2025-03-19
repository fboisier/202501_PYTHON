import os

from flask import Flask, render_template, flash, request, redirect, session
from model.usuarios import Usuario
from model.usuario_avanzado import UsuarioAvanzado
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def home():

    if 'usuario' not in session:
        return redirect("/login")

    return render_template("inicio.html")

@app.route("/usuarios")
def listar_usuarios():

    usuarios = Usuario.get_all()

    return render_template("usuarios.html", usuarios=usuarios)

@app.route("/usuarios_avanzado")
def listar_usuarios_avanzado():

    usuarios = UsuarioAvanzado.get_all()

    return render_template("usuarios.html", usuarios=usuarios)

@app.route("/usuarios/<id>")
def detalle_usuario(id):

    usuario = Usuario.get_data_by_id(id)

    return render_template("usuarios_detalle.html", usuario=usuario)

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
    app.run(debug=os.getenv("DEBUG"), port=os.getenv("PUERTO"))
