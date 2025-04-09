from flask import Flask
from flask_bcrypt import Bcrypt
from flask import flash, session

app = Flask(__name__)
app.secret_key = "tu_clave_secreta_aqui"

bcrypt = Bcrypt(app)