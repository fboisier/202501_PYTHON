## Coding Dojo - Python Bootcamp Jan 2025
## Tutoriza
## Roberto Alvarez, 2025

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import date
from datetime import datetime
from flask_app.models.usuario import Usuario


today = date.today()

class Assessoria:

    def __init__( self , data):
        self.id = data['id']
        self.tema = data['tema']
        self.data = data['data']
        self.usuario_id = data['usuario_id']
        self.nome_usuario = data['nome_usuario']
        self.duracao = data['duracao']
        self.notas = data['notas']
        self.tutor = data['tutor']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = """
        SELECT assessorias.id as id, assessorias.tema as tema, assessorias.data as data, assessorias.duracao as duracao, assessorias.tutor as tutor, assessorias.notas as notas, assessorias.created_at as created_at, assessorias.updated_at as updated_at, assessorias.usuario_id as usuario_id, usuarios.nome as nome_usuario 
        FROM assessorias
        LEFT JOIN usuarios
        ON assessorias.usuario_id = usuarios.id;"""
        results = connectToMySQL('db_tutoriza').query_db(query)
        assessorias = []
        for assessoria in results:
            assessorias.append( cls(assessoria) )
            print ()
            print ("#############")
            print (assessoria)
        return assessorias


    @classmethod
    def get_one(cls, id):
        query = """
        SELECT assessorias.id as id, assessorias.tema as tema, assessorias.data as data, assessorias.duracao as duracao, assessorias.tutor as tutor, assessorias.notas as notas, assessorias.created_at as created_at, assessorias.updated_at as updated_at, assessorias.usuario_id as usuario_id, usuarios.nome as nome_usuario 
        FROM assessorias
        LEFT JOIN usuarios
        ON assessorias.usuario_id = usuarios.id
        WHERE assessorias.id = %(id)s;"""
        data = { "id": id }
        assessoria = connectToMySQL('db_tutoriza').query_db(query, data)
        return cls(assessoria[0])


    @classmethod
    def save(cls, data):
        query = "INSERT INTO assessorias (tema, data, duracao, notas, tutor, created_at, updated_at, usuario_id) VALUES (%(tema)s, %(data)s, %(duracao)s, %(notas)s, %(tutor)s, NOW(), NOW(), %(usuario_id)s)"
        return connectToMySQL('db_tutoriza').query_db(query, data)


    @classmethod
    def delete(cls, id):
        query = "DELETE FROM assessorias WHERE id = %(id)s;"
        data = { "id": id }
        return connectToMySQL('db_tutoriza').query_db(query, data)


    @classmethod
    def update(cls, data):
        query = "UPDATE assessorias SET tema = %(tema)s, data = %(data)s, duracao = %(duracao)s, notas = %(notas)s, tutor = %(tutor)s, updated_at = NOW() WHERE id = %(id)s"
        return connectToMySQL('db_tutoriza').query_db(query, data)
    

    @classmethod
    def update_tutor(cls, data):
        query = "UPDATE assessorias SET tutor = %(tutor)s, updated_at = NOW() WHERE id = %(id)s"
        return connectToMySQL('db_tutoriza').query_db(query, data)


    @staticmethod
    def validar_assessoria(assessoria):
        valido = True
        assessoria['data'] = datetime.strptime(assessoria['data'], '%Y-%m-%d').date()
        if len(assessoria['notas']) > 50:
            flash("O tamanha máximo da nota é 50 caracteres. Ajuste a descrição e tente novamente.", "error")
            valido = False
        if assessoria['data'] < today:
            flash("Você não pode marcar ums sessão no passado. Verifique e corrija a data.", "error")
            valido = False
        if int(assessoria['duracao']) > 8:
            flash("O tempo máximo para uma sessão de tutoria é de 8 horas. Ajuste e tente novamente.", "error")
            valido = False
        return valido