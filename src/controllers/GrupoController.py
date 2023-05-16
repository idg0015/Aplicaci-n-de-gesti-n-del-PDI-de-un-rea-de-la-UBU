from flask import render_template, request

from models.Curso import Curso
from models.CursoAsignatura import CursoAsignatura
from models.Grupo import Grupo


def index():
    # info = CursoAsignatura.get_all_json()
    return render_template('grupos/index.html', cursos=Curso.get_all())


def gestion(id_curso_asignatura):
    grupos = Grupo.get_all_json()
    return render_template('grupos/gestion.html', grupos=grupos)


def get_all_json():
    if request.method == "POST":
        return CursoAsignatura.get_all_json(request.form.get('id'))
