from datetime import datetime

from flask import render_template, request ,redirect,session
from flask_app import app,bcrypt  # Importamos la app de la carpeta flask_app

from flask_app.models.usuario import Usuario, crear_usuario,obtener_usuario_por_email, obtener_todos_los_usuarios
from flask_app.models.asesoria import Asesoria, crear_asesoria, obtener_todas_las_asesorias, obtener_asesoria_por_id , editar_asesoria_por_id,eliminar_asesoria_por_id
@app.route("/inicio")
def cursos():
    return render_template("inicio.html")


import re


@app.route("/", methods=["GET",'POST'])
def inicio():
    if "id" in session:
        return redirect("/home")
    if request.method == 'GET':
        return render_template("inicio.html")
    # Obtener los datos del formulario
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    contrasena1 = request.form["password1"]
    contrasena2 = request.form["password2"]

    # Expresiones regulares para validaciones
    regex_nombre_apellido = r"^[a-zA-Z]{2,}$"  # Solo letras, al menos 2 caracteres
    regex_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"  # Formato de correo válido
    regex_contrasena = r"^(?=.*[A-Z])(?=.*\d).+$"  # Al menos una mayúscula y un número

    validaciones =[]
    # Validaciones
    if not re.match(regex_nombre_apellido, nombre):
        validaciones.append("El nombre debe contener solo letras y al menos 2 caracteres.")
        
    if not re.match(regex_nombre_apellido, apellido):
        validaciones.append("El apellido debe contener solo letras y al menos 2 caracteres.")
        
    if not re.match(regex_email, email):
        validaciones.append("El correo electrónico no tiene un formato válido.")
        
    if len(contrasena1) < 8:
        validaciones.append("La contraseña debe tener al menos 8 caracteres.")
    
    if not re.match(regex_contrasena, contrasena1):
        validaciones.append("La contraseña debe incluir al menos una letra mayúscula y un número.")
     
    if contrasena1 != contrasena2:
        validaciones.append("Las contraseñas no coinciden.")
        
    # Si todas las validaciones pasan
    usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "contrasena": bcrypt.generate_password_hash(contrasena1) 
    }
    
    if not validaciones:
        # Aquí puedes guardar el usuario en la base de datos
        id_usuario_creado=crear_usuario(usuario)
        print("ID del usuario creado:", id_usuario_creado)
        if id_usuario_creado == False:
            return render_template("inicio.html", 
                           validaciones_registro=["El correo electrónico ya está registrado."],
                           usuario=usuario)
        if id_usuario_creado != 0:
            session["id"] = id_usuario_creado
            session["nombre"] = nombre
            session["email"] = email
            return redirect("/home")
        return redirect("/inicio")
    
    
    return render_template("inicio.html", 
                           validaciones_registro=validaciones,
                           usuario=usuario)

@app.route("/home")
def home():
   
    if "id" in session:
        asesorias = [asesoria for asesoria in obtener_todas_las_asesorias() if asesoria.fecha >= datetime.now()]
        return render_template("home.html", id=session["id"], nombre=session["nombre"], asesorias=asesorias)
    return redirect("/inicio")

@app.route("/cerrar_sesion")
def cerrar_sesion():
    session.clear()
    return redirect("/inicio")


@app.route("/inicio_sesion", methods=["GET", "POST"])
def inicio_sesion():
    
    email = request.form['email']
    contrasena = request.form['contrasena']
    
    usuario = obtener_usuario_por_email(email)
    if usuario == False:
        return render_template("inicio.html", 
                               validaciones_login=["El correo electrónico no está registrado"])
    
    if usuario and bcrypt.check_password_hash(usuario.contrasena, contrasena):
        session["id"] = usuario.id
        session["nombre"] = usuario.nombre
        session["email"] = usuario.email
        return redirect("/home")
    else:
        return render_template("inicio.html", 
                               validaciones_login=["contraseña incorrectos."])


@app.route("/nueva", methods=["POST", "GET"])
def nueva_asesoria():
    if "id" not in session:
        return redirect("/inicio")
    if request.method == "GET":   
        return render_template("nueva_asesoria.html",usuario_id=session["id"],tutores=obtener_todos_los_usuarios())
    
    print("**********")
    print(request.form)
    print("**********")
    tema = request.form['tema']
    fecha = request.form['fecha']
    duracion = request.form['duracion']
    notas = request.form['notas']
    tutor = request.form['tutor']
    
    asesoria = {
        "tema": tema,
        "fecha": fecha,
        "duracion": duracion,
        "notas": notas,
        "id_usuario": session["id"],
        "tutor_id": tutor
    }
    
    validaciones =[]
    
    if not tema:
        validaciones.append("El tema no puede estar vacío.")
    if not fecha:
        validaciones.append("La fecha no puede estar vacía.")
    else:
        fecha_actual = datetime.now()
        fecha_ingresada = datetime.strptime(fecha, "%Y-%m-%dT%H:%M")
        if fecha_ingresada < fecha_actual:
            validaciones.append("La fecha no puede ser anterior a la fecha actual.")
    
    if not duracion:
        validaciones.append("La duración no puede estar vacía.")
    if float(duracion) <= 0:
        validaciones.append("La duración debe ser mayor a 0.")
    if float(duracion) > 8:
        validaciones.append("La duración no puede ser mayor a 8 horas.")
    if not tutor:
        validaciones.append("El tutor no puede estar vacío.")
    if not notas:
        validaciones.append("Las notas no pueden estar vacías.")
    
    if validaciones:
        return render_template("nueva_asesoria.html", 
                                validaciones_registro=validaciones,
                                usuario_id=session["id"],
                                asesoria=asesoria,
                                tutores=obtener_todos_los_usuarios())
    
    id_asesoria_creada = crear_asesoria(asesoria)
    
    if id_asesoria_creada:
        return redirect("/home")
    else:
        return render_template("nueva_asesoria.html", 
                               validaciones_registro=["Error al crear la asesoría."])


@app.route("/ver/<int:id>")
def ver_asesoria(id):
    if "id" not in session:
        return redirect("/inicio")
    asesoria = obtener_asesoria_por_id(id)
    
    if asesoria:
        return render_template("ver_asesoria.html", asesoria=asesoria)
    else:
        return redirect("/home")

@app.route("/eliminar/<int:id>")
def eliminar_asesoria(id):
    if "id" not in session:
        return redirect("/inicio")
    asesoria = obtener_asesoria_por_id(id)
    if asesoria:
        eliminar_asesoria_por_id(id)  
        return redirect("/home")
    else:
        return redirect("/home")
    
@app.route("/editar/<int:id>", methods=["POST", "GET"])
def editar_asesoria(id):
    if "id" not in session:
        return redirect("/inicio")
    if request.method == "GET":
        asesoria = obtener_asesoria_por_id(id)
        if asesoria:
            return render_template("editar_asesoria.html",usuario_id=session["id"], asesoria=asesoria,tutores=obtener_todos_los_usuarios())
        else:
            return redirect("/home")
    print("editar")
    print(request.form)
    print("**********")
    tema = request.form['tema']
    fecha = request.form['fecha']
    duracion = request.form['duracion']
    notas = request.form['notas']
    tutor = request.form['tutor']
    asesorias_editar = {
        "id": id,
        "tema": tema,
        "fecha": fecha,
        "duracion": duracion,
        "notas": notas,
        "id_usuario": session["id"],
        "tutor_id": tutor
    }
    validaciones =[]
    
    if not tema:
        validaciones.append("El tema no puede estar vacío.")
    if not fecha:
        validaciones.append("La fecha no puede estar vacía.")
    else:
        fecha_actual = datetime.now()
        fecha_ingresada = datetime.strptime(fecha, "%Y-%m-%dT%H:%M")
        if fecha_ingresada < fecha_actual:
            validaciones.append("La fecha no puede ser anterior a la fecha actual.")
    
    if not duracion:
        validaciones.append("La duración no puede estar vacía.")
    if float(duracion) <= 0:
        validaciones.append("La duración debe ser mayor a 0.")
    if float(duracion) > 8:
        validaciones.append("La duración no puede ser mayor a 8 horas.")
    if not tutor:
        validaciones.append("El tutor no puede estar vacío.")
    if not notas:
        validaciones.append("Las notas no pueden estar vacías.")
    
    if validaciones:
        print("validaciones")
        print(validaciones)
        print("**********")
        return render_template("editar_asesoria.html", 
                                validaciones_registro=validaciones,
                                usuario_id=session["id"],
                                asesoria=asesorias_editar,
                                tutores=obtener_todos_los_usuarios())
    
    
    
    editar_asesoria_por_id(asesorias_editar)
    
    return redirect("/home")