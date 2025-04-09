from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuarios import Usuario
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 

@app.route("/")
def home():

    if 'usuario' not in session:
        return redirect("/login")

    return redirect("/asesorias")


@app.route("/login")
def login():
    if 'usuario' in session:
        flash("No seas loco. Ya estás logeado.", "info")
        return redirect("/")

    return render_template("login.html")

@app.route("/login_usuario", methods=["POST"])
def login_usuario():
    print(request.form)
    
    usuario = Usuario.get_by_email(request.form['email'])
    if not usuario:
        flash("Correo no existe o contraseña mal ingresada", "error")
        return redirect("/login")
    
    if not bcrypt.check_password_hash(usuario.contraseña, request.form['password']):
        flash("Correo no existe o contraseña mal ingresada", "error")
        return redirect("/login")

    flash("Logeado correctamente", "success")
    session['usuario'] = {
        'email': usuario.email,
        'id': usuario.id,
        'nombre': usuario.nombre
    }
    return redirect("/")

@app.route("/salir")
def salir():

    if 'usuario' in session:
        del session['usuario'] 
        session.clear()
        flash("Saliste sin problemas.", "info")

    return redirect("/")

@app.route("/registrar_usuario", methods=["POST"])
def registrar_usuario():

    if not Usuario.validar(request.form):
        return redirect('/login')
    
    datos = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'contraseña': bcrypt.generate_password_hash(request.form['password']),
    }

    Usuario.save(datos)
    flash("Usuario agregado correctamente", "success")


    return redirect("/login")