from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^\S+@\S+\.\S+$')

class Alumno:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.correo = data['correo']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO alumnos (nombre, apellido, correo, password, created_at, updated_at)
        VALUES (%(nombre)s, %(apellido)s, %(correo)s, %(password)s, NOW(), NOW())
        """
        return connectToMySQL('tutoriza').query_db(query, data)

    @classmethod
    def get_by_correo(cls, data):
        query = "SELECT * FROM alumnos WHERE correo = %(correo)s"
        results = connectToMySQL('tutoriza').query_db(query, data)
        return cls(results[0]) if results else None

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM alumnos WHERE id = %(id)s"
        results = connectToMySQL('tutoriza').query_db(query, data)
        return cls(results[0]) if results else None

    @staticmethod
    def validar_registro(data):
        is_valid = True

        if len(data['nombre']) < 2:
            flash("El nombre debe tener al menos 2 caracteres", 'registro')
            is_valid = False

        if len(data['apellido']) < 2:
            flash("El apellido debe tener al menos 2 caracteres", 'registro')
            is_valid = False

        if not EMAIL_REGEX.match(data['correo']):
            flash("Correo electrónico no válido", 'registro')
            is_valid = False

        if len(data['password']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres", 'registro')
            is_valid = False

        if data['password'] != data['confirmar']:
            flash("Las contraseñas no coinciden", 'registro')
            is_valid = False

        if Alumno.get_by_correo({'correo': data['correo']}):
            flash("Este correo ya está registrado", 'registro')
            is_valid = False

        return is_valid
    
    @staticmethod
    def validar_login(data):
        is_valid = True

        if not EMAIL_REGEX.match(data['correo']):
            flash("Correo electrónico no válido", 'login')
            is_valid = False

        if len(data['password']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres", 'login')
            is_valid = False

        return is_valid