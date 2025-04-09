from flask_app.config.mysqlconnection import connectToMySQL
from flask import session

class Asesoria:
    db = "tutoriza"

    def __init__(self, data):
        self.id = data['id']
        self.tema = data['tema']
        self.duracion = data['duracion']
        self.fecha = data['fecha']
        self.notas = data['notas']
        self.usuario_id = data['usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.tutor = data['tutor']
        self.creador = data['creador']

    @classmethod
    def guardar(cls, data):
        query = """
        INSERT INTO asesorias (tema, duracion, fecha, notas, usuario_id, created_at, updated_at, nombre, tutor)
        VALUES (%(tema)s, %(duracion)s, %(fecha)s, %(notas)s, %(usuario_id)s, NOW(), NOW(), (SELECT nombre FROM usuarios WHERE id = %(usuario_id)s), %(tutor)s);
        """
        resultado = connectToMySQL(cls.db).query_db(query, data)
        return resultado

    @classmethod
    def obtener_uno(cls, data):
        query = """
        SELECT asesorias.*, usuarios.nombre AS creador
        FROM asesorias
        JOIN usuarios ON asesorias.usuario_id = usuarios.id
        WHERE asesorias.id = %(id)s;
        """
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            return cls(result[0])
        return None

    @classmethod
    def actualizar(cls, data):
        query = """
        UPDATE asesorias
        SET tema = %(tema)s, duracion = %(duracion)s,
        fecha = %(fecha)s, notas = %(notas)s, updated_at = NOW(), tutor = %(tutor)s
        WHERE id = %(id)s AND usuario_id = %(usuario_id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def borrar(cls, data):
        query = "DELETE FROM asesorias WHERE id = %(id)s AND usuario_id = %(usuario_id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def obtener_todos_con_creador(cls):
        query = """
        SELECT asesorias.*, usuarios.nombre AS creador
        FROM asesorias
        JOIN usuarios ON asesorias.usuario_id = usuarios.id;
        """
        resultados = connectToMySQL(cls.db).query_db(query)
        asesorias = []
        for row in resultados:
            asesoria = cls(row)
            asesoria.creador = row['creador']
            asesorias.append(asesoria)
        return asesorias

    @classmethod
    def cambiar_tutor(cls, data):
        query = """
        UPDATE asesorias
        SET tutor = %(tutor)s, updated_at = NOW()
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)