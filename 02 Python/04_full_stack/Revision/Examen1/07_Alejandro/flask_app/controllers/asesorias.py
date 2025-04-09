from flask import render_template, redirect, request, session, flash
from flask_app.models.asesoria import Asesoria
from datetime import datetime
from flask_app import app

@app.route('/asesorias')
def asesorias():
    if 'alumno_id' not in session:
        return redirect('/')
    
    from flask_app.models.alumno import Alumno
    alumno = Alumno.get_by_id({'id': session['alumno_id']})
    asesorias = Asesoria.obtener_todas()
    
    return render_template('asesorias.html', alumno=alumno, asesorias=asesorias)


@app.route('/nueva')
def nueva():
    if 'alumno_id' not in session:
        return redirect('/')
    hoy = datetime.today().strftime('%Y-%m-%d')
    return render_template('nueva.html', fecha_actual=hoy)


@app.route('/crear_asesoria', methods=['POST'])

def crear():
    print("Datos recibidos:", request.form)
    if 'alumno_id' not in session:
        return redirect('/')

    try:
        datos = {
            'tema': request.form['tema'],
            'fecha': request.form['fecha'],
            'tiempo': request.form['tiempo'],
            'nota': request.form['nota'],
            'alumno_id': session['alumno_id']
        }
    except KeyError as e:
        flash(f"Falta el campo: {e.args[0]}", "asesoria")
        return redirect('/nueva')
    except ValueError:
        flash("Datos inválidos. Verifica la fecha y la duración.", "asesoria")
        return redirect('/nueva')

    if not Asesoria.validar_asesoria(datos):
        return redirect('/nueva')

    Asesoria.guardar(datos)
    flash("Asesoría creada correctamente", "asesoria")
    return redirect('/asesorias')


@app.route('/asesoria/<int:id>/ver')
def ver_asesoria(id):
    if 'alumno_id' not in session:
        return redirect('/')
    data = {'id': id}
    asesoria = Asesoria.obtener_por_id_con_alumno(data)
    if not asesoria:
        flash("Asesoría no encontrada", "asesoria")
        return redirect('/asesorias')
    return render_template('ver.html', asesoria=asesoria)

@app.route('/asesoria/<int:id>/editar')
def editar(id):
    if 'alumno_id' not in session:
        return redirect('/')
    data = {'id': id}
    asesoria = Asesoria.obtener_por_id(data)
    if asesoria.alumno_id != session['alumno_id']:
        flash('No tienes permiso para editar esta asesoría.', 'asesoria')
        return redirect('/asesorias')
    hoy = datetime.today().strftime('%Y-%m-%d')
    return render_template('editar.html', asesoria=asesoria, fecha_actual=hoy)


@app.route('/asesoria/<int:id>/actualizar', methods=['POST'])
def actualizar(id):
    if 'alumno_id' not in session:
        return redirect('/')

    try:
        datos = {
            'id': id,
            'tema': request.form['tema'],
            'fecha': request.form['fecha'], 
            'tiempo': float(request.form['tiempo']), 
            'nota': request.form['nota'],
            'alumno_id': session['alumno_id']
        }
    except KeyError as e:
        flash(f"Falta el campo: {e.args[0]}", "asesoria")
        return redirect(f'/asesoria/{id}/editar')
    except ValueError:
        flash("Datos inválidos. Verifica la fecha y la duración.", "asesoria")
        return redirect(f'/asesoria/{id}/editar')

    if not Asesoria.validar_asesoria(datos):
        return redirect(f'/asesoria/{id}/editar')

    Asesoria.actualizar(datos)
    flash("Asesoría actualizada correctamente", "asesoria")
    return redirect('/asesorias')


@app.route('/asesoria/<int:id>/eliminar')
def eliminar(id):
    if 'alumno_id' not in session:
        return redirect('/')
    data = {'id': id}
    asesoria = Asesoria.obtener_por_id(data)
    if asesoria and asesoria.alumno_id == session['alumno_id']:
        Asesoria.eliminar(data)
        flash("Asesoría eliminada correctamente", "asesoria")
    else:
        flash("No tienes permiso para eliminar esta asesoría", "asesoria")
    return redirect('/asesorias')