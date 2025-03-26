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

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO usuarios (nombre, email, contraseña, created_at, updated_at) VALUES (%(nombre)s, %(email)s, %(contraseña)s , NOW(), NOW());"
        return connectToMySQL().query_db(query, datos)
    

    def update(self):
        query = """
                UPDATE usuarios
                    SET
                        nombre = %(nombre)s,
                        email = %(email)s,
                        contraseña = %(contraseña)s,
                        updated_at = NOW()
                    WHERE id = %(id)s;
                """
        
        datos = {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'contraseña': self.contraseña
        }
        return connectToMySQL().query_db(query, datos)
    

    @classmethod
    def delete(cls, id):

        query = f"DELETE FROM usuarios WHERE id = %(id)s;"
        data = {
            'id': id
        }
        connectToMySQL().query_db(query, data)
        return True