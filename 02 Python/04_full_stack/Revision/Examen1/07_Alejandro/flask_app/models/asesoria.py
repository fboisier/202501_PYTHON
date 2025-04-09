from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime

class Asesoria:
    def __init__(self, data):
        self.id = data['id']
        self.tema = data['tema']
        self.fecha = data['fecha']  
        self.tiempo = data['tiempo'] 
        self.nota = data['nota']
        self.alumno_id = data['alumno_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.alumno = None

    @staticmethod
    def validar_asesoria(data):
        is_valid = True
        if len(data['tema']) < 3:
            flash("El título debe tener al menos 3 caracteres", "asesoria")
            is_valid = False
        try:
            # Validar que 'tiempo' sea un número mayor a 0
            if float(data['tiempo']) <= 0:
                flash("La duración debe ser mayor a 0 horas y menor a 8", "asesoria")
                is_valid = False
            elif float(data['tiempo']) > 8:
                flash("La duración no puede exceder las 8 horas", "asesoria")
                is_valid = False
        except ValueError:
            flash("La duración debe ser un número válido", "asesoria")
            is_valid = False
        try:
            # Validar que 'tiempo' sea una fecha válida
            fecha = datetime.strptime(data['fecha'], '%Y-%m-%d')
            if fecha < datetime.now():
                flash("La fecha debe ser en el futuro", "asesoria")
                is_valid = False
        except ValueError:
            flash("La fecha debe ser válida", "asesoria")
            is_valid = False
        if len(data['nota']) < 5:
            flash("Las nota deben tener al menos 5 caracteres", "asesoria")
            is_valid = False
        return is_valid

    @classmethod
    def guardar(cls, data):
        query = """
            INSERT INTO asesorias (tema, fecha, tiempo, nota, alumno_id, created_at, updated_at)
            VALUES (%(tema)s, %(fecha)s, %(tiempo)s, %(nota)s, %(alumno_id)s, NOW(), NOW())
        """
        return connectToMySQL("tutoriza").query_db(query, data)

    @classmethod
    def obtener_todas(cls):
        query = "SELECT * FROM asesorias JOIN alumnos ON asesorias.alumno_id = alumnos.id"
        results = connectToMySQL("tutoriza").query_db(query)
        if not results:
            return [] 
        asesorias = []
        for row in results:
            asesorias.append(cls(row))
        return asesorias

    @classmethod
    def obtener_por_id(cls, data):
        query = "SELECT * FROM asesorias WHERE id = %(id)s"
        results = connectToMySQL("tutoriza").query_db(query, data)
        if not results:
            return None
        return cls(results[0])  

    @classmethod
    def obtener_por_id_con_alumno(cls, data):
        query = """
        SELECT asesorias.*, 
               alumnos.id AS alumno_id, 
               alumnos.nombre AS alumno_nombre, 
               alumnos.apellido AS alumno_apellido, 
               alumnos.correo AS alumno_correo, 
               alumnos.password AS alumno_password, 
               alumnos.created_at AS alumno_created_at, 
               alumnos.updated_at AS alumno_updated_at
        FROM asesorias 
        JOIN alumnos ON asesorias.alumno_id = alumnos.id 
        WHERE asesorias.id = %(id)s
    """
        results = connectToMySQL("tutoriza").query_db(query, data)
        if not results:
            return None
    
        row = results[0]
        asesoria = cls(row)
        from flask_app.models.alumno import Alumno
        data_alumno = {
        "id": row["alumno_id"],
        "nombre": row["alumno_nombre"],
        "apellido": row["alumno_apellido"],
        "correo": row["alumno_correo"],
        "password": row["alumno_password"],
        "created_at": row["alumno_created_at"],
        "updated_at": row["alumno_updated_at"]
    }
        asesoria.alumno = Alumno(data_alumno)
        return asesoria

    @classmethod
    def actualizar(cls, data):
        query = """
            UPDATE asesorias
            SET tema = %(tema)s, fecha = %(fecha)s, tiempo = %(tiempo)s, nota = %(nota)s, updated_at = NOW()
            WHERE id = %(id)s AND alumno_id = %(alumno_id)s
        """
        return connectToMySQL("tutoriza").query_db(query, data)

    @classmethod
    def eliminar(cls, data):
        query = "DELETE FROM asesorias WHERE id = %(id)s"
        return connectToMySQL("tutoriza").query_db(query, data)