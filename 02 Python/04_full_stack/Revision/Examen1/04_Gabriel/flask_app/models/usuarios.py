from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app

bcrypt = Bcrypt(app)


class Usuario:

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def validar_usuario(cls, data):
        is_valid = True
        
        if len(data['nombre']) < 2:
            flash("El nombre debe tener al menos 2 caracteres", "error_nombre")
            is_valid = False
        
        if len(data['apellido']) < 2:
            flash("El apellido debe tener al menos 2 caracteres", "error_apellido")
            is_valid = False
        
        
        if data['password'] != data['confirm_password']:
            flash("Las contraseñas no coinciden", "error_confirm_password")
            is_valid = False

        if cls.existe_correo(data['email']):
            flash("El correo ya existe", "error_email")
            is_valid = False
        
        return is_valid

    @classmethod
    def get_all(cls):

        query = "SELECT id, nombre, apellido, email, password, created_at, updated_at FROM usuarios;"
        resultados = connectToMySQL('tutoriza').query_db(query)

        usuarios = []
        for dato in resultados:
            usuario_nuevo = cls(dato)
            usuarios.append(usuario_nuevo)
        return usuarios
    
    @classmethod
    def get_by_email(cls, email):

        query = f"SELECT id, nombre, apellido, email, password, created_at, updated_at FROM usuarios WHERE email = %(email)s;"
        data = {
            'email': email
        }
        resultados = connectToMySQL('tutoriza').query_db(query, data)
        print(resultados)
        if len(resultados) == 0:
            return None
        instancia_nueva = cls(resultados[0])
        return instancia_nueva
    
    @classmethod
    def existe_correo(cls, correo):

        query = "SELECT id FROM usuarios WHERE email = %(correo)s;"
        data = {
            'correo': correo,
        }
        resultados = connectToMySQL('tutoriza').query_db(query, data)
        print("RESULTADO DEL EXISTE CORREO: ", resultados)

        return len(resultados) > 0
    
    @classmethod
    def save(cls, datos):
        query = "INSERT INTO usuarios (nombre, apellido, email, password, created_at, updated_at) VALUES (%(nombre)s,%(apellido)s, %(email)s, %(password)s , NOW(), NOW());"
        return connectToMySQL('tutoriza').query_db(query, datos)