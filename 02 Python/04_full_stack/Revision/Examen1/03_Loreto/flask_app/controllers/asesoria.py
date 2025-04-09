from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.usuarios import Usuario
from flask_app.models.asesorias import Asesoria
from flask_bcrypt import Bcrypt
from datetime import datetime

bcrypt = Bcrypt(app)


@app.route("/asesorias/nuevo")
def nueva_asesoria():
    if 'usuario' not in session:
        flash("Debes iniciar sesión para acceder a esta página", "error")
        return redirect("/login")

    tutores = ["Juan", "María", "Alicia"]
    return render_template("asesorias/solicitar_asesoria.html", tutores=tutores)

@app.route("/asesorias/crear", methods=['POST'])
def crear_asesoria():
    if 'usuario' not in session:
        return redirect("/login")

    datos = {
        "tema": request.form.get('tema', '').strip(),
        "fecha": request.form.get('fecha', ''),
        "duracion": request.form.get('duracion', ''),
        "notas": request.form.get('notas', '').strip(),
        "tutor": request.form.get('tutor'),
        "usuarios_id": session['usuario']['id']
    }

    print("Recibí datos del formulario:", datos)

    if not Asesoria.validar(datos):
        print("Validación falló")
        return redirect("/asesorias/nuevo")

    print("Guardando en base de datos...")
    Asesoria.save(datos)
    flash("Asesoría creada correctamente", "success")
    return redirect("/")

# Detalle asesoria
@app.route("/asesorias/<int:id>")
def detalle_asesoria(id):
    asesoria = Asesoria.get_data_by_id(id)
    if not asesoria:
        return "Asesoría no encontrada", 404

    tutores = ["Juan", "María", "Alicia"]
    return render_template("asesorias/asesorias_detalle.html", asesoria=asesoria, tutores=tutores)

# Cambiar tutor 
@app.route("/cambiar_tutor/<int:id>", methods=['POST'])
def cambiar_tutor(id):
    if 'usuario' not in session:
        return redirect("/login")

    asesoria = Asesoria.get_data_by_id(id)
    if not asesoria or asesoria.usuarios_id != session['usuario']['id']:
        return "No autorizado", 403

    nuevo_tutor = request.form.get('nuevo_tutor')
    if nuevo_tutor:
        Asesoria.update_tutor({"id": id, "tutor": nuevo_tutor})
        flash("Tutor cambiado correctamente", "success")
    else:
        flash("Debes seleccionar un nuevo tutor", "error")

    return redirect(f"/asesorias/{id}")

# Editar
@app.route("/editar_asesoria/<int:id>")
def editar_asesoria(id):
    if 'usuario' not in session:
        flash("Debes iniciar sesión para acceder a esta página", "error")
        return redirect("/login")

    asesoria = Asesoria.get_data_by_id(id)
    if not asesoria or asesoria.usuarios_id != session['usuario']['id']:
        return "No autorizado", 403

    tutores = ["Juan", "María", "Alicia"]
    return render_template("asesorias/editar_asesoria.html", asesoria=asesoria, tutores=tutores)

# Actualización 
@app.route("/actualizar_asesoria/<int:id>", methods=['POST'])
def actualizar_asesoria(id):
    if 'usuario' not in session:
        return redirect("/login")

    datos = {
        "id": id,
        "tema": request.form.get('tema', '').strip(),
        "fecha": request.form.get('fecha', ''),
        "duracion": request.form.get('duracion', ''),
        "notas": request.form.get('notas', '').strip(),
        "tutor": request.form.get('tutor'),
        "usuarios_id": session['usuario']['id']
    }

    if not Asesoria.validar(datos):
        return redirect(f"/editar_asesoria/{id}")

    Asesoria.update(datos)
    flash("Asesoría actualizada correctamente", "success")
    return redirect("/dashboard")

#Eliminar
@app.route("/eliminar_asesoria/<int:id>", methods=["POST"])
def eliminar_asesoria(id):
    if 'usuario' not in session:
        return redirect("/login")

    asesoria = Asesoria.get_data_by_id(id)
    if not asesoria or asesoria.usuarios_id != session['usuario']['id']:
        return "No autorizado", 403

    Asesoria.delete({"id": id})
    flash("Asesoría eliminada", "success")
    return redirect("/")
