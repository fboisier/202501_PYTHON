from flask import render_template, request, redirect, flash, session
from flask_app.models.alumno import Alumno
from flask_bcrypt import Bcrypt
from flask_app import app

bcrypt = Bcrypt(app)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/registro", methods=["POST"])
def registrar():
    if not Alumno.validar_registro(request.form):
        return redirect("/")
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "correo": request.form['correo'],
        "password": pw_hash
    }
    alumno_id = Alumno.save(data)
    session['alumno_id'] = alumno_id
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    print("Datos recibidos en /login:", request.form)
    if not Alumno.validar_login(request.form):
        return redirect("/")
    
    alumno = Alumno.get_by_correo({"correo": request.form['correo']})
    if not alumno:
        flash("Contraseña o correo incorrecta", "login")
        return redirect("/")

    if not bcrypt.check_password_hash(alumno.password, request.form['password']):
        flash("Contraseña o correo incorrecta", "login")
        return redirect("/")
    
    session['alumno_id'] = alumno.id
    return redirect("/asesorias")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
