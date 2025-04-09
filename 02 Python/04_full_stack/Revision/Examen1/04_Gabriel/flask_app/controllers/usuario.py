from flask_app import app
from flask_app.models.usuarios import Usuario
from flask_app.models.asesorias import Asesoria
from flask import render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def registro():
    return render_template("login.html")


@app.route('/registrar_usuario', methods=[ 'POST'])
def registrar_usuario():
    print(request.form)

    if not Usuario.validar_usuario(request.form):
        return redirect("/")
    datos = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password']),
    }

    if request.form['password'] != request.form['confirm_password']:
        flash("Las contraseñas no coinciden", "error_confirm_password")
        return redirect("/")

    Usuario.save(datos)
    flash("Usuario agregado correctamente", "success")

    return redirect("/")

@app.route("/login_usuario", methods=["POST"])
def login_usuario():
    print(request.form)
    
    usuario = Usuario.get_by_email(request.form['email'])
    if not usuario:
        flash("Correo no existe o contraseña mal ingresada", "error")
        return redirect("/")
    
    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("Correo no existe o contraseña mal ingresada", "error")
        return redirect("/")
    
    flash("Logeado correctamente", "success")
    session['usuario'] = {
        'nombre': usuario.nombre,
        'apellido': usuario.apellido,
        'email': usuario.email
    }
    return redirect("/dashboard")

@app.route("/logout")
def logout():

    if 'usuario' in session:
        del session['usuario']
        session.clear()
        flash("Saliste de la sesión.", "info")

    return redirect("/")

@app.route("/dashboard")
def home():

    if 'usuario' not in session:
        return redirect("/")
    
    usuarios = Usuario.get_all()
    if not usuarios:
        usuarios = []
    asesorias = Asesoria.get_all()
    if not asesorias:
        asesorias = []
    

    return render_template("dashboard.html", username = session['usuario']['nombre'], asesorias = asesorias, usuarios = usuarios)

@app.route("/nueva")
def crear_asesoria():

    if 'usuario' not in session:
        return redirect("/")
    
    return render_template("crear_asesoria.html", username = session['usuario']['nombre'])

@app.route("/nueva", methods=["POST"])
def crear_asesoria_post():
    print(request.form)
    if 'usuario' not in session:
        return redirect("/")

    if not Asesoria.validar(request.form):
        return redirect("/nueva")

    data = {
        'tema': request.form['tema'],
        'fecha': request.form['fecha'],
        'duracion': request.form['duracion'],
        'notas': request.form['notas']
    }

    Asesoria.save(data)
    flash("Asesoria creada correctamente", "success")
    return redirect("/dashboard")

@app.route("/editar/<int:id>")
def editar_asesoria(id):

    if 'usuario' not in session:
        return redirect("/")
    
    asesorias = Asesoria.get_by_id(id)
    if not asesorias:
        asesorias = None

    return render_template("editar_asesoria.html", username = session['usuario']['nombre'], asesorias = asesorias)