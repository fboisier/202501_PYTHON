from flask import render_template, redirect, request, session, flash
from flask_app import app, bcrypt
from flask_app.models.usuario import Usuario

@app.route("/")
def index():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    print("Entrando a la función login")
    if request.method == "POST":
        print("Método POST detectado")
        usuario = Usuario.obtener_por_email({"email": request.form["email"]})

        if not usuario:
            print("Correo no registrado")
            flash("Correo no registrado", "error_login")
            return redirect("/login")

        if not bcrypt.check_password_hash(usuario.password, request.form["password"]):
            print("Contraseña incorrecta")
            flash("Contraseña incorrecta", "error_login")
            return redirect("/login")

        print("Login exitoso")
        session["usuario_id"] = usuario.id
        return redirect("/dashboard")
    print("Renderizando login.html")
    return render_template("login.html")

@app.route("/registrar", methods=["POST"])
def registrar():
    print("Entrando a la función registrar")
    print("Datos del formulario:", request.form)
    if not Usuario.validar_registro(request.form):
        print("Error de validación")
        return redirect("/login")

    password_hash = bcrypt.generate_password_hash(request.form["password"]).decode('utf-8')
    print("Contraseña hasheada:", password_hash)

    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"],
        "password": password_hash
    }
    print("Datos para guardar:", data)

    id_usuario = Usuario.guardar(data)
    print("Usuario guardado con ID:", id_usuario)
    session["usuario_id"] = id_usuario
    return redirect("/dashboard")


@app.route("/logout")
def logout():
    print("Cerrando sesión")
    session.clear()
    return redirect("/login")