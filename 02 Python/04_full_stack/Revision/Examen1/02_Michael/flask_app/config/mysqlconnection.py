import pymysql.cursors
from flask import flash
import re

# EMAIL_REGEX = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')  <-- Eliminar esta línea

class MySQLConnection:
    def __init__(self, db):
        print("Intentando conectar a la base de datos:", db)  # 👈 Agregar este print
        try:
            connection = pymysql.connect(
                host='localhost',
                user='root',
                password='sql12345',
                database=db,  # Usar la variable db que se pasa como argumento
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=True
            )
            self.connection = connection
            print("✅ Conexión a la base de datos exitosa")  # 👈 Agregar este print
        except pymysql.err.OperationalError as e:
            print("❌ Error al conectar a la base de datos:", e)  # 👈 Agregar este print
            self.connection = None  # Establecer la conexión a None en caso de error

    def query_db(self, query, data=None):
        if self.connection is None:
            print("🚫 No hay conexión a la base de datos. No se puede ejecutar la consulta.")  # 👈 Agregar este print
            return None

        print("Ejecutando query en base:", self.connection.db.decode() if hasattr(self.connection, 'db') else 'desconocida')
        print("Consulta SQL:", query)
        print("Datos enviados:", data)

        with self.connection.cursor() as cursor:
            cursor.execute(query, data)
            if query.strip().lower().startswith("select"):
                resultado = cursor.fetchall()
                print("📥 Resultado:", resultado)
                return resultado
            resultado = cursor.lastrowid
            return resultado

def connectToMySQL(db):
    return MySQLConnection(db)