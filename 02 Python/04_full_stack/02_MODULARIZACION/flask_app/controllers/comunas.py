from flask_app import app
from flask_app.model.comunas import Comuna
from flask_app.model.paises import Pais
from flask import render_template, request, flash, redirect

@app.route("/comunas")
def listar_comunas():
    datos = Comuna.get_all_with_country()
    sujeto = "comunas"
    return render_template("comunas/listado.html", datos=datos, sujeto=sujeto)

@app.route("/comunas/<id>")
def detalle_comuna(id):
    objeto = Comuna.get(id)
    sujeto = "comuna"
    return render_template("comunas/detalle.html", objeto=objeto, sujeto=sujeto)

# region CREAR
@app.route("/comunas/crear")
def comuna_crear():
    paises = Pais.get_all()
    return render_template("comunas/formulario.html", sujeto='comuna', paises=paises)

@app.route("/comunas", methods=["POST"])
def procesar_comuna():
    print("FORMULARIO", request.form)
    datos = {
        'nombre': request.form['nombre'],
        'pais_id': request.form['pais_id']
    }
    Comuna.save(datos)
    flash("Comuna ingresada correctamente", "success")
    return redirect("/comunas")
# endregion

# region EDITAR
@app.route("/comunas/<int:id>/editar")
def comuna_actualizar(id):
    objeto = Comuna.get(id)
    print("OBJETO: ", id , objeto.__dict__)
    sujeto = "comuna"
    paises = Pais.get_all()
    return render_template("comunas/formulario_editar.html", sujeto=sujeto, objeto=objeto, paises=paises)

@app.route("/comunas/<int:id>/editar", methods=["POST"])
def procesar_editar_comuna(id):
    print("FORMULARIO", request.form)
    objeto = Comuna.get(id)
    objeto.nombre = request.form['nombre']
    objeto.pais_id = request.form['pais_id']
    objeto.update()
    flash("Comuna actualizada correctamente", "success")
    return redirect("/comunas")
# endregion

@app.route("/comunas/<int:id>/eliminar")
def procesar_eliminado_comuna(id):
    Comuna.delete(id)
    flash("Comuna eliminada correctamente", "success")
    return redirect("/comunas")
