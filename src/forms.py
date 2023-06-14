from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, SelectField, HiddenField, IntegerField, FieldList, FormField, \
    SelectMultipleField, DateField, MultipleFileField, BooleanField, PasswordField, FileField
from wtforms.validators import DataRequired, Email, URL, InputRequired, ValidationError, Optional, NumberRange
from wtforms.widgets import HiddenInput

from models.Abreviatura import Abreviatura
from models.Area import Area
from models.Centro import Centro
from models.Contrato import TipoContrato
from models.Curso import Curso
from models.Departamento import Departamento
from models.Docente import Docente
from models.Grupo import Grupo
from models.Plaza import Plaza
from models.Titulacion import Titulacion


class FormCentro(FlaskForm):
    codigo = IntegerField('Código interno', validators=[InputRequired(message='El código interno es obligatorio'),
                                                        NumberRange(min=0,
                                                                    message='El código interno debe ser mayor o igual que 0')])
    nombre = StringField('Nombre', validators=[DataRequired(message='El nombre es obligatorio')])
    abreviatura = StringField('Abreviatura', validators=[DataRequired(message='La abreviatura es obligatoria')])
    email = StringField('Email del administrativo',
                        validators=[DataRequired(message='El email del administrativo es obligatorio'),
                                    Email(message='La dirección de email no es válida')])
    submit = SubmitField('Añadir')


class FormTitulacion(FlaskForm):
    codigo = IntegerField('Código interno', validators=[InputRequired(message='El código interno es obligatorio'),
                                                        NumberRange(min=0,
                                                                    message='El código interno debe ser mayor o igual que 0')])
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
    codigo = IntegerField('Código interno', validators=[DataRequired(message='El código interno es obligatorio'),
                                                        NumberRange(min=0,
                                                                    message='El código interno debe ser mayor o igual que 0')])
    nombre = StringField('Nombre', validators=[DataRequired(message='El nombre es obligatorio')])
    tipo = SelectField('Tipo', choices=[('FB', 'Formación Básica'), ('Ob', 'Obligatoria'), ('Op', 'Optativa')],
                       validators=[DataRequired(message='El tipo es obligatorio')])
    abreviatura = SelectMultipleField('Abreviatura(s)', choices=[], validate_choice=False)
    creditos_teoria = IntegerField('Créditos de teoría',
                                   validators=[InputRequired(message='El número de créditos de teoría es obligatorio'),
                                               NumberRange(min=0,
                                                           message='El número de créditos de teoría debe ser mayor o igual que 0')])
    creditos_practica = IntegerField('Créditos de práctica', validators=[
        InputRequired(message='El número de créditos de práctica es obligatorio'),
        NumberRange(min=0, message='El número de créditos de práctica debe ser mayor o igual que 0')])
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
    reducciones = IntegerField('Reducciones', default=0, validators=[InputRequired(message='Las reducciones son obligatorias'),
                                                          NumberRange(min=0,
                                                                      message='El número de reducciones debe ser mayor o igual que 0')])
    read_flag = BooleanField('Permisos de consulta', default=False)
    modification_flag = BooleanField('Permisos de modificación', default=False)
    submit = SubmitField('Añadir')

    def validate_email(self, email):
        docente = Docente.get_docente_email(email.data)
        if docente:
            raise ValidationError('Ya existe un docente con ese email')


class FormDocenteUpdate(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message='El nombre es obligatorio')])
    apellidos = StringField('Apellidos', validators=[DataRequired(message='Los apellidos son obligatorios')])
    email = StringField('Email', validators=[DataRequired(message='El email es obligatorio'),
                                             Email(message='La dirección de email no es válida')])
    reducciones = IntegerField('Reducciones', validators=[InputRequired(message='Las reducciones son obligatorias'),
                                                          NumberRange(min=0,
                                                                      message='El número de reducciones debe ser mayor o igual que 0')])
    read_flag = BooleanField('Permisos de consulta', default=False)
    modification_flag = BooleanField('Permisos de modificación', default=False)
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
                                   validators=[InputRequired(message='La capacidad anual es obligatoria'),
                                               NumberRange(min=0,
                                                           message='La capacidad anual debe ser mayor o igual que 0')])
    submit = SubmitField('Añadir')


class FormPlaza(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(message='El nombre es obligatorio')])
    rpt = StringField('RPT', validators=[DataRequired(message='La RPT es obligatoria')])
    num_concursos_contratacion = IntegerField('Número de concursos de contratación',
                                              validators=[Optional(), InputRequired(
                                                  message='El número de concursos de contratación es obligatorio'),
                                                          NumberRange(min=0, message='El número debe ser mayor que 0')])
    fecha_incorporacion = DateField('Fecha de incorporación',
                                    validators=[DataRequired(message='La fecha de incorporación es obligatoria')])
    fecha_cese = DateField('Fecha de cese', validators=[Optional()])
    docente = SelectField('Docente', coerce=int, choices=[(-1, 'Ninguno')], validate_choice=False)
    area = SelectField('Área', coerce=int, choices=[], validators=[DataRequired(message='El área es obligatoria')],
                       validate_choice=False)
    contrato = SelectField('Tipo de contrato', coerce=int, choices=[],
                           validators=[DataRequired(message='El tipo de contrato es obligatorio')],
                           validate_choice=False)
    submit = SubmitField('Añadir')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contrato.choices = [(m.id, m.nombre) for m in TipoContrato.get_all()]

    def validate_fecha_cese(self, fecha_cese):
        fecha_cese = fecha_cese.data
        if fecha_cese is not None:
            fecha_incorporacion = self.fecha_incorporacion.data
            if fecha_cese and fecha_cese < fecha_incorporacion:
                raise ValidationError('La fecha de cese no puede ser anterior a la fecha de incorporación.')
        else:
            self.fecha_cese.data = None

    def validate_docente(self, docente):
        docente_id = docente.data
        if docente_id != -1:
            docente_seleccionado = Docente.get_docente(docente_id)
            if not docente_seleccionado:
                raise ValidationError('Seleccione un docente válido.')
            else:
                plazas_docente = docente_seleccionado.plazas
                if plazas_docente is not None:
                    for plaza in plazas_docente:
                        if plaza.fecha_cese is None and plaza.fecha_cese is not self.fecha_cese.data:
                            raise ValidationError(
                                'El docente ' + docente_seleccionado.nombre + ' ' + docente_seleccionado.apellidos + ' ya tiene una plaza activa.')

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
    ano_inicio = IntegerField('Año de inicio del curso', validators=[DataRequired('El año es obligatorio'),
                                                                     NumberRange(min=2000,
                                                                                 message='El año de inicio debe ser mayor que 2000')])
    submit = SubmitField('Añadir')

    def validate_ano_inicio(self, ano_inicio):
        ano_inicio = ano_inicio.data
        curso = Curso.get_curso_by_year(ano_inicio)
        if curso:
            raise ValidationError('Ya existe un curso con ese año de inicio.')


class FormCursoUpdate(FlaskForm):
    ano_inicio = IntegerField('Año de inicio', validators=[DataRequired(message='El año de inicio es obligatorio')])
    message = "No puede dejar el campo vacío. Al menos introduzca 0"

    n_a_p = IntegerField('Nº alumnos previstos presencial',
                         validators=[InputRequired(message='Presencial: ' + message), NumberRange(min=0,
                                                                                                  message='El número de alumnos previstos para presencial debe ser mayor que 0')])

    n_a_o = IntegerField('Nº alumnos previstos online',
                         validators=[InputRequired(message='Online: ' + message),
                                     NumberRange(min=0,
                                                 message='El número de alumnos previstos para online debe ser mayor que 0')])

    n_a_i = IntegerField('Nº alumnos previstos inglés',
                         validators=[InputRequired(message='Inglés: ' + message),
                                     NumberRange(min=0,
                                                 message='El número de alumnos previstos para inglés debe ser mayor que 0')])

    id_asignaturas = StringField('Id Asignaturas', widget=HiddenInput(), id='id_asignaturas')

    def validate_id_asignaturas(self, id_asignaturas):
        if len(id_asignaturas.data) == 0 or id_asignaturas.data == ['']:
            raise ValidationError('Es necesario seleccionar alguna asignatura')

    submit = SubmitField('Añadir')


class UpdateYearCursoForm(FlaskForm):
    id_curso = IntegerField('Id Curso', widget=HiddenInput())
    year = IntegerField('Año de inicio del curso', validators=[DataRequired('El año es obligatorio'),
                                                               NumberRange(min=2000,
                                                                           message='El año de inicio debe ser mayor que 2000')])
    submit = SubmitField('Guardar Cambios')


class FormGrupo(FlaskForm):
    tipo = SelectField('Tipo', coerce=str, choices=Grupo.Tipos,
                       validators=[DataRequired(message='El tipo del grupo es obligatorio')],
                       validate_choice=False)
    id_curso_asignatura = IntegerField('Id Curso_Asignatura', widget=HiddenInput())
    submit = SubmitField('Añadir')


class FormCursoAsignatura(FlaskForm):
    n_a_p = IntegerField('Nº alumnos previstos',
                         validators=[InputRequired(message='Debe indicar el número de alumnos previstos'),
                                     NumberRange(min=0, message='El número de alumnos previstos debe ser mayor que 0')])
    n_g_t = IntegerField('Nº grupos teoría previstos',
                         validators=[InputRequired(message='Debe indicar el número de grupos teoría previstos'),
                                     NumberRange(min=0,
                                                 message='El número de grupos teoría previstos debe ser mayor que 0')])
    n_g_p = IntegerField('Nº grupos prácticas previstos',
                         validators=[InputRequired(message='Debe indicar el número de grupos prácticas previstos'),
                                     NumberRange(min=0,
                                                 message='El número de grupos prácticas previstos debe ser mayor que 0')])
    submit = SubmitField('Modificar')


class FormPlazaGrupo(FlaskForm):
    group_id = IntegerField('Id Grupo', widget=HiddenInput())
    vacant = SelectField('Plaza', coerce=int, choices=[], validators=[DataRequired(message='La plaza es obligatoria')],
                         validate_choice=False)
    hours = IntegerField('Horas anuales',
                         validators=[DataRequired(message='Las horas son obligatorias'),
                                     NumberRange(min=1,
                                                 message='El número de grupos prácticas previstos debe ser mayor que 0')])
    submit = SubmitField('Añadir')

    def validate_vacant(self, vacant):
        vacant_id = vacant.data
        selected_vacant = Plaza.get_plaza(vacant_id)
        if not selected_vacant:
            raise ValidationError('Seleccione una plaza válida.')


class FormPlazaGrupoUpdate(FlaskForm):
    vacant_group_id = IntegerField('Id Plaza_Grupo', widget=HiddenInput())
    hours = IntegerField('Horas anuales',
                         validators=[DataRequired(message='Las horas son obligatorias'),
                                     NumberRange(min=1,
                                                 message='El número de grupos prácticas previstos debe ser mayor que 0')])
    submit = SubmitField('Modificar')


class FormLogin(FlaskForm):
    username = StringField('Correo electrónico', validators=[DataRequired(message='El usuario es obligatorio')])
    password = PasswordField('Contraseña', validators=[DataRequired(message='La contraseña es obligatoria')])
    submit = SubmitField('Iniciar Sesión')


class FormDataBase(FlaskForm):
    sql_file = FileField('Archivo SQL',
                         validators=[DataRequired(message='Debe seleccionar un archivo'),
                                     FileAllowed(['sql'], 'Solo se permiten archivos SQL (.sql)')])
    submit = SubmitField('Importar')
