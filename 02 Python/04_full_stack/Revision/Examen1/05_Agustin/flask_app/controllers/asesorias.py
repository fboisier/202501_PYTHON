from flask_app import app
from flask_app.models.asesorias import Asesoria
from flask_app.models.usuarios import Usuario
from flask import render_template, request, flash, redirect, session
from flask_app.utils.decoradores import login_required
import pprint


@app.route("/asesorias")
@login_required
def mostrar_asesorias():
    datos = Asesoria.get_all_with_users()
    sujeto = "asesorias"
    return render_template('inicio.html', datos=datos, sujeto=sujeto)


@app.route("/asesorias/<id>")
@login_required
def detalle_asesoria(id):
    objeto = Asesoria.get(id)
    print("Objeto obtenido:", objeto)  
    if not objeto:
        flash("La asesoría no existe o no se encontró.", "error")
        return redirect("/asesorias")
    sujeto = "asesorias"
    return render_template("detalle.html", objeto=objeto, sujeto=sujeto)



# region CREAR
@app.route("/asesorias/crear")
@login_required
def asesoria_crear():
    usuarios = Usuario.get_all() 
    return render_template("formulario.html", sujeto='asesoria', usuarios=usuarios)

@app.route("/asesorias", methods=["POST"])
@login_required
def procesar_asesoria():
    print("FORMULARIO", request.form)
    if 'usuario' not in session:
        flash("Debes iniciar sesión para realizar esta acción.", "error")
        return redirect("/login")
    
    datos = {
        'tema': request.form['tema'],
        'duracion': request.form['duracion'],
        'notas': request.form['notas'],
        'usuario_id': session['usuario']['id'] 
    }
    Asesoria.save(datos)
    flash("Asesoría ingresada correctamente", "success")
    return redirect("/asesorias")
# endregion



# region EDITAR
@app.route("/asesorias/<int:id>/editar")
@login_required
def asesoria_actualizar(id):
    objeto = Asesoria.get(id)
    print("OBJETO: ", id, objeto.__dict__) 
    sujeto = "asesoria"
    usuarios = Usuario.get_all()
    return render_template("formulario_editar.html", sujeto=sujeto, objeto=objeto, usuarios=usuarios)

@app.route("/asesorias/<int:id>/editar", methods=["POST"])
@login_required
def procesar_editar_asesoria(id):
    print("FORMULARIO ENVIADO:", request.form)
    datos = {
        'id': id,
        'tema': request.form['tema'],
        'duracion': request.form['duracion'],
        'notas': request.form['notas'],
        'usuario_id': session['usuario']['id'] 
    }
    Asesoria.update(datos)
    flash("Asesoría actualizada correctamente", "success")
    return redirect("/asesorias")
# endregion

# region ELIMINAR
@app.route("/asesorias/<int:id>/eliminar", methods=["POST"])
@login_required
def procesar_eliminado_asesoria(id):
    Asesoria.delete(id)
    flash("Asesoría eliminada correctamente", "success")
    return redirect("/asesorias")
# endregion