from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, HiddenField, IntegerField, FieldList, FormField, \
    SelectMultipleField
from wtforms.validators import DataRequired, Email, URL

from models.Abreviatura import Abreviatura
from models.Centro import Centro
from models.Titulacion import Titulacion


class FormCentro(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message='El nombre es obligatorio')])
    abreviatura = StringField('Abreviatura', validators=[DataRequired(message='La abreviatura es obligatoria')])
    email = StringField('Email del administrativo',
                        validators=[DataRequired(message='El email del administrativo es obligatorio'),
                                    Email(message='La dirección de email no es válida')])
    submit = SubmitField('Añadir')


class FormTitulacion(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message='El nombre es obligatorio')])
    abreviatura = StringField('Abreviatura', validators=[DataRequired(message='La abreviatura es obligatoria')])
    url = StringField('URL', validators=[DataRequired(message='La URL es obligatoria'),
                                         URL(message='La URL no es válida. Debe empezar por http:// o https://')])
    centro = SelectField('Centro', choices=[], validators=[DataRequired(message='El centro es obligatorio')])
    submit = SubmitField('Añadir')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.centro.choices = [(m.id, m.nombre) for m in Centro.get_all()]


class FormAsignatura(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message='El nombre es obligatorio')])
    tipo = SelectField('Tipo', choices=[('FB', 'Formación Básica'), ('Ob', 'Obligatoria'), ('Op', 'Optativa')],
                       validators=[DataRequired(message='El tipo es obligatorio')])
    abreviatura = SelectMultipleField('Abreviatura(s)', choices=[], validate_choice=False)
    creditos_teoria = IntegerField('Créditos de teoría',
                                   validators=[DataRequired(message='El número de créditos de teoría es obligatorio')])
    creditos_practica = IntegerField('Créditos de práctica', validators=[
        DataRequired(message='El número de créditos de práctica es obligatorio')])
    curso = SelectField('Curso', choices=[('1', '1º'), ('2', '2º'), ('3', '3º'), ('4', '4º')],
                        validators=[DataRequired(message='El curso es obligatorio')])
    semestre = SelectField('Semestre', choices=[('1', '1º'), ('2', '2º'), ('1.2', '1º y 2º')],
                           validators=[DataRequired(message='El semestre es obligatorio')])
    titulacion = SelectField('Titulación', choices=[],
                             validators=[DataRequired(message='La titulación es obligatoria')])
    submit = SubmitField('Añadir')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.titulacion.choices = [(m.id, m.nombre) for m in Titulacion.get_all()]


class FormDocente(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message='El nombre es obligatorio')])
    apellidos = StringField('Apellidos', validators=[DataRequired(message='Los apellidos son obligatorios')])
    email = StringField('Email', validators=[DataRequired(message='El email es obligatorio'),
                                             Email(message='La dirección de email no es válida')])
    reducciones = IntegerField('Reducciones', validators=[DataRequired(message='Las reducciones son obligatorias')])
    submit = SubmitField('Añadir')
