from flask_app import app
from flask_app.model.usuarios import Usuario
from flask_app.model.usuario_avanzado import UsuarioAvanzado
from flask import render_template

@app.route("/usuarios")
def listar_usuarios():

    usuarios = Usuario.get_all()

    return render_template("usuarios/usuarios.html", usuarios=usuarios)

@app.route("/usuarios_avanzado")
def listar_usuarios_avanzado():

    usuarios = UsuarioAvanzado.get_all()

    return render_template("usuarios.html", usuarios=usuarios)

@app.route("/usuarios/<id>")
def detalle_usuario(id):

    usuario = Usuario.get(id)

    return render_template("usuarios/usuarios_detalle.html", usuario=usuario)
