from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Usuario:
    db = "tutoriza"
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def obtener_por_email(cls, data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        resultados = connectToMySQL(cls.db).query_db(query, data)
        if resultados:
            return cls(resultados[0])
        return None

    @classmethod
    def obtener_por_id(cls, id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        data = {"id": id}
        resultados = connectToMySQL(cls.db).query_db(query, data)
        if resultados:
            return cls(resultados[0])
        return None

    @classmethod
    def guardar(cls, data):
        query = """
        INSERT INTO usuarios (nombre, apellido, email, password, created_at, updated_at) 
        VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW(), NOW());
        """
        resultado = connectToMySQL(cls.db).query_db(query, data)
        return resultado

    @staticmethod
    def validar_registro(usuario):
        es_valido = True
        if len(usuario['nombre']) < 3:
            flash("El nombre debe tener al menos 3 caracteres.", 'error_registro')
            es_valido = False
        if len(usuario['apellido']) < 3:
            flash("El apellido debe tener al menos 3 caracteres.", 'error_registro')
            es_valido = False
        if not EMAIL_REGEX.match(usuario['email']):
            flash("Dirección de correo electrónico no válida.", 'error_registro')
            es_valido = False
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        results = connectToMySQL(Usuario.db).query_db(query, usuario)
        if len(results) >= 1:
            flash("La dirección de correo electrónico ya está en uso.", 'error_registro')
            es_valido = False
        if len(usuario['password']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", 'error_registro')
            es_valido = False
        if usuario['password'] != usuario['confirm_password']:
            flash("Las contraseñas no coinciden.", 'error_registro')
            es_valido = False
        return es_valido
    