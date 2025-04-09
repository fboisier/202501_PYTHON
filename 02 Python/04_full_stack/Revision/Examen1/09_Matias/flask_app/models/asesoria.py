from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime

class Asesoria:
    db = "tutoriza"

    def __init__(self, data):
        self.id = data['id']
        self.tema = data['tema']
        self.fecha = data['fecha']
        self.duracion = data['duracion']
        self.notas = data['notas']
        self.create_at = data['create_at']
        self.update_at = data['update_at']
        self.alumno_id = data['alumno_id']
        self.tutor_id = data.get('tutor_id', None)

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO asesorias (tema, fecha, duracion, notas, create_at, update_at, alumno_id, tutor_id)
            VALUES (%(tema)s, %(fecha)s, %(duracion)s, %(notas)s, NOW(), NOW(), %(alumno_id)s, %(tutor_id)s);
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM asesorias;"
        results = connectToMySQL(cls.db).query_db(query)
        return [cls(row) for row in results] if results else []

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM asesorias WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0]) if result else None

    @classmethod
    def get_by_alumno(cls, data):
        query = "SELECT * FROM asesorias WHERE alumno_id = %(alumno_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return [cls(row) for row in results] if results else []

    @classmethod
    def update(cls, data):
        query = """
            UPDATE asesorias 
            SET tema=%(tema)s, fecha=%(fecha)s, duracion=%(duracion)s, 
                notas=%(notas)s, update_at=NOW(), tutor_id=%(tutor_id)s
            WHERE id=%(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update_tutor(cls, data):
        query = "UPDATE asesorias SET tutor_id = %(tutor_id)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM asesorias WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_asesoria(asesoria):
        is_valid = True
        if len(asesoria['tema']) < 1:
            flash("Tema no puede estar vacío.", 'asesoria')
            is_valid = False
        if len(asesoria['notas']) < 1:
            flash("Notas no pueden estar vacías.", 'asesoria')
            is_valid = False
        try:
            duracion = int(asesoria['duracion'])
            if duracion <= 0:
                flash("Duración debe ser mayor a 0.", 'asesoria')
                is_valid = False
        except ValueError:
            flash("Duración debe ser un número válido.", 'asesoria')
            is_valid = False

        try:
            fecha_asesoria = datetime.strptime(asesoria['fecha'], '%Y-%m-%d')
            if fecha_asesoria < datetime.now():
                flash("La fecha no puede ser en el pasado.", 'asesoria')
                is_valid = False
        except ValueError:
            flash("Formato de fecha inválido. Use YYYY-MM-DD.", 'asesoria')
            is_valid = False

        return is_valid