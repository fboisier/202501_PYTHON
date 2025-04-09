from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.usuarios import Usuario  

class Asesoria:
    def __init__(self, data):
        self.id = data["id"]
        self.tema = data["tema"]
        self.duracion = data["duracion"]
        self.notas = data["notas"]
        self.usuarios_id = data["usuario_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
        # Datos relacionados (para joins)
        self.usuario = None

    @classmethod
    def get_all_with_users(cls):
        query = """
        SELECT asesorias.id, asesorias.tema, asesorias.duracion, asesorias.notas, asesorias.usuario_id, asesorias.created_at, asesorias.updated_at,
            usuarios.id AS usuario_id, usuarios.nombre AS usuario_nombre, usuarios.apellido AS usuario_apellido, usuarios.email AS usuario_email, usuarios.contraseña AS usuario_contraseña, 
            usuarios.created_at AS usuario_created_at, usuarios.updated_at AS usuario_updated_at
        FROM asesorias
        JOIN usuarios ON asesorias.usuario_id = usuarios.id
        """ 
        resultados = connectToMySQL('core').query_db(query)
        print("Resultados de la consulta:", resultados) 
        instancias = []
        for dato in resultados:
            asesoria_instancia = cls(dato)
            
            dato_usuario = {
                'id': dato['usuario_id'],
                'nombre': dato['usuario_nombre'],
                'apellido': dato['usuario_apellido'],
                'email': dato['usuario_email'],
                'contraseña': dato['usuario_contraseña'],
                'created_at': dato['usuario_created_at'],
                'updated_at': dato['usuario_updated_at'],
            }

            usuario_instancia = Usuario(dato_usuario)
            asesoria_instancia.usuario = usuario_instancia
            instancias.append(asesoria_instancia)
        return instancias
            
    @classmethod
    def get(cls, id):
        query = """
        SELECT asesorias.id, asesorias.tema, asesorias.duracion, asesorias.notas, asesorias.usuario_id, asesorias.created_at, asesorias.updated_at,
            usuarios.id AS usuario_id, usuarios.nombre AS usuario_nombre, usuarios.apellido AS usuario_apellido, usuarios.email AS usuario_email, usuarios.contraseña AS usuario_contraseña, 
            usuarios.created_at AS usuario_created_at, usuarios.updated_at AS usuario_updated_at
        FROM asesorias
        JOIN usuarios ON asesorias.usuario_id = usuarios.id
        WHERE asesorias.id = %(id)s;
        """
        data = {"id": id}
        resultado = connectToMySQL('core').query_db(query, data)
        
        if not resultado:
            return None  # Si no hay resultados, devuelve None
        
        dato = resultado[0]
        asesoria = cls(dato)
        
        # Preparamos datos del usuario
        usuario_data = {
            "id": dato["usuario_id"],
            "nombre": dato["usuario_nombre"],
            "apellido": dato["usuario_apellido"],
            "email": dato["usuario_email"],
            "contraseña": dato["usuario_contraseña"],
            "created_at": dato["usuario_created_at"],
            "updated_at": dato["usuario_updated_at"]
        }
        asesoria.usuario = Usuario(usuario_data)
        
        return asesoria

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO asesorias (tema, duracion, notas, usuario_id, created_at, updated_at)
        VALUES (%(tema)s, %(duracion)s, %(notas)s, %(usuario_id)s, NOW(), NOW());
        """
        return connectToMySQL('core').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
        UPDATE asesorias
        SET tema = %(tema)s,
            duracion = %(duracion)s,
            notas = %(notas)s,
            usuario_id = %(usuario_id)s,
            updated_at = NOW()
        WHERE id = %(id)s;
        """
        return connectToMySQL('core').query_db(query, data)

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM asesorias WHERE id = %(id)s;"
        data = {"id": id}
        return connectToMySQL('core').query_db(query, data)

 