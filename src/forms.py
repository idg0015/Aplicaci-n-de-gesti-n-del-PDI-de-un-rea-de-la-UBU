from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, HiddenField, IntegerField, FieldList, FormField, \
    SelectMultipleField
from wtforms.validators import DataRequired, Email, URL, InputRequired, ValidationError

from models.Abreviatura import Abreviatura
from models.Centro import Centro
from models.Departamento import Departamento
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
    reducciones = IntegerField('Reducciones', validators=[InputRequired(message='Las reducciones son obligatorias')])
    submit = SubmitField('Añadir')


class FormDepartamento(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message='El nombre es obligatorio')])
    abreviatura = StringField('Abreviatura', validators=[DataRequired(message='La abreviatura es obligatoria')])
    submit = SubmitField('Añadir')


class FormArea(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message='El nombre es obligatorio')])
    abreviatura = StringField('Abreviatura', validators=[DataRequired(message='La abreviatura es obligatoria')])
    departamento = SelectField('Departamento', coerce=int, choices=[],
                               validators=[DataRequired(message='El departamento es obligatorio')], validate_choice=False)
    submit = SubmitField('Añadir')

    def validate_departamento(self, departamento):
        departamento_id = departamento.data
        departamento_seleccionado = Departamento.get_departamento(departamento_id)
        if not departamento_seleccionado:
            raise ValidationError('Seleccione un departamento válido.')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.departamento.choices = [(m.id, m.nombre) for m in Departamento.get_all()]


class FormContrato(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message='El nombre es obligatorio')])
    abreviatura = StringField('Abreviatura', validators=[DataRequired(message='La abreviatura es obligatoria')])
    capacidad_anual = IntegerField('Capacidad anual (horas)',
                                   validators=[InputRequired(message='La capacidad anual es obligatoria')])
    # DataRequired para que no se pueda enviar 0
    submit = SubmitField('Añadir')
