from flask import render_template, redirect, request, session, flash
from flask_app.models.asesoria import Asesoria
from flask_app.models.usuario import Usuario
from flask_app import app
from flask_app.forms import AsesoriaForm
from flask_app.config.mysqlconnection import connectToMySQL

@app.route("/dashboard")
def dashboard():
    print("Entrando a la función dashboard")
    if "usuario_id" not in session:
        print("Usuario no logueado, redirigiendo a /")
        return redirect("/")
    usuario_id = session["usuario_id"]

    usuario = Usuario.obtener_por_id(usuario_id)

    asesorias = Asesoria.obtener_todos_con_creador()

    print("Renderizando dashboard.html")
    return render_template("dashboard.html", usuario=usuario, asesorias=asesorias)

@app.route("/nueva_asesoria")
def nueva_asesoria():
    print("Entrando a la función nueva_asesoria")
    if "usuario_id" not in session:
        print("Usuario no logueado, redirigiendo a /")
        return redirect("/")
    form = AsesoriaForm()
    print("Renderizando nueva_asesoria.html")
    return render_template("nueva_asesoria.html", form=form)

@app.route("/crear_asesoria", methods=['POST'])
def crear_asesoria():
    print("Entrando a la función crear_asesoria")
    if "usuario_id" not in session:
        print("Usuario no logueado, redirigiendo a /")
        return redirect("/")

    form = AsesoriaForm(request.form)

    if form.validate():
        print("Formulario validado correctamente")
        data = {
            "tema": form.tema.data,
            "duracion": form.duracion.data,
            "fecha": form.fecha.data,
            "notas": form.notas.data,
            "usuario_id": session["usuario_id"],
            "tutor": form.tutor.data
        }
        print("Datos para guardar:", data)
        Asesoria.guardar(data)
        print("Asesoria guardada correctamente")
        return redirect("/dashboard")
    else:
        print("Error en la validación del formulario")
        return render_template("nueva_asesoria.html", form=form)

@app.route("/ver_asesoria/<int:asesoria_id>")
def ver_asesoria(asesoria_id):
    print(f"Entrando a la función ver_asesoria con ID: {asesoria_id}")
    if "usuario_id" not in session:
        print("Usuario no logueado, redirigiendo a /")
        return redirect("/")

    asesoria = Asesoria.obtener_uno({"id": asesoria_id})
    usuario = Usuario.obtener_por_id(session["usuario_id"])
    tutores = [('Camilo', 'Camilo'), ('Seba', 'Seba'), ('Humilda', 'Humilda'), ('Tutor4', 'Tutor 4'), ('Tutor5', 'Tutor 5')]
    print("Renderizando ver_asesoria.html")
    return render_template("ver_asesoria.html", asesoria=asesoria, user=usuario, tutores=tutores)

@app.route("/editar_asesoria/<int:asesoria_id>")
def editar_asesoria(asesoria_id):
    print(f"Entrando a la función editar_asesoria con ID: {asesoria_id}")
    if "usuario_id" not in session:
        print("Usuario no logueado, redirigiendo a /")
        return redirect("/")

    asesoria = Asesoria.obtener_uno({"id": asesoria_id})
    if asesoria.usuario_id != session["usuario_id"]:
        print("Usuario no autorizado para editar esta asesoria, redirigiendo a /dashboard")
        return redirect("/dashboard")

    form = AsesoriaForm()
    print("Renderizando editar_asesoria.html")
    return render_template("editar_asesoria.html", asesoria=asesoria, form=form)

@app.route("/actualizar_asesoria/<int:asesoria_id>", methods=['POST'])
def actualizar_asesoria(asesoria_id):
    print(f"Entrando a la función actualizar_asesoria con ID: {asesoria_id}")
    if "usuario_id" not in session:
        print("Usuario no logueado, redirigiendo a /")
        return redirect("/")

    form = AsesoriaForm(request.form)

    if form.validate():
        print("Formulario validado correctamente")
        data = {
            "id": form.id.data,
            "tema": form.tema.data,
            "duracion": form.duracion.data,
            "fecha": form.fecha.data,
            "notas": form.notas.data,
            "usuario_id": session["usuario_id"],
            "tutor": form.tutor.data
        }
        print("Datos para actualizar:", data)
        Asesoria.actualizar(data)
        print("Asesoria actualizada correctamente")
        return redirect("/dashboard")
    else:
        print("Error en la validación del formulario")
        asesoria = Asesoria.obtener_uno({"id": asesoria_id})
        return render_template("editar_asesoria.html", asesoria=asesoria, form=form)

@app.route("/borrar_asesoria/<int:asesoria_id>")
def borrar_asesoria(asesoria_id):
    print(f"Entrando a la función borrar_asesoria con ID: {asesoria_id}")
    if "usuario_id" not in session:
        print("Usuario no logueado, redirigiendo a /")
        return redirect("/")

    Asesoria.borrar({"id": asesoria_id, "usuario_id": session["usuario_id"]})
    print("Asesoria borrada correctamente")
    return redirect("/dashboard")

@app.route("/cambiar_tutor/<int:asesoria_id>", methods=['POST'])
def cambiar_tutor(asesoria_id):
    print(f"Entrando a la función cambiar_tutor con ID: {asesoria_id}")
    if "usuario_id" not in session:
        print("Usuario no logueado, redirigiendo a /")
        return redirect("/")

    tutor = request.form['tutor']
    print(f"El nuevo tutor es: {tutor}")
    data = {
        "id": asesoria_id,
        "tutor": tutor
    }
    Asesoria.cambiar_tutor(data)
    print("Tutor cambiado correctamente")
    return redirect("/dashboard")