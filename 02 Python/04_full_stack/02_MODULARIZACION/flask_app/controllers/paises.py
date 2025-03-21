from flask_app import app
from flask_app.model.paises import Pais
from flask import render_template, request, flash, redirect

@app.route("/paises")
def listar_paises():

    datos = Pais.get_all()
    sujeto = "paises"

    return render_template("paises/listado.html", datos=datos, sujeto=sujeto)


@app.route("/paises/<id>")
def detalle_pais(id):

    objeto = Pais.get(id)
    sujeto = "país"

    return render_template("paises/detalle.html", objeto=objeto, sujeto=sujeto)


@app.route("/paises/crear")
def pais_crear():

    return render_template("paises/formulario.html", sujeto='pais')



@app.route("/paises", methods=["POST"])
def procesar_pais():
    print(request.form)
    datos = {
        'nombre': request.form['nombre']
    }

    Pais.save(datos)
    flash("Pais ingresado correctamente", "success")
    return redirect("/paises")
