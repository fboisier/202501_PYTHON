from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField, SelectField, HiddenField
from wtforms.validators import DataRequired

class AsesoriaForm(FlaskForm):
    id = HiddenField('ID')
    tema = StringField('Tema', validators=[DataRequired()])
    duracion = StringField('Duración', validators=[DataRequired()])
    fecha = DateField('Fecha', format='%Y-%m-%d', validators=[DataRequired()])
    notas = TextAreaField('Notas')
    tutor = SelectField('Tutor', choices=[('Camilo', 'Camilo'), ('Seba', 'Seba'), ('Humilda', 'Humilda'), ('Tutor4', 'Tutor 4'), ('Tutor5', 'Tutor 5')])
    submit = SubmitField('Crear Asesoria')