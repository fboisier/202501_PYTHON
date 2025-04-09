from flask import Flask
import os
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "somebody"
bcrypt = Bcrypt(app)