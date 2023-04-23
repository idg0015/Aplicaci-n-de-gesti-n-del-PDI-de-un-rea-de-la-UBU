from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class FormCentro(FlaskForm):
    locales = ['es_ES', 'es']
    nombre = StringField('Nombre', validators=[DataRequired(message='El nombre es obligatorio')])
    abreviatura = StringField('Abreviatura', validators=[DataRequired(message='La abreviatura es obligatoria')])
    email = StringField('Email del administrativo', validators=[DataRequired(message='El email del administrativo es obligatorio'), Email(message='La dirección de email no es válida')])
    submit = SubmitField('Añadir')
