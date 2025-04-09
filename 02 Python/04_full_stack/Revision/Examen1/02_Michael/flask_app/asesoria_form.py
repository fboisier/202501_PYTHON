from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, SubmitField
from wtforms.validators import DataRequired

class AsesoriaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])  # Agrega el campo nombre
    tema = StringField('Tema', validators=[DataRequired()])
    duracion = StringField('Duración', validators=[DataRequired()])
    fecha = DateTimeField('Fecha', format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    notas = TextAreaField('Notas')
    submit = SubmitField('Crear Asesoria')