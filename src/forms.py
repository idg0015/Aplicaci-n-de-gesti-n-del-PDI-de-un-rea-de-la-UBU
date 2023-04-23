from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, URL

from models.Centro import Centro


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
