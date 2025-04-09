from flask import Flask
from flask_bcrypt import Bcrypt  # Importar Bcrypt
import os  # Importar el módulo os

app = Flask(__name__, static_folder='statics')
app.secret_key = "clave_secreta_segura"

bcrypt = Bcrypt(app)  # Crear la instancia de Bcrypt aquí y pasar app