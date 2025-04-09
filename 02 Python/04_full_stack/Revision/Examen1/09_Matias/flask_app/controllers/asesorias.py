from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.asesoria import Asesoria
from flask_app.models.usuario import Usuario
from datetime import datetime

@app.route('/inicio')
def inicio():
    if 'usuario_id' not in session:
        return redirect('/')
    
    data = {'alumno_id': session['usuario_id']}
    asesorias = Asesoria.get_by_alumno(data)
    usuario = Usuario.get_by_id({'id': session['usuario_id']})
    return render_template('inicio.html', asesorias=asesorias, usuario=usuario)

@app.route('/solicitar_asesoria')
def solicitar_asesoria():
    if 'usuario_id' not in session:
        return redirect('/')
    
    tutores = Usuario.get_all_except(session['usuario_id'])
    return render_template('solicitar_asesoria.html', tutores=tutores)

@app.route('/crear_asesoria', methods=['POST'])
def crear_asesoria():
    if 'usuario_id' not in session:
        return redirect('/')
    
    if not Asesoria.validate_asesoria(request.form):
        return redirect('/solicitar_asesoria')
    
    data = {
        'tema': request.form['tema'],
        'fecha': request.form['fecha'],
        'duracion': request.form['duracion'],
        'notas': request.form['notas'],
        'alumno_id': session['usuario_id'],
        'tutor_id': request.form.get('tutor_id', None)
    }
    
    Asesoria.save(data)
    return redirect('/inicio')

@app.route('/editar_asesoria/<int:id>')
def editar_asesoria(id):
    if 'usuario_id' not in session:
        return redirect('/')
    
    data = {'id': id}
    asesoria = Asesoria.get_by_id(data)
    tutores = Usuario.get_all_except(session['usuario_id'])
    return render_template('editar_asesoria.html', asesoria=asesoria, tutores=tutores)

@app.route('/actualizar_asesoria', methods=['POST'])
def actualizar_asesoria():
    if 'usuario_id' not in session:
        return redirect('/')
    
    if not Asesoria.validate_asesoria(request.form):
        return redirect(f"/editar_asesoria/{request.form['id']}")
    
    data = {
        'id': request.form['id'],
        'tema': request.form['tema'],
        'fecha': request.form['fecha'],
        'duracion': request.form['duracion'],
        'notas': request.form['notas'],
        'tutor_id': request.form.get('tutor_id', None)
    }
    
    Asesoria.update(data)
    return redirect('/inicio')

@app.route('/ver_asesoria/<int:id>')
def ver_asesoria(id):
    if 'usuario_id' not in session:
        return redirect('/')
    
    data = {'id': id}
    asesoria = Asesoria.get_by_id(data)
    tutor = Usuario.get_by_id({'id': asesoria.tutor_id}) if asesoria.tutor_id else None
    alumno = Usuario.get_by_id({'id': asesoria.alumno_id})
    tutores = Usuario.get_all_except(asesoria.alumno_id)
    
    return render_template('detalle_asesoria.html', 
                         asesoria=asesoria, 
                         tutor=tutor, 
                         alumno=alumno, 
                         tutores=tutores)

@app.route('/asignar_tutor/<int:asesoria_id>', methods=['POST'])
def asignar_tutor(asesoria_id):
    if 'usuario_id' not in session:
        return redirect('/')
    
    data = {
        'id': asesoria_id,
        'tutor_id': request.form['tutor_id']
    }
    
    Asesoria.update_tutor(data)
    return redirect(f'/ver_asesoria/{asesoria_id}')

@app.route('/eliminar_asesoria/<int:id>')
def eliminar_asesoria(id):
    if 'usuario_id' not in session:
        return redirect('/')
    
    data = {'id': id}
    Asesoria.delete(data)
    return redirect('/inicio')