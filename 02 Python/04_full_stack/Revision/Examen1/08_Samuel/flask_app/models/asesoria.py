from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime

class Asesoria:
    db_name = "tutoriza_db"
    
    def __init__(self, data):
        self.id = data['id']
        self.tema = data['tema']
        self.fecha = data['fecha']
        self.duracion = data['duracion']
        self.notas = data['notas']
        self.usuario_id = data['usuario_id']
        self.tutor_id = data.get('tutor_id')
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.solicitante = None
        self.tutor = None
    
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO asesorias (tema, fecha, duracion, notas, usuario_id, tutor_id, created_at, updated_at)
            VALUES (%(tema)s, %(fecha)s, %(duracion)s, %(notas)s, %(usuario_id)s, %(tutor_id)s, NOW(), NOW())
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = """
            SELECT a.*, u1.nombre as solicitante_nombre, u2.nombre as tutor_nombre
            FROM asesorias a
            JOIN usuarios u1 ON a.usuario_id = u1.id
            LEFT JOIN usuarios u2 ON a.tutor_id = u2.id
            ORDER BY a.fecha DESC;
        """
        results = connectToMySQL(cls.db_name).query_db(query)
        asesorias = []
        for row in results:
            asesoria = {
                'id': row['id'],
                'tema': row['tema'],
                'fecha': row['fecha'],
                'duracion': row['duracion'],
                'notas': row['notas'],
                'usuario_id': row['usuario_id'],
                'tutor_id': row['tutor_id'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at'],
                'solicitante_nombre': row['solicitante_nombre'],
                'tutor_nombre': row['tutor_nombre']
            }
            asesorias.append(asesoria)
        return asesorias
    
    @classmethod
    def get_all_current(cls):
        today = datetime.now().strftime('%Y-%m-%d')
        query = f"""
            SELECT a.*, u1.nombre as solicitante_nombre, u2.nombre as tutor_nombre
            FROM asesorias a
            JOIN usuarios u1 ON a.usuario_id = u1.id
            LEFT JOIN usuarios u2 ON a.tutor_id = u2.id
            WHERE a.fecha >= '{today}'
            ORDER BY a.fecha DESC;
        """
        results = connectToMySQL(cls.db_name).query_db(query)
        asesorias = []
        for row in results:
            asesoria = {
                'id': row['id'],
                'tema': row['tema'],
                'fecha': row['fecha'],
                'duracion': row['duracion'],
                'notas': row['notas'],
                'usuario_id': row['usuario_id'],
                'tutor_id': row['tutor_id'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at'],
                'solicitante_nombre': row['solicitante_nombre'],
                'tutor_nombre': row['tutor_nombre']
            }
            asesorias.append(asesoria)
        return asesorias
    
    @classmethod
    def get_by_id(cls, id):
        query = """
            SELECT a.*, u1.nombre as solicitante_nombre, u2.nombre as tutor_nombre
            FROM asesorias a
            JOIN usuarios u1 ON a.usuario_id = u1.id
            LEFT JOIN usuarios u2 ON a.tutor_id = u2.id
            WHERE a.id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, {'id': id})
        if len(results) < 1:
            return False
        
        row = results[0]
        asesoria = {
            'id': row['id'],
            'tema': row['tema'],
            'fecha': row['fecha'],
            'duracion': row['duracion'],
            'notas': row['notas'],
            'usuario_id': row['usuario_id'],
            'tutor_id': row['tutor_id'],
            'created_at': row['created_at'],
            'updated_at': row['updated_at'],
            'solicitante_nombre': row['solicitante_nombre'],
            'tutor_nombre': row['tutor_nombre']
        }
        return asesoria
    
    @classmethod
    def update(cls, data):
        query = """
            UPDATE asesorias
            SET tema = %(tema)s, fecha = %(fecha)s, duracion = %(duracion)s, 
                notas = %(notas)s, tutor_id = %(tutor_id)s, updated_at = NOW()
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM asesorias WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, {'id': id})
    
    @classmethod
    def update_tutor(cls, data):
        query = """
            UPDATE asesorias
            SET tutor_id = %(tutor_id)s, updated_at = NOW()
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @staticmethod
    def validar(asesoria):
        is_valid = True
        
        if not asesoria['tema']:
            flash("El tema no puede estar vacío", "asesoria")
            is_valid = False
        
        if not asesoria['fecha']:
            flash("La fecha no puede estar vacía", "asesoria")
            is_valid = False
        else:
            fecha_asesoria = datetime.strptime(asesoria['fecha'], '%Y-%m-%d')
            if fecha_asesoria < datetime.now():
                flash("No puede ingresar una fecha en el pasado", "asesoria")
                is_valid = False
        
        if not asesoria['duracion']:
            flash("La duración no puede estar vacía", "asesoria")
            is_valid = False
        else:
            try:
                duracion = int(asesoria['duracion'])
                if duracion < 1 or duracion > 8:
                    flash("La duración debe ser un número entre 1 y 8", "asesoria")
                    is_valid = False
            except ValueError:
                flash("La duración debe ser un número", "asesoria")
                is_valid = False
        
        if len(asesoria['notas']) > 50:
            flash("Las notas no pueden tener más de 50 caracteres", "asesoria")
            is_valid = False
        
        return is_valid