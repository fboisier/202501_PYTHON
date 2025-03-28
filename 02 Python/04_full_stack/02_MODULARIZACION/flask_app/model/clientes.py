from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.model.direcciones import Direccion
from flask_app.model.tipos_clientes import TipoCliente

class Cliente:

    def __init__(self, data):
        # nativas
        self.id = data["id"]
        self.dni = data["dni"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.direccion_id = data["direccion_id"]
        self.tipo_cliente_id = data["tipo_cliente_id"]
        self.eliminado = data["eliminado"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # generadas
        self.direccion = None
        self.tipo_cliente = None

    @classmethod
    def get_all(cls):
        query = "SELECT id, dni, nombre, apellido, direccion_id, tipo_cliente_id, eliminado, created_at, updated_at FROM clientes WHERE eliminado = 0;"
        resultados = connectToMySQL().query_db(query)

        instancias = []
        for dato in resultados:
            cliente_instancia = cls(dato)
            cliente_instancia.direccion = Direccion.get(cliente_instancia.direccion_id)
            cliente_instancia.tipo_cliente = TipoCliente.get(cliente_instancia.tipo_cliente_id)
            instancias.append(cliente_instancia)
        return instancias
    
    @classmethod
    def get_all_with_relations(cls):
        query = """
        SELECT
            clientes.id, clientes.dni, clientes.nombre, clientes.apellido, clientes.direccion_id, 
            clientes.tipo_cliente_id, clientes.eliminado, clientes.created_at, clientes.updated_at,
            direcciones.id, direcciones.calle, direcciones.numero, direcciones.comuna_id, direcciones.created_at, direcciones.updated_at,
            tipos_clientes.id, tipos_clientes.nombre, tipos_clientes.created_at, tipos_clientes.updated_at
        FROM clientes 
        JOIN direcciones ON direcciones.id = clientes.direccion_id
        JOIN tipos_clientes ON tipos_clientes.id = clientes.tipo_cliente_id
        WHERE clientes.eliminado = 0
        """
        resultados = connectToMySQL().query_db(query)

        instancias = []
        for dato in resultados:
            cliente_instancia = cls(dato)
            
            dato_direccion = {
                'id': dato['direcciones.id'],
                'calle': dato['calle'],
                'numero': dato['numero'],
                'comuna_id': dato['comuna_id'],
                'created_at': dato['direcciones.created_at'],
                'updated_at': dato['direcciones.updated_at'],
            }
            
            dato_tipo_cliente = {
                'id': dato['tipos_clientes.id'],
                'nombre': dato['tipos_clientes.nombre'],
                'created_at': dato['tipos_clientes.created_at'],
                'updated_at': dato['tipos_clientes.updated_at'],
            }

            cliente_instancia.direccion = Direccion(dato_direccion)
            cliente_instancia.tipo_cliente = TipoCliente(dato_tipo_cliente)
            instancias.append(cliente_instancia)
        return instancias
    
    @classmethod
    def get(cls, id):
        query = "SELECT id, dni, nombre, apellido, direccion_id, tipo_cliente_id, eliminado, created_at, updated_at FROM clientes WHERE id = %(id)s AND eliminado = 0;"
        data = {
            'id': id
        }
        resultados = connectToMySQL().query_db(query, data)
        if resultados:
            instancia_nueva = cls(resultados[0])
            return instancia_nueva
        return None

    @classmethod
    def save(cls, datos):
        query = """
        INSERT INTO clientes (dni, nombre, apellido, direccion_id, tipo_cliente_id, eliminado, created_at, updated_at) 
        VALUES (%(dni)s, %(nombre)s, %(apellido)s, %(direccion_id)s, %(tipo_cliente_id)s, 0, NOW(), NOW());
        """
        return connectToMySQL().query_db(query, datos)
    
    def update(self):
        query = """
                UPDATE clientes
                    SET
                        dni = %(dni)s,
                        nombre = %(nombre)s,
                        apellido = %(apellido)s,
                        direccion_id = %(direccion_id)s,
                        tipo_cliente_id = %(tipo_cliente_id)s,
                        updated_at = NOW()
                    WHERE id = %(id)s AND eliminado = 0;
                """
        
        datos = {
            'id': self.id,
            'dni': self.dni,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'direccion_id': self.direccion_id,
            'tipo_cliente_id': self.tipo_cliente_id
        }
        return connectToMySQL().query_db(query, datos)
    
    @classmethod
    def delete(cls, id):
        # Soft delete - actualiza el campo eliminado a 1 en lugar de eliminar el registro
        query = "UPDATE clientes SET eliminado = 1, updated_at = NOW() WHERE id = %(id)s;"
        data = {
            'id': id
        }
        connectToMySQL().query_db(query, data)
        return True
