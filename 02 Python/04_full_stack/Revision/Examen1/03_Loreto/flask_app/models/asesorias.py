from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime

class Asesoria:
    base_datos = "esquema_tutoriza"

    def __init__(self, data):
        self.id = data['id']
        self.tema = data['tema']
        self.fecha = data['fecha']
        self.duracion = data['duracion']
        self.notas = data['notas']
        self.tutor = data['tutor']
        self.usuarios_id = data['usuarios_id']
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO asesorias (tema, fecha, duracion, notas, tutor, usuarios_id, created_at, updated_at)
        VALUES (%(tema)s, %(fecha)s, %(duracion)s, %(notas)s, %(tutor)s, %(usuarios_id)s, NOW(), NOW());
        """
        return connectToMySQL(cls.base_datos).query_db(query, data)

    @classmethod
    def get_data_by_id(cls, id):
        query = "SELECT * FROM asesorias WHERE id = %(id)s;"
        data = {'id': id}
        result = connectToMySQL(cls.base_datos).query_db(query, data)
        if not result:
            return None
        return cls(result[0])

    @classmethod
    def get_by_usuario_id(cls, usuario_id):
        query = """
        SELECT * FROM asesorias 
        WHERE usuarios_id = %(usuario_id)s 
        ORDER BY fecha DESC;
        """
        resultados = connectToMySQL(cls.base_datos).query_db(query, {"usuario_id": usuario_id})
        return [cls(fila) for fila in resultados] if resultados else []

    @staticmethod
    def validar(datos):
        es_valido = True

        if not datos.get('tema'):
            flash("Tema es obligatorio", "error")
            es_valido = False

        if not datos.get('fecha'):
            flash("Fecha es obligatoria", "error")
            es_valido = False
        else:
            fecha_actual = datetime.now().date()
            try:
                fecha_ingresada = datetime.strptime(datos['fecha'], '%Y-%m-%d').date()
                if fecha_ingresada < fecha_actual:
                    flash("La fecha no puede estar en el pasado", "error")
                    es_valido = False
            except ValueError:
                flash("Formato de fecha inválido", "error")
                es_valido = False

        duracion = datos.get('duracion')
        if not duracion or not duracion.isdigit() or not (1 <= int(duracion) <= 8):
            flash("Duración debe ser un número entre 1 y 8", "error")
            es_valido = False

        if len(datos.get('notas', '')) > 50:
            flash("Notas no puede tener más de 50 caracteres", "error")
            es_valido = False

        if not datos.get('tutor'):
            flash("Debes seleccionar un tutor", "error")
            es_valido = False

        return es_valido
    
    @classmethod
    def update_tutor(cls, data):
        query = """
        UPDATE asesorias 
        SET tutor = %(tutor)s, updated_at = NOW() 
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.base_datos).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
        UPDATE asesorias 
        SET tema = %(tema)s, fecha = %(fecha)s, duracion = %(duracion)s, notas = %(notas)s, tutor = %(tutor)s, updated_at = NOW()
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.base_datos).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM asesorias WHERE id = %(id)s;"
        if cls.get_data_by_id(data['id']):
            return connectToMySQL(cls.base_datos).query_db(query, data)
        return False
