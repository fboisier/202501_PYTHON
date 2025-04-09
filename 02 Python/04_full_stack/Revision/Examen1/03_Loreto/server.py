from flask import render_template, redirect, request, session, flash, url_for
from flask_app import app
from flask_app.controllers import usuario
from flask_app.controllers import asesoria
from datetime import datetime


if __name__ == "__main__":
    app.run(debug=True)