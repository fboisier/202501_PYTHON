from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app

class Asesoria:

    def __init__(self, data):
        self.id = data["id"]
        self.tema = data["tema"]
        self.fecha = data["fecha"]
        self.duracion = data["duracion"]
        self.notas = data["notas"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def validar(cls, data):
        is_valid = True
        if len(data['tema']) < 2:
            flash("El tema debe tener al menos 2 caracteres", "error_tema")
            is_valid = False
        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT id, tema, fecha, duracion, notas, tutor, created_at, updated_at FROM asesorias;"
        resultados = connectToMySQL('tutoriza').query_db(query)

        asesorias = []
        for dato in resultados:
            asesoria_nueva = cls(dato)
            asesorias.append(asesoria_nueva)
        return asesorias

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT id, tema, fecha, duracion, notas, tutor created_at, updated_at FROM asesorias WHERE id = %(id)s;"
        data = {
            'id': id
        }
        resultado = connectToMySQL('tutoriza').query_db(query, data)
        return cls(resultado[0]) if resultado else None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO asesorias (tema, fecha, duracion, notas, usuario_id) VALUES (%(tema)s, %(fecha)s, %(duracion)s, %(notas)s, %(usuario_id)s);"
        return connectToMySQL('tutoriza').query_db(query, data)