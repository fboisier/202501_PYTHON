from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data.get('apellido', '')
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def validar(cls, datos):
        todo_ok = True

        if datos['password'] != datos['password_confirm']:
            flash("Las contraseñas no son iguales", "error")
            todo_ok = False

        if cls.existe_correo(datos['email']):
            flash("El correo ya existe", "error")
            todo_ok = False

        return todo_ok

    @classmethod
    def existe_correo(cls, email):
        query = "SELECT id FROM usuarios WHERE email = %(email)s;"
        data = {'email': email}
        resultados = connectToMySQL("esquema_tutoriza").query_db(query, data)
        return len(resultados) > 0

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL("esquema_tutoriza").query_db(query)
        instancias = []
        for dato in resultados:
            instancias.append(cls(dato))
        return instancias

    @classmethod
    def get(cls, id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        data = {'id': id}
        resultados = connectToMySQL("esquema_tutoriza").query_db(query, data)
        if resultados:
            return cls(resultados[0])
        return None

    @classmethod
    def get_by_email(cls, email):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        data = {'email': email}
        resultados = connectToMySQL("esquema_tutoriza").query_db(query, data)
        if len(resultados) == 0:
            return None
        return cls(resultados[0])

    @classmethod
    def save(cls, datos):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, password, created_at, updated_at)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW(), NOW());
        """
        return connectToMySQL("esquema_tutoriza").query_db(query, datos)

    def update(self):
        query = """
            UPDATE usuarios
            SET nombre = %(nombre)s,
                apellido = %(apellido)s,
                email = %(email)s,
                password = %(password)s,
                updated_at = NOW()
            WHERE id = %(id)s;
        """
        datos = {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'password': self.password
        }
        return connectToMySQL("esquema_tutoriza").query_db(query, datos)

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        data = {'id': id}
        connectToMySQL("esquema_tutoriza").query_db(query, data)
        return True
    


