from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, HiddenField, IntegerField, FieldList, FormField, \
    SelectMultipleField, DateField, MultipleFileField
from wtforms.validators import DataRequired, Email, URL, InputRequired, ValidationError
from wtforms.widgets import HiddenInput

from models.Abreviatura import Abreviatura
from models.Area import Area
from models.Centro import Centro
from models.Contrato import TipoContrato
from models.Departamento import Departamento
from models.Docente import Docente
from models.Titulacion import Titulacion


class FormCentro(FlaskForm):
    codigo = IntegerField('Código interno', validators=[DataRequired(message='El código interno es obligatorio')])
    nombre = StringField('Nombre', validators=[DataRequired(message='El nombre es obligatorio')])
    abreviatura = StringField('Abreviatura', validators=[DataRequired(message='La abreviatura es obligatoria')])
    email = StringField('Email del administrativo',
                        validators=[DataRequired(message='El email del administrativo es obligatorio'),
                                    Email(message='La dirección de email no es válida')])
    submit = SubmitField('Añadir')


class FormTitulacion(FlaskForm):
    codigo = IntegerField('Código interno', validators=[DataRequired(message='El código interno es obligatorio')])
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
    codigo = IntegerField('Código interno', validators=[DataRequired(message='El código interno es obligatorio')])
    nombre = StringField('Nombre', validators=[DataRequired(message='El nombre es obligatorio')])
    tipo = SelectField('Tipo', choices=[('FB', 'Formación Básica'), ('Ob', 'Obligatoria'), ('Op', 'Optativa')],
                       validators=[DataRequired(message='El tipo es obligatorio')])
    abreviatura = SelectMultipleField('Abreviatura(s)', choices=[], validate_choice=False)
    creditos_teoria = IntegerField('Créditos de teoría',
                                   validators=[InputRequired(message='El número de créditos de teoría es obligatorio')])
    creditos_practica = IntegerField('Créditos de práctica', validators=[
        InputRequired(message='El número de créditos de práctica es obligatorio')])
    curso = SelectField('Curso', choices=[('1', '1º'), ('2', '2º'), ('3', '3º'), ('4', '4º'), ('Todos', 'Todos')],
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
                               validators=[DataRequired(message='El departamento es obligatorio')],
                               validate_choice=False)
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


class FormPlaza(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message='El nombre es obligatorio')])
    rpt = StringField('RPT', validators=[DataRequired(message='La RPT es obligatoria')])
    num_concursos_contratacion = IntegerField('Número de concursos de contratación',
                                              validators=[InputRequired(
                                                  message='El número de concursos de contratación es obligatorio')])
    fecha_incorporacion = DateField('Fecha de incorporación',
                                    validators=[DataRequired(message='La fecha de incorporación es obligatoria')])
    fecha_cese = DateField('Fecha de cese', validators=[DataRequired(message='La fecha de cese es obligatoria')])
    docente = SelectField('Docente', coerce=int, choices=[], validate_choice=False)
    area = SelectField('Área', coerce=int, choices=[], validators=[DataRequired(message='El área es obligatoria')],
                       validate_choice=False)
    contrato = SelectField('Tipo de contrato', coerce=int, choices=[],
                           validators=[DataRequired(message='El tipo de contrato es obligatorio')],
                           validate_choice=False)
    submit = SubmitField('Añadir')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contrato.choices = [(m.id, m.nombre) for m in TipoContrato.get_all()]

    def validate_docente(self, docente):
        docente_id = docente.data
        if docente_id != -1:
            docente_seleccionado = Docente.get_docente(docente_id)
            if not docente_seleccionado:
                raise ValidationError('Seleccione un docente válido.')

    def validate_area(self, area):
        area_id = area.data
        area_seleccionada = Area.get_area(area_id)
        if not area_seleccionada:
            raise ValidationError('Seleccione un área válido.')

    # def validate_contrato(self, contrato):
    #     contrato_id = contrato.data
    #     contrato_seleccionado = TipoContrato.get_contrato(contrato_id)
    #     if not contrato_seleccionado:
    #         raise ValidationError('Seleccione un tipo de contrato válido.')


class FormCurso(FlaskForm):
    ano_inicio = IntegerField('Año de inicio', validators=[InputRequired(message='El año de inicio es obligatorio')])
    n_a_p = IntegerField('Nº alumnos previstos',
                         validators=[InputRequired(message='Debe indicar el número de alumnos previstos')])
    n_g_t_p = IntegerField('Nº previsto de grupos de teoría',
                           validators=[InputRequired(message='Las reducciones son obligatorias')])
    n_g_p_p = IntegerField('Nº previsto de grupos de práctica',
                           validators=[InputRequired(message='Las reducciones son obligatorias')])

    n_a_o = IntegerField('Nº alumnos previstos',
                         validators=[InputRequired(message='Debe indicar el número de alumnos previstos')])
    n_g_t_o = IntegerField('Nº previsto de grupos de teoría',
                           validators=[InputRequired(message='Las reducciones son obligatorias')])
    n_g_p_o = IntegerField('Nº previsto de grupos de práctica',
                           validators=[InputRequired(message='Las reducciones son obligatorias')])

    n_a_i = IntegerField('Nº alumnos previstos',
                         validators=[InputRequired(message='Debe indicar el número de alumnos previstos')])
    n_g_t_i = IntegerField('Nº previsto de grupos de teoría',
                           validators=[InputRequired(message='Las reducciones son obligatorias')])
    n_g_p_i = IntegerField('Nº previsto de grupos de práctica',
                           validators=[InputRequired(message='Las reducciones son obligatorias')])

    id_asignaturas = MultipleFileField('Id Asignaturas', widget=HiddenInput(), id='id_asignaturas')

    def validate_id_asignaturas(self, id_asignaturas):
        if len(id_asignaturas.data) == 0 or id_asignaturas.data == ['']:
            raise ValidationError('Es necesario seleccionar alguna asignatura')

    submit = SubmitField('Añadir')


class UpdateYearCursoForm(FlaskForm):
    id_curso = IntegerField('Id Curso', widget=HiddenInput())
    year = IntegerField('Año de inicio del curso', validators=[DataRequired('El año es obligatorio')])
    submit = SubmitField('Guardar Cambios')
