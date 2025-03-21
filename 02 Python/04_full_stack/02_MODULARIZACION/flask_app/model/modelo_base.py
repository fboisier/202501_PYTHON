from flask_app.config.mysqlconnection import connectToMySQL


class BaseModelo:

    tabla_nombre = ""
    campos = []

    def __init__(self, data):
        for campo in self.campos:
            setattr(self, campo, data[campo])

    @classmethod
    def get_all(cls):
        campos_join = ", ".join(cls.campos)
        query = f"SELECT {campos_join} FROM {cls.tabla_nombre};"
        resultados = connectToMySQL().query_db(query)

        instancias = []
        for dato in resultados:
            instancia_nueva = cls(dato)
            instancias.append(instancia_nueva)
        return instancias
    
    @classmethod
    def get(cls, id):
        campos_join = ", ".join(cls.campos)
        query = f"SELECT {campos_join} FROM {cls.tabla_nombre} WHERE id = %(id)s;"
        data = {
            'id': id
        }
        resultados = connectToMySQL().query_db(query, data)
        instancia_nueva = cls(resultados[0])
        return instancia_nueva
