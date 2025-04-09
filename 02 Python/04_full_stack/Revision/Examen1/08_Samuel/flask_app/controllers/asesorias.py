from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.asesoria import Asesoria
from flask_app.models.usuario import Usuario

@app.route('/nueva')
def nueva_asesoria():
    if 'usuario_id' not in session:
        flash("El usuario debe haber iniciado sesión para ver esta página", "info")
        return redirect('/login')
    
    usuarios = Usuario.get_all()

    tutores = [u for u in usuarios if u.id != session['usuario_id']]
    return render_template('nueva_asesoria.html', tutores=tutores)

@app.route('/crear_asesoria', methods=['POST'])
def crear_asesoria():
    if 'usuario_id' not in session:
        return redirect('/login')
    
    if not Asesoria.validar(request.form):
        return redirect('/nueva')
    
    data = {
        'tema': request.form['tema'],
        'fecha': request.form['fecha'],
        'duracion': request.form['duracion'],
        'notas': request.form['notas'],
        'usuario_id': session['usuario_id'],
        'tutor_id': request.form['tutor_id'] if 'tutor_id' in request.form else None
    }
    Asesoria.save(data)
    
    return redirect('/dashboard')

@app.route('/editar/<int:id>')
def editar_asesoria(id):
    if 'usuario_id' not in session:
        return redirect('/login')
    
    asesoria = Asesoria.get_by_id(id)
    
    if not asesoria:
        return redirect('/dashboard')
    
    if asesoria['usuario_id'] != session['usuario_id']:
        flash("No puedes editar una asesoría que no creaste", "info")
        return redirect('/dashboard')
    
    usuarios = Usuario.get_all()
    tutores = [u for u in usuarios if u.id != session['usuario_id']]
    
    return render_template('editar_asesoria.html', asesoria=asesoria, tutores=tutores)

@app.route('/actualizar_asesoria', methods=['POST'])
def actualizar_asesoria():
    if 'usuario_id' not in session:
        return redirect('/login')
    
    if not Asesoria.validar(request.form):
        return redirect(f'/editar/{request.form["id"]}')
    
    data = {
        'id': request.form['id'],
        'tema': request.form['tema'],
        'fecha': request.form['fecha'],
        'duracion': request.form['duracion'],
        'notas': request.form['notas'],
        'tutor_id': request.form['tutor_id'] if 'tutor_id' in request.form else None
    }
    
    Asesoria.update(data)
    
    return redirect('/dashboard')

@app.route('/borrar/<int:id>')
def borrar_asesoria(id):
    if 'usuario_id' not in session:
        return redirect('/login')
    
    asesoria = Asesoria.get_by_id(id)
    
    if not asesoria:
        return redirect('/dashboard')
    
    if asesoria['usuario_id'] != session['usuario_id']:
        flash("No puedes borrar una asesoría que no creaste", "info")
        return redirect('/dashboard')
    
    Asesoria.delete(id)
    
    return redirect('/dashboard')

@app.route('/ver/<int:id>')
def ver_asesoria(id):
    if 'usuario_id' not in session:
        return redirect('/login')
    
    asesoria = Asesoria.get_by_id(id)
    
    if not asesoria:
        return redirect('/dashboard')
    
    usuarios = Usuario.get_all()
    tutores = [u for u in usuarios if u.id != asesoria['usuario_id']]
    
    return render_template('ver_asesoria.html', asesoria=asesoria, tutores=tutores)

@app.route('/cambiar_tutor', methods=['POST'])
def cambiar_tutor():
    if 'usuario_id' not in session:
        return redirect('/login')
    
    data = {
        'id': request.form['id'],
        'tutor_id': request.form['tutor_id']
    }
    Asesoria.update_tutor(data)
    
    return redirect(f'/ver/{request.form["id"]}')