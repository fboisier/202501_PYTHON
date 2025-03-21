from flask_app.config.mysqlconnection import connectToMySQL


class Usuario:

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.email = data["email"]
        self.contraseña = data["contraseña"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):

        query = "SELECT id, nombre, email, contraseña, created_at, updated_at FROM usuarios;"
        resultados = connectToMySQL().query_db(query)

        instancias = []
        for dato in resultados:
            instancia_nueva = cls(dato)
            instancias.append(instancia_nueva)
        return instancias
    
    @classmethod
    def get(cls, id):

        query = f"SELECT id, nombre, email, contraseña, created_at, updated_at FROM usuarios WHERE id = %(id)s;"
        data = {
            'id': id
        }
        resultados = connectToMySQL().query_db(query, data)
        instancia_nueva = cls(resultados[0])
        return instancia_nueva
