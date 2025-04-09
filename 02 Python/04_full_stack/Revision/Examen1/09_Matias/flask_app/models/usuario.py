from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    db = "tutoriza"
    
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.contraseña = data['contraseña']
        self.create_at = data['create_at']
        self.update_at = data['update_at']
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO alumnos (nombre, apellido, email, contraseña, create_at, update_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(contraseña)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM alumnos WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM alumnos WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if len(result) < 1:
            return None
        return cls(result[0])
    
    @classmethod
    def get_all_except(cls, usuario_id):
        query = "SELECT * FROM alumnos WHERE id != %(id)s;"
        data = {'id': usuario_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        usuarios = []
        for row in results:
            usuarios.append(cls(row))
        return usuarios
    
    @staticmethod
    def validate_registro(usuario):
        is_valid = True
        if len(usuario['nombre']) < 2:
            flash("Nombre debe tener al menos 2 caracteres.", 'registro')
            is_valid = False
        if len(usuario['apellido']) < 2:
            flash("Apellido debe tener al menos 2 caracteres.", 'registro')
            is_valid = False
        if not EMAIL_REGEX.match(usuario['email']):
            flash("Email inválido.", 'registro')
            is_valid = False
        if usuario['contraseña'] != usuario['confirmar_contraseña']:
            flash("Contraseñas no coinciden.", 'registro')
            is_valid = False
        if len(usuario['contraseña']) < 8:
            flash("Contraseña debe tener al menos 8 caracteres.", 'registro')
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_login(usuario):
        is_valid = True
        if not EMAIL_REGEX.match(usuario['email']):
            flash("Email inválido.", 'login')
            is_valid = False
        if len(usuario['contraseña']) < 8:
            flash("Contraseña debe tener al menos 8 caracteres.", 'login')
            is_valid = False
        return is_valid