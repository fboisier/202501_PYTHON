from flask_app.config.my_sql_conection import connectToMySQL

from flask_app.models.usuario import Usuario

class Asesoria:
    def __init__(self, id, tema,fecha, duracion,notas ,created_at,updated_at,usuario:Usuario,tutor:Usuario):
        self.id = id
        self.tema = tema
        self.fecha = fecha
        self.duracion = duracion
        self.notas = notas
        self.created_at = created_at
        self.updated_at = updated_at
        self.usuario = usuario
        self.tutor = tutor

    def __str__(self):
        return f"Id: {self.id}, Tema: {self.tema}, Fecha: {self.fecha}, Duracion: {self.duracion}, Notas: {self.notas}, Usuario: {self.usuario}, Tutor: {self.tutor}"
  

def crear_asesoria(asesoria):
    # INSERT INTO `tutoriza`.`asesorias` (`tema`, `fecha`, `duracion`, `notas`, `usuarios_id`) VALUES ('Mongo', '2025-04-04 20:00:00', '2', 'BASES DE DATOS NO DOCUMENTALES', '1');
    query = "INSERT INTO tutoriza.asesorias (tema, fecha, duracion, notas, usuarios_id,tutor_id) VALUES (%(tema)s, %(fecha)s, %(duracion)s, %(notas)s, %(id_usuario)s,%(id_tutor)s);"
    data = {
        "tema": asesoria['tema'],
        "fecha": asesoria['fecha'],
        "duracion": float(asesoria['duracion']),
        "notas": asesoria['notas'],
        "id_usuario": int(asesoria['id_usuario']),
        "id_tutor": int(asesoria['tutor_id'])
    }
    return connectToMySQL("tutoriza").query_db(query, data)

def obtener_todas_las_asesorias():
    query = """
    SELECT * FROM tutoriza.asesorias 
    JOIN 
        tutoriza.usuarios as usuario ON asesorias.usuarios_id = usuario.id
    JOIN 
        tutoriza.usuarios as tutor ON asesorias.tutor_id = tutor.id;
    """
    result = connectToMySQL("tutoriza").query_db(query)
    asesorias = []
    for row in result:
        
        usuario = Usuario(
            id=row['usuario.id'],
            nombre=row['nombre'],
            apellido=row['apellido'],
            email=row['email'],
            contrasena=None,
            created_at=row['usuario.created_at'],
            updated_at=row['usuario.updated_at']
        )
        tutor = Usuario(
            id=row['tutor.id'],
            nombre=row['tutor.nombre'],
            apellido=row['tutor.apellido'],
            email=row['tutor.email'],
            contrasena=None,
            created_at=row['tutor.created_at'],
            updated_at=row['tutor.updated_at']
        )
        asesorias.append(Asesoria(
            id=row['id'],
            tema=row['tema'],
            fecha=row['fecha'],
            duracion=row['duracion'],
            notas=row['notas'],
            created_at=row['created_at'],
            updated_at=row['updated_at'],
            usuario=usuario,
            tutor=tutor
        ))
    return asesorias

def obtener_asesoria_por_id(id):
    query = """
    SELECT * FROM tutoriza.asesorias 
    JOIN 
        tutoriza.usuarios as usuario ON asesorias.usuarios_id = usuario.id
    JOIN 
        tutoriza.usuarios as tutor ON asesorias.tutor_id = tutor.id
    WHERE asesorias.id = %(id)s;
    """
    data = {
        "id": id
    }
    result = connectToMySQL("tutoriza").query_db(query, data)
    if len(result) == 0:
        return False
    else:
        print(result[0])
        usuario = Usuario(
            id=result[0]['usuario.id'],
            nombre=result[0]['nombre'],
            apellido=result[0]['apellido'],
            email=result[0]['email'],
            contrasena=None,
            created_at=result[0]['created_at'],
            updated_at=result[0]['updated_at']
        )
        tutor = Usuario(
            id=result[0]['tutor.id'],
            nombre=result[0]['tutor.nombre'],
            apellido=result[0]['tutor.apellido'],
            email=result[0]['tutor.email'],
            contrasena=None,
            created_at=result[0]['tutor.created_at'],
            updated_at=result[0]['tutor.updated_at']
        )
        
        asesoria =Asesoria(
            id=result[0]['id'],
            tema=result[0]['tema'],
            fecha=result[0]['fecha'],
            duracion=result[0]['duracion'],
            notas=result[0]['notas'],
            created_at=result[0]['created_at'],
            updated_at=result[0]['updated_at'],
            usuario=usuario,
            tutor=tutor
        )
        return asesoria

def editar_asesoria_por_id(asesoria):
    query = "UPDATE tutoriza.asesorias SET tema = %(tema)s, fecha = %(fecha)s, duracion = %(duracion)s, notas = %(notas)s, usuarios_id = %(id_usuario)s, tutor_id = %(tutor_id)s WHERE id = %(id)s;"
    data = {
        "tema": asesoria['tema'],
        "fecha": asesoria['fecha'],
        "duracion": float(asesoria['duracion']),
        "notas": asesoria['notas'],
        "id_usuario": int(asesoria['id_usuario']),
        "tutor_id": int(asesoria['tutor_id']),
        "id": int(asesoria['id'])
    }
    return connectToMySQL("tutoriza").query_db(query, data)
    
def eliminar_asesoria_por_id(id):
    query = "DELETE FROM tutoriza.asesorias WHERE id = %(id)s;"
    data = {
        "id": int(id)
    }
    return connectToMySQL("tutoriza").query_db(query, data)