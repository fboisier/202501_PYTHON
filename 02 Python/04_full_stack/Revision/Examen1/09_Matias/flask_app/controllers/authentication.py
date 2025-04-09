from flask import render_template, redirect, request, session, flash
from flask_app import app, bcrypt
from flask_app.models.usuario import Usuario

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/registro', methods=['POST'])
def registro():
    if not Usuario.validate_registro(request.form):
        return redirect('/')
    
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'contraseña': bcrypt.generate_password_hash(request.form['contraseña'])
    }
    
    id = Usuario.save(data)
    session['usuario_id'] = id
    return redirect('/inicio')

@app.route('/login', methods=['POST'])
def login():
    if not Usuario.validate_login(request.form):
        return redirect('/')
    
    usuario = Usuario.get_by_email({'email': request.form['email']})
    if not usuario:
        flash("Email no registrado.", 'login')
        return redirect('/')
    
    if not bcrypt.check_password_hash(usuario.contraseña, request.form['contraseña']):
        flash("Contraseña incorrecta.", 'login')
        return redirect('/')
    
    session['usuario_id'] = usuario.id
    return redirect('/inicio')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')