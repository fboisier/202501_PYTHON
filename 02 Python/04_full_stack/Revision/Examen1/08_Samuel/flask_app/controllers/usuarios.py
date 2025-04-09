from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.usuario import Usuario
from flask_app.models.asesoria import Asesoria
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'usuario_id' in session:
        return redirect('/dashboard')
    return redirect('/login')

@app.route('/login')
def login():
    if 'usuario_id' in session:
        return redirect('/dashboard')
    return render_template('login.html')

@app.route('/login_usuario', methods=['POST'])
def login_usuario():
    usuario = Usuario.get_by_email(request.form['email'])
    
    if not usuario:
        flash("Correo no existe o contraseña mal ingresada", "login")
        return redirect('/login')
    
    if not bcrypt.check_password_hash(usuario.contraseña, request.form['password']):
        flash("Correo no existe o contraseña mal ingresada", "login")
        return redirect('/login')
    
    session['usuario_id'] = usuario.id
    session['usuario_nombre'] = usuario.nombre
    
    return redirect('/dashboard')

@app.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
    if not Usuario.validar(request.form):
        return redirect('/login')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'contraseña': pw_hash
    }
    usuario_id = Usuario.save(data)
    
    session['usuario_id'] = usuario_id
    session['usuario_nombre'] = request.form['nombre']
    
    return redirect('/dashboard')

@app.route('/cerrar_sesion')
def cerrar_sesion():
    session.clear()
    return redirect('/login')

@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect('/login')
    
    asesorias = Asesoria.get_all_current()
    
    return render_template('dashboard.html', asesorias=asesorias)